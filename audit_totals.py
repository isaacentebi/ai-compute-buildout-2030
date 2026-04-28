#!/usr/bin/env python3
"""
audit_totals.py — audit the hand-written `totals:` block in
compute_commitments_overlay.yaml against the per-row incrementals,
AND compute the seven canonical totals on top of the six-tier evidence
framework (see CONFIDENCE_DECOMPOSITION.md).

NOT a source of truth for the per-row incrementals. The source of truth
is the YAML itself — this script only re-adds the rows so you get warned
if the hand-written sums drift out of sync with the inputs.

For the probability-weighted rollup, this script IS the source of truth.

Usage:
    python3 audit_totals.py                    # horizon overlay audit (default)
    python3 audit_totals.py --basis anatomy    # rev-4 unit-economics audit
    python3 audit_totals.py --basis all        # both

Exit code 0 if all sums match. Exit code 1 if any disagree (prints diff).

Seven canonical totals emitted:
    1. operational_today_gw          — T1 today
    2. announced_horizon_gw          — Σ row_gw unweighted
    3. probability_weighted_gw       — Σ(row_gw × row_probability)
    4. conservative_case_gw          — T1 + T2 + T3 only
    5. full_realization_gw           — arithmetic high ceiling
    6. capital_envelope_usd_b        — total capex requirement estimate
    7. rpo_obligations_usd_b         — contracted customer revenue
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import yaml  # type: ignore

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
OVERLAY = ROOT / "compute_commitments_overlay.yaml"
NEOCLOUD = ROOT / "neocloud_overlay.yaml"
ANATOMY_LAYER_COSTS = ROOT / "anatomy_layer_costs.yaml"
CANONICAL_ATOMS = ROOT / "canonical_capacity_atoms.yaml"

# Bottom-up unit-economics rollup fallback values (used only if the YAML
# does not declare them; the audit reads canonical values from the YAML
# at runtime to prevent drift between this file and the data layer).
# anatomy_layer_costs.yaml#aggregate_rollup_facility_mw_2026.total_all_in_facility_gw_2026
ANATOMY_TOTAL_LOW = 30.0
ANATOMY_TOTAL_HIGH = 47.0
ANATOMY_TOTAL_CENTRAL = 37.45
ANATOMY_CAPEX_ENVELOPE_T_LOW = 1.5
ANATOMY_CAPEX_ENVELOPE_T_HIGH = 2.4
ANATOMY_CAPEX_ENVELOPE_T_CENTRAL = 1.9
# Fallback only — the canonical raw Western 2027-2030 facility horizon
# is read from compute_commitments_overlay.yaml#totals.western_horizon_2027_2030_facility
# at runtime so it cannot drift from the data layer it audits.
ANATOMY_RAW_HORIZON_GW_FALLBACK = 51.427

# $/MW tolerance (0.5M = 500k drift on a layer line)
ANATOMY_TOL_USD_M_PER_MW = 0.5
# $T tolerance for capex envelope (0.05T = $50B)
ANATOMY_TOL_USD_T = 0.05

# Sovereign-AI row ids. Anything not in this set is treated as Western.
SOVEREIGN_IDS = {
    "microsoft_g42_uae_khazna_2025_11",
    "xai_humain_saudi",
    "humain_amd_saudi_2025_05",
    "reliance_jio_jamnagar_2024_08",
    "uk_culham_ai_growth_zone_2025_01",
}

TOL = 0.02  # GW tolerance for rounding (20 MW)
CAPEX_CENTRAL_USD_B_PER_GW = 37.0
CAPEX_TOL_USD_B = 1.5

# Tier-default realization probabilities (midpoints of plan-specified ranges)
TIER_DEFAULTS = {
    "T1": 1.00,
    "T2": 0.88,
    "T3": 0.78,
    "T4": 0.58,
    "T5": 0.32,
    "T6": 0.25,
}

ROW_BASIS_OVERRIDES = {
    "xai_humain_saudi": ("facility", 1.35),
    "humain_amd_saudi_2025_05": ("facility", 1.35),
    "reliance_jio_jamnagar_2024_08": ("facility", 1.40),
}

# For the conservative-case rollup
CONSERVATIVE_TIERS = {"T1", "T2", "T3"}


def fmt(v):
    return "-" if v is None else f"{v:.2f}"


def load_overlay() -> dict:
    with OVERLAY.open() as f:
        return yaml.safe_load(f)


def load_neocloud() -> dict:
    with NEOCLOUD.open() as f:
        return yaml.safe_load(f)


def sum_class_a(commitments: list, scope: str) -> tuple[float, float, float]:
    """Re-sum Class A rows for a given scope on the true IT-load bridge.
    Facility-basis rows are divided by pue_assumed; IT rows pass through.
    Returns (point, low, high).
    """
    point = low = high = 0.0
    for c in commitments:
        if c.get("announcement_class") != "A":
            continue
        cid = c["commitment_id"]
        is_sov = cid in SOVEREIGN_IDS
        row_scope = "sovereign" if is_sov else "western"
        if row_scope != scope:
            continue
        p = c.get("incremental_gw_point")
        r = list(c.get("incremental_gw_range") or [None, None])
        basis, pue = ROW_BASIS_OVERRIDES.get(
            cid, (c.get("mw_basis", "IT"), c.get("pue_assumed") or 1.0)
        )
        if basis == "facility":
            if p is not None:
                p = p / pue
            if r[0] is not None:
                r[0] = r[0] / pue
            if r[1] is not None:
                r[1] = r[1] / pue
        if p is not None:
            point += p
        if r[0] is not None:
            low += r[0]
        if r[1] is not None:
            high += r[1]
    return round(point, 2), round(low, 2), round(high, 2)


def sum_class_a_facility(commitments: list, scope: str) -> tuple[float, float, float]:
    """Re-sum Class A rows for a given scope under FACILITY basis.
    Reads row_audit.incremental_gw_facility_point + range (rev-3 A.1 fields).
    Falls back to IT point × pue_assumed if facility fields are missing.
    Returns (point, low, high).
    """
    point = low = high = 0.0
    for c in commitments:
        if c.get("announcement_class") != "A":
            continue
        cid = c["commitment_id"]
        is_sov = cid in SOVEREIGN_IDS
        row_scope = "sovereign" if is_sov else "western"
        if row_scope != scope:
            continue
        # A.1 fields live at the commitment top level (siblings of
        # incremental_gw_point), not inside row_audit.
        p = c.get("incremental_gw_facility_point")
        r = list(c.get("incremental_gw_facility_range") or [None, None])
        # Fallback: compute from IT × PUE if A.1 facility fields missing.
        if p is None:
            it_p = c.get("incremental_gw_point")
            basis = c.get("mw_basis", "unknown")
            pue = c.get("pue_assumed", 1.25)
            if it_p is not None:
                p = it_p if basis == "facility" else round(it_p * pue, 3)
        if r[0] is None or r[1] is None:
            it_r = c.get("incremental_gw_range") or [None, None]
            basis = c.get("mw_basis", "unknown")
            pue = c.get("pue_assumed", 1.25)
            if it_r[0] is not None and r[0] is None:
                r[0] = it_r[0] if basis == "facility" else round(it_r[0] * pue, 3)
            if it_r[1] is not None and r[1] is None:
                r[1] = it_r[1] if basis == "facility" else round(it_r[1] * pue, 3)
        if p is not None:
            point += p
        if r[0] is not None:
            low += r[0]
        if r[1] is not None:
            high += r[1]
    return round(point, 3), round(low, 3), round(high, 3)


def compare(label: str, got: tuple, expected: tuple) -> bool:
    """Return True if (point, low, high) match within tolerance."""
    ok = all(abs(a - b) <= TOL for a, b in zip(got, expected))
    mark = "OK  " if ok else "FAIL"
    print(f"  [{mark}] {label}")
    print(f"         re-summed rows:  point={fmt(got[0])}  low={fmt(got[1])}  high={fmt(got[2])}")
    print(f"         YAML totals:     point={fmt(expected[0])}  low={fmt(expected[1])}  high={fmt(expected[2])}")
    if not ok:
        print(f"         *** drift detected — update the YAML `totals:` block ***")
    return ok


def compute_probability_weighted_western(doc: dict) -> dict:
    """
    Walk the Class A commitments and roll up probability-weighted GW
    using the per-row evidence_tier + realization_probability fields.
    For Epoch and neocloud contributions, use the tier aggregates in
    the CONFIDENCE_DECOMPOSITION.md framework (recorded as
    evidence_tier_rollup_western in the overlay totals block).
    """
    totals = doc.get("totals", {})
    tier_block = totals.get("evidence_tier_rollup_western", {})

    gw_announced_point = 0.0
    gw_probability_weighted = 0.0
    gw_conservative = 0.0
    gw_full_realization = 0.0
    unassigned_rows = []

    # Per-tier aggregation for Epoch + neocloud (framework-level)
    for tier_key, tier_content in tier_block.items():
        if not tier_key.startswith("T"):
            continue
        tier = tier_key.split("_")[0]  # T1, T2, T3, T4, T5, T6
        gw = tier_content.get("gw", 0.0)
        prob = tier_content.get(
            "realization_probability_default", TIER_DEFAULTS.get(tier, 0.5)
        )
        gw_announced_point += gw
        gw_probability_weighted += gw * prob
        if tier in CONSERVATIVE_TIERS:
            gw_conservative += gw
        gw_full_realization += gw  # all tiers at ceiling

    return {
        "announced_horizon_gw": round(gw_announced_point, 2),
        "probability_weighted_gw": round(gw_probability_weighted, 2),
        "conservative_case_gw": round(gw_conservative, 2),
        "full_realization_gw_framework_ceiling": round(gw_full_realization, 2),
        "unassigned_rows": unassigned_rows,
    }


def compute_probability_weighted_western_facility(doc: dict) -> dict:
    """
    Parallel to compute_probability_weighted_western but reads the
    evidence_tier_rollup_western_facility block (rev-3 primary basis).
    """
    totals = doc.get("totals", {})
    tier_block = totals.get("evidence_tier_rollup_western_facility", {})

    gw_announced_point = 0.0
    gw_probability_weighted = 0.0
    gw_conservative = 0.0
    gw_full_realization = 0.0

    for tier_key, tier_content in tier_block.items():
        if not tier_key.startswith("T"):
            continue
        tier = tier_key.split("_")[0]
        gw = tier_content.get("gw", 0.0)
        prob = tier_content.get(
            "realization_probability_default", TIER_DEFAULTS.get(tier, 0.5)
        )
        gw_announced_point += gw
        gw_probability_weighted += gw * prob
        if tier in CONSERVATIVE_TIERS:
            gw_conservative += gw
        gw_full_realization += gw

    return {
        "announced_horizon_gw": round(gw_announced_point, 3),
        "probability_weighted_gw": round(gw_probability_weighted, 3),
        "conservative_case_gw": round(gw_conservative, 3),
        "full_realization_gw_framework_ceiling": round(gw_full_realization, 3),
    }


def compute_per_row_probability_weighted(doc: dict) -> tuple[float, list]:
    """
    Walk Class A commitments only; apply per-row realization_probability
    (falling back to tier default). Returns (weighted_gw_sum, per_row_list).
    This is finer-grained than the framework-level rollup above and
    catches per-row overrides.
    """
    total_weighted = 0.0
    rows = []
    for c in doc.get("commitments", []):
        if c.get("announcement_class") != "A":
            continue
        cid = c["commitment_id"]
        if cid in SOVEREIGN_IDS:
            continue
        p = c.get("incremental_gw_point")
        if p is None or p == 0.0:
            continue
        tier = c.get("evidence_tier", "T4")
        prob = c.get("realization_probability", TIER_DEFAULTS.get(tier, 0.58))
        weighted = p * prob
        total_weighted += weighted
        rows.append(
            {"id": cid, "gw_point": p, "tier": tier, "prob": prob, "weighted": round(weighted, 3)}
        )
    return round(total_weighted, 2), rows


def compute_per_row_probability_weighted_facility(doc: dict) -> tuple[float, list]:
    """
    Parallel to compute_per_row_probability_weighted but reads
    row_audit.incremental_gw_facility_point (rev-3 A.1 field).
    Falls back to IT × pue_assumed if facility field missing.
    """
    total_weighted = 0.0
    rows = []
    for c in doc.get("commitments", []):
        if c.get("announcement_class") != "A":
            continue
        cid = c["commitment_id"]
        if cid in SOVEREIGN_IDS:
            continue
        # A.1 fields live at commitment top level, not in row_audit.
        p = c.get("incremental_gw_facility_point")
        if p is None:
            it_p = c.get("incremental_gw_point")
            basis = c.get("mw_basis", "unknown")
            pue = c.get("pue_assumed", 1.25)
            if it_p is not None:
                p = it_p if basis == "facility" else round(it_p * pue, 3)
        if p is None or p == 0.0:
            continue
        tier = c.get("evidence_tier", "T4")
        prob = c.get("realization_probability", TIER_DEFAULTS.get(tier, 0.58))
        weighted = p * prob
        total_weighted += weighted
        rows.append(
            {"id": cid, "gw_point": p, "tier": tier, "prob": prob, "weighted": round(weighted, 3)}
        )
    return round(total_weighted, 3), rows


def compute_sovereign_probability_weighted(doc: dict) -> tuple[float, list]:
    total_weighted = 0.0
    rows = []
    for c in doc.get("commitments", []):
        if c.get("announcement_class") != "A":
            continue
        cid = c["commitment_id"]
        if cid not in SOVEREIGN_IDS:
            continue
        p = c.get("incremental_gw_point") or 0.0
        tier = c.get("evidence_tier", "T4")
        prob = c.get("realization_probability", TIER_DEFAULTS.get(tier, 0.58))
        weighted = p * prob
        total_weighted += weighted
        rows.append(
            {"id": cid, "gw_point": p, "tier": tier, "prob": prob, "weighted": round(weighted, 3)}
        )
    epoch_weighted, epoch_rows = compute_epoch_sovereign_probability_weighted(doc.get("totals", {}))
    total_weighted += epoch_weighted
    rows.extend(epoch_rows)
    return round(total_weighted, 2), rows


def compute_epoch_sovereign_probability_weighted(totals: dict) -> tuple[float, list]:
    rows = totals.get("sovereign_ai_sidebar_horizon", {}).get("rows", {})
    epoch_keys = {str(k): float(v) for k, v in rows.items() if str(k).startswith("epoch_")}
    if not epoch_keys:
        return 0.0, []

    atom_rows = []
    if CANONICAL_ATOMS.exists():
        with CANONICAL_ATOMS.open() as f:
            atom_doc = yaml.safe_load(f) or {}
        for atom in atom_doc.get("atoms", []):
            atom_id = str(atom.get("atom_id", ""))
            if not atom_id.startswith("epoch_") or atom.get("scope") != "sovereign":
                continue
            matching_key = next((key for key in epoch_keys if atom_id.startswith(key)), None)
            if not matching_key:
                continue
            p = (atom.get("capacity_mw_it") or 0.0) / 1000.0
            tier = atom.get("evidence_tier", "T4")
            prob = atom.get("realization_probability", TIER_DEFAULTS.get(tier, 0.58))
            weighted = p * prob
            atom_rows.append(
                {"id": atom_id, "gw_point": p, "tier": tier, "prob": prob, "weighted": round(weighted, 3)}
            )

    if atom_rows:
        return sum(row["gw_point"] * row["prob"] for row in atom_rows), atom_rows

    fallback_rows = []
    for key, p in epoch_keys.items():
        tier = "T4"
        prob = TIER_DEFAULTS[tier]
        weighted = p * prob
        fallback_rows.append(
            {"id": key, "gw_point": p, "tier": tier, "prob": prob, "weighted": round(weighted, 3)}
        )
    return sum(row["gw_point"] * row["prob"] for row in fallback_rows), fallback_rows


def add_epoch_sovereign_sidebar_rows(sov: tuple[float, float, float], totals: dict) -> tuple[float, float, float]:
    """Add fixed Epoch-origin sovereign sidebar rows to the IT bridge audit.

    The Class A commitment rows cover supplemental sovereign commitments.
    The atom-ledger reconciliation can also reclassify Epoch sites out of
    the Western denominator. Those rows live in totals.sovereign_ai_sidebar
    rather than in commitments, so the old audit needs to add them explicitly.
    """
    rows = totals.get("sovereign_ai_sidebar_horizon", {}).get("rows", {})
    epoch_extra = sum(float(v) for k, v in rows.items() if str(k).startswith("epoch_"))
    if not epoch_extra:
        return sov
    return (
        round(sov[0] + epoch_extra, 3),
        round(sov[1] + epoch_extra, 3),
        round(sov[2] + epoch_extra, 3),
    )


def compute_capital_envelope(doc: dict) -> dict:
    """
    Aggregate the capex_actual / capex_future / rpo_or_take_or_pay
    fields. Falls back to announced_usd_b when explicit capital fields
    are not yet populated on a row (Phase A.7 will add them systematically).
    """
    capex_announced = 0.0
    rpo_contracted = 0.0
    for c in doc.get("commitments", []):
        usd = c.get("announced_usd_b") or c.get("announced_compute_usd_b") or 0.0
        if c.get("announcement_class") in ("A", "B"):
            capex_announced += usd
        # Rough: customer-revenue-obligation rows (recognise names)
        cid = c.get("commitment_id", "")
        if cid in ("meta_nebius_2026_03_16",):
            rpo_contracted += usd
    # Chip-procurement dollar envelopes
    for c in doc.get("chip_procurement_commitments", []):
        usd = c.get("announced_usd_b") or 0.0
        capex_announced += usd
    return {
        "capex_envelope_usd_b_rough": round(capex_announced, 1),
        "rpo_contracted_usd_b_rough": round(rpo_contracted, 1),
        "note": "A.7 will replace these rough estimates with per-row capex_actual / capex_future / rpo_or_take_or_pay fields.",
    }


def print_seven_canonical_totals(doc: dict, neocloud: dict) -> None:
    totals = doc.get("totals", {})
    op_today = totals["operational_today_2026_q2"]["total_gw"]
    capital = compute_capital_envelope(doc)

    # ------------------------------------------------------------------
    # PRIMARY: FACILITY BASIS (rev-3)
    # ------------------------------------------------------------------
    print()
    print("=" * 70)
    print("SEVEN CANONICAL TOTALS  (facility basis — PRIMARY, Rev-4.1)")
    print("=" * 70)

    framework_fac = compute_probability_weighted_western_facility(doc)
    class_a_weighted_fac, class_a_rows_fac = compute_per_row_probability_weighted_facility(doc)

    west_fac_block = totals.get("western_horizon_2027_2030_facility", {})
    west_horizon_fac = west_fac_block.get("total_gw_point", 0.0)
    west_range_fac = west_fac_block.get("total_gw_range", [0.0, 0.0])

    tier_fac = totals.get("evidence_tier_rollup_western_facility", {})
    non_stretch_fac = tier_fac.get("total_gw_non_stretch_facility", 0.0)
    full_real_fac = tier_fac.get("total_gw_full_realization_facility", west_range_fac[1])

    tier_clean_t1 = tier_fac.get("T1_operational", {}).get("gw", 0.0)
    print(f"  1. operational_today_gw         = {op_today:>6.2f} GW facility  "
          f"(includes T6-inferred operational capacity; tier-clean T1 = {tier_clean_t1:.2f} GW facility)")
    print(f"  2. announced_horizon_gw         = {west_horizon_fac:>6.2f} GW facility  "
          f"[{west_range_fac[0]:.2f}, {west_range_fac[1]:.2f}]")
    print(f"  3. raw_non_stretch_gw           = {non_stretch_fac:>6.2f} GW facility  "
          f"(announced − T5; replaces retired 'bear' label)")
    print(f"  4. probability_weighted_gw      = {framework_fac['probability_weighted_gw']:>6.2f} GW facility  "
          f"(tier-default midpoints)")
    print(f"  5. conservative_case_gw         = {framework_fac['conservative_case_gw']:>6.2f} GW facility  "
          f"(T1+T2+T3 only)")
    print(f"  6. full_realization_gw          = {full_real_fac:>6.2f} GW facility  "
          f"(arithmetic ceiling)")
    print(f"  7. named_dollar_commitments_subtotal_usd_b = {capital['capex_envelope_usd_b_rough']:>6.1f} $B")
    anatomy_doc = load_anatomy() if ANATOMY_LAYER_COSTS.exists() else {}
    anatomy_total = (
        anatomy_doc.get("aggregate_rollup_facility_mw_2026", {})
        .get("total_all_in_facility_gw_2026", {})
    )
    print(f"     anatomy_capital_envelope_usd_t_central = {anatomy_total.get('capital_envelope_at_raw_horizon_usd_t_central', 1.84)}")
    print(f"     anatomy_capital_envelope_usd_t_range   = [{anatomy_total.get('capital_envelope_at_raw_horizon_usd_t_low', 1.49)}, {anatomy_total.get('capital_envelope_at_raw_horizon_usd_t_high', 2.34)}]")
    print(f"     basis = \"$30-47B/facility-GW × {west_horizon_fac:.3f} GW\"")

    print()
    print("  Sovereign sidebar facility (not in Western denominator):")
    sov_fac_block = totals.get("sovereign_ai_sidebar_horizon_facility", {})
    sov_fac_pt = sov_fac_block.get("total_gw_point", 0.0)
    print(f"    announced_horizon_sov_gw_fac  = {sov_fac_pt:>6.2f} GW facility")

    print()
    print("  Per-row Class A facility-basis probability-weighted detail (Western only):")
    for r in class_a_rows_fac:
        print(
            f"    [{r['tier']}] {r['id']:<40s}  "
            f"gw_fac={r['gw_point']:>5.3f}  prob={r['prob']:>4.2f}  weighted={r['weighted']:>5.3f}"
        )
    print(f"    SUM Class A Western facility weighted = {class_a_weighted_fac:.3f} GW")

    # ------------------------------------------------------------------
    # SECONDARY: IT-LOAD BRIDGE (rev-2 legacy)
    # ------------------------------------------------------------------
    print()
    print("=" * 70)
    print("SEVEN CANONICAL TOTALS  (IT-load bridge — SECONDARY)")
    print("=" * 70)

    framework = compute_probability_weighted_western(doc)
    class_a_weighted, class_a_rows = compute_per_row_probability_weighted(doc)
    sov_weighted, sov_rows = compute_sovereign_probability_weighted(doc)
    west_horizon = totals["western_horizon_2027_2030"]["total_gw_point"]
    west_range = totals["western_horizon_2027_2030"]["total_gw_range"]

    print(f"  1. operational_today_gw         = {op_today:>6.2f} GW facility primary; see tier block for IT bridge")
    print(f"  2. announced_horizon_gw         = {west_horizon:>6.2f} GW  "
          f"[{west_range[0]:.2f}, {west_range[1]:.2f}]  (IT-load bridge)")
    print(f"  3. probability_weighted_gw      = {framework['probability_weighted_gw']:>6.2f} GW  "
          f"(tier-default midpoints)")
    print(f"  4. conservative_case_gw         = {framework['conservative_case_gw']:>6.2f} GW  "
          f"(T1+T2+T3 only)")
    print(f"  5. full_realization_gw          = {west_range[1]:>6.2f} GW  "
          f"(arithmetic ceiling)")
    print(f"  6. named_dollar_commitments_subtotal_usd_b = {capital['capex_envelope_usd_b_rough']:>6.1f} $B")
    print(f"  7. rpo_obligations_usd_b_rough  = {capital['rpo_contracted_usd_b_rough']:>6.1f} $B")

    print()
    print("  Sovereign sidebar IT (not in Western denominator):")
    sov_point = totals["sovereign_ai_sidebar_horizon"]["total_gw_point"]
    print(f"    announced_horizon_sov_gw      = {sov_point:>6.2f} GW")
    print(f"    probability_weighted_sov_gw   = {sov_weighted:>6.2f} GW")
    print()


def load_anatomy() -> dict:
    """Load anatomy_layer_costs.yaml (rev-4 unit-economics data layer)."""
    with open(ANATOMY_LAYER_COSTS, "r") as f:
        return yaml.safe_load(f)


def audit_anatomy_layer_costs() -> bool:
    """Audit anatomy_layer_costs.yaml: validate per-sub-component centrals
    sum within tolerance to the layer rollup, and that the aggregate rollup
    × raw horizon reconciles to the rev-4 capital envelope.

    Cross-checks added 2026-04-27 after ultrareview:
    - Skipped layers (those without a single layer_total_..._central)
      are now logged with [SKIP] markers rather than silently dropped.
    - Layer-block centrals are cross-checked against the corresponding
      aggregate_rollup component central, catching drift like
      cooling.layer=3.0 vs rollup.cooling_central=2.75.
    - YAML high/low/central are read from the rollup, not hardcoded
      module-level constants, so the script cannot disagree with the
      data layer it audits.

    Returns True if all anatomy checks pass.
    """
    print("=" * 70)
    print("AUDIT: anatomy_layer_costs.yaml unit-economics consistency")
    print("=" * 70)

    doc = load_anatomy()
    layers = doc.get("layers", [])
    rollup = doc.get("aggregate_rollup_facility_mw_2026", {})

    # Pull canonical totals from the YAML rather than hardcoded constants
    yaml_total_block = rollup.get("total_all_in_facility_gw_2026", {})
    yaml_total_low = yaml_total_block.get("low", ANATOMY_TOTAL_LOW)
    yaml_total_high = yaml_total_block.get("high", ANATOMY_TOTAL_HIGH)
    yaml_total_central = yaml_total_block.get("central_grid_tied", ANATOMY_TOTAL_CENTRAL)

    # Read the canonical Western raw 2027-2030 facility horizon from the
    # overlay YAML — single source of truth, prevents drift between the
    # script's constant and the actual data layer.
    overlay_doc = load_overlay()
    overlay_totals = overlay_doc.get("totals", {})
    raw_horizon_gw = (
        overlay_totals
        .get("western_horizon_2027_2030_facility", {})
        .get("total_gw_point", ANATOMY_RAW_HORIZON_GW_FALLBACK)
    )

    # Map of rollup component centrals (for cross-check against layer blocks)
    facility_only_block = rollup.get("facility_only_no_it", {})
    it_bom_block = rollup.get("it_bom_at_customer", {})
    rollup_component_centrals = {
        "shell_civil_land": facility_only_block.get("shell_civil_land_central"),
        "cooling": facility_only_block.get("cooling_central"),
        "power_infrastructure": facility_only_block.get("power_grid_tied_central"),
        "grid_interconnect": facility_only_block.get("grid_interface_median_central"),
        "accelerator_server_bom": it_bom_block.get("accelerator_server_rack_complete_central"),
        "networking_fabric": it_bom_block.get("networking_out_of_rack_central"),
    }

    all_ok = True

    # --- Per-layer sub-component sum vs declared layer central ---
    print()
    print("Per-layer sub-component sum vs declared layer central:")

    for layer in layers:
        lid = layer.get("layer_id", "?")
        sub_components = layer.get("sub_components", [])
        if not sub_components:
            continue

        # Skip sub-components flagged as alternates or already-counted-elsewhere
        sub_central_sum = sum(
            sc.get("cost_usd_m_per_mw_central", 0.0)
            for sc in sub_components
            if sc.get("count_in_layer_sum", True)
        )

        declared = layer.get("layer_total_usd_m_per_mw_central")
        if declared is None:
            # Layer carries variant centrals (grid-tied/BTM, chip-only/rack-complete, posture envelopes)
            # rather than a single canonical layer_total_..._central. Show as SKIP so the user knows.
            variants = [
                k for k in layer.keys()
                if k.startswith("layer_total_usd_m_per_mw_central_") or k == "posture_envelopes"
            ]
            print(f"  [SKIP] {lid:30s}  no single layer_total_..._central; variants: {','.join(variants) or 'none'}")
            continue

        diff = abs(sub_central_sum - declared)
        ok = diff <= ANATOMY_TOL_USD_M_PER_MW
        mark = "OK  " if ok else "FAIL"
        print(f"  [{mark}] {lid:30s}  Σ subs central: {sub_central_sum:6.2f}  declared: {declared:6.2f}  Δ: {diff:5.2f}")
        all_ok &= ok

    # --- Layer-block central vs aggregate-rollup component central (drift detector) ---
    print()
    print("Layer-block central vs aggregate-rollup component central:")
    for layer in layers:
        lid = layer.get("layer_id", "?")
        layer_central = layer.get("layer_total_usd_m_per_mw_central")
        rollup_central = rollup_component_centrals.get(lid)
        if layer_central is None or rollup_central is None:
            continue
        diff = abs(layer_central - rollup_central)
        ok = diff <= ANATOMY_TOL_USD_M_PER_MW
        mark = "OK  " if ok else "FAIL"
        print(f"  [{mark}] {lid:30s}  layer-block: {layer_central:6.2f}  rollup: {rollup_central:6.2f}  Δ: {diff:5.2f}")
        all_ok &= ok

    # --- Aggregate rollup × raw horizon reconciles to capital envelope ---
    facility_only_central = facility_only_block.get("subtotal_central", 0.0)
    it_bom_central = it_bom_block.get("subtotal_central", 0.0)
    total_central_declared = yaml_total_central
    total_central_computed = facility_only_central + it_bom_central

    print()
    print("Aggregate rollup arithmetic:")
    diff = abs(total_central_computed - total_central_declared)
    ok = diff <= ANATOMY_TOL_USD_M_PER_MW
    mark = "OK  " if ok else "FAIL"
    print(f"  [{mark}] facility_only ({facility_only_central:.2f}) + it_bom ({it_bom_central:.2f}) = {total_central_computed:.2f}M/MW")
    print(f"         declared central_grid_tied: {total_central_declared:.2f}M/MW (Δ: {diff:.2f})")
    all_ok &= ok

    # --- Capital envelope at raw horizon (cross-check declared vs computed at low/central/high) ---
    declared_envelope_central = yaml_total_block.get(
        "capital_envelope_at_raw_horizon_usd_t_central", 0.0
    )
    declared_envelope_low = yaml_total_block.get(
        "capital_envelope_at_raw_horizon_usd_t_low", 0.0
    )
    declared_envelope_high = yaml_total_block.get(
        "capital_envelope_at_raw_horizon_usd_t_high", 0.0
    )

    print(f"         (raw horizon read from overlay YAML: {raw_horizon_gw:.3f} GW facility)")
    computed_envelope_central = (total_central_declared * raw_horizon_gw) / 1000.0
    diff = abs(computed_envelope_central - declared_envelope_central)
    ok = diff <= ANATOMY_TOL_USD_T
    mark = "OK  " if ok else "FAIL"
    print(f"  [{mark}] capital envelope central: declared {declared_envelope_central:.2f}T vs computed {computed_envelope_central:.2f}T  (Δ: {diff:.2f})")
    all_ok &= ok

    # Cross-check declared envelope_high against YAML's total_high × horizon
    # (the merged_bug_001 case: yaml.high=47.5 implies $2.47T, not $2.4T)
    computed_envelope_low = (yaml_total_low * raw_horizon_gw) / 1000.0
    computed_envelope_high = (yaml_total_high * raw_horizon_gw) / 1000.0
    high_consistent = abs(computed_envelope_high - declared_envelope_high) <= ANATOMY_TOL_USD_T
    low_consistent = abs(computed_envelope_low - declared_envelope_low) <= ANATOMY_TOL_USD_T
    if not high_consistent:
        print(f"  [FAIL] envelope_high: yaml.high={yaml_total_high} implies {computed_envelope_high:.2f}T vs declared {declared_envelope_high:.2f}T")
        all_ok = False
    if not low_consistent:
        print(f"  [FAIL] envelope_low: yaml.low={yaml_total_low} implies {computed_envelope_low:.2f}T vs declared {declared_envelope_low:.2f}T")
        all_ok = False
    print(f"         arithmetic range: [{computed_envelope_low:.2f}T, {computed_envelope_high:.2f}T]")
    print(f"         declared band:    [{declared_envelope_low:.2f}T, {declared_envelope_high:.2f}T]")

    print()
    print("=" * 70)
    if all_ok:
        print("ANATOMY AUDIT PASSED")
    else:
        print("ANATOMY AUDIT FAILED — anatomy_layer_costs.yaml inconsistency")
    print("=" * 70)
    return all_ok


def audit_stress_scenario_capex(doc: dict) -> bool:
    scenarios = doc.get("stress_scenarios", {})
    all_ok = True
    print()
    print("Stress scenario capex basis check:")
    for key, scenario in scenarios.items():
        if not isinstance(scenario, dict):
            continue
        if "gw_delta_2030" not in scenario or "capex_delta_usd_b" not in scenario:
            continue
        if scenario.get("capex_delta_basis") and "37b_per_gw" not in str(scenario.get("capex_delta_basis")):
            print(f"  [SKIP] {key:42s} declares alternate basis: {scenario.get('capex_delta_basis')}")
            continue
        expected = scenario["gw_delta_2030"] * CAPEX_CENTRAL_USD_B_PER_GW
        got = float(scenario["capex_delta_usd_b"])
        ok = abs(got - expected) <= CAPEX_TOL_USD_B
        mark = "OK  " if ok else "FAIL"
        print(f"  [{mark}] {key:42s} capex={got:7.1f} expected={expected:7.1f}")
        all_ok &= ok
    return all_ok


def audit_neocloud_tier_crossfile(doc: dict, neocloud: dict) -> bool:
    main = doc.get("totals", {}).get("evidence_tier_rollup_western_facility", {})
    cloud = neocloud.get("aggregate_rollup_facility", {}).get("evidence_tier_rollup_facility", {})
    expected_t3 = float(cloud.get("T3_firm_commercial_contract_gw", 0.0))
    expected_t4_delta = float(cloud.get("T4_announced_private_co_gw", 0.0))
    got_t3 = float(main.get("T3_firm_commercial", {}).get("components", {}).get("neocloud_rpo_take_or_pay_contracted", 0.0))
    got_t4_delta = float(main.get("T4_announced_site_plan", {}).get("components", {}).get("neocloud_private_co_contracted", 0.0))
    ok_t3 = abs(got_t3 - expected_t3) <= TOL
    ok_t4 = abs(got_t4_delta - expected_t4_delta) <= TOL
    print()
    print("Neocloud cross-file tier check:")
    print(f"  [{'OK  ' if ok_t3 else 'FAIL'}] T3 main={got_t3:.3f} neocloud_overlay={expected_t3:.3f}")
    print(f"  [{'OK  ' if ok_t4 else 'FAIL'}] T4 main={got_t4_delta:.3f} neocloud_overlay={expected_t4_delta:.3f}")
    return ok_t3 and ok_t4


def audit_h100e_denominator(doc: dict) -> bool:
    totals = doc.get("totals", {})
    horizon = float(totals.get("western_horizon_2027_2030_facility", {}).get("total_gw_point", 0.0))
    scenarios = doc.get("chip_density_scenarios", {})
    all_ok = True
    print()
    print("H100e denominator check:")
    for key, scenario in scenarios.items():
        if not isinstance(scenario, dict) or "total_h100e_2030_m" not in scenario:
            continue
        expected = round(float(scenario["total_h100e_2030_m"]) * 1_000_000 / (horizon * 1000))
        got = int(scenario.get("implied_per_mw_blend_2030", -1))
        ok = math.isclose(got, expected, abs_tol=1)
        mark = "OK  " if ok else "FAIL"
        print(f"  [{mark}] {key:14s} implied={got:4d} expected={expected:4d}")
        all_ok &= ok
    return all_ok


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit compute_commitments_overlay.yaml + anatomy_layer_costs.yaml",
    )
    parser.add_argument(
        "--basis",
        choices=["horizon", "anatomy", "all"],
        default="horizon",
        help="Which audit to run: horizon (default) | anatomy | all",
    )
    args = parser.parse_args()
    basis = args.basis

    if basis == "anatomy":
        return 0 if audit_anatomy_layer_costs() else 1

    doc = load_overlay()
    neocloud = load_neocloud()
    commitments = doc.get("commitments", [])
    totals = doc.get("totals", {})

    print("=" * 70)
    print("AUDIT: compute_commitments_overlay.yaml `totals:` vs per-row sums")
    print("=" * 70)

    all_ok = True

    # --- Western Class A incrementals ---
    west = sum_class_a(commitments, "western")
    west_expected_pt = totals["western_horizon_2027_2030"]["arithmetic"]["class_a_western_incremental_point_gw"]
    west_expected_rng = totals["western_horizon_2027_2030"]["arithmetic"]["class_a_western_incremental_range_gw"]
    all_ok &= compare(
        "Class A western subtotal",
        west,
        (west_expected_pt, west_expected_rng[0], west_expected_rng[1]),
    )

    # --- Sovereign Class A incrementals ---
    sov = add_epoch_sovereign_sidebar_rows(sum_class_a(commitments, "sovereign"), totals)
    sov_pt = totals["sovereign_ai_sidebar_horizon"]["total_gw_point"]
    sov_rng = totals["sovereign_ai_sidebar_horizon"]["total_gw_range"]
    all_ok &= compare(
        "Class A sovereign-AI sidebar subtotal",
        sov,
        (sov_pt, sov_rng[0], sov_rng[1]),
    )

    # --- Western horizon grand total ---
    arith = totals["western_horizon_2027_2030"]["arithmetic"]
    west_grand_computed = (
        round(arith["epoch_buildout_gw"] + west[0] + arith["neocloud_ex_epoch_total_gw"], 2),
        round(arith["epoch_buildout_gw"] + west[1] + arith["neocloud_ex_epoch_total_gw"], 2),
        round(arith["epoch_buildout_gw"] + west[2] + arith["neocloud_ex_epoch_total_gw"], 2),
    )
    west_grand_declared = (
        totals["western_horizon_2027_2030"]["total_gw_point"],
        totals["western_horizon_2027_2030"]["total_gw_range"][0],
        totals["western_horizon_2027_2030"]["total_gw_range"][1],
    )
    all_ok &= compare(
        "Western horizon grand total (epoch + class_a_west + neocloud_ex_epoch)",
        west_grand_computed,
        west_grand_declared,
    )

    # --- Global reference total = Western + Sovereign ---
    global_computed = (
        round(west_grand_declared[0] + sov[0], 2),
        round(west_grand_declared[1] + sov[1], 2),
        round(west_grand_declared[2] + sov[2], 2),
    )
    global_declared = (
        totals["global_reference_horizon_2027_2030"]["total_gw_point"],
        totals["global_reference_horizon_2027_2030"]["total_gw_range"][0],
        totals["global_reference_horizon_2027_2030"]["total_gw_range"][1],
    )
    all_ok &= compare(
        "Global reference horizon total (western + sovereign)",
        global_computed,
        global_declared,
    )

    # --- Operational-today sanity check ---
    op_today = totals["operational_today_2026_q2"]
    op_sum = round(op_today["components"]["epoch_current_gw"] + op_today["components"]["neocloud_ex_epoch_op_gw"], 2)
    op_declared = op_today["total_gw"]
    mark = "OK  " if abs(op_sum - op_declared) <= TOL else "FAIL"
    print(f"  [{mark}] Operational-today total")
    print(f"         epoch_current + neocloud_op = {op_sum}")
    print(f"         YAML total_gw              = {op_declared}")
    all_ok &= mark == "OK  "

    # --- Framing gap sanity check ---
    fg = totals["framing_gap"]
    gap_computed = round(fg["western_horizon_gw"] - fg["operational_today_gw"], 2)
    mark = "OK  " if abs(gap_computed - fg["gap_gw"]) <= TOL else "FAIL"
    print(f"  [{mark}] Framing gap (western_horizon - operational_today)")
    print(f"         re-computed: {gap_computed}")
    print(f"         YAML gap_gw: {fg['gap_gw']}")
    all_ok &= mark == "OK  "

    # --- NEW: six-tier framework sum vs announced horizon ---
    tier_block = totals.get("evidence_tier_rollup_western", {})
    if tier_block:
        tier_sum = sum(
            tier_block[k].get("gw", 0.0)
            for k in tier_block
            if k.startswith("T")
        )
        declared = tier_block.get("total_gw_announced", 0.0)
        mark = "OK  " if abs(tier_sum - declared) <= TOL else "FAIL"
        print(f"  [{mark}] Six-tier framework sum vs declared announced horizon (IT)")
        print(f"         Σ tier GW:              {tier_sum:.2f}")
        print(f"         declared announced:     {declared:.2f}")
        all_ok &= mark == "OK  "

    # --- rev-3: FACILITY-BASIS checks ---
    print()
    print("-" * 70)
    print("rev-3 FACILITY-BASIS audit")
    print("-" * 70)

    # Class A western facility incremental vs declared
    west_fac_block = totals.get("western_horizon_2027_2030_facility", {})
    if west_fac_block:
        west_fac = sum_class_a_facility(commitments, "western")
        arith_fac = west_fac_block.get("arithmetic", {})
        west_fac_exp_pt = arith_fac.get("class_a_western_incremental_point_gw", 0.0)
        west_fac_exp_rng = arith_fac.get("class_a_western_incremental_range_gw", [0.0, 0.0])
        all_ok &= compare(
            "Class A western facility subtotal",
            west_fac,
            (west_fac_exp_pt, west_fac_exp_rng[0], west_fac_exp_rng[1]),
        )

        # Western horizon facility grand total
        west_grand_fac_computed = (
            round(arith_fac["epoch_buildout_gw"] + west_fac[0] + arith_fac["neocloud_ex_epoch_total_gw"], 3),
            round(arith_fac["epoch_buildout_gw"] + west_fac[1] + arith_fac["neocloud_ex_epoch_total_gw"], 3),
            round(arith_fac["epoch_buildout_gw"] + west_fac[2] + arith_fac["neocloud_ex_epoch_total_gw"], 3),
        )
        west_grand_fac_declared = (
            west_fac_block["total_gw_point"],
            west_fac_block["total_gw_range"][0],
            west_fac_block["total_gw_range"][1],
        )
        all_ok &= compare(
            "Western horizon facility grand total",
            west_grand_fac_computed,
            west_grand_fac_declared,
        )

    # Six-tier facility rollup sum
    tier_fac_block = totals.get("evidence_tier_rollup_western_facility", {})
    if tier_fac_block:
        tier_fac_sum = sum(
            tier_fac_block[k].get("gw", 0.0)
            for k in tier_fac_block
            if k.startswith("T")
        )
        declared_fac = tier_fac_block.get("total_gw_announced_facility", 0.0)
        mark = "OK  " if abs(tier_fac_sum - declared_fac) <= TOL else "FAIL"
        print(f"  [{mark}] Six-tier framework sum vs declared announced horizon (facility)")
        print(f"         Σ tier GW_facility:     {tier_fac_sum:.3f}")
        print(f"         declared announced:     {declared_fac:.3f}")
        all_ok &= mark == "OK  "

    # Sovereign facility sidebar sum
    sov_fac_block = totals.get("sovereign_ai_sidebar_horizon_facility", {})
    if sov_fac_block:
        sov_fac_declared = sov_fac_block["total_gw_point"]
        sov_fac_rows_sum = round(sum(sov_fac_block["rows"].values()), 3)
        mark = "OK  " if abs(sov_fac_rows_sum - sov_fac_declared) <= TOL else "FAIL"
        print(f"  [{mark}] Sovereign sidebar facility sum vs declared")
        print(f"         Σ sov rows facility:    {sov_fac_rows_sum:.3f}")
        print(f"         declared sov facility:  {sov_fac_declared:.3f}")
        all_ok &= mark == "OK  "

    all_ok &= audit_stress_scenario_capex(doc)
    all_ok &= audit_neocloud_tier_crossfile(doc, neocloud)
    all_ok &= audit_h100e_denominator(doc)

    print("=" * 70)
    if all_ok:
        print("AUDIT PASSED — `totals:` block matches per-row sums.")
    else:
        print("AUDIT FAILED — update the `totals:` block in the YAML.")

    # Always print the seven canonical totals (informational)
    print_seven_canonical_totals(doc, neocloud)

    # When --basis all, also run the anatomy audit
    if basis == "all":
        print()
        anatomy_ok = audit_anatomy_layer_costs()
        all_ok &= anatomy_ok

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
