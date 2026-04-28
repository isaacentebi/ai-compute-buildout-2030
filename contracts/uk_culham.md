# UK Culham AI Growth Zone

## TL;DR

First UK AI Growth Zone, designated by UK Government on Jan 13, 2025 (AI Opportunities Action Plan response). UKAEA sponsor/landlord; strategic investment partner TBD via EOI process. Two atoms in canonical sovereign sidebar: `uk_culham_ai_growth_zone_initial_100mw` (0.120 GW facility = 100 MW IT × PUE 1.20, T4) + `uk_culham_ai_growth_zone` (0.180 GW facility = 150 MW IT × PUE 1.20, T5 scale-out residual). Total = 0.300 GW facility. **Rev-4.2 split addresses the reviewer-flagged 300 vs 500 MW inconsistency**: 300 MW is the analyst central case (100 IT initial + 150 IT scale-out, both at PUE 1.20). The 500 MW figure is the EOI/policy maximum, not a contracted build. Sovereign sidebar only — UK domestic public-private compute, **not Western denominator**.

## Counterparties

- **Operator**: TBD strategic investment partner (UKAEA-led EOI process, no executed selection)
- **Anchor tenant / user**: UKAEA fusion/R&D allocation (up to 20 MW or equivalent services); UK public-sector / sovereign compute; commercial AI users TBD
- **Government partner**: UK Government (DSIT) + UKAEA (sponsor) + AIGZ Delivery Unit
- **Financing partner(s)**: TBD private capital via PPP; no contracted government support package found

## Structure

- **Type**: Public-private partnership — strategic investor sought to build, finance, and operate large AI data centre on UKAEA Culham Campus
- **Term**: Undisclosed (target April 2028 for 100 MW per Find a Tender)
- **Announced contract value**: Undisclosed
- **Take-or-pay coverage**: None disclosed
- **Sovereign-AI policy framing**: UK AI Growth Zone programme; "secure, dedicated public sector computing capacity"; UK Compute Roadmap 6 GW by 2030 envelope
- **Optionality**: 100 MW initial proposal can scale "potentially up to 500 MW" pending expanded acreage; Local Development Order pending

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.000 / 0.000 / 0.001 | Construction | Sunrise 1.4 MW fusion AI supercomputer goes live June 2026 (separate, not the 100 MW programme) |
| 2027 | 0.000 / 0.000 / 0.050 | Construction | EOI partner selection + planning consent |
| 2028 | 0.000 / 0.050 / 0.120 | T4 | April 2028 ambitious target per Find a Tender |
| 2029 | 0.050 / 0.120 / 0.300 | T4/T5 | Initial 100 MW operational; scale-out underway |
| 2030 | 0.100 / 0.300 / 0.600 | T4/T5 | Initial 0.12 facility + scale-out 0.18 facility = 0.30 central; high case ≈ 500 MW IT envelope |

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Culham Campus first plot | Culham, Oxfordshire | UKAEA → TBD partner | None in Epoch | Initial 100 MW IT atom | T4 |
| Culham Campus expanded acreage | Culham, Oxfordshire | UKAEA → TBD partner | None in Epoch | Scale-out 150 MW IT residual atom | T5 |
| Land adjacent to Culham Campus (No. 1 site) | Oxfordshire | Adjacent developer | None in Epoch | Planning context, separate application | Context |
| Sunrise fusion AI supercomputer | Culham | UKAEA | None in Epoch | 1.4 MW, separate from 100/500 MW programme | Context |

## Financing Stack

- **UK Government / DSIT / UKAEA**: site, designation, AIGZ Delivery Unit, planning support
- **TBD strategic investor**: capex, O&M, customer acquisition, technology stack
- No capex envelope, lease economics, debt/equity stack, or government support package disclosed

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `uk_culham_ai_growth_zone_initial_100mw` — 100 MW IT / 120 MW facility @ PUE 1.20, T4 announced sovereign, source UKAEA EOI Aug 12, 2025
- `uk_culham_ai_growth_zone` — 150 MW IT / 180 MW facility @ PUE 1.20, T5 speculative sovereign (scale-out residual), source AI Opportunities Action Plan response Jan 13, 2025

## Dedupe Notes

**Reviewer's 300 vs 500 MW question resolved by Rev-4.2 split.** Initial atom = 100 MW IT × 1.20 PUE = 120 MW facility. Scale-out atom = 150 MW IT × 1.20 PUE = 180 MW facility. Sum = 300 MW facility. The prior 300 MW central figure was an analyst conversion of 250 MW IT × 1.20, **never a 500 MW figure** — primary sources state 100 MW initial and "up to 500 MW" maximum.

