# The AI Compute Build-Out, 2026–2030

**Scale, capex, silicon, and counterparty geography of the frontier AI
infrastructure arms race.**

A quantitative forecast paper with a full audit trail: every headline number
resolves to a row in the data layer, every row carries an evidence tier
(T1–T6) and a realization probability, and the 2030 horizon is reported as
a Monte Carlo distribution rather than a point estimate.

- **Paper**: [`report.pdf`](report.pdf) (30 pages)
- **Latest revision**: 2026-04-24 (rev-3, facility-basis reconciliation + Figure 8 rebuild)
- **Data cutoff**: 2026-04-24
- **Primary data**: [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) (CC BY 4.0)

---

## The headline numbers (facility basis, primary)

| Metric | Value | Notes |
|---|---|---|
| Operational today (Q2 2026) | **7.56 GW tier-clean** (~7.81 GW facility including T6-inferred) | T1; +0.25 GW facility T6-inferred |
| 2030 raw announced horizon (Western) | **51.4 GW facility** (43.9 GW IT-load bridge) | Unweighted sum across T1–T6 |
| 2030 tier-weighted point | **36.5 GW facility** | Σ tier_GW × tier_default_probability |
| **2030 Monte Carlo median** | **31.5 GW facility** | 10,000 draws; our probability-honest central estimate |
| Monte Carlo p10–p90 | **[24.6, 37.4] GW facility** | Interdecile range — the relevant LP sensitivity band |
| Raw non-stretch (replaces retired "bear") | **44.7 GW facility** | Announced minus T5 stretch targets |
| Conservative case (T1+T2+T3 only) | **27.9 GW facility** | |
| Full-realization ceiling | **54.7 GW facility** | Arithmetic high |
| Sovereign-AI sidebar (separate) | **2.56 GW facility** (1.91 GW IT-load) | UAE + Saudi + India + UK; not in Western denom. |
| Capital envelope | **~$1.2–1.5T** | Capex requirement; distinct from RPO |
| RPO (revenue underwriting, not capex) | **~$550B** | Oracle–OpenAI, Anthropic–AWS, Meta–Nebius, CoreWeave |
| 2030 H100-equivalents (Western) | **78.2M** | vs. 4.2M operational today — 18.7× growth (basis-invariant) |

**The central fact**: approximately 85% of the 51.4 GW facility raw 2030 horizon is
not yet operational. The forecast stands or falls on whether the 2028–2030
pipeline materializes on announced timelines — which is why every number
here carries an evidence tier and a realization probability.

