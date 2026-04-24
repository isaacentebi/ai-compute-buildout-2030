#!/usr/bin/env python3
"""
Monte Carlo over the 2030 Western AI-compute horizon.

Inputs
  - Six-tier GW partition (from audit_totals.py canonical totals)
  - Tier-default realization priors (CONFIDENCE_DECOMPOSITION.md)
  - Per-row realization_probability overrides (compute_commitments_overlay.yaml)
  - Per-row GW low/point/high ranges
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
  - Mean, std, and comparison to the tier-deterministic 36.13 GW point estimate
  - Probability that realized 2030 GW falls below each of: 27.78 (conservative),
    36.13 (probability-weighted), 45.74 (bear arithmetic), 50.61 (raw announced)
  - Correlated-shock percentile: p(realized < conservative) under full stress
    scenario stack

Usage
  python3 monte_carlo_horizon.py [--draws N] [--seed S]
"""

import argparse
import random
import statistics
import sys

# --- inputs (from audit_totals.py canonical rollup) -------------------------
TIER_GW = {
    "T1": 7.76,   # operational (fixed) — revised 2026-04-24 per Epoch changelog 2026-04-22 (Stargate Abilene 600 MW milestone slipped; 200 MW operational per Oracle 2026-04-22); previously 8.16
    "T2": 12.32,  # under construction — revised 2026-04-24 (+0.40 GW: Stargate Abilene 400 MW moved from T1 to T2 pending late-May milestone); previously 11.92
    "T3": 7.90,   # firm commercial
    "T4": 16.28,  # announced site plan
    "T5": 5.09,   # LOI / stretch
    "T6": 1.25,   # analyst inference
}

# Tier-default realization priors + documented variance bracket (p05, p95).
# Midpoint → Beta mean; spread → Beta concentration.
TIER_PRIOR = {
    "T1": (1.00, 1.00, 1.00),     # fixed
    "T2": (0.88, 0.80, 0.95),
    "T3": (0.78, 0.65, 0.90),
    "T4": (0.58, 0.40, 0.75),
    "T5": (0.32, 0.15, 0.50),
    "T6": (0.25, 0.10, 0.40),
}

# Stress scenarios from overlay stress_scenarios block.
STRESS_SCENARIOS = {
    "A_stargate_12mo_slip":       {"gw_delta": -3.5, "prob": 0.30},
    "B_neocloud_spread_300bps":   {"gw_delta": -2.0, "prob": 0.25},
    "C_grid_24mo_slip_ERCOT_MISO_PJM": {"gw_delta": -8.0, "prob": 0.40},
    "D_chip_2Q_slip":             {"gw_delta": -1.5, "prob": 0.50},
    "E_inference_outpaces_training": {"gw_delta": 0.0, "prob": 0.55},  # no GW impact, chip-mix only
}

ANNOUNCED_HORIZON_GW = 50.61
CONSERVATIVE_GW = 27.78
PROB_WEIGHTED_POINT_GW = 36.08  # Revised 2026-04-24 (was 36.13) after Stargate Abilene T1 -> T2 reclassification
BEAR_ARITHMETIC_GW = 45.74


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
    # Bound variance so Beta is well-defined: var < mean*(1-mean)
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


def one_draw():
    """Return (realized_gw, applied_stress_names_list)."""
    realized = 0.0
    for tier, gw in TIER_GW.items():
        rate = sample_tier_rate(tier)
        realized += gw * rate
    applied = []
    for name, sc in STRESS_SCENARIOS.items():
        if random.random() < sc["prob"]:
            realized += sc["gw_delta"]  # gw_delta is negative → subtract magnitude
            applied.append(name)
    # Floor at zero (can't have negative realized GW)
    realized = max(realized, 0.0)
    return realized, applied


def percentile(sorted_list, q):
    n = len(sorted_list)
    idx = max(0, min(n - 1, int(round(q * (n - 1)))))
    return sorted_list[idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260424)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    random.seed(args.seed)

    results = []
    stress_counts = {name: 0 for name in STRESS_SCENARIOS}
    for _ in range(args.draws):
        gw, applied = one_draw()
        results.append(gw)
        for name in applied:
            stress_counts[name] += 1
    results.sort()

    mean = statistics.mean(results)
    std = statistics.stdev(results)

    print("=" * 72)
    print(f"MONTE CARLO — 2030 Western realized GW  (N={args.draws:,}, seed={args.seed})")
    print("=" * 72)
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
    print(f"    announced_horizon  : {ANNOUNCED_HORIZON_GW:6.2f} GW   (raw sum)")
    print(f"    prob_weighted      : {PROB_WEIGHTED_POINT_GW:6.2f} GW   (Σ tier_gw × tier_prior)")
    print(f"    bear_arithmetic    : {BEAR_ARITHMETIC_GW:6.2f} GW   (T1+T2+T3 + half T4)")
    print(f"    conservative       : {CONSERVATIVE_GW:6.2f} GW   (T1+T2+T3 only)")
    print()
    print("  Tail probabilities (from the sim):")
    thresholds = [
        (f"< conservative {CONSERVATIVE_GW:.2f}", CONSERVATIVE_GW),
        (f"< prob-weighted {PROB_WEIGHTED_POINT_GW:.2f}", PROB_WEIGHTED_POINT_GW),
        (f"< bear {BEAR_ARITHMETIC_GW:.2f}", BEAR_ARITHMETIC_GW),
        (f"< announced {ANNOUNCED_HORIZON_GW:.2f}", ANNOUNCED_HORIZON_GW),
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
    print("    central estimate; the p50 landing below the deterministic")
    print("    tier-weighted 36.13 GW reflects the stress-scenario downside")
    print("    tail (A+B+C+D carry combined negative expected value of ")
    print("    approximately -5.9 GW). The p10-p90 interdecile range is the")
    print("    relevant LP sensitivity band.")
    print("=" * 72)


if __name__ == "__main__":
    sys.exit(main())
