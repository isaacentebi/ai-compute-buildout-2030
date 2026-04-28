# Confidence Decomposition (Rev-4.1)

**Current denominator:** Western 2027-2030 horizon = **49.813 GW facility** (rounded to **49.8 GW**), with an IT-load bridge of **42.47 GW** and facility range **[44.40, 53.12] GW**.

**Answer in one line:** **26.3 GW facility** is in T1+T2+T3 (operational, physically evidenced, or firm commercial); **16.5 GW facility** is T4 announced site-level plan; **7.1 GW facility** is T5+T6 stretch or analyst inference. Deterministic tier-weighted realization is **35.1 GW facility**.

## Tier Rollup

| Tier | Interpretation | GW facility | Default realization | Weighted GW |
|---|---|---:|---:|---:|
| T1 | Operational | 7.37 | 1.00 | 7.37 |
| T2 | Under construction / physically evidenced | 12.413 | 0.88 | 10.92 |
| T3 | Firm commercial commitment | 6.48 | 0.78 | 5.05 |
| T4 | Announced site-level plan | 16.48 | 0.58 | 9.56 |
| T5 | LOI / stretch target | 6.747 | 0.32 | 2.16 |
| T6 | Analyst inference | 0.328 | 0.25 | 0.08 |
| **Total** |  | **49.813** |  | **35.143** |

## Canonical Totals

| Metric | Value |
|---|---:|
| Operational today | 7.62 GW facility |
| Tier-clean operational | 7.37 GW facility |
| Raw announced horizon | 49.813 GW facility |
| Raw non-stretch horizon | 43.066 GW facility |
| Conservative T1+T2+T3 raw | 26.262 GW facility |
| Conservative T1+T2+T3 weighted subset | 23.347 GW facility |
| Deterministic tier-weighted | 35.143 GW facility |
| Full-realization ceiling | 53.115 GW facility |
| Sovereign sidebar | 3.96 GW facility |

## Neocloud Correction

Rev-4.1 adopts the `neocloud_overlay.yaml` tier split. Only neocloud capacity backed by RPO / take-or-pay / investment-grade counterparty evidence remains in T3. Nscale, Lambda, and Together contracted capacity are carried in T4 unless future primary evidence supports T3 treatment.

| Neocloud tier contribution | GW facility |
|---|---:|
| T1 operational directly disclosed | 1.29 |
| T3 firm commercial contract | 6.48 |
| T4 announced private-company capacity | 1.47 |
| T6 analyst inference | 0.25 |
| **Total neocloud incremental** | **9.49** |

## Monte Carlo Output

Seed-pinned run: `python3 monte_carlo_horizon.py --basis facility --draws 10000 --seed 20260424`.

| Statistic | GW facility |
|---|---:|
| p05 | 21.9 |
| p10 | 23.4 |
| p25 | 26.5 |
| p50 | 31.4 |
| p75 | 35.0 |
| p90 | 37.2 |
| p95 | 38.4 |
| Mean | 30.74 |
| Std dev | 5.29 |

Tail probabilities: below conservative 26.262 GW = 24.0%; below deterministic weighted 35.143 GW = 75.8%; below raw non-stretch 43.066 GW = 100.0%; below raw announced 49.813 GW = 100.0%.

## Sovereign Sidebar

Sovereign rows are not part of the Western denominator. Stargate UAE is carried as a **1.40 GW facility** T4 row at p=0.58 in the sovereign sidebar, and Microsoft/G42 Khazna is carried as a **0.26 GW facility-equivalent** T4 row at p=0.70. Neither enters the Western denominator.
