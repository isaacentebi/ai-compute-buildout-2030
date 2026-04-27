#!/usr/bin/env python3
"""
Monte Carlo over the 2030 Western AI-compute horizon.

Inputs
  - Six-tier GW partition (loaded from compute_commitments_overlay.yaml
    via `evidence_tier_rollup_western_facility` (facility, default) or
    `evidence_tier_rollup_western` (IT, via --basis it).
  - Tier-default realization priors (CONFIDENCE_DECOMPOSITION.md)
  - Per-row realization_probability overrides (compute_commitments_overlay.yaml)
  - Downside, upside, demand-stress, and systemic-infrastructure scenarios

Model
  - Tier realization rate ~ Beta fitted so that the tier-default sits at the
    mean and the 5th/95th percentile bracket the tier-documented range.
  - Each tier's realized GW = tier_gw × sampled_rate.
  - T1 is treated as deterministic (operational MW online Q2 2026).
  - A systemic infrastructure-stress state fires first. If it fires, A+B+C are
    represented by a single -10.5 GW combined delta and are not independently
    sampled in that draw.
  - If systemic stress does not fire, A and C fire independently with conditional
    probabilities calibrated to preserve their approximate unconditional priors.
  - Demand/RPO stress F is sampled separately. If F fires, it subtracts -2.5 GW
    and raises the standalone B neocloud-financing probability to 0.60 in that
    draw; otherwise B uses the normal non-systemic conditional probability.
  - Upside scenarios U1-U3 add facility GW. U4 affects H100e only and is tracked
    but does not change facility-power GW.
  - 10,000 draws by default.

Outputs
  - p05 / p10 / p25 / p50 / p75 / p90 / p95 of 2030 realized GW distribution
  - Mean, std, and comparison to the tier-deterministic probability-weighted point
  - Tail probabilities vs: conservative, prob-weighted, raw_non_stretch, announced

Usage
  python3 monte_carlo_horizon.py [--basis facility|it] [--draws N] [--seed S]

Basis
  facility (default) — primary denominator (matches Epoch convention)
  it                 — IT-load bridge (kept for audit parity)
"""

import argparse
import json
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

T4_SENSITIVITY_PRIORS = {
    0.45: (0.45, 0.30, 0.60),
    0.58: (0.58, 0.40, 0.75),
    0.70: (0.70, 0.55, 0.85),
}

P_SYSTEMIC = 0.15
P_DEMAND_RPO = 0.15

# Conditional probabilities if systemic stress does not fire. These preserve
# the current A/B/C priors before the demand-stress correlation is layered in.
P_A_IF_NO_SYSTEMIC = (0.30 - P_SYSTEMIC) / (1.0 - P_SYSTEMIC)
P_B_IF_NO_SYSTEMIC = (0.25 - P_SYSTEMIC) / (1.0 - P_SYSTEMIC)
P_C_IF_NO_SYSTEMIC = (0.40 - P_SYSTEMIC) / (1.0 - P_SYSTEMIC)

