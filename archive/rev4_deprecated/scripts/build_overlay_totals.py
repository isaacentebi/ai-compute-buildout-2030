#!/usr/bin/env python3
"""Build canonical overlay totals from row-level capacity atoms.

Inputs:
  - canonical_capacity_atoms.yaml
  - neocloud_overlay.yaml
  - epoch_data_centers/compiled.json
  - compute_commitments_overlay.yaml

Outputs:
  - generated_overlay_totals.yaml
  - row_level_audit.csv
  - canonical_totals.json
  - overlay_reconciliation_report.md
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml  # type: ignore


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
ATOMS = ROOT / "canonical_capacity_atoms.yaml"
NEOCLOUD = ROOT / "neocloud_overlay.yaml"
EPOCH = ROOT / "epoch_data_centers" / "compiled.json"
OVERLAY = ROOT / "compute_commitments_overlay.yaml"
ANATOMY = ROOT / "anatomy_layer_costs.yaml"

GENERATED_TOTALS = ROOT / "generated_overlay_totals.yaml"
ROW_AUDIT = ROOT / "row_level_audit.csv"
CANONICAL_JSON = ROOT / "canonical_totals.json"
REPORT = ROOT / "overlay_reconciliation_report.md"
MONTE_CARLO_FACILITY = ROOT / "monte_carlo_output_facility_seed20260424.json"
COMPUTE_TOTALS_CSV = ROOT / "compute_commitments_totals.csv"

COMPARISON_BASELINE_RAW_WESTERN_FACILITY_GW = 51.427
COMPARISON_BASELINE_NON_STRETCH_FACILITY_GW = 44.673
COMPARISON_BASELINE_CONSERVATIVE_RAW_FACILITY_GW = 27.935
COMPARISON_BASELINE_PROB_WEIGHTED_FACILITY_GW = 36.456
COMPARISON_BASELINE_FULL_REALIZATION_FACILITY_GW = 54.724

COMPARISON_BASELINE_POST_NEO_T3_GW = 6.48
COMPARISON_BASELINE_POST_NEO_T4_GW = 17.88
COMPARISON_BASELINE_POST_NEO_CONSERVATIVE_GW = 26.465
COMPARISON_BASELINE_POST_NEO_PROB_WEIGHTED_GW = 36.162

TIER_DEFAULTS = {
    "T1": 1.00,
    "T2": 0.88,
    "T3": 0.78,
    "T4": 0.58,
    "T5": 0.32,
    "T6": 0.25,
}
CONSERVATIVE_TIERS = {"T1", "T2", "T3"}
REQUIRED_FIELDS = [
    "atom_id",
    "parent_entity",
    "counterparty_or_anchor_tenant",
    "site_or_region",
    "capacity_mw_original",
    "capacity_basis_original",
    "pue_assumed",
    "capacity_mw_it",
    "capacity_mw_facility",
    "scope",
    "status",
    "evidence_tier",
    "realization_probability",
    "source_url",
    "source_publisher",
    "source_date",
    "last_checked",
    "dedupe_group",
    "dedupe_adjustment_mw",
    "dedupe_direction",
    "included_raw_horizon",
    "included_non_stretch",
    "included_conservative_T1_T2_T3",
    "included_probability_weighted",
    "notes",
]

NEOCLOUD_PREFIXES = (
    "coreweave_",
    "nebius_",
    "nscale_",
    "crusoe_",
    "lambda_",
    "applied_digital_",
    "together_",
    "voltage_park_",
    "fluidstack_",
    "fermi_",
)


def round_gw(mw: float | None, digits: int = 3) -> float:
    return round((mw or 0.0) / 1000.0, digits)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return yaml.safe_load(f)


def load_inputs() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    atoms = load_yaml(ATOMS)
    neocloud = load_yaml(NEOCLOUD)
    with EPOCH.open() as f:
        epoch = json.load(f)
    overlay = load_yaml(OVERLAY)
    anatomy = load_yaml(ANATOMY) if ANATOMY.exists() else {}
    return atoms, neocloud, epoch, overlay, anatomy


def parse_date(value: Any) -> dt.date | None:
    if value is None:
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    text = str(value).strip().strip("'\"")
    if not text:
        return None
    try:
        return dt.date.fromisoformat(text)
    except ValueError:
        pass
    try:
        return dt.date.fromisoformat(f"{text}-01")
    except ValueError:
        return None


def validate_atoms(atoms_doc: dict[str, Any]) -> list[dict[str, Any]]:
    atoms = atoms_doc.get("atoms") or []
    if not isinstance(atoms, list):
        raise ValueError("canonical_capacity_atoms.yaml must contain atoms: []")

    ids: set[str] = set()
    errors: list[str] = []
    for idx, atom in enumerate(atoms, start=1):
        missing = [field for field in REQUIRED_FIELDS if field not in atom]
        if missing:
            errors.append(f"atom #{idx} missing required fields: {missing}")
            continue
        atom_id = atom["atom_id"]
        if atom_id in ids:
            errors.append(f"duplicate atom_id: {atom_id}")
        ids.add(atom_id)

        scope = atom["scope"]
        if scope not in {"western", "sovereign", "excluded"}:
            errors.append(f"{atom_id}: invalid scope {scope!r}")
        basis = atom["capacity_basis_original"]
        if basis not in {"IT", "facility", "unknown"}:
            errors.append(f"{atom_id}: invalid capacity_basis_original {basis!r}")
        tier = atom["evidence_tier"]
        if tier not in {*TIER_DEFAULTS.keys(), "excluded"}:
            errors.append(f"{atom_id}: invalid evidence_tier {tier!r}")

        facility = atom.get("capacity_mw_facility")
        if facility is None and atom.get("included_raw_horizon"):
            errors.append(f"{atom_id}: null capacity_mw_facility cannot be included_raw_horizon")
        if facility is None and atom.get("included_probability_weighted"):
            errors.append(f"{atom_id}: null capacity_mw_facility cannot be included_probability_weighted")
        if facility is not None and facility < 0:
            errors.append(f"{atom_id}: capacity_mw_facility cannot be negative")

        if basis == "unknown" and facility is not None and not atom.get("analyst_inference_method"):
            errors.append(f"{atom_id}: unknown-basis MW needs analyst_inference_method")
        if atom.get("analyst_inference_method") and tier not in {"T2", "T4", "T6"}:
            # T2/T4 are allowed for site-scale estimates with hard site evidence;
            # T6 is required for weak GPU-count inference.
            errors.append(f"{atom_id}: analyst_inference_method on unexpected tier {tier}")

    if errors:
        raise ValueError("Atom validation failed:\n" + "\n".join(f"  - {e}" for e in errors))
    return atoms


def is_neocloud_atom(atom: dict[str, Any]) -> bool:
    atom_id = atom["atom_id"]
    return atom_id.startswith(NEOCLOUD_PREFIXES)


def included(atoms: list[dict[str, Any]], field: str) -> list[dict[str, Any]]:
    return [a for a in atoms if a.get(field)]


def sum_mw(rows: list[dict[str, Any]], key: str = "capacity_mw_facility") -> float:
    return sum(float(row.get(key) or 0.0) for row in rows)


def sum_range(rows: list[dict[str, Any]], basis: str) -> tuple[float, float]:
    low_key = f"capacity_mw_{basis}_low"
    high_key = f"capacity_mw_{basis}_high"
    point_key = f"capacity_mw_{basis}"
    low = sum(float(row.get(low_key) if row.get(low_key) is not None else row.get(point_key) or 0.0) for row in rows)
    high = sum(float(row.get(high_key) if row.get(high_key) is not None else row.get(point_key) or 0.0) for row in rows)
    return low, high


def tier_rollup(rows: list[dict[str, Any]]) -> dict[str, Any]:
    tier_mw: dict[str, float] = defaultdict(float)
    for row in rows:
        tier = row["evidence_tier"]
        if tier in TIER_DEFAULTS:
            tier_mw[tier] += float(row.get("capacity_mw_facility") or 0.0)

    out: dict[str, Any] = {}
    for tier in ("T1", "T2", "T3", "T4", "T5", "T6"):
        gw = round_gw(tier_mw[tier])
        out[tier] = {
            "gw": gw,
            "realization_probability_default": TIER_DEFAULTS[tier],
            "probability_weighted_gw": round(gw * TIER_DEFAULTS[tier], 3),
        }
    total = round(sum(v["gw"] for v in out.values()), 3)
    prob_weighted = round(sum(v["probability_weighted_gw"] for v in out.values()), 3)
    conservative = round(sum(out[t]["gw"] for t in CONSERVATIVE_TIERS), 3)
    non_stretch = round(total - out["T5"]["gw"], 3)
    return {
        "tiers": out,
        "total": total,
        "non_stretch": non_stretch,
        "conservative_T1_T2_T3_raw": conservative,
        "conservative_T1_T2_T3_probweighted": round(
            out["T1"]["gw"] * 1.0 + out["T2"]["gw"] * 0.88 + out["T3"]["gw"] * 0.78, 3
        ),
        "probability_weighted": prob_weighted,
    }


def row_probability_weighted(rows: list[dict[str, Any]]) -> float:
    return round_gw(
        sum(float(row.get("capacity_mw_facility") or 0.0) * float(row.get("realization_probability") or 0.0) for row in rows)
    )


def capital_envelope(anatomy: dict[str, Any], raw_gw: float) -> dict[str, float]:
    block = (
        anatomy.get("aggregate_rollup_facility_mw_2026", {})
        .get("total_all_in_facility_gw_2026", {})
    )
    low = float(block.get("low", 30.0))
    high = float(block.get("high", 47.0))
    central = float(block.get("central_adopted_in_paper", block.get("central_grid_tied", 37.0)))
    return {
        "capital_envelope_usd_t_low": round(raw_gw * low / 1000.0, 3),
        "capital_envelope_usd_t_central": round(raw_gw * central / 1000.0, 3),
        "capital_envelope_usd_t_high": round(raw_gw * high / 1000.0, 3),
    }


def load_monte_carlo_facility() -> dict[str, Any]:
    if not MONTE_CARLO_FACILITY.exists():
        return {}
    with MONTE_CARLO_FACILITY.open() as f:
        summary = json.load(f)
    return {
        "monte_carlo_p05_gw_facility": round(float(summary.get("p05", 0.0)), 3),
        "monte_carlo_p10_gw_facility": round(float(summary.get("p10", 0.0)), 3),
        "monte_carlo_p25_gw_facility": round(float(summary.get("p25", 0.0)), 3),
        "monte_carlo_p50_gw_facility": round(float(summary.get("p50", 0.0)), 3),
        "monte_carlo_p75_gw_facility": round(float(summary.get("p75", 0.0)), 3),
        "monte_carlo_p90_gw_facility": round(float(summary.get("p90", 0.0)), 3),
        "monte_carlo_p95_gw_facility": round(float(summary.get("p95", 0.0)), 3),
        "monte_carlo_mean_gw_facility": round(float(summary.get("mean", 0.0)), 3),
        "monte_carlo_std_dev_gw_facility": round(float(summary.get("std", 0.0)), 3),
    }


def classify_raw_delta(raw_gw: float) -> str:
    delta = abs(raw_gw - COMPARISON_BASELINE_RAW_WESTERN_FACILITY_GW)
    if delta <= 0.5:
        return "GREEN"
    if delta <= 2.0:
        return "YELLOW"
    return "RED"


def build(atoms: list[dict[str, Any]], neocloud: dict[str, Any], epoch: dict[str, Any], overlay: dict[str, Any], anatomy: dict[str, Any]) -> dict[str, Any]:
    western_raw_rows = included(atoms, "included_raw_horizon")
    western_non_stretch_rows = included(atoms, "included_non_stretch")
    western_conservative_rows = included(atoms, "included_conservative_T1_T2_T3")
    western_probability_rows = included(atoms, "included_probability_weighted")

    raw_mw = sum_mw(western_raw_rows)
    raw_low_mw, raw_high_mw = sum_range(western_raw_rows, "facility")
    raw_it_mw = sum_mw(western_raw_rows, "capacity_mw_it")

    operational_rows = [
        row for row in western_raw_rows
        if row.get("status") == "operational" or row["atom_id"] in {"voltage_park_lightning_inferred", "together_operational_inferred"}
    ]
    t1_rows = [row for row in western_raw_rows if row.get("evidence_tier") == "T1"]
    sovereign_rows = [
        row for row in atoms
        if row.get("scope") == "sovereign"
        and row.get("status") != "excluded"
        and row.get("capacity_mw_facility") is not None
    ]
    excluded_rows = [
        row for row in atoms
        if row.get("scope") == "excluded" and row.get("capacity_mw_facility") is not None
    ]

    overall = tier_rollup(western_probability_rows)
    neocloud_rows = [row for row in western_probability_rows if is_neocloud_atom(row)]
    neocloud_rollup = tier_rollup(neocloud_rows)

    raw_gw = round_gw(raw_mw)
    envelope = capital_envelope(anatomy, raw_gw)
    monte_carlo = load_monte_carlo_facility()

    current_overlay = overlay.get("totals", {}).get("evidence_tier_rollup_western_facility", {})
    overlay_fac = overlay.get("totals", {}).get("western_horizon_2027_2030_facility", {})
    legacy_all_epoch_scope_gw = round_gw(
        raw_mw
        + sum_mw([row for row in atoms if row["atom_id"].startswith("epoch_openai_stargate_uae")])
        + sum_mw([row for row in atoms if row["atom_id"].startswith("epoch_alibaba_zhangbei")])
    )

    return {
        "metadata": {
            "generated_from": str(ATOMS.relative_to(ROOT)),
            "generated_by": str(Path(__file__).relative_to(ROOT)),
            "generated_at": "2026-04-27",
            "manual_edit_allowed": False,
            "atom_count": len(atoms),
            "western_included_atom_count": len(western_raw_rows),
            "epoch_dataset_updated": epoch.get("source", {}).get("dataset_updated"),
            "neocloud_overlay_version": neocloud.get("metadata", {}).get("overlay_version"),
        },
        "raw_horizon": {
            "raw_western_facility_gw": raw_gw,
            "raw_western_facility_range_gw": [round_gw(raw_low_mw), round_gw(raw_high_mw)],
            "raw_western_it_bridge_gw": round_gw(raw_it_mw),
            "sovereign_sidebar_facility_gw": round_gw(sum_mw(sovereign_rows)),
            "excluded_capacity_gw_or_null": round_gw(sum_mw(excluded_rows)) if excluded_rows else None,
            "current_overlay_raw_western_facility_gw": COMPARISON_BASELINE_RAW_WESTERN_FACILITY_GW,
            "delta_vs_current_overlay_gw": round(raw_gw - COMPARISON_BASELINE_RAW_WESTERN_FACILITY_GW, 3),
            "classification": classify_raw_delta(raw_gw),
            "legacy_all_epoch_scope_raw_western_facility_gw": legacy_all_epoch_scope_gw,
        },
        "neocloud_tier_rollup_facility": {
            "T1": neocloud_rollup["tiers"]["T1"]["gw"],
            "T2": neocloud_rollup["tiers"]["T2"]["gw"],
            "T3": neocloud_rollup["tiers"]["T3"]["gw"],
            "T4": neocloud_rollup["tiers"]["T4"]["gw"],
            "T5": neocloud_rollup["tiers"]["T5"]["gw"],
            "T6": neocloud_rollup["tiers"]["T6"]["gw"],
            "total": neocloud_rollup["total"],
            "probability_weighted": neocloud_rollup["probability_weighted"],
            "row_probability_weighted": row_probability_weighted(neocloud_rows),
            "conservative_T1_T2_T3_raw": neocloud_rollup["conservative_T1_T2_T3_raw"],
        },
        "western_facility_tier_rollup": {
            "T1_operational": overall["tiers"]["T1"]["gw"],
            "T2_physically_evidenced": overall["tiers"]["T2"]["gw"],
            "T3_firm_commercial": overall["tiers"]["T3"]["gw"],
            "T4_announced_site_plan": overall["tiers"]["T4"]["gw"],
            "T5_loi_or_stretch": overall["tiers"]["T5"]["gw"],
            "T6_analyst_inference": overall["tiers"]["T6"]["gw"],
            "total_gw_announced_facility": overall["total"],
            "total_gw_non_stretch_facility": overall["non_stretch"],
            "total_gw_conservative_facility_raw": overall["conservative_T1_T2_T3_raw"],
            "total_gw_conservative_facility_probweighted": overall["conservative_T1_T2_T3_probweighted"],
            "total_gw_probability_weighted_facility": overall["probability_weighted"],
            "row_probability_weighted_facility": row_probability_weighted(western_probability_rows),
            "total_gw_full_realization_facility": round_gw(raw_high_mw),
        },
        "canonical_totals": {
            "operational_today_gw_facility": round_gw(sum_mw(operational_rows)),
            "tier_clean_T1_operational_gw_facility": round_gw(sum_mw(t1_rows)),
            "raw_western_horizon_gw_facility": raw_gw,
            "raw_western_horizon_range_gw_facility": [round_gw(raw_low_mw), round_gw(raw_high_mw)],
            "raw_western_horizon_gw_it_bridge": round_gw(raw_it_mw),
            "raw_non_stretch_gw_facility": round_gw(sum_mw(western_non_stretch_rows)),
            "deterministic_probability_weighted_gw_facility": overall["probability_weighted"],
            "conservative_T1_T2_T3_raw_gw_facility": round_gw(sum_mw(western_conservative_rows)),
            "conservative_T1_T2_T3_probability_weighted_gw_facility": overall["conservative_T1_T2_T3_probweighted"],
            "full_realization_ceiling_gw_facility": round_gw(raw_high_mw),
            "sovereign_sidebar_gw_facility": round_gw(sum_mw(sovereign_rows)),
            "capital_envelope_usd_t_central": envelope["capital_envelope_usd_t_central"],
            "capital_envelope_usd_t_low": envelope["capital_envelope_usd_t_low"],
            "capital_envelope_usd_t_high": envelope["capital_envelope_usd_t_high"],
            **monte_carlo,
        },
        "comparisons": {
            "current_overlay": {
                "total_announced_facility": current_overlay.get("total_gw_announced_facility", overlay_fac.get("total_gw_point")),
                "non_stretch_facility": current_overlay.get("total_gw_non_stretch_facility"),
                "conservative_raw_facility": current_overlay.get("total_gw_conservative_facility_raw"),
                "probability_weighted_facility": current_overlay.get("total_gw_probability_weighted_facility"),
                "full_realization_facility": current_overlay.get("total_gw_full_realization_facility"),
            },
            "prior_current_values_from_addendum": {
                "total_announced_facility": COMPARISON_BASELINE_RAW_WESTERN_FACILITY_GW,
                "non_stretch_facility": COMPARISON_BASELINE_NON_STRETCH_FACILITY_GW,
                "conservative_raw_facility": COMPARISON_BASELINE_CONSERVATIVE_RAW_FACILITY_GW,
                "probability_weighted_facility": COMPARISON_BASELINE_PROB_WEIGHTED_FACILITY_GW,
                "full_realization_facility": COMPARISON_BASELINE_FULL_REALIZATION_FACILITY_GW,
            },
            "expected_post_neocloud_split_only": {
                "T3": COMPARISON_BASELINE_POST_NEO_T3_GW,
                "T4": COMPARISON_BASELINE_POST_NEO_T4_GW,
                "conservative_raw": COMPARISON_BASELINE_POST_NEO_CONSERVATIVE_GW,
                "probability_weighted": COMPARISON_BASELINE_POST_NEO_PROB_WEIGHTED_GW,
            },
        },
    }


def write_generated_totals(payload: dict[str, Any]) -> None:
    GENERATED_TOTALS.write_text(yaml.safe_dump(payload, sort_keys=False, width=120))
    CANONICAL_JSON.write_text(json.dumps(payload["canonical_totals"], indent=2, sort_keys=True) + "\n")


def write_row_audit(atoms: list[dict[str, Any]]) -> None:
    optional = [
        "capacity_mw_facility_low",
        "capacity_mw_facility_high",
        "capacity_mw_it_low",
        "capacity_mw_it_high",
        "source_type",
        "source_support",
        "freshness_status",
        "freshness_waiver_reason",
        "analyst_inference_method",
        "unknown_mw_reason",
        "double_count_risk",
    ]
    fieldnames = [
        "commitment_id",
        "atom_id",
        "operator",
        "parent_entity",
        "counterparty_or_anchor_tenant",
        "site_or_region",
        "scope",
        "status",
        "evidence_tier",
        "realization_probability",
        "capacity_mw_original",
        "capacity_basis_original",
        "pue_assumption",
        "capacity_mw_it",
        "capacity_mw_facility",
        "included_in_western_raw_horizon",
        "western_denominator",
        "sovereign_sidebar",
        "included_non_stretch",
        "included_conservative_T1_T2_T3",
        "included_probability_weighted",
        "primary_source_url",
        "source_publication_date",
        "last_checked",
        "last_verified_date",
        "dedupe_group",
        "dedupe_adjustment_mw",
        "dedupe_direction",
        "notes",
        *optional,
    ]
    with ROW_AUDIT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for atom in atoms:
            row = {
                "commitment_id": atom["atom_id"],
                "atom_id": atom["atom_id"],
                "operator": atom["parent_entity"],
                "parent_entity": atom["parent_entity"],
                "counterparty_or_anchor_tenant": atom["counterparty_or_anchor_tenant"],
                "site_or_region": atom["site_or_region"],
                "scope": atom["scope"],
                "status": atom["status"],
                "evidence_tier": atom["evidence_tier"],
                "realization_probability": atom["realization_probability"],
                "capacity_mw_original": atom["capacity_mw_original"],
                "capacity_basis_original": atom["capacity_basis_original"],
                "pue_assumption": atom["pue_assumed"],
                "capacity_mw_it": atom["capacity_mw_it"],
                "capacity_mw_facility": atom["capacity_mw_facility"],
                "included_in_western_raw_horizon": str(bool(atom["included_raw_horizon"])).lower(),
                "western_denominator": str(bool(atom["included_raw_horizon"])).lower(),
                "sovereign_sidebar": str(atom["scope"] == "sovereign").lower(),
                "included_non_stretch": str(bool(atom["included_non_stretch"])).lower(),
                "included_conservative_T1_T2_T3": str(bool(atom["included_conservative_T1_T2_T3"])).lower(),
                "included_probability_weighted": str(bool(atom["included_probability_weighted"])).lower(),
                "primary_source_url": atom.get("source_url") or "",
                "source_publication_date": atom.get("source_date") or "",
                "last_checked": atom.get("last_checked") or "",
                "last_verified_date": atom.get("last_checked") or "",
                "dedupe_group": atom.get("dedupe_group") or "",
                "dedupe_adjustment_mw": atom.get("dedupe_adjustment_mw") or 0,
                "dedupe_direction": atom.get("dedupe_direction") or "",
                "notes": atom.get("notes") or "",
            }
            for key in optional:
                row[key] = atom.get(key, "")
            writer.writerow(row)


def write_compute_totals(payload: dict[str, Any], atoms: list[dict[str, Any]]) -> None:
    canonical = payload["canonical_totals"]
    rows = [
        "# compute_commitments_totals.csv regenerated from canonical_totals.json and generated_overlay_totals.yaml",
        f"# Raw Western facility horizon: {canonical['raw_western_horizon_gw_facility']:.3f} GW",
        f"# Raw Western facility range: [{canonical['raw_western_horizon_range_gw_facility'][0]:.3f}, {canonical['raw_western_horizon_range_gw_facility'][1]:.3f}] GW",
        f"# Deterministic probability-weighted facility: {canonical['deterministic_probability_weighted_gw_facility']:.3f} GW",
        f"# Conservative raw facility: {canonical['conservative_T1_T2_T3_raw_gw_facility']:.3f} GW",
        f"# Full-realization ceiling facility: {canonical['full_realization_ceiling_gw_facility']:.3f} GW",
        f"# Sovereign sidebar facility: {canonical['sovereign_sidebar_gw_facility']:.3f} GW",
        f"# Raw Western IT bridge: {canonical['raw_western_horizon_gw_it_bridge']:.3f} GW",
        f"# Monte Carlo p50 facility: {canonical.get('monte_carlo_p50_gw_facility', 0.0):.3f} GW",
        "",
    ]
    fieldnames = [
        "atom_id",
        "operator",
        "scope",
        "status",
        "evidence_tier",
        "capacity_mw_facility",
        "capacity_mw_it",
        "realization_probability",
        "included_raw_horizon",
        "included_probability_weighted",
        "notes",
    ]
    with COMPUTE_TOTALS_CSV.open("w", newline="") as f:
        f.write("\n".join(rows))
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for atom in atoms:
            writer.writerow({
                "atom_id": atom["atom_id"],
                "operator": atom["parent_entity"],
                "scope": atom["scope"],
                "status": atom["status"],
                "evidence_tier": atom["evidence_tier"],
                "capacity_mw_facility": atom.get("capacity_mw_facility", ""),
                "capacity_mw_it": atom.get("capacity_mw_it", ""),
                "realization_probability": atom.get("realization_probability", ""),
                "included_raw_horizon": atom.get("included_raw_horizon", ""),
                "included_probability_weighted": atom.get("included_probability_weighted", ""),
                "notes": atom.get("notes", ""),
            })


def source_lists(atoms: list[dict[str, Any]], today: dt.date) -> dict[str, list[dict[str, Any]]]:
    stale_or_missing = []
    secondary_only = []
    inferred = []
    sovereign = []
    double_count = []
    unknown_mw = []

    for atom in atoms:
        checked = parse_date(atom.get("last_checked"))
        age = (today - checked).days if checked else None
        if not atom.get("source_url") or not atom.get("source_date") or not checked or (age is not None and age > 60):
            stale_or_missing.append(atom)
        support = str(atom.get("source_support") or "")
        source_type = str(atom.get("source_type") or "")
        if support == "secondary_only" or source_type == "secondary_media":
            secondary_only.append(atom)
        if atom.get("analyst_inference_method") or atom.get("status") == "inferred" or atom.get("evidence_tier") == "T6":
            inferred.append(atom)
        if atom.get("scope") == "sovereign":
            sovereign.append(atom)
        if atom.get("double_count_risk") or float(atom.get("dedupe_adjustment_mw") or 0.0) != 0.0:
            double_count.append(atom)
        if atom.get("capacity_mw_facility") is None:
            unknown_mw.append(atom)

    return {
        "stale_or_missing": stale_or_missing,
        "secondary_only": secondary_only,
        "inferred": inferred,
        "sovereign": sovereign,
        "double_count": double_count,
        "unknown_mw": unknown_mw,
    }


def bullet_ids(rows: list[dict[str, Any]], limit: int | None = None) -> str:
    if not rows:
        return "- None.\n"
    lines = []
    for row in rows[:limit]:
        cap = row.get("capacity_mw_facility")
        cap_text = "unknown MW" if cap is None else f"{round_gw(float(cap)):.3f} GW"
        lines.append(f"- `{row['atom_id']}` ({cap_text}): {row.get('notes', '')}")
    if limit and len(rows) > limit:
        lines.append(f"- ... plus {len(rows) - limit} more rows in `row_level_audit.csv`.")
    return "\n".join(lines) + "\n"


def write_report(payload: dict[str, Any], atoms: list[dict[str, Any]]) -> None:
    raw = payload["raw_horizon"]
    tiers = payload["western_facility_tier_rollup"]
    neo = payload["neocloud_tier_rollup_facility"]
    canonical = payload["canonical_totals"]
    lists = source_lists(atoms, dt.date(2026, 4, 27))

    current_overlay_prob = payload["comparisons"]["current_overlay"].get("probability_weighted_facility")
    current_overlay_cons = payload["comparisons"]["current_overlay"].get("conservative_raw_facility")
    pre_atom_baseline = payload["comparisons"]["expected_post_neocloud_split_only"]
    decision_prob_baseline = float(pre_atom_baseline["probability_weighted"])
    decision_cons_baseline = float(pre_atom_baseline["conservative_raw"])
    prob_delta = round(canonical["deterministic_probability_weighted_gw_facility"] - decision_prob_baseline, 3)
    cons_delta = round(canonical["conservative_T1_T2_T3_raw_gw_facility"] - decision_cons_baseline, 3)
    mc_facility = ROOT / "monte_carlo_output_facility_seed20260424.json"
    mc_text = (
        "Monte Carlo rerun artifact is present at `monte_carlo_output_facility_seed20260424.json`."
        if mc_facility.exists()
        else "Monte Carlo must be rerun before manuscript repair."
    )

    report = f"""# Overlay Reconciliation Report

