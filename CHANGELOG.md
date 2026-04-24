# CHANGELOG — Revisions of 2026-04-23 (rev-1) and 2026-04-24 (rev-2)

Revisions of "The AI Compute Build-Out, 2026--2030". This changelog documents every
headline number that moved across three PDF generations: pre-revision (17 pages),
rev-1 2026-04-23 (27 pages), and rev-2 2026-04-24 (incorporating the Epoch
2026-04-22 and 2026-04-10 changelog entries).

## REV-2 (2026-04-24) — Epoch data-drift incorporation

Epoch published two changelog entries that affect our numbers:

1. **2026-04-22 — Stargate Abilene schedule slip.** An Oracle post indicated ~200 MW operational at Abilene as of April 22, not the 600 MW April-1 milestone Epoch had previously projected. Epoch pushed the 600 MW milestone to late May 2026 and Buildings 7–8 from July to November 2026.
2. **2026-04-10 — Meta Prometheus H100e revision.** Epoch excluded five production DCs and the first tent building from the Prometheus H100e count (retrofit-only / non-AI use). Full-buildout H100e revised 1.2M → 1.0M.

| Metric | Rev-1 (2026-04-23) | Rev-2 (2026-04-24) | Delta |
|--------|--------------------|--------------------|-------|
| Operational-today GW | 8.16 | 7.76 | -0.40 |
| Operational-today H100e | 4.74M | 4.18M | -0.56M |
| Epoch current GW | 6.67 | 6.27 | -0.40 |
| T1 rollup GW | 7.96 | 7.56 | -0.40 |
| T2 rollup GW | 11.92 | 12.32 | +0.40 |
| 2030 Western H100e total | 78.41M | 78.21M | -0.20M |
| Growth multiple (ops → 2030) | 16.5× | 18.7× | +2.2× (driven by smaller-ops denominator) |
| Probability-weighted GW | 36.13 | 36.08 | -0.05 |
| Conservative case GW | 27.78 | 27.78 | 0 (intra-conservative shift) |
| Full-realization GW | 53.48 | 53.48 | 0 |
| Announced horizon GW | 50.62 | 50.62 | 0 |
| Monte Carlo median | 31.3 | 31.2 | -0.1 |
| Monte Carlo p10 | 24.1 | 24.0 | -0.1 |
| Monte Carlo p90 | 36.7 | 36.7 | 0 |
| P(<conservative 27.78) | 30.4% | 30.7% | +0.3pp |
| P(<prob-weighted) | 86.0% | 86.3% | +0.3pp |
| "Not operational" share (raw) | 84% | 85% | +1pp |

**Decision rationale**: the April 16 cutoff in rev-1 was a publication convention; rev-2 incorporates the real Epoch-disclosed numbers rather than footnoting them as post-publication drift. Updated data cutoff: 2026-04-24.

**Files touched in rev-2**:
- `compute_commitments_overlay.yaml`: `operational_today_2026_q2.total_gw` 8.16→7.76; `epoch_current_gw` 6.67→6.27; `evidence_tier_rollup_western.T1_operational.gw` 7.96→7.56; `T2_physically_evidenced.gw` 11.92→12.32; `total_gw_probability_weighted` 36.13→36.08; added `revision_note` + `last_checked: 2026-04-24` to `openai_stargate_aggregate` and `meta_hyperion_prometheus` row_audit entries
- `compute_commitments_totals.csv`: H100e reconciliation comments revised (78.41M→78.21M, growth 16.5×→18.7×, operational 4.74M→4.18M across 6.67→6.27 GW)
- `monte_carlo_horizon.py`: TIER_GW constants T1 8.16→7.76, T2 11.92→12.32; PROB_WEIGHTED_POINT_GW 36.13→36.08; threshold label f-strings for parameterization
- `report.tex`: title-page stop-press replaced with rev-2 changelog paragraph; abstract 8.2→7.8 GW operational + rev-2 annotation; §1 opening 4.7M→4.2M H100e + 8.2→7.8 GW; central-fact paragraph 84%→85% raw-horizon; Fig 1 reference line 8.16→7.76; Fig 2 H100e 78.4→78.2 + growth 16.5×→18.6× in caption and table; Fig 10 T1=7.76 T2=12.32; Fig 10B T1=7.76 T2=10.84; §7.6 MC table percentiles p05 22.7→22.6, p50 31.3→31.2; caption noting rev-2 shift; conclusion paragraph MC citation updated
- `row_level_audit.csv`: last_checked 2026-04-22→2026-04-24 on `openai_stargate_aggregate` and `meta_hyperion_prometheus`

---

## REV-1 (2026-04-23) — Six-tier evidence framework introduction

## Numbers that did NOT move (but gained an epistemic label)

