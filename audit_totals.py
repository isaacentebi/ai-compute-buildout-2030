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
    python3 audit_totals.py

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

import sys
from pathlib import Path

import yaml  # type: ignore

ROOT = Path(__file__).parent
OVERLAY = ROOT / "compute_commitments_overlay.yaml"
NEOCLOUD = ROOT / "neocloud_overlay.yaml"

# Sovereign-AI row ids. Anything not in this set is treated as Western.
SOVEREIGN_IDS = {
    "microsoft_g42_uae_khazna_2025_11",
    "humain_amd_saudi_2025_05",
    "reliance_jio_jamnagar_2024_08",
    "uk_culham_ai_growth_zone_2025_01",
}

TOL = 0.02  # GW tolerance for rounding (20 MW)

# Tier-default realization probabilities (midpoints of plan-specified ranges)
TIER_DEFAULTS = {
    "T1": 1.00,
    "T2": 0.88,
    "T3": 0.78,
    "T4": 0.58,
    "T5": 0.32,
    "T6": 0.25,
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
    """Re-sum Class A rows for a given scope. Returns (point, low, high)."""
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
        r = c.get("incremental_gw_range") or [None, None]
        if p is not None:
            point += p
        if r[0] is not None:
            low += r[0]
        if r[1] is not None:
            high += r[1]
    return round(point, 2), round(low, 2), round(high, 2)


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
    return round(total_weighted, 2), rows


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
    print()
    print("=" * 70)
    print("SEVEN CANONICAL TOTALS  (six-tier evidence framework, Western)")
    print("=" * 70)

    totals = doc.get("totals", {})
    op_today = totals["operational_today_2026_q2"]["total_gw"]

    # Framework-level rollup
    framework = compute_probability_weighted_western(doc)
    # Per-row Class A weighted (for drift detection vs framework)
    class_a_weighted, class_a_rows = compute_per_row_probability_weighted(doc)
    sov_weighted, sov_rows = compute_sovereign_probability_weighted(doc)
    capital = compute_capital_envelope(doc)

    west_horizon = totals["western_horizon_2027_2030"]["total_gw_point"]
    west_range = totals["western_horizon_2027_2030"]["total_gw_range"]

    print(f"  1. operational_today_gw         = {op_today:>6.2f} GW  (T1)")
    print(f"  2. announced_horizon_gw         = {west_horizon:>6.2f} GW  "
          f"[{west_range[0]:.2f}, {west_range[1]:.2f}]")
    print(f"  3. probability_weighted_gw      = {framework['probability_weighted_gw']:>6.2f} GW  "
          f"(tier-default midpoints)")
    print(f"  4. conservative_case_gw         = {framework['conservative_case_gw']:>6.2f} GW  "
          f"(T1+T2+T3 only)")
    print(f"  5. full_realization_gw          = {west_range[1]:>6.2f} GW  "
          f"(arithmetic ceiling)")
    print(f"  6. capital_envelope_usd_b       = {capital['capex_envelope_usd_b_rough']:>6.1f} $B  "
          f"(rough; A.7 will refine)")
    print(f"  7. rpo_obligations_usd_b_rough  = {capital['rpo_contracted_usd_b_rough']:>6.1f} $B  "
          f"(rough; A.7 will refine)")

    print()
    print("  Sovereign sidebar (not in Western denominator):")
    sov_point = totals["sovereign_ai_sidebar_horizon"]["total_gw_point"]
    print(f"    announced_horizon_sov_gw      = {sov_point:>6.2f} GW")
    print(f"    probability_weighted_sov_gw   = {sov_weighted:>6.2f} GW")

    print()
    print("  Per-row Class A probability-weighted detail (Western only):")
    for r in class_a_rows:
        print(
            f"    [{r['tier']}] {r['id']:<40s}  "
            f"gw={r['gw_point']:>5.2f}  prob={r['prob']:>4.2f}  weighted={r['weighted']:>5.3f}"
        )
    print(f"    SUM Class A Western weighted = {class_a_weighted:.2f} GW")
    print()


def main() -> int:
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
    sov = sum_class_a(commitments, "sovereign")
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
        print(f"  [{mark}] Six-tier framework sum vs declared announced horizon")
        print(f"         Σ tier GW:              {tier_sum:.2f}")
        print(f"         declared announced:     {declared:.2f}")
        all_ok &= mark == "OK  "

    print("=" * 70)
    if all_ok:
        print("AUDIT PASSED — `totals:` block matches per-row sums.")
    else:
        print("AUDIT FAILED — update the `totals:` block in the YAML.")

    # Always print the seven canonical totals (informational)
    print_seven_canonical_totals(doc, neocloud)

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
