# Confidence decomposition — six-tier evidence framework with realization probabilities

**The question:** of the Western 2027-2030 horizon (**51.9 GW facility announced**; 50.6 GW IT-load bridge; facility range [46.40, 55.32]), how much is *basically certain*, how much is *likely*, how much is *speculative*, how much is *analyst inference*?

**The answer in one line:** ~54% of the 51.9 GW facility is anchored in physical evidence or firm commercial contracts (T1+T2+T3 = 27.9 GW facility); ~33% is plausible-on-timeline announced pipeline at named sites (T4 = 16.9 GW facility); ~13% is LOI / stretch target or analyst inference (T5+T6 = 7.1 GW facility).

This document defines the **six-tier evidence framework** used throughout the paper, the **realization probabilities** attached to each tier, and the **four canonical output totals** (announced horizon, probability-weighted, conservative, full-realization) that the rest of the analysis rolls up to.

## A.8 Basis discipline (rev-3)

The paper's primary physical denominator is **facility power** — total MW drawn at the
substation (IT accelerators + cooling + lighting + power-conversion losses + auxiliary
load). This matches Epoch AI's Frontier Data Centers `Power (MW)` convention documented
at `epoch.ai/data/data-centers-documentation`, and it is the basis most relevant to grid
interconnection and facility capex.

**Per-row `mw_basis` field.** Every Class A commitment row and every neocloud row carries
a `mw_basis: facility | IT | unknown` tag and a `pue_assumed` field. The
facility-basis rollup is computed row-by-row:

- `mw_basis == facility`: `incremental_gw_facility_point = incremental_gw_point` (pass-through).
- `mw_basis == IT`: `incremental_gw_facility_point = incremental_gw_point × pue_assumed`.
- `mw_basis == unknown`: `incremental_gw_facility_point = incremental_gw_point × 1.25` (paper default).

**IT-load bridge.** The IT-load-equivalent aggregate is reported as a secondary bridge
table, computed by dividing facility by PUE. This is the number readers should use
when comparing against chip-nameplate commitments (NVIDIA/AMD/Broadcom "X GW" silicon
announcements are implicitly IT-basis).

**Chip counts are basis-invariant.** H100e deployments don't change under the basis
flip — only the MW denominator does. The 78.2M H100e total in the 2030 Western
horizon is unchanged from rev-2; what shifts is that the per-MW density is now
quoted per IT-MW (Epoch convention) with a facility-MW equivalent footnote
(~1,157 H100e per facility-MW at blended PUE 1.20, vs ~1,388 per IT-MW).

---

## The six tiers

Each row in `compute_commitments_overlay.yaml` and `neocloud_overlay.yaml` carries an `evidence_tier: T1|T2|T3|T4|T5|T6` label. The six tiers partition the commitment surface from hard-evidenced to analyst-inferred:

| Tier | Label | What qualifies | Realization probability default |
|---|---|---|---:|
| **T1** | Operational | MW currently online as of 2026-Q2; verifiable from permits, satellite imagery, 10-Q disclosures | **1.00** |
| **T2** | Physically evidenced / under construction | Construction visible on satellite, permits filed, Epoch active-construction sites with end-of-timeline 2026–2027 | **0.88** (range 0.80–0.95) |
| **T3** | Firm commercial commitment | RPO / take-or-pay / 10–15-year contract with an investment-grade counterparty (CoreWeave RPO, Nebius-MSFT, Nebius-Meta, Applied Digital PF2 lease) | **0.78** (range 0.65–0.90) |
| **T4** | Announced site-level plan | Named site, named operator, MW disclosed, primary-source-backed; typically 2028 scheduled | **0.58** (range 0.40–0.75) |
| **T5** | LOI / stretch target | Announced but range floors at zero, or dollar-only commitment, or CEO earnings-call stretch language | **0.32** (range 0.15–0.50) |
| **T6** | Analyst inference | MW derived by extrapolation from GPU count or investment size; not primary-disclosed | **0.25** (range 0.10–0.40) |

