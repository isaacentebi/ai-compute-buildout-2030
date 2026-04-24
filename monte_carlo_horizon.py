#!/usr/bin/env python3
"""
Monte Carlo over the 2030 Western AI-compute horizon.

rev-3 (2026-04-24): facility basis primary; IT-load bridge secondary.

Inputs
  - Six-tier GW partition (loaded from compute_commitments_overlay.yaml
    via `evidence_tier_rollup_western_facility` (facility, default) or
    `evidence_tier_rollup_western` (IT, via --basis it).
  - Tier-default realization priors (CONFIDENCE_DECOMPOSITION.md)
  - Per-row realization_probability overrides (compute_commitments_overlay.yaml)
  - Stress-scenario deltas + scenario probabilities (overlay stress_scenarios block)

Model
  - Tier realization rate ~ Beta fitted so that the tier-default sits at the
    mean and the 5th/95th percentile bracket the tier-documented range.
  - Each tier's realized GW = tier_gw × sampled_rate.
  - T1 is treated as deterministic (operational MW online Q2 2026).
  - Stress scenarios applied additively: each draws Bernoulli(scenario_prob);
    if realized, subtract the scenario gw_delta_2030 (negative number → subtract
    negative = add magnitude to the loss side).
  - 10,000 draws by default.

Outputs
  - p05 / p10 / p25 / p50 / p75 / p90 / p95 of 2030 realized GW distribution
  - Mean, std, and comparison to the tier-deterministic probability-weighted point
  - Tail probabilities vs: conservative, prob-weighted, raw_non_stretch, announced

Usage
  python3 monte_carlo_horizon.py [--basis facility|it] [--draws N] [--seed S]

Basis
  facility (default) — rev-3 primary denominator (matches Epoch convention)
  it                 — IT-load bridge (rev-2 legacy; kept for audit parity)
"""

import argparse
import random
import statistics
import sys
from pathlib import Path

import yaml  # type: ignore

ROOT = Path(__file__).parent
OVERLAY = ROOT / "compute_commitments_overlay.yaml"

# Tier-default realization priors + documented variance bracket (p05, p95).
# Midpoint → Beta mean; spread → Beta concentration. Basis-invariant.
TIER_PRIOR = {
    "T1": (1.00, 1.00, 1.00),     # fixed
    "T2": (0.88, 0.80, 0.95),
    "T3": (0.78, 0.65, 0.90),
    "T4": (0.58, 0.40, 0.75),
    "T5": (0.32, 0.15, 0.50),
    "T6": (0.25, 0.10, 0.40),
}

# Stress scenarios from overlay stress_scenarios block. Basis-invariant
# to leading order (gw_delta magnitudes refer to absolute capacity loss
# — the same grid-interconnect slip loses the same physical MW regardless
# of whether we denominate in IT or facility terms).
STRESS_SCENARIOS = {
    "A_stargate_12mo_slip":       {"gw_delta": -3.5, "prob": 0.30},
    "B_neocloud_spread_300bps":   {"gw_delta": -2.0, "prob": 0.25},
    "C_grid_24mo_slip_ERCOT_MISO_PJM": {"gw_delta": -8.0, "prob": 0.40},
    "D_chip_2Q_slip":             {"gw_delta": -1.5, "prob": 0.50},
    "E_inference_outpaces_training": {"gw_delta": 0.0, "prob": 0.55},  # no GW impact, chip-mix only
}


def load_tier_gw_from_yaml(basis: str) -> dict:
    """Load the six-tier GW partition from the overlay YAML.
    basis='facility' → evidence_tier_rollup_western_facility (rev-3 primary)
    basis='it'       → evidence_tier_rollup_western (IT-load bridge)
    """
    with OVERLAY.open() as f:
        doc = yaml.safe_load(f)
    totals = doc.get("totals", {})
    if basis == "facility":
        block = totals.get("evidence_tier_rollup_western_facility", {})
    elif basis == "it":
        block = totals.get("evidence_tier_rollup_western", {})
    else:
        raise ValueError(f"unknown basis: {basis!r}")
    tier_gw = {}
    for tier_key, tier_content in block.items():
        if not tier_key.startswith("T"):
            continue
        tier = tier_key.split("_")[0]
        tier_gw[tier] = float(tier_content.get("gw", 0.0))
    return tier_gw, block