| Number | Pre-revision | Post-revision |
|--------|--------------|---------------|
| Operational fleet today | 8.2 GW | 8.2 GW (T1, 100% realization) |
| Western 2030 announced horizon | 50.6 GW | 50.6 GW (unweighted raw horizon) |
| Capital envelope | $1.2--1.5T | $1.2--1.5T (capex only; distinct from RPO) |
| Sovereign pipeline | 2 GW | 1.95 GW (T1 + T4 + T5 mix; 0.69 GW prob-weighted) |
| H100e 2030 base | 78.4M | 78.4M (base silicon-uplift scenario) |
| H100e growth multiple | 16.5x | 16.5x base; 12.7x conservative; 23.2x aggressive |

## NEW numbers introduced (previously unstated)

| Concept | Value |
|---------|-------|
| Probability-weighted 2030 horizon (tier-deterministic) | ~36.1 GW |
| Monte Carlo 2030 median (10,000 draws, Beta-fit tier rates + stress firings) | ~31.3 GW |
| Monte Carlo p10–p90 interdecile range | [24.1, 36.7] GW |
| Monte Carlo p05–p95 | [22.7, 37.7] GW |
| P(realized < conservative 27.78 GW) | 30% |
| P(realized < tier-weighted 36.13 GW) | 86% |
| Conservative case (T1+T2+T3 only) | ~27.8 GW |
| Full-realization ceiling | ~53.5 GW |
| Contracted RPO envelope (separated from capex) | ~$550B |
| T1 segment | 8.16 GW / 16% / prob=1.00 |
| T2 segment | 11.92 GW / 24% / prob=0.88 |
| T3 segment | 7.90 GW / 16% / prob=0.78 |
| T4 segment | 16.28 GW / 32% / prob=0.58 |
| T5 segment | 5.09 GW / 10% / prob=0.32 |
| T6 segment | 1.25 GW / 2% / prob=0.25 |
| PUE sensitivity band | 50.6 GW IT = [55.7, 80.9] GW facility across PUE 1.1-1.6 |
| Stress scenario A (Stargate slip) | -3.5 GW / -$120B / 30% prob |
| Stress scenario B (neocloud spread +300bps) | -2.0 GW / -$60B / 25% prob |
| Stress scenario C (grid 24mo slip) | -8.0 GW / -$180B / 40% prob |
| Stress scenario D (chip 2Q slip) | -1.5 GW / -$40B / 50% prob |
| Stress scenario E (inference > training) | 0 GW / -$20B / 55% prob |
| Correlated A+B+C tail | -10 to -12 GW / -$300 to -$350B |

## STRUCTURAL additions (not in pre-revision)

- §1.1 "Power units and PUE sensitivity" (new subsection, ~1 page)
- §4.5 "H100e sensitivity: conservative, base, aggressive" (new subsection, ~1.5 pages)
- §5.5 "Capex bridge: what the money pays for" (new subsection, ~0.7 pages)
- §5.6 "Financing bridge: where the money comes from" (new subsection, ~0.8 pages)
- §7.5 "Stress scenarios: five transmission mechanisms" (new subsection, ~2 pages)
- §7.6 "Monte Carlo: distribution of the 2030 realized horizon" (new subsection, ~0.7 pages)
- §9 "Known unknowns" (new section, 10 subsections, ~2 pages)
- §10 "Conclusion" (new section, ~1 page)
- Appendix B "Row-level audit (summary)" (new appendix, ~1 page)
- Figure 10 rebuilt for 6-tier framework (was 5-tier)
- Figure 10B NEW — same segments re-scaled by tier-default realization probability

## NUMBERS restated as forecast objects (language changed, value same)

- Abstract: "roughly 50 GW" → "raw horizon of 50.6 GW / probability-weighted ~36 GW / conservative ~28 GW / full-realization ~53.5 GW"
- §1 "84% of horizon not yet built" → "84% of raw horizon not operational; 78% of prob-weighted 36 GW not operational"
- §5 "Oracle $300B take-or-pay" → reclassified as RPO revenue obligation, NOT capex channel
- §7 "55% physically evidenced / 32% announced / 13% speculative" → 6-tier split (16/24/16/32/10/2 %)
- §8 sovereign pipeline → each of 4 programs gets T1--T5 tier + probability
- Fig 10 caption → per-tier realization probability labeled

## DATA LAYER additions

- `compute_commitments_overlay.yaml`:
  - `evidence_tier: T1|T2|T3|T4|T5|T6` per Class A / B / C row (23 rows)
  - `realization_probability: 0.00-1.00` per row with tier-default override
  - new top-level `row_audit:` block with mw_basis / pue / utility / iso_rto / interconnection_status / chip_family / capex_actual / capex_future / rpo / financing_source / capex_bridge per row
  - new top-level `chip_density_assumptions:` with per-family H100e/MW 2024-2030
  - new top-level `chip_density_scenarios:` conservative / base / aggressive
  - new top-level `stress_scenarios:` block with 5 named scenarios
