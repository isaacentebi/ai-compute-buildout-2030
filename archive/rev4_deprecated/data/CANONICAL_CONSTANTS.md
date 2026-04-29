# Rev-4.4 Canonical Constants

All current-facing manuscript, README, audit, Monte Carlo, and confidence-decomposition values resolve to this block. Historical values (Rev-3, Rev-4.1, Rev-4.2, Rev-4.3) belong only in clearly labeled changelog or reconciliation contexts.

**Single source of truth**: `row_level_audit.csv` (atom ledger) → `canonical_totals.json` (generated scalars). Every printable figure in this file is reproducible from those two artifacts.

## Final Constants

| Quantity | Exact | Manuscript rounded |
|---|---:|---:|
| operational_today_gw_facility | 6.769 | 6.77 |
| tier_clean_T1_operational_gw_facility | 6.519 | 6.52 |
| raw_western_horizon_gw_facility | 47.901 | 47.9 |
| raw_western_horizon_range_gw_facility_low | 39.520 | 39.5 |
| raw_western_horizon_range_gw_facility_high | 54.210 | 54.2 |
| raw_western_horizon_gw_it_bridge | 40.878 | 40.9 |
| raw_non_stretch_gw_facility | 39.044 | 39.0 |
| conservative_T1_T2_T3_raw_gw_facility | 22.927 | 22.9 |
| conservative_T1_T2_T3_probability_weighted_gw_facility | 20.508 | 20.5 |
| deterministic_probability_weighted_gw_facility | 32.582 | 32.6 |
| full_realization_ceiling_gw_facility | 54.210 | 54.2 |
| sovereign_sidebar_gw_facility | 4.960 | 4.96 |
| capital_envelope_usd_t_central | 1.772 | 1.77 |
| capital_envelope_usd_t_low | 1.437 | 1.44 |
| capital_envelope_usd_t_high | 2.251 | 2.25 |
| monte_carlo_p05_gw_facility | 19.395 | 19.4 |
| monte_carlo_p10_gw_facility | 20.855 | 20.9 |
| monte_carlo_p25_gw_facility | 23.908 | 23.9 |
| monte_carlo_p50_gw_facility | 28.829 | 28.8 |
| monte_carlo_p75_gw_facility | 32.465 | 32.5 |
| monte_carlo_p90_gw_facility | 34.664 | 34.7 |
| monte_carlo_p95_gw_facility | 35.855 | 35.9 |
| monte_carlo_mean_gw_facility | 28.181 | 28.2 |
| monte_carlo_std_dev_gw_facility | 5.287 | 5.29 |

## Six-Tier Facility Split (Western raw horizon, 67 atoms)

Tier sums and probability weighting are atom-derived from `row_level_audit.csv` rows where `included_in_western_raw_horizon=true`. Default tier probabilities (T1=1.00, T2=0.88, T3=0.78, T4=0.58, T5=0.32, T6=0.25) reproduce the deterministic 32.582 GW.

| Tier | Atoms | GW facility (low / central / high) | Default probability | Weighted GW |
|---|---:|---:|---:|---:|
| T1 operational | 22 | 6.519 / 6.519 / 6.519 | 1.00 | 6.519 |
| T2 physically evidenced | 19 | 11.888 / 11.908 / 12.218 | 0.88 | 10.479 |
| T3 firm commercial | 3 | 4.500 / 4.500 / 4.500 | 0.78 | 3.510 |
| T4 announced site plan | 13 | 13.810 / 15.789 / 18.316 | 0.58 | 9.158 |
| T5 LOI / stretch | 7 | 2.553 / 8.857 / 12.147 | 0.32 | 2.834 |
| T6 analyst inference | 3 | 0.250 / 0.328 / 0.510 | 0.25 | 0.082 |
| **Total Western raw horizon** | **67** | **39.520 / 47.901 / 54.210** |  | **32.582** |

## Sovereign Sidebar (separate, NOT in Western denominator)

The sovereign sidebar aggregates 9 included atoms (all carry `sovereign_sidebar=true` and `included_in_western_raw_horizon=false` in `row_level_audit.csv`). One additional row, `digital_connexion_vizag_1gw_overlap`, also carries `sovereign_sidebar=true` but is tier `excluded` and represents the Reliance/Andhra dedupe overlap; it is excluded from the 4.960 GW total. Filters that compute the sovereign sidebar must drop tier=`excluded`.

| Quantity | Value |
|---|---:|
| sovereign_sidebar_gw_facility (9 included atoms) | 4.960 |
| sovereign_sidebar_excluded_overlap_gw_facility | 1.000 |

## Historical Comparison

| Quantity | Rev-4.1 | Rev-4.3 | Rev-4.4 | Net delta vs Rev-4.1 |
|---|---:|---:|---:|---:|
| raw_western_horizon_gw_facility | 49.813 | 47.901 | 47.901 | -1.912 |
| deterministic_probability_weighted_gw_facility | 35.143 | 32.582 | 32.582 | -2.561 |
| conservative_T1_T2_T3_raw_gw_facility | 26.262 | 22.927 | 22.927 | -3.335 |
| full_realization_ceiling_gw_facility | 53.115 | 54.210 | 54.210 | +1.095 |
| sovereign_sidebar_gw_facility | 3.960 | 4.960 | 4.960 | +1.000 |
| capital_envelope_usd_t_central | 1.843 | 1.772 | 1.772 | -0.071 |

Capex basis: all physical-capacity scenario capex deltas use $37B/facility-GW (paper-adopted central) unless explicitly labeled chip-mix or silicon-only. The bottoms-up grid-tied unit cost in `anatomy_layer_costs.yaml` is $37.45B/GW; the rounded $37B/GW used in headline arithmetic is the basis cheat-sheet rounding adopted in §3.