600 MW peak campus power (UKAEA strategic investor PDF) is combined National Grid + SSE infrastructure, not committed data-centre load. **Not a third atom.**

Sunrise 1.4 MW is a separate fusion AI supercomputer programme. **Not part of the 100/500 MW data-centre count.**

No Epoch overlap; no Western frontier-lab overlap.

## Risk Axes

1. **Counterparty risk** — Strategic investment partner not yet selected; no operator/anchor tenant/contract economics found.
2. **Regulatory risk** — Planning permission outstanding (Local Development Order in flight; No. 1 adjacent site application live); environmental review; community/local-benefit commitments.
3. **Power / interconnect risk** — UKAEA EOI: 132 kV + 400 kV connections, ~100 MW steady-state dual-resilient power available for first plot. Scale-up to 500 MW depends on further National Grid + NESO arrangements.
4. **Supply chain risk** — No GPU/server/cooling/EPC procurement for the 100 MW; Sunrise suppliers are for the separate 1.4 MW machine.
5. **Technology risk** — Official MW basis is not cleanly IT vs facility (NESO flags this market-wide); we apply PUE 1.20 per UK climate.
6. **Financing risk** — No capex envelope, lease economics, debt/equity stack disclosed.
7. **Structural optionality** — 100 MW is firm initial opportunity; 500 MW is policy aspiration / EOI maximum, not a contracted build.

## Temporal Logic

- **Earliest plausible energization**: April 2028 ("ambitious" Find a Tender date, subject to planning permission)
- **Central case**: 2029–2030 (initial 100 MW operational; scale-out underway)
- **Latest plausible**: 2030 (UK Compute Roadmap "each AIGZ at least 500 MW by 2030" criterion)
- **Critical-path dependency**: Strategic investor selection → planning consent → grid connection → energization

## Sovereign Sidebar Treatment

Per user direction, this is a **sovereign stretch annex** entry, not Western denominator. Both atoms `scope: sovereign`, both `included_*: false`. Culham is UK domestic sovereign/public-private compute. UKAEA fusion R&D + AI Research Resource + UK Compute Roadmap. **Not** a Western frontier-lab take-or-pay row.

Per-row tier: **T4** initial (designated site, EOI, ~100 MW dual-resilient power, target April 2028), **T5** scale-out (policy aspiration without partner/planning/grid allocation). **No "floor" language anywhere.**

## Reviewer Findings Addressed

- **Finding #9 (sovereign treatment)** + reviewer's 300 vs 500 MW inconsistency: Rev-4.2 split converts the prior analyst 300 MW central into two source-anchored atoms (100 MW IT initial + 150 MW IT scale-out); 500 MW is high case, not central. This page documents the math (100 + 150 IT = 250 IT; × PUE 1.20 = 300 MW facility) explicitly.

## Open Questions / Gaps

- Strategic investor name; PPP/lease terms
- MW basis (IT vs facility vs grid import)
- Planning consent timeline; Culham-specific NESO connection milestones
- Whether 500 MW replaces 300 MW central or stays as high case in long-run policy framing

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [UK Government, AI Opportunities Action Plan](https://www.gov.uk/government/publications/ai-opportunities-action-plan) | 2025-01-13 | Government policy | AI Growth Zone programme; Culham first AIGZ | "AI Growth Zones" |
| [UKAEA Culham EOI](https://culham.org.uk/invest-at-culham-campus/expression-of-interest/) | 2025-08-12 | Government / agency | Initial 100 MW opportunity; 132 kV + 400 kV; dual-resilient power | "100 MW dual-resilient" |
| [Find a Tender, Culham AI DC](https://www.find-tender.service.gov.uk/) | 2025 | Government tender | April 2028 target; partner selection in flight | "ambitious April 2028" |
| [UK Compute Roadmap](https://www.gov.uk/government/publications/uk-compute-roadmap) | 2025 | Government policy | UK Compute 6 GW by 2030; per-AIGZ ≥500 MW criterion | "at least 500 MW by 2030" |
| [Engineering at UKAEA, Sunrise supercomputer](https://www.gov.uk/government/news/sunrise-fusion-ai-supercomputer) | 2026 | Government release | Separate 1.4 MW Sunrise programme | "Sunrise fusion AI" |

## Cross-Links

- Research dispatch: `docs/research/D3_uk_culham.md`
- Atoms: `canonical_capacity_atoms.yaml` (search `uk_culham_ai_growth_zone`, `uk_culham_ai_growth_zone_initial_100mw`)
- Dedupe entries: `dedupe_audit.csv` (group `uk_culham_ai_growth_zone`)
- Audit response: `RESPONSE_TO_AUDIT.md` (Finding #9)