SCENARIOS = {
    "S_systemic_infrastructure_stress": {"gw_delta": -10.5, "prob": P_SYSTEMIC, "h100e_delta": -25.0},
    "A_stargate_12mo_slip": {"gw_delta": -3.5, "prob": P_A_IF_NO_SYSTEMIC, "h100e_delta": -8.0},
    "B_neocloud_spread_300bps": {"gw_delta": -2.0, "prob": P_B_IF_NO_SYSTEMIC, "h100e_delta": -4.0},
    "C_grid_24mo_slip_ERCOT_MISO_PJM": {"gw_delta": -8.0, "prob": P_C_IF_NO_SYSTEMIC, "h100e_delta": -18.0},
    "D_chip_2Q_slip": {"gw_delta": -1.5, "prob": 0.50, "h100e_delta": -12.0},
    "E_inference_outpaces_training": {"gw_delta": 0.0, "prob": 0.55, "h100e_delta": -5.0},
    "F_lab_revenue_rpo_stress": {"gw_delta": -2.5, "prob": P_DEMAND_RPO, "h100e_delta": -5.0},
    "U1_grid_interconnection_acceleration": {"gw_delta": 2.0, "prob": 0.20, "h100e_delta": 4.0},
    "U2_neocloud_financing_open": {"gw_delta": 1.5, "prob": 0.20, "h100e_delta": 3.0},
    "U3_t4_over_realization": {"gw_delta": 2.25, "prob": 0.15, "h100e_delta": 5.0},
    "U4_silicon_acceleration": {"gw_delta": 0.0, "prob": 0.25, "h100e_delta": 10.0},
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


def sample_tier_rate(tier, t4_prior=None):
    mean, p05, p95 = t4_prior if tier == "T4" and t4_prior else TIER_PRIOR[tier]
    params = fit_beta_from_quantiles(mean, p05, p95)
    if params is None:
        return mean
    alpha, beta = params
    return random.betavariate(alpha, beta)


def one_draw(tier_gw: dict, t4_prior=None):
    """Return (realized_gw, applied_scenario_names_list, h100e_delta_m)."""
    realized = 0.0
    for tier, gw in tier_gw.items():
        rate = sample_tier_rate(tier, t4_prior=t4_prior)
        realized += gw * rate
    applied = []
    h100e_delta = 0.0

    systemic = random.random() < P_SYSTEMIC
    if systemic:
        sc = SCENARIOS["S_systemic_infrastructure_stress"]
        realized += sc["gw_delta"]
        h100e_delta += sc["h100e_delta"]
        applied.append("S_systemic_infrastructure_stress")
    else:
        for name, prob in (
            ("A_stargate_12mo_slip", P_A_IF_NO_SYSTEMIC),
            ("C_grid_24mo_slip_ERCOT_MISO_PJM", P_C_IF_NO_SYSTEMIC),
        ):
            if random.random() < prob:
                sc = SCENARIOS[name]
                realized += sc["gw_delta"]
                h100e_delta += sc["h100e_delta"]
                applied.append(name)

    demand = random.random() < P_DEMAND_RPO
    if demand:
        sc = SCENARIOS["F_lab_revenue_rpo_stress"]
        realized += sc["gw_delta"]
        h100e_delta += sc["h100e_delta"]
        applied.append("F_lab_revenue_rpo_stress")

    if not systemic:
        b_prob = 0.60 if demand else P_B_IF_NO_SYSTEMIC
        if random.random() < b_prob:
            sc = SCENARIOS["B_neocloud_spread_300bps"]
            realized += sc["gw_delta"]
            h100e_delta += sc["h100e_delta"]
            applied.append("B_neocloud_spread_300bps")

    for name in (
        "D_chip_2Q_slip",
        "E_inference_outpaces_training",
        "U1_grid_interconnection_acceleration",
        "U2_neocloud_financing_open",
        "U3_t4_over_realization",
        "U4_silicon_acceleration",
    ):
        sc = SCENARIOS[name]
        if random.random() < sc["prob"]:
            realized += sc["gw_delta"]
            h100e_delta += sc["h100e_delta"]
            applied.append(name)

    realized = max(realized, 0.0)
    return realized, applied, h100e_delta


def percentile(sorted_list, q):
    n = len(sorted_list)
    idx = max(0, min(n - 1, int(round(q * (n - 1)))))
    return sorted_list[idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--basis", choices=["facility", "it"], default="facility",
                    help="'facility' (primary, default) or 'it' (IT-load bridge)")
    ap.add_argument("--draws", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260424)
    ap.add_argument("--t4-prob", type=float, default=0.58,
                    help="T4 default mean for sensitivity runs; common values: 0.45, 0.58, 0.70")
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
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

    if args.t4_prob in T4_SENSITIVITY_PRIORS:
        t4_prior = T4_SENSITIVITY_PRIORS[args.t4_prob]
    else:
        spread_low, spread_high = 0.18, 0.17
        t4_prior = (args.t4_prob, max(0.05, args.t4_prob - spread_low), min(0.95, args.t4_prob + spread_high))

    t4_base = TIER_PRIOR["T4"][0]
    t4_gw = tier_gw.get("T4", 0.0)
    scalars["prob_weighted_point_gw"] = (
        float(scalars["prob_weighted_point_gw"]) + t4_gw * (args.t4_prob - t4_base)
    )

    basis_label = "FACILITY (primary)" if args.basis == "facility" else "IT-LOAD bridge"

    results = []
    h100e_deltas = []
    scenario_counts = {name: 0 for name in SCENARIOS}
    for _ in range(args.draws):
        gw, applied, h100e_delta = one_draw(tier_gw, t4_prior=t4_prior)
        results.append(gw)
        h100e_deltas.append(h100e_delta)
        for name in applied:
            scenario_counts[name] += 1
    results.sort()

    mean = statistics.mean(results)
    std = statistics.stdev(results)

    summary = {
        "basis": args.basis,
        "draws": args.draws,
        "seed": args.seed,
        "t4_prob": args.t4_prob,
        "t4_prior": t4_prior,
        "tier_gw": tier_gw,
        "mean": mean,
        "std": std,
        "p05": percentile(results, 0.05),
        "p10": percentile(results, 0.10),
        "p25": percentile(results, 0.25),
        "p50": percentile(results, 0.50),
        "p75": percentile(results, 0.75),
        "p90": percentile(results, 0.90),
        "p95": percentile(results, 0.95),
        "h100e_delta_mean_m": statistics.mean(h100e_deltas),
        "h100e_delta_p50_m": percentile(sorted(h100e_deltas), 0.50),
        "scalars": scalars,
        "scenario_frequency": {name: n / args.draws for name, n in scenario_counts.items()},
    }

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0

    print("=" * 72)
    print(f"MONTE CARLO — 2030 Western realized GW  (N={args.draws:,}, seed={args.seed})")
    print(f"  Basis: {basis_label}")
    print(f"  T4 default mean: {args.t4_prob:.2f}  (p05={t4_prior[1]:.2f}, p95={t4_prior[2]:.2f})")
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
    print(f"    raw_non_stretch    : {scalars['raw_non_stretch_gw']:6.2f} GW   (announced - T5; accounting total, not a bear case)")
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
    print("  Scenario realization frequency:")
    for name, n in scenario_counts.items():
        target = SCENARIOS[name]["prob"]
        actual = n / args.draws
        print(f"    {name:44s}: prior={target:.2f}  empirical={actual:.3f}")
    print()
    print("  Reading")
    print("    The Monte Carlo is a probability-weighted realization distribution:")
    print("    it combines tier-level realization uncertainty, named downside shocks,")
    print("    named upside shocks, demand/RPO stress, and a correlated infrastructure")
    print("    stress state. U4 changes H100e only and does not move facility GW.")
    print("=" * 72)


if __name__ == "__main__":
    sys.exit(main())