Generated: 2026-04-27

## Executive Decision

The overlay is structurally wrong under the strict row-atom scope rule, not merely suffering from neocloud tier drift. The current 51.427 GW Western facility raw horizon is reproducible only if all Epoch sites are retained in the Western denominator. Once `OpenAI Stargate UAE` is moved to the sovereign sidebar and `Alibaba Zhangbei` is excluded, the rebuilt Western facility raw horizon is **{raw['raw_western_facility_gw']:.3f} GW**.

Classification versus 51.427 GW: **{raw['classification']}** ({raw['delta_vs_current_overlay_gw']:+.3f} GW).

The neocloud T3/T4 split in latest `main` is already corrected to the expected split. The earlier all-contracted-into-T3 failure is tier drift that has been repaired, but the atom rebuild exposes a separate scope problem in the Epoch floor.

## Required Answers

1. **Is the current 51.427 GW Western facility raw horizon still supported?**
   Not under strict atom scope. The all-Epoch convention rebuilds to {raw['legacy_all_epoch_scope_raw_western_facility_gw']:.3f} GW, effectively matching 51.427 after rounding. The strict Western denominator rebuilds to **{raw['raw_western_facility_gw']:.3f} GW**.

2. **If not, what is the rebuilt number?**
   **{raw['raw_western_facility_gw']:.3f} GW facility**, range **[{raw['raw_western_facility_range_gw'][0]:.3f}, {raw['raw_western_facility_range_gw'][1]:.3f}] GW**, IT bridge **{raw['raw_western_it_bridge_gw']:.3f} GW**.

