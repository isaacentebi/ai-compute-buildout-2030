# Confidence Decomposition (Rev-4.1)

**Current denominator:** Western 2027-2030 horizon = **51.427 GW facility** (rounded to **51.4 GW**), with an IT-load bridge of **43.93 GW** and facility range **[46.00, 54.72] GW**.

**Answer in one line:** **26.5 GW facility** is in T1+T2+T3 (operational, physically evidenced, or firm commercial); **17.9 GW facility** is T4 announced site-level plan; **7.1 GW facility** is T5+T6 stretch or analyst inference. Deterministic tier-weighted realization is **36.2 GW facility**.

## Tier Rollup

| Tier | Interpretation | GW facility | Default realization | Weighted GW |
|---|---|---:|---:|---:|
| T1 | Operational | 7.56 | 1.00 | 7.56 |
| T2 | Under construction / physically evidenced | 12.425 | 0.88 | 10.93 |
| T3 | Firm commercial commitment | 6.48 | 0.78 | 5.05 |
| T4 | Announced site-level plan | 17.88 | 0.58 | 10.37 |
| T5 | LOI / stretch target | 6.754 | 0.32 | 2.16 |
| T6 | Analyst inference | 0.328 | 0.25 | 0.08 |
| **Total** |  | **51.427** |  | **36.162** |

## Canonical Totals

| Metric | Value |
|---|---:|
| Operational today | 7.81 GW facility |
| Tier-clean operational | 7.56 GW facility |
| Raw announced horizon | 51.427 GW facility |
| Raw non-stretch horizon | 44.673 GW facility |
| Conservative T1+T2+T3 raw | 26.465 GW facility |
| Conservative T1+T2+T3 weighted subset | 23.548 GW facility |
| Deterministic tier-weighted | 36.162 GW facility |
| Full-realization ceiling | 54.724 GW facility |
| Sovereign sidebar | 2.56 GW facility |

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
| p05 | 22.8 |
| p10 | 24.4 |
| p25 | 27.5 |
| p50 | 32.4 |
| p75 | 36.1 |
| p90 | 38.3 |
| p95 | 39.5 |
| Mean | 31.76 |
| Std dev | 5.34 |

Tail probabilities: below conservative 26.465 GW = 19.9%; below deterministic weighted 36.162 GW = 75.8%; below raw non-stretch 44.673 GW = 100.0%; below raw announced 51.427 GW = 100.0%.

## Sovereign Sidebar

Sovereign rows are not part of the Western denominator. Microsoft/G42 Khazna is carried as a **0.26 GW facility-equivalent** T4 row at p=0.70. Stargate UAE is qualitative unless separately entered into the structured data layer.