- `neocloud_overlay.yaml`: evidence_tier_operational + evidence_tier_contracted + probabilities per row; evidence_tier_rollup at aggregate level
- `compute_commitments_totals.csv`: new columns evidence_tier, realization_probability, prob_weighted_gw_point; SIX-TIER WESTERN ROLLUP footer
- `CONFIDENCE_DECOMPOSITION.md`: fully rewritten from 5-tier to 6-tier (132 → 189 lines)
- `audit_totals.py`: extended 175 → 281 lines; emits 7 canonical totals; six-tier sum validation
- `row_level_audit.csv`: NEW — 33 rows × 25 columns; companion to Appendix B
- `monte_carlo_horizon.py`: NEW — 10,000-draw simulation over six-tier GW partition with Beta-fitted tier realization rates (mean = tier-default prior, p05/p95 = tier-documented bracket) and Bernoulli firing of the five stress scenarios at their prior probabilities. Emits p05/p10/p25/p50/p75/p90/p95 of 2030 realized GW, mean, std dev, and tail probabilities against the four reference point estimates (conservative 27.78, tier-weighted 36.13, bear 45.74, announced 50.61). Seed-pinned (`--seed 20260424`) for reproducibility. Output feeds §7.6 subsection.
- `check_source_freshness.py`: NEW — staleness linter over `row_audit.last_checked` and neocloud `as_of_date`. Classifies each row GREEN (≤30 d), YELLOW (31–60 d), RED (61+ d), or MISSING. Not a re-fetch tool; flags which rows need manual source re-verification. Exit code 1 if any RED or MISSING, 0 otherwise. Supports `--json` for machine-readable output.

## KEY GRID-ISO CORRECTIONS

- xAI Colossus 2 Memphis: corrected to MLGW/MISO (was loose-referenced as ERCOT-adjacent)
- Meta Hyperion Richland Parish LA: tagged Entergy/MISO-South (not ERCOT)
- Fairwater WI: ATC/MISO
- Anthropic-AWS New Carlisle IN: AEP Indiana/MISO
- CoreWeave Helios ND: Basin Electric/MISO

## PAGE COUNT

| Version | Pages |
|---------|-------|
| Pre-revision | 17 |
| Rev-1 (2026-04-23) | 27 |
| Rev-2 (2026-04-24) | 28 |

## VERIFICATION RUN

```
$ python3 audit_totals.py
AUDIT PASSED — `totals:` block matches per-row sums.
SEVEN CANONICAL TOTALS (six-tier evidence framework, Western)
  1. operational_today_gw         =   8.16 GW  (T1)
  2. announced_horizon_gw         =  50.61 GW  [45.74, 53.48]
  3. probability_weighted_gw      =  36.13 GW  (tier-default midpoints)
  4. conservative_case_gw         =  27.78 GW  (T1+T2+T3 only)
  5. full_realization_gw          =  53.48 GW  (arithmetic ceiling)
  6. capital_envelope_usd_b       =  847.0 $B  (rough; A.7 will refine)
  7. rpo_obligations_usd_b_rough  =   27.0 $B  (rough; A.7 will refine)
```

All 7 canonical totals emit cleanly. Tier-sum framework validation: 50.62 GW Σ tier GW
= 50.62 GW declared announced horizon.

## EPOCH METHODOLOGY CITATION (rev-1 addition, retained in rev-2)

Explicit citation of Epoch's documented uncertainty bands in title-page footnote:
- Cooling-model power estimates can in principle vary by up to a factor of 2 against ground truth; Epoch's validation against known-capacity sites agrees within ~50%.
- Capital-cost estimates apply a uniform $44 B/GW ($30 B hardware + $14 B infrastructure) and are not site-specific.

These bands are consistent with our T2 realization-probability range of 80–95% and T3 of 65–90%, which provides external validation for the tier-default priors in the six-tier framework.

```
$ python3 monte_carlo_horizon.py --draws 10000 --seed 20260424
MONTE CARLO — 2030 Western realized GW  (N=10,000, seed=20260424)
  Mean                 :  30.74 GW
  Std dev              :   4.82 GW
  p05                  :  22.66 GW
  p10                  :  24.09 GW
  p25                  :  26.87 GW
  p50 (median)         :  31.26 GW
  p75                  :  34.78 GW
  p90                  :  36.72 GW
  p95                  :  37.73 GW

  Tail probabilities:
    P(realized < conservative 27.78)  = 30.4%
    P(realized < prob-weighted 36.13) = 86.0%
    P(realized < bear 45.74)          = 100.0%
    P(realized < announced 50.61)     = 100.0%
```

The Monte Carlo median (31 GW) sits approximately 5 GW below the deterministic
tier-weighted 36 GW point estimate. The gap is the stress-scenario downside
expected value (scenarios A+B+C+D carry combined unconditional EV ≈ –5.9 GW; E is
GW-neutral by construction). The p10–p90 interdecile range [24.1, 36.7] is the
probability-honest band an LP should stress against; the raw 50.6 GW sum and the
tier-weighted 36 GW point estimate both sit in the upper tail of the distribution.