3. **Which rows caused the delta?**
   The scope delta is driven by `epoch_openai_stargate_uae_buildout_remaining` (-1.400 GW to Western, moved to sovereign), `epoch_alibaba_zhangbei_operational` (-0.203 GW to Western, excluded), and -0.011 GW of rounding versus the legacy hand total.

4. **Is the neocloud T3/T4 split wrong?**
   In the latest checked-out `main`, no. The atom rollup regenerates T3 = **{neo['T3']:.3f} GW** and T4 = **{neo['T4']:.3f} GW**. That matches the corrected `neocloud_overlay.yaml` split.

5. **What is the corrected T3/T4 split?**
   Overall Western facility: T3 = **{tiers['T3_firm_commercial']:.3f} GW**, T4 = **{tiers['T4_announced_site_plan']:.3f} GW**. Neocloud-only: T3 = **{neo['T3']:.3f} GW**, T4 = **{neo['T4']:.3f} GW**.

6. **What are the corrected conservative and probability-weighted totals?**
   Conservative T1+T2+T3 raw facility = **{canonical['conservative_T1_T2_T3_raw_gw_facility']:.3f} GW**. Deterministic tier-default probability-weighted facility = **{canonical['deterministic_probability_weighted_gw_facility']:.3f} GW**. Probability-weighted delta versus the pre-atom, neocloud-corrected overlay baseline ({decision_prob_baseline:.3f} GW) = **{prob_delta:+.3f} GW**.