**Per-row override**: any commitment can deviate from the tier default via the `realization_probability` field in the YAML. Anthropic-AWS is set at 0.72 (above T4 default 0.58) because the 1 GW near-term floor is higher-confidence than the 5 GW ceiling; Reliance Jio Jamnagar is set at 0.20 (below T5 default 0.32) because the range spans 0.12–3.00 GW and the Indian grid/land-acquisition risk is materially higher than Western analogues.

---

## The five-tier → six-tier migration

The previous framework (in prior versions of this document) used five tiers labelled HIGH / MEDIUM-HIGH / MEDIUM / SPECULATIVE / MOONSHOT. The six-tier framework refines that partition along three axes:

1. **Physical evidence (T1, T2) separated from commercial firmness (T3).** Previously, Microsoft Fairwater Wisconsin (construction visible on satellite) and the CoreWeave 15-year RPO (legally binding but purely commercial) lived in the same MEDIUM-HIGH bucket. They're now T2 and T3 respectively.
2. **SPECULATIVE + MOONSHOT merged into T5.** The previous distinction between "range bottoms at zero" (MOONSHOT) and "outer-year scheduled" (SPECULATIVE) was more emotional than empirical. Both are realistically "announced but range-at-zero is live" and share the same transmission mechanism to the balance sheet.
3. **Analyst inference (T6) made explicit.** Previously buried inside the neocloud imputed-MW rows (Voltage Park from GPU count; Together AI from fleet estimates) and xAI Colossus 2 residual, these are now tagged T6 and carry their own lower probability.

---

## The six-tier decomposition

| Tier | Epoch GW | Overlay Class A GW | Neocloud GW | **Total GW** | **% of 50.62** |
|---|---:|---:|---:|---:|---:|
| **T1 — Operational** | 6.67 | 0.00 | 1.29 | **7.96** | **15.7%** |
| **T2 — Physically evidenced / UC** | 11.22 | 0.70 | 0.00 | **11.92** | **23.6%** |
| **T3 — Firm commercial commitment** | 0.00 | 0.00 | 7.90 | **7.90** | **15.6%** |
| **T4 — Announced site-level plan** | 12.61 | 3.67 | 0.00 | **16.28** | **32.2%** |
| **T5 — LOI / stretch target** | 2.56 | 3.74 | 0.00 | **6.30** | **12.4%** |
| **T6 — Analyst inference** | 0.00 | 0.06 | 0.20 | **0.26** | **0.5%** |
| **Total** | **33.05** | **8.17** | **9.39** | **50.62** | **100%** |

**Read this as:** T1+T2+T3 = 55% hard-anchored. T4 = 32% plausible-on-timeline. T5+T6 = 13% stretch or inference.

---

## The four canonical output totals

The probability framework produces **four distinct numbers** for the 2027–2030 Western horizon. Every headline number in the paper refers to one of these; the abstract cites all four:

| Output | How it's computed | 2027-2030 Western value |
|---|---|---:|
| **Announced horizon** | Σ row_gw (unweighted) | **50.62 GW** |
| **Probability-weighted horizon** | Σ(row_gw × row_probability), using tier defaults unless overridden | **~36.1 GW** |
| **Conservative case** | T1 + T2 + T3 only (the 55% hard-anchored) | **~27.8 GW** |
| **Full-realization case** | Arithmetic high-range ceiling (all stretch + all neocloud contracted materializes) | **~53.5 GW** |

### Worked-out probability-weighted arithmetic

```
Tier   Total GW   Default prob   Weighted GW
T1      7.96       1.00           7.96
T2     11.92       0.88          10.49
T3      7.90       0.78           6.16
T4     16.28       0.58           9.44
T5      6.30       0.32           2.02
T6      0.26       0.25           0.07
                                 ─────
                                 36.13 GW
```