**Power-basis note**: facility power (IT + cooling + losses + auxiliaries) is the
primary denominator, matching [Epoch AI's methodology](https://epoch.ai/data/data-centers-documentation)
and the basis most relevant to grid interconnection and facility capex. IT-load-equivalent
capacity is reported as a secondary bridge against chip-nameplate commitments; the
central IT-load bridge is ~43 GW at blended PUE 1.20.

---

## What's in this repo

### Paper
- [`report.tex`](report.tex) — LaTeX source
- [`report.pdf`](report.pdf) — 30-page PDF

### Data layer (the ledger)

**Horizon side — what is being committed (one row per commitment)**
- [`compute_commitments_overlay.yaml`](compute_commitments_overlay.yaml) — 14 Class A commitments + Class B chips + Class C $-only rows, each with primary-source verbatim, Epoch-overlap dedup reasoning, evidence tier, realization probability, row-level audit fields (PUE, mw_basis, ISO/RTO, interconnection status, chip family, capex split, RPO, financing source, capex bridge), plus top-level `stress_scenarios:` and `chip_density_assumptions:` blocks
- [`neocloud_overlay.yaml`](neocloud_overlay.yaml) — CoreWeave, Nebius, Applied Digital, Crusoe, Lambda, Voltage Park, Together AI, Fermi, Nscale — operational + contracted capacity per operator with evidence-tier rollup
- [`facts_extract.yaml`](facts_extract.yaml) — the 11 facts added or modified by the overlay with full source metadata inlined
- [`compute_commitments_totals.csv`](compute_commitments_totals.csv) — flat per-row table (Excel-ready)
- [`row_level_audit.csv`](row_level_audit.csv) — 33 rows × 40 columns, the companion to Appendix B in the paper
- [`epoch_data_centers/`](epoch_data_centers/) — upstream Epoch AI Frontier Data Centers snapshot (CC BY 4.0) this overlay sits on top of

**Unit-economics side — what 1 facility GW costs (added rev-4 prep, 2026-04-27)**
- [`anatomy_layer_costs.yaml`](anatomy_layer_costs.yaml) — per-layer / per-sub-component cost decomposition for one 2026-vintage AI facility GW. Six physical layers (shell, cooling, power, networking, accelerator+server, grid), ~40 sub-components, each with `cost_usd_m_per_mw_{low,high,central}`, basis, vintage, evidence tier (T1–T6), primary sources with retrieval dates, and inflation flags. Includes the basis-conventions cheat sheet that resolves cross-forecaster disagreement.
- [`anatomy_layer_costs.csv`](anatomy_layer_costs.csv) — flat companion (Excel-ready)
- [`anatomy_named_projects.yaml`](anatomy_named_projects.yaml) — project-level disclosed capex anchors (Crusoe Abilene, Meta Hyperion, AEP/SB Energy Piketon, Microsoft Mt Pleasant, AWS Madison, Talen-AWS, etc.) with verbatim figures and reconciliation back to the bottoms-up layer ranges
- [`forecaster_capex_comparison.yaml`](forecaster_capex_comparison.yaml) — 18-source cross-forecaster $/GW reconciliation (Epoch, Bernstein, McKinsey, Bain, JLL, Cushman, Goldman, Morgan Stanley, JPM, BNEF, Synergy, Dell'Oro, IEA, LBNL, Aschenbrenner, NVIDIA, Barclays, Stargate, Hyperion, CoreWeave, Nebius). Verdict on the paper's $23–30B/GW with explicit basis declaration.
- [`research/`](research/) — eight per-agent research notes (one per layer + Crusoe + forecasters); intermediate scratchpad behind the structured YAML

### Framework docs
- [`CONFIDENCE_DECOMPOSITION.md`](CONFIDENCE_DECOMPOSITION.md) — the six-tier evidence framework (T1 Operational through T6 Analyst inference) with per-tier realization-probability defaults and per-row override rules
- [`RUNDOWN.md`](RUNDOWN.md) — plain-English summary with the 8 key tables (pre-rev-2; still useful for the overlay mechanics)
- [`CHANGELOG.md`](CHANGELOG.md) — every number that moved across the pre-revision, rev-1, and rev-2 PDFs

### Tooling
- [`audit_totals.py`](audit_totals.py) — re-sums YAML per-row incrementals vs. the declared `totals:` block; emits the seven canonical totals (operational-today, announced horizon, probability-weighted, conservative, full-realization, capital envelope, RPO); exits 1 on drift
- [`monte_carlo_horizon.py`](monte_carlo_horizon.py) — 10,000-draw simulation. Samples tier realization rates from Beta distributions fitted to (tier_default_mean, tier_p05, tier_p95); applies the five stress scenarios as independent Bernoulli firings. Reports p05 / p10 / p25 / p50 / p75 / p90 / p95 and tail probabilities. Seed-pinned.
- [`check_source_freshness.py`](check_source_freshness.py) — staleness linter on `row_audit.last_checked` and neocloud `as_of_date`. GREEN (≤30 d) / YELLOW (31–60 d) / RED (61+ d) / MISSING. Exit code 1 if any RED or MISSING.

---

## Running the tools

```bash
# Install
pip install pyyaml

# Audit the data layer (exits 1 if totals drift)
python3 audit_totals.py

# Monte Carlo (seed-pinned; reproducible)
python3 monte_carlo_horizon.py --draws 10000 --seed 20260424

# Source-freshness linter (exits 1 if any rows are RED or MISSING)
python3 check_source_freshness.py

# Rebuild the PDF
pdflatex report.tex && pdflatex report.tex
```

---

## The six-tier evidence framework

Every row in the data layer carries a tier label. Tiers map to default
realization probabilities; individual rows can override via the
`realization_probability` field.

| Tier | Label | GW (Western) | Default P(realize) | Documented range |
|------|-------|-------------:|-------------------:|------------------|
| T1 | Operational | 7.56 | 1.00 | n/a |
| T2 | Under construction / physically evidenced | 12.43 | 0.88 | 0.80–0.95 |
| T3 | Firm commercial commitment | 7.95 | 0.78 | 0.65–0.90 |
| T4 | Announced site-level plan | 16.41 | 0.58 | 0.40–0.75 |
| T5 | LOI / stretch target | 6.75 | 0.32 | 0.15–0.50 |
| T6 | Analyst inference | 0.33 | 0.25 | 0.10–0.40 |
| **Total** | | **43.93** | | |

The full tier definitions and per-row assignment rules are in
[`CONFIDENCE_DECOMPOSITION.md`](CONFIDENCE_DECOMPOSITION.md).

---

## Scope decisions

1. **Western-aligned vs. sovereign-AI reported separately.** The Western
   subtotal (43.9 GW) is the capex-revenue denominator for any analysis
   of OpenAI / Anthropic / Google / Meta / Microsoft / xAI. The sovereign
   sidebar (1.91 GW — UAE, Saudi, India, UK) is reported but NOT added
   to the Western denominator.
2. **Class B (chip procurement) adds zero physical GW.** AMD 6 GW +
   Broadcom 10 GW + NVIDIA 10 GW = 26 GW in chip nameplate, but those
   chips deploy into Class A shells already counted at the site level.
3. **Class C (dollar-only commitments) is tracked but does not add GW.**
   Altman's $1.4T aggregate, Alphabet UK £5B, etc. — envelopes that
   overlap Class A capex.
4. **China excluded except qualitatively** (§9 known-unknowns). Publicly
   disclosed Chinese AI datacenter capacity materially understates actual
   build-out and cannot be corroborated from open sources at the same
   granularity as the Western-aligned set.
5. **Seven commitments explicitly excluded** after primary-source review
   (Apple PCC, Oracle ex-Stargate, Tesla Cortex, Cohere/DeepMind,
   DLR/Equinix merchant, EuroHPC, Mistral Bruyères). Each exclusion is
   logged in [`compute_commitments_overlay.yaml`](compute_commitments_overlay.yaml)
   under `excluded_with_reason` with the primary source we checked.

---

## Known sharp edges

- **Reliance Jio Jamnagar range is [0.12, 3.00] GW.** Ambani's AGM statement
  uses "gigawatt-scale" without specificity.
- **Meta Hyperion range is [0, 2.74] GW.** Meta's own newsroom commits to
  "over 2 GW" (already matched by Epoch). The incremental is Zuckerberg's
  earnings-call stretch target of "5 GW over several years."
- **Anthropic-AWS 5 GW "new" range is [2.50, 5.00] GW.** Low bound allows
  for overlap with Madison + Ridgeland + future New Carlisle expansion
  beyond Epoch's current 1.23 GW.
- **The $52B Anthropic-Google TPU figure should NOT be added to the $50B
  Fluidstack commitment.** Anthropic's April 2026 blog frames the TPU
  deal as "a major expansion of our November 2025 commitment to invest
  $50 billion."
- **Epoch data moves.** The 2026-04-22 changelog slipped Stargate
  Abilene's 600 MW milestone from April 1 to late May 2026; rev-2 of
  the paper (2026-04-24) incorporates this. Run `check_source_freshness.py`
  to see which rows are stale relative to your current date.

---

## Methodology and uncertainty

- **Epoch's disclosed uncertainty bands** (from their methodology docs):
  cooling-model power estimates can in principle vary up to a factor of
  2 against ground truth, though validation against known-capacity sites
  shows agreement within ~50%. Capital-cost estimates apply a uniform
  $44B/GW ($30B hardware + $14B infrastructure). These bands are consistent
  with our T2/T3 realization-probability ranges.
- **Monte Carlo design**: tier rates are sampled from Beta distributions
  fitted so the tier-default is the mean and the tier-documented range
  is p05–p95 (method-of-moments with normal approximation on the
  quantile spread). T1 treated deterministically. Stress scenarios
  (A Stargate slip, B neocloud spread, C grid slip, D chip slip,
  E inference > training) fire independently as Bernoulli(scenario_prob);
  their combined unconditional EV is approximately −5.9 GW, which is
  why the Monte Carlo median (31.5 GW) sits ~5 GW below the deterministic
  tier-weighted point (36 GW).
- **What we don't forecast** is enumerated in §9 of the paper: PUE
  ambiguity, interconnection-queue opacity, chip-roadmap uncertainty
  post-2027, cluster utilization, training vs inference mix,
  double-count residual, RPO enforceability, neocloud financing under
  stress, sovereign disclosure asymmetry, China.

---

## License

- **Paper, data, and documentation** (`report.tex`, `report.pdf`, all
  `.yaml` / `.csv` / `.md` files in the repo root): [CC BY 4.0](LICENSE).
  Attribution required; commercial use permitted.
- **Scripts** (`audit_totals.py`, `monte_carlo_horizon.py`,
  `check_source_freshness.py`): MIT License (embedded in the same
  [LICENSE](LICENSE) file).
- **Upstream Epoch AI data** (`epoch_data_centers/`): CC BY 4.0 per
  Epoch's license. Attribution: "Epoch AI, *Frontier Data Centers*,
  2026-04-24 snapshot. https://epoch.ai/data/data-centers".

---

## Citation

```bibtex
@techreport{entebi2026aicompute,
  title   = {The AI Compute Build-Out, 2026--2030:
             Scale, capex, silicon, and counterparty geography},
  author  = {Entebi, Isaac},
  year    = {2026},
  month   = {April},
  note    = {Revision 2, 2026-04-24. 28 pages.
             Data and scripts at
             https://github.com/isaacentebi/ai-compute-buildout-2030}
}
```
