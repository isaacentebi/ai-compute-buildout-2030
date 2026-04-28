# Rev-4.1 Canonical Constants

All current-facing manuscript, README, audit, Monte Carlo, and confidence-decomposition values should resolve to this block. Historical Rev-3 values belong only in clearly labeled changelog or reconciliation contexts.

## Final Constants

| Quantity | Exact | Manuscript rounded |
|---|---:|---:|
| operational_today_gw_facility | 7.619 | 7.62 |
| tier_clean_T1_operational_gw_facility | 7.369 | 7.37 |
| raw_western_horizon_gw_facility | 49.813 | 49.8 |
| raw_western_horizon_range_gw_facility_low | 44.396 | 44.4 |
| raw_western_horizon_range_gw_facility_high | 53.115 | 53.1 |
| raw_western_horizon_gw_it_bridge | 42.467 | 42.5 |
| raw_non_stretch_gw_facility | 43.066 | 43.1 |
| conservative_T1_T2_T3_raw_gw_facility | 26.262 | 26.3 |
| conservative_T1_T2_T3_probability_weighted_gw_facility | 23.346 | 23.3 |
| deterministic_probability_weighted_gw_facility | 35.143 | 35.1 |
| full_realization_ceiling_gw_facility | 53.115 | 53.1 |
| sovereign_sidebar_gw_facility | 3.960 | 4.0 |
| sovereign_sidebar_gw_it_bridge | 3.117 | 3.1 |
| sovereign_sidebar_probability_weighted_gw_facility | 1.834 | 1.8 |
| capital_envelope_usd_t_central | 1.843 | 1.84 |
| capital_envelope_usd_t_low | 1.494 | 1.49 |
| capital_envelope_usd_t_high | 2.341 | 2.34 |
| monte_carlo_p05_gw_facility | 21.926 | 21.9 |
| monte_carlo_p10_gw_facility | 23.445 | 23.4 |
| monte_carlo_p25_gw_facility | 26.470 | 26.5 |
| monte_carlo_p50_gw_facility | 31.406 | 31.4 |
| monte_carlo_p75_gw_facility | 35.036 | 35.0 |
| monte_carlo_p90_gw_facility | 37.234 | 37.2 |
| monte_carlo_p95_gw_facility | 38.409 | 38.4 |
| monte_carlo_mean_gw_facility | 30.743 | 30.7 |
| monte_carlo_std_dev_gw_facility | 5.290 | 5.3 |

## Six-Tier Facility Split

| Tier | GW facility | Default probability | Weighted GW |
|---|---:|---:|---:|
| T1 operational | 7.369 | 1.00 | 7.369 |
| T2 physically evidenced | 12.413 | 0.88 | 10.923 |
| T3 firm commercial | 6.480 | 0.78 | 5.054 |
| T4 announced site plan | 16.476 | 0.58 | 9.556 |
| T5 LOI / stretch | 6.747 | 0.32 | 2.159 |
| T6 analyst inference | 0.328 | 0.25 | 0.082 |
| **Total** | **49.813** |  | **35.143** |

## Historical Comparison

| Quantity | Previous current-facing value | Final Rev-4.1 value | Delta |
|---|---:|---:|---:|
| raw_western_horizon_gw_facility | 51.427 | 49.813 | -1.614 |
| deterministic_probability_weighted_gw_facility | 36.162 | 35.143 | -1.019 |
| conservative_T1_T2_T3_raw_gw_facility | 26.465 | 26.262 | -0.203 |
| full_realization_ceiling_gw_facility | 54.724 | 53.115 | -1.609 |
| sovereign_sidebar_gw_facility | 2.560 | 3.960 | +1.400 |

Stress capex basis: all physical-capacity stress scenario capex deltas use $37B/facility-GW unless explicitly labeled as chip-mix or silicon-only.