### Why the conservative case matters

The **conservative case of 27.8 GW** is the bear reading: everything that doesn't already have physical evidence or a legally enforceable firm contract is stripped out. This is the floor the capex-revenue coverage analysis should survive on. The MED-tier pipeline (16 GW) and SPEC/INFER pipeline (6.5 GW) sit above this floor — but the floor itself pays for the thesis.

The **full-realization case of 53.5 GW** is the bull reading: every stretch target hits, every LOI converts, every inferred MW materializes. That's the number the industry press tends to cite, and the least falsifiable.

---

## What's in each tier, line by line

### T1 — Operational today (7.96 GW)

Physical MW online as of 2026-Q2. Probability of existing = 1.00 (it already exists). Realization is orthogonal to existence: even T1 MW can under-deliver economically if utilization drops, but the physical GW is evidenced.

| Source | GW |
|---|---:|
| Epoch-evidenced current operational (all frontier AI sites) | 6.67 |
| Neocloud ex-Epoch directly-disclosed (CoreWeave 0.85 + Nebius 0.17 + Crusoe 0.20 + Nscale 0.02 + Lambda 0.05) | 1.29 |
| **Subtotal** | **7.96** |

Note: Voltage Park 0.135 GW and Together AI 0.065 GW are ex-Epoch operational but MW is *inferred* (Voltage Park from 35,000-GPU footprint disclosed; Together from fleet footprint estimate). Those 0.20 GW sit in T6, not T1.

### T2 — Physically evidenced / under construction (11.92 GW)

Construction visible on satellite imagery, permits filed, end-of-timeline 2026–2027. Higher-probability than announced-plan because physical steel and interconnect approvals are already in motion.

| Component | GW | What it is |
|---|---:|---|
| Epoch sites w/ end-of-timeline 2026-2027, construction visible | 11.22 | MSFT Fairwater WI, Fairwater MS, Meta Temple, Meta Richland Parish, Stargate Abilene, xAI Colossus 2, Google Council Bluffs |
| Overlay: Fairwater international (Narvik, Loughton, Dublin) | 0.70 | MSFT press + Nscale/Ark press; sites named, leases signed, hydropower PPA in Narvik |
| **Subtotal** | **11.92** |

Why "medium-high" and not "high": construction delays, grid-interconnection queue slippage, and chip-delivery pacing. Not all T2 lands on schedule even when the physical build is real and the contracts are signed.

### T3 — Firm commercial commitment (7.90 GW)

Legally binding commercial contracts — RPO, take-or-pay, 10–15-year leases — with investment-grade counterparties. No physical construction visible yet (that would push to T2), but the commercial commitment is enforceable.

| Component | GW | What it is |
|---|---:|---|
| Neocloud contracted ex-Epoch | 7.90 | CoreWeave 2.30 + Nebius 2.00 + Nscale 0.90 + Crusoe 1.98 + Lambda 0.32 + Applied Digital PF2 0.20 + Together 0.20 |

Anchor contracts: CoreWeave FY2025 RPO $60.7B (primarily MSFT, OpenAI, Meta), Nebius-MSFT $17.4–19.4B, Nebius-Meta up to $27B (Mar 2026 expansion), Applied Digital 15-year CoreWeave leases ($11B across ELN-02/03 + PF2 hyperscaler undisclosed).

Why not T2: while the contracts are binding, the shells these contracts will run on are mostly still greenfield or early-permit. CoreWeave's Cheyenne WY 1.8 GW, Nebius's 3-GW-by-EOY-2026 fleet build, Crusoe's Cheyenne site — all contracted, none yet satellite-evidenced.

### T4 — Announced site-level plan (16.28 GW)

Primary-sourced announcements with named site, named operator, disclosed MW, and a 2028 (or earlier) timeline. Substantial delivery risk (2–3 years out; grid + chip + construction pacing) but backed by material primary sources and real money.