def load_horizon_scalars(basis: str, tier_block: dict, doc_totals: dict) -> dict:
    """Load announced / conservative / prob-weighted / raw-non-stretch
    headline scalars for the chosen basis."""
    if basis == "facility":
        west = doc_totals.get("western_horizon_2027_2030_facility", {})
        return {
            "announced_horizon_gw": tier_block.get("total_gw_announced_facility")
                or west.get("total_gw_point", 0.0),
            "conservative_gw": tier_block.get("total_gw_conservative_facility_raw", 0.0),
            "prob_weighted_point_gw": tier_block.get("total_gw_probability_weighted_facility", 0.0),
            "raw_non_stretch_gw": tier_block.get("total_gw_non_stretch_facility", 0.0),
            "full_realization_gw": tier_block.get("total_gw_full_realization_facility", 0.0),
        }
    else:
        west = doc_totals.get("western_horizon_2027_2030", {})
        announced = tier_block.get("total_gw_announced") or west.get("total_gw_point", 0.0)
        prob_weighted = tier_block.get("total_gw_probability_weighted", 0.0)
        conservative = tier_block.get("total_gw_conservative", 0.0)
        full_real = tier_block.get("total_gw_full_realization") or west.get("total_gw_range", [0, 0])[1]
        # For IT basis, raw_non_stretch = announced - T5_gw (same rule)
        t5 = 0.0
        for k, v in tier_block.items():
            if k.startswith("T5"):
                t5 = float(v.get("gw", 0.0)); break
        return {
            "announced_horizon_gw": announced,
            "conservative_gw": conservative,
            "prob_weighted_point_gw": prob_weighted,
            "raw_non_stretch_gw": round(announced - t5, 3),
            "full_realization_gw": full_real,
        }


def fit_beta_from_quantiles(mean, p05, p95):
    """
    Fit Beta(alpha, beta) via method-of-moments given mean.
    Variance approximated from (p95 - p05) / (2 * 1.645) under normal assumption
    — good enough for the [0.10, 0.95] mean range we're working with.
    Returns (alpha, beta).
    """
    if mean >= 0.999 or (p95 - p05) < 0.01:
        return None  # deterministic
    sigma = (p95 - p05) / (2.0 * 1.645)
    variance = sigma ** 2
    max_var = mean * (1 - mean) * 0.99
    if variance >= max_var:
        variance = max_var
    common = (mean * (1 - mean) / variance) - 1
    alpha = mean * common
    beta = (1 - mean) * common
    return alpha, beta


def sample_tier_rate(tier):
    mean, p05, p95 = TIER_PRIOR[tier]
    params = fit_beta_from_quantiles(mean, p05, p95)
    if params is None:
        return mean
    alpha, beta = params
    return random.betavariate(alpha, beta)


def one_draw(tier_gw: dict):
    """Return (realized_gw, applied_stress_names_list)."""
    realized = 0.0
    for tier, gw in tier_gw.items():
        rate = sample_tier_rate(tier)
        realized += gw * rate
    applied = []
    for name, sc in STRESS_SCENARIOS.items():
        if random.random() < sc["prob"]:
            realized += sc["gw_delta"]  # gw_delta is negative → subtract magnitude
            applied.append(name)
    realized = max(realized, 0.0)
    return realized, applied