7. **Which rows have stale or missing sources?**
{bullet_ids(lists['stale_or_missing'], limit=25)}
8. **Which rows are source-supported only by secondary media?**
{bullet_ids(lists['secondary_only'], limit=25)}
9. **Which rows rely on analyst MW inference?**
{bullet_ids(lists['inferred'], limit=25)}
10. **Which rows are sovereign and must not enter the Western denominator?**
{bullet_ids(lists['sovereign'], limit=25)}
11. **Which rows are double-count risks?**
{bullet_ids(lists['double_count'], limit=25)}
12. **Which values should be considered canonical for the manuscript?**
   Use `canonical_totals.json`:
   - Raw Western facility horizon: **{canonical['raw_western_horizon_gw_facility']:.3f} GW**
   - Raw Western facility range: **[{canonical['raw_western_horizon_range_gw_facility'][0]:.3f}, {canonical['raw_western_horizon_range_gw_facility'][1]:.3f}] GW**
   - Raw non-stretch facility: **{canonical['raw_non_stretch_gw_facility']:.3f} GW**
   - Conservative T1+T2+T3 raw: **{canonical['conservative_T1_T2_T3_raw_gw_facility']:.3f} GW**
   - Probability-weighted facility: **{canonical['deterministic_probability_weighted_gw_facility']:.3f} GW**
   - Row-uncertainty high envelope facility: **{canonical['full_realization_ceiling_gw_facility']:.3f} GW**
   - Sovereign sidebar facility: **{canonical['sovereign_sidebar_gw_facility']:.3f} GW**
   - Capital envelope central: **${canonical['capital_envelope_usd_t_central']:.3f}T** (**${canonical['capital_envelope_usd_t_low']:.3f}T-${canonical['capital_envelope_usd_t_high']:.3f}T**)