| Component | GW | What it is |
|---|---:|---|
| Epoch sites scheduled 2028 | 12.61 | Mostly Meta Hyperion outer phases, MSFT Fairwater future buildings, Stargate Shackelford/NM/Michigan/Wisconsin/Milam, Google future sites |
| Overlay: Anthropic-AWS incremental (Apr 20, 2026) | 3.17 | "Up to 5 GW new capacity" — primary Anthropic+Amazon announcement; 1 GW near-term (end-2026) floor, residual by 2030 |
| Overlay: xAI-HUMAIN Saudi | 0.50 | Announced Nov 2025, 18k GB300 Phase 1 cluster |
| **Subtotal** | **16.28** |

### T5 — LOI / stretch target (6.30 GW)

Announced commitments where the range bottoms at zero, CEO earnings-call stretch language, or dollar-envelope-only commitments. Execution is uncertain along multiple dimensions.

| Component | GW | What it is |
|---|---:|---|
| Epoch #speculative-tagged future portion | 1.49 | Amazon Ridgeland +1.008 GW + Amazon Madison future +0.478 GW — Epoch's own #speculative tag |
| Epoch 2029–2030 scheduled | 1.07 | CoreWeave Helios +0.800 GW by 2029, Stream Phoenix +0.267 GW by 2030 |
| Overlay: Anthropic-Azure "1 GW" (no sites disclosed) | 1.00 | Could be zero if sites land in already-tracked Azure campuses |
| Overlay: Meta Hyperion stretch (Zuck Q2 FY25 "5 GW") | 2.74 | Range explicitly [0, 2.74]; Meta newsroom commits to "over 2 GW" (already in T2/T4) |
| **Subtotal** | **6.30** |

Why T5 not T4: every row here either has an announced MW figure that floors to zero in bear case, or has a stretch timeline (2029–2030) where Epoch's own confidence tagging drops to #speculative. Not throwaway — just below the firm-announcement threshold.

### T6 — Analyst inference (0.26 GW)

MW that is **not primary-disclosed** but extrapolated from GPU counts, fleet sizes, or investment dollar figures.

| Component | GW | What it is |
|---|---:|---|
| Overlay: xAI Colossus 2 residual beyond Epoch | 0.06 | Musk X-post "almost 2 GW" net of Epoch's 1.94 GW buildout |
| Neocloud: Voltage Park / Lightning operational | 0.135 | Inferred from 35k-GPU footprint, no direct MW disclosure |
| Neocloud: Together AI operational | 0.065 | Fleet estimate from Sacra secondary |
| **Subtotal** | **0.26** |