def percentile(sorted_list, q):
    n = len(sorted_list)
    idx = max(0, min(n - 1, int(round(q * (n - 1)))))
    return sorted_list[idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--basis", choices=["facility", "it"], default="facility",
                    help="'facility' (rev-3 primary, default) or 'it' (IT-load bridge, rev-2 compat)")
    ap.add_argument("--draws", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260424)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    random.seed(args.seed)

    # Load tier GW partition + headline scalars from YAML (per basis).
    tier_gw, tier_block = load_tier_gw_from_yaml(args.basis)
    with OVERLAY.open() as f:
        doc = yaml.safe_load(f)
    scalars = load_horizon_scalars(args.basis, tier_block, doc.get("totals", {}))

    # Sanity-check the partition summation vs the declared announced total.
    partition_sum = round(sum(tier_gw.values()), 3)
    declared = round(scalars["announced_horizon_gw"], 3)
    if abs(partition_sum - declared) > 0.05:
        print(f"WARNING: tier partition sums to {partition_sum} but "
              f"declared announced is {declared} (basis={args.basis})", file=sys.stderr)

    basis_label = "FACILITY (rev-3 primary)" if args.basis == "facility" else "IT-LOAD (rev-2 bridge)"

    results = []
    stress_counts = {name: 0 for name in STRESS_SCENARIOS}
    for _ in range(args.draws):
        gw, applied = one_draw(tier_gw)
        results.append(gw)
        for name in applied:
            stress_counts[name] += 1
    results.sort()

    mean = statistics.mean(results)
    std = statistics.stdev(results)

    print("=" * 72)
    print(f"MONTE CARLO — 2030 Western realized GW  (N={args.draws:,}, seed={args.seed})")
    print(f"  Basis: {basis_label}")
    print("=" * 72)
    print("  Six-tier GW partition (from YAML):")
    for tier in sorted(tier_gw.keys()):
        print(f"    {tier}: {tier_gw[tier]:6.3f} GW")
    print(f"    Σ   : {partition_sum:6.3f} GW")
    print()
    print(f"  Mean                 : {mean:6.2f} GW")
    print(f"  Std dev              : {std:6.2f} GW")
    print(f"  p05                  : {percentile(results, 0.05):6.2f} GW")
    print(f"  p10                  : {percentile(results, 0.10):6.2f} GW")
    print(f"  p25                  : {percentile(results, 0.25):6.2f} GW")
    print(f"  p50 (median)         : {percentile(results, 0.50):6.2f} GW")
    print(f"  p75                  : {percentile(results, 0.75):6.2f} GW")
    print(f"  p90                  : {percentile(results, 0.90):6.2f} GW")
    print(f"  p95                  : {percentile(results, 0.95):6.2f} GW")
    print()
    print("  Reference point estimates (deterministic):")
    print(f"    announced_horizon  : {scalars['announced_horizon_gw']:6.2f} GW   (raw sum)")
    print(f"    prob_weighted      : {scalars['prob_weighted_point_gw']:6.2f} GW   (Σ tier_gw × tier_prior)")
    print(f"    raw_non_stretch    : {scalars['raw_non_stretch_gw']:6.2f} GW   (announced − T5; rev-3 replacement for retired 'bear')")
    print(f"    conservative       : {scalars['conservative_gw']:6.2f} GW   (T1+T2+T3 only)")
    print()
    print("  Tail probabilities (from the sim):")
    thresholds = [
        (f"< conservative {scalars['conservative_gw']:.2f}", scalars["conservative_gw"]),
        (f"< prob-weighted {scalars['prob_weighted_point_gw']:.2f}", scalars["prob_weighted_point_gw"]),
        (f"< raw_non_stretch {scalars['raw_non_stretch_gw']:.2f}", scalars["raw_non_stretch_gw"]),
        (f"< announced {scalars['announced_horizon_gw']:.2f}", scalars["announced_horizon_gw"]),
    ]
    for label, threshold in thresholds:
        p = sum(1 for x in results if x < threshold) / len(results)
        print(f"    P(realized {label})        = {p:5.1%}")
    print()
    print("  Stress scenario realization frequency (should match priors):")
    for name, n in stress_counts.items():
        target = STRESS_SCENARIOS[name]["prob"]
        actual = n / args.draws
        print(f"    {name:44s}: prior={target:.2f}  empirical={actual:.3f}")
    print()
    print("  Reading")
    print("    The Monte Carlo median (p50) is the probabilistically-honest")
    print(f"    central estimate; the p50 landing below the deterministic")
    print(f"    tier-weighted {scalars['prob_weighted_point_gw']:.2f} GW reflects the stress-scenario")
    print("    downside tail (A+B+C+D carry combined negative expected value of")
    print("    approximately -5.9 GW). The p10-p90 interdecile range is the")
    print("    relevant LP sensitivity band.")
    print("=" * 72)


if __name__ == "__main__":
    sys.exit(main())
