# Confidence Decomposition (Rev-4.4)

**Current denominator:** Western 2027–2030 horizon = **47.901 GW facility** (rounded to **47.9 GW**), with an IT-load bridge of **40.878 GW** and facility range **[39.520, 54.210] GW**.

**Answer in one line:** **22.9 GW facility** is in T1+T2+T3 (operational, physically evidenced, or firm commercial); **15.8 GW facility** is T4 announced site-level plan; **9.2 GW facility** is T5+T6 stretch or analyst inference. Deterministic tier-weighted realization is **32.6 GW facility**.

All numbers in this document resolve to [`canonical_totals.json`](canonical_totals.json) and are reproducible by re-summing the atoms in [`row_level_audit.csv`](row_level_audit.csv) with the inclusion flags as documented.

## Tier Rollup (Western raw horizon, 67 atoms)

| Tier | Interpretation | GW facility | Default realization | Weighted GW |
|---|---|---:|---:|---:|
| T1 | Operational | 6.519 | 1.00 | 6.519 |
| T2 | Under construction / physically evidenced | 11.908 | 0.88 | 10.479 |
| T3 | Firm commercial commitment | 4.500 | 0.78 | 3.510 |
| T4 | Announced site-level plan | 15.789 | 0.58 | 9.158 |
| T5 | LOI / stretch target | 8.857 | 0.32 | 2.834 |
| T6 | Analyst inference | 0.328 | 0.25 | 0.082 |
| **Total** |  | **47.901** |  | **32.582** |

## Canonical Totals

| Metric | Value |
|---|---:|
| Operational today (incl. T6-inferred) | 6.769 GW facility |
| Tier-clean operational (T1) | 6.519 GW facility |
| Raw announced horizon | 47.901 GW facility |
| Raw non-stretch horizon (excl. T5) | 39.044 GW facility |
| Conservative T1+T2+T3 raw | 22.927 GW facility |
| Conservative T1+T2+T3 weighted | 20.508 GW facility |
| Deterministic tier-weighted | 32.582 GW facility |
| Row-uncertainty high envelope | 54.210 GW facility |
| Sovereign sidebar | 4.960 GW facility |

## Neocloud Correction

Rev-4.3 adopted the `neocloud_overlay.yaml` tier split. Only neocloud capacity backed by RPO / take-or-pay / investment-grade counterparty evidence is in T3. Nscale, Lambda, and Together contracted capacity carry T4 unless future primary evidence supports T3 treatment.

| Neocloud tier contribution | GW facility |
|---|---:|
| T1 operational directly disclosed | 0.44 |
| T3 firm commercial contract | 4.50 |
| T4 announced private-company capacity | 2.61 |
| T6 analyst inference | 0.25 |
| **Total neocloud incremental** | **7.80** |

CoreWeave note: the `coreweave_operational_disclosed` 0.85 GW T1 row is retained at row-audit level for visibility but excluded from the Western raw horizon (`included_in_western_raw_horizon=false`) to avoid double-counting against `coreweave_contracted_ex_epoch` (T3, 2.30 GW), which derives from the 3.10 GW total contracted disclosure in CoreWeave's FY2025 10-K.

## Monte Carlo Output

Seed-pinned run: `python3 monte_carlo_horizon.py --basis facility --draws 10000 --seed 20260424`. Reproducible from the current atom ledger.

| Statistic | GW facility |
|---|---:|
| p05 | 19.4 |
| p10 | 20.9 |
| p25 | 23.9 |
| p50 | 28.8 |
| p75 | 32.5 |
| p90 | 34.7 |
| p95 | 35.9 |
| Mean | 28.2 |
| Std dev | 5.29 |

Tail probabilities versus the deterministic anchors are reported in `monte_carlo_output_facility_seed20260424.json`.

## Sovereign Stretch Annex

Sovereign rows are not part of the Western denominator. Nine atoms aggregate to **4.960 GW facility** (`sovereign_sidebar_gw_facility` in `canonical_totals.json`):

| Sovereign atom | GW facility | Tier |
|---|---:|:--:|
| Stargate UAE (Epoch site) | 1.40 | T4 |
| Microsoft / G42 Khazna UAE | 0.26 | T4 |
| HUMAIN xAI Saudi | 0.50 | T4 |
| HUMAIN AMD Saudi | 0.50 | T4 |
| Reliance Jamnagar near-term (120 MW) | 0.12 | T2 |
| Reliance Jamnagar stretch | 0.88 | T5 |
| Reliance Andhra MoU (NEW Rev-4.4) | 1.00 | T5 |
| UK Culham initial 100 MW | 0.12 | T4 |
| UK Culham scale-out | 0.18 | T5 |
| **Total** | **4.96** | |

The `digital_connexion_vizag_1gw_overlap` atom is also flagged `sovereign_sidebar=true` in the row-level audit but is tier `excluded` and does not enter the 4.960 GW total — it represents the dedupe overlap between the Reliance/Andhra MoU and the Digital Connexion / Reliance-Brookfield JV at Vizag. Filters that compute the sidebar must drop tier=`excluded`.

Sovereign upside of 5–7 GW by 2030 is plausible if state-backed programmes scale ahead of disclosure (e.g. the Microsoft/G42 200 MW UAE expansion announced 2025-11-05 may accelerate, and Reliance disclosure in Visakhapatnam could resolve to 1.5 GW per regional reporting), but it sits outside the Western horizon.