Why T6 not T1: these facilities are almost certainly operational (they're renting GPUs today), but because the primary disclosure is GPU count rather than MW, we can't place them in T1 without an inference step. The 0.26 GW carries a 0.25 realization probability — not because they don't exist, but because the *MW attribution* may be off by up to half.

---

## What drives the [45.74, 53.48] arithmetic range

```
LOW  (45.74) = T1 (7.96) + T2 (11.92) + T3 (7.90) + T4 low-reading (~14.4)
                                                + T5 & T6 mostly zero
HIGH (53.48) = T1 (7.96) + T2 (11.92) + T3 (7.90) + T4 high-reading (~17.8)
                                                + T5 full (6.30) + T6 full (0.26)
                                                + overlay ceilings on T4 rows
```

**Put plainly:** the low-bound `45.74 GW` is what happens if T5 and T6 compress to zero (Meta stays at 2 GW, Anthropic-Azure sites live inside existing Azure campuses, Ridgeland pushes out) and T4 reads at its lower range. The high-bound `53.48 GW` is what happens if every stretch target hits and overlay ranges read at ceiling.

**Compare to probability-weighted ~36 GW:** the probability-weighted horizon is *below* even the arithmetic low because probabilities < 1.00 on T2/T3/T4 pull down even the hard-anchored tiers. That's the price of treating these as *forecasts* rather than *commitments*.

---

## Sovereign-AI sidebar (not in the 50.62 above)

Applying the same six-tier framework to the 1.95 GW sovereign sidebar:

| Tier | Commitment | GW (point) | Range | Realization prob | Why this tier |
|---|---|---:|---|---:|---|
| **T4** | Microsoft-G42 UAE Khazna | 0.20 | [0.20, 0.20] | 0.70 | Firm Phase 1, narrow range; just outside Western operator set |
| **T4** | HUMAIN-AMD Saudi | 0.50 | [0.30, 0.70] | 0.55 | $10B JV, primary-announced, narrow range |
| **T5** | UK Culham AI Growth Zone | 0.25 | [0.10, 0.50] | 0.30 | Gov announcement, no anchor tenant, UK grid-queue risk material |
| **T5** | Reliance Jio Jamnagar | 1.00 | [0.12, 3.00] | 0.20 | Ambani AGM verbatim "gigawatt-scale"; Phase 1 (120 MW) is T4 subelement |

Sovereign-AI is structurally less anchored than Western (fewer primary disclosures, longer execution horizons, bigger grid-queue risk, non-IG counterparties), which is why we report it as a separate sidebar rather than folding it into the Western coverage-ratio denominator.

Sovereign probability-weighted total: 0.20×0.70 + 0.50×0.55 + 0.25×0.30 + 1.00×0.20 = **0.69 GW** (versus 1.95 GW announced).

---

## How Epoch tags feed into tier assignment

Epoch tags sites with `#confident`, `#likely`, `#speculative` on owner / user / project attribution. Mapping to our tiers:

- Epoch `#confident` operational → **T1**
- Epoch `#confident` end-of-timeline 2026–2027 → **T2**
- Epoch `#confident` end-of-timeline 2028 → **T4**
- Epoch `#speculative` attribution, any timeline → **T5** (regardless of whether buildout MW exists — the attribution uncertainty is the binding constraint)
- Epoch `#confident` 2029–2030 → **T5** (outer-year slippage risk)

Our overlay adds its own confidence signal via the **range width** of each commitment:

- **Range floor ~ point** (e.g. UAE Khazna [0.20, 0.20]) → T3/T4 depending on contract status
- **Range narrow, symmetric around point** (e.g. HUMAIN Saudi [0.40, 0.60]) → T4
- **Range floor at zero** (e.g. Meta Hyperion [0, 2.74], Anthropic-Azure [0, 1.00]) → **T5**
- **Range ceiling 3×+ the point** (e.g. Reliance Jio [0.12, 3.00]) → **T5** with override probability below T5 default

That's the overlay's native confidence signal. The `totals:` block in the YAML preserves it; the CSV makes it sortable; `audit_totals.py` rolls it up.

---

## Bottom line for the paper

The flywheel story depends on **T2 + T3 + T4 = 36.1 GW** of "announced but not yet operational" capacity with material commercial or physical backing actually materializing. That's the mass under the probability-weighted curve.

The **6.56 GW in T5 + T6** is the cushion the reader can strip out in a bear reading — giving a **27.8 GW conservative floor**, which the capex-revenue coverage analysis must survive on.

**So the defensible framing for an LP:**
> "Our Western AI horizon is 50.6 GW announced, ~36 GW probability-weighted, 27.8 GW conservative (T1+T2+T3 only), 53.5 GW full-realization ceiling. Of the announced 50.6 GW, ~8 GW is already operational (T1), another ~12 GW has physical construction visible (T2), ~8 GW is firm commercial contract (T3), ~16 GW is plausibly-on-timeline announced at named sites (T4), and ~6.5 GW is stretch or inference (T5/T6). The capex-revenue coverage analysis rests on the 28 GW conservative floor actually landing; the additional ~8 GW to the 36 GW probability-weighted line is the realistic-case upside; the remaining ~17 GW to full-realization is the path-to-abundance scenario."