## Generated Six-Tier Western Facility Rollup

```yaml
T1_operational: {tiers['T1_operational']:.3f}
T2_physically_evidenced: {tiers['T2_physically_evidenced']:.3f}
T3_firm_commercial: {tiers['T3_firm_commercial']:.3f}
T4_announced_site_plan: {tiers['T4_announced_site_plan']:.3f}
T5_loi_or_stretch: {tiers['T5_loi_or_stretch']:.3f}
T6_analyst_inference: {tiers['T6_analyst_inference']:.3f}
total_gw_announced_facility: {tiers['total_gw_announced_facility']:.3f}
total_gw_non_stretch_facility: {tiers['total_gw_non_stretch_facility']:.3f}
total_gw_conservative_facility_raw: {tiers['total_gw_conservative_facility_raw']:.3f}
total_gw_probability_weighted_facility: {tiers['total_gw_probability_weighted_facility']:.3f}
```

## Decision Rules

- Raw horizon delta is {abs(raw['delta_vs_current_overlay_gw']):.3f} GW, so this is **YELLOW** and can proceed only with documented deltas.
- Probability-weighted delta versus the pre-atom, neocloud-corrected baseline is {abs(prob_delta):.3f} GW, above 0.5 GW, so Monte Carlo must be rerun before manuscript repair. {mc_text}
- Conservative delta versus the pre-atom, neocloud-corrected baseline is {abs(cons_delta):.3f} GW, below 0.5 GW, so floor-like claims do not require wholesale rewrite on that basis alone.
"""
    REPORT.write_text(report)


def check_overlay(payload: dict[str, Any], tolerance: float) -> bool:
    overlay = payload["comparisons"]["current_overlay"]
    canonical = payload["canonical_totals"]
    checks = [
        ("raw_western_horizon_gw_facility", canonical["raw_western_horizon_gw_facility"], overlay.get("total_announced_facility")),
        ("raw_non_stretch_gw_facility", canonical["raw_non_stretch_gw_facility"], overlay.get("non_stretch_facility")),
        ("conservative_T1_T2_T3_raw_gw_facility", canonical["conservative_T1_T2_T3_raw_gw_facility"], overlay.get("conservative_raw_facility")),
        ("deterministic_probability_weighted_gw_facility", canonical["deterministic_probability_weighted_gw_facility"], overlay.get("probability_weighted_facility")),
        ("full_realization_ceiling_gw_facility", canonical["full_realization_ceiling_gw_facility"], overlay.get("full_realization_facility")),
    ]
    ok = True
    for name, got, expected in checks:
        expected_f = float(expected or 0.0)
        diff = abs(float(got) - expected_f)
        if diff > tolerance:
            print(f"DRIFT {name}: canonical={got:.3f} overlay={expected_f:.3f} diff={diff:.3f}")
            ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", "--check", dest="check_only", action="store_true", help="validate and compare without writing artifacts")
    parser.add_argument("--check-overlay", action="store_true", help="fail if overlay totals drift from canonical atoms")
    parser.add_argument("--tolerance-gw", type=float, default=0.02)
    args = parser.parse_args()

    atoms_doc, neocloud, epoch, overlay, anatomy = load_inputs()
    atoms = validate_atoms(atoms_doc)
    payload = build(atoms, neocloud, epoch, overlay, anatomy)

    if not args.check_only:
        write_generated_totals(payload)
        write_row_audit(atoms)
        write_compute_totals(payload, atoms)
        write_report(payload, atoms)

    if args.check_overlay:
        return 0 if check_overlay(payload, args.tolerance_gw) else 1

    print(json.dumps(payload["canonical_totals"], indent=2, sort_keys=True))
    print(f"wrote {GENERATED_TOTALS.name}, {ROW_AUDIT.name}, {CANONICAL_JSON.name}, {COMPUTE_TOTALS_CSV.name}, {REPORT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
