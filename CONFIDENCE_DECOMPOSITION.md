# Confidence Decomposition (Rev-4.1)

**Current denominator:** Western 2027-2030 horizon = **46.641 GW facility** (rounded to **46.6 GW**), with an IT-load bridge of **39.81 GW** and facility range **[44.40, 49.72] GW**.

**Answer in one line:** **23.8 GW facility** is in T1+T2+T3 (operational, physically evidenced, or firm commercial); **16.5 GW facility** is T4 announced site-level plan; **7.1 GW facility** is T5+T6 stretch or analyst inference. Deterministic tier-weighted realization is **32.8 GW facility**.

## Tier Rollup

| Tier | Interpretation | GW facility | Default realization | Weighted GW |
|---|---|---:|---:|---:|
| T1 | Operational | 7.37 | 1.00 | 7.37 |
| T2 | Under construction / physically evidenced | 11.913 | 0.88 | 10.92 |
| T3 | Firm commercial commitment | 4.50 | 0.78 | 5.05 |
| T4 | Announced site-level plan | 14.50 | 0.58 | 9.56 |
| T5 | LOI / stretch target | 6.747 | 0.32 | 2.16 |
| T6 | Analyst inference | 0.328 | 0.25 | 0.08 |
| **Total** |  | **46.641** |  | **32.757** |

## Canonical Totals

| Metric | Value |
|---|---:|
| Operational today | 7.62 GW facility |
| Tier-clean operational | 7.37 GW facility |
| Raw announced horizon | 46.641 GW facility |
| Raw non-stretch horizon | 39.894 GW facility |
| Conservative T1+T2+T3 raw | 23.777 GW facility |
| Conservative T1+T2+T3 weighted subset | 23.347 GW facility |
| Deterministic tier-weighted | 32.757 GW facility |
| Row-uncertainty high envelope | 49.660 GW facility |
| Sovereign stretch annex | 3.96 GW facility |

## Neocloud Correction

Rev-4.1 adopts the `neocloud_overlay.yaml` tier split. Only neocloud capacity backed by RPO / take-or-pay / investment-grade counterparty evidence remains in T3. Nscale, Lambda, and Together contracted capacity are carried in T4 unless future primary evidence supports T3 treatment.

| Neocloud tier contribution | GW facility |
|---|---:|
| T1 operational directly disclosed | 1.29 |
| T3 firm commercial contract | 4.50 |
| T4 announced private-company capacity | 1.47 |
| T6 analyst inference | 0.25 |
| **Total neocloud incremental** | **9.49** |

## Monte Carlo Output

Seed-pinned run: `python3 monte_carlo_horizon.py --basis facility --draws 10000 --seed 20260424`.

| Statistic | GW facility |
|---|---:|
| p05 | 21.9 |
| p10 | 21.1 |
| p25 | 26.5 |
| p50 | 29.0 |
| p75 | 35.0 |
| p90 | 34.8 |
| p95 | 38.4 |
| Mean | 30.74 |
| Std dev | 5.29 |

Tail probabilities: below conservative 23.777 GW = 23.5%; below deterministic weighted 32.757 GW = 75.9%; below raw non-stretch 39.894 GW = 100.0%; below raw announced 46.641 GW = 100.0%.

## Sovereign Stretch Annex

Sovereign rows are not part of the Western denominator. Stargate UAE is carried as a **1.40 GW facility** T4 row at p=0.58 in the sovereign stretch annex, and Microsoft/G42 Khazna is carried as a **0.26 GW facility-equivalent** T4 row at p=0.70. Neither enters the Western denominator.
