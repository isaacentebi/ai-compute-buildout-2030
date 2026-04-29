# Reliance / Jio — Jamnagar + Andhra India AI Capacity

## TL;DR

Reliance Industries / Jio Platforms / Reliance Intelligence / Digital Connexion sovereign program. Four atoms in canonical: `reliance_jio_jamnagar` (0.880 GW T5 Jamnagar stretch residual), `reliance_jio_jamnagar_near_term_120mw` (0.120 GW T2 from India AI Impact Summit Feb 19, 2026), Rev-4.3 NEW `reliance_andhra_1gw_ai_dc_mou` (1.000 GW T5 sovereign, included via dedupe-once), Rev-4.3 NEW `digital_connexion_vizag_1gw_overlap` (excluded — same program as Andhra MoU, 12 days apart). RIL FY25 plan = ~$110B over 7 years. Google Cloud Jamnagar region dedicated to Reliance. Kutch generation + Kutch-to-Jamnagar dedicated transmission line under construction. **Sovereign sidebar only — not in Western denominator.** Per-row tiers shown.

## Counterparties

- **Operator**: Reliance Industries / Jio Platforms / Reliance Intelligence
- **Anchor tenant / user**: Reliance-owned + Indian enterprise + Indian sovereign-AI users; Google Cloud as Jamnagar cloud-region partner
- **Government partner**: Government of India (IndiaAI Mission, MeitY); Government of Andhra Pradesh (Economic Development Board MoU Nov 14, 2025); Government of Gujarat (Jamnagar host)
- **Financing partner(s)**: Reliance balance-sheet equity; Brookfield + Digital Realty (Digital Connexion JV); no project-level debt disclosed

## Structure

- **Type**: Reliance-owned sovereign-AI compute (not a Western take-or-pay cloud lease)
- **Term**: undisclosed; Rs 10 lakh crore plan over 7 years
- **Announced contract value**: ~$110B group AI infrastructure plan FY25–FY32; Digital Connexion $11B by 2030 for AP campus
- **Take-or-pay coverage**: None disclosed
- **Sovereign-AI policy framing**: India sovereign compute affordability + Indian-language AI + India-first compliance + IndiaAI common compute (Jio Platforms eligible bidder)
- **Optionality**: Phased gigawatt ambition; near-term tranche carved out; Andhra MoU-level

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.12 / 0.18 / 0.30 | T2 | >120 MW H2 2026 tranche per ETTelecom Feb 19, 2026 |
| 2027 | 0.20 / 0.35 / 0.50 | T2/T5 | Jamnagar ramp + AP construction begins |
| 2028 | 0.30 / 0.55 / 0.80 | T5 | Multi-GW Jamnagar buildout |
| 2029 | 0.50 / 0.85 / 1.30 | T5 | AP + Jamnagar scaling |
| 2030 | 0.70 / 1.30 / 2.00 | T5 | Jamnagar 1 GW + AP 1 GW envelope; Digital Connexion excluded as same-program |

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Jamnagar near-term tranche | Jamnagar, Gujarat | Reliance Intelligence / Jio | None in Epoch | Same canonical row | T2 |
| Jamnagar GW-scale stretch | Jamnagar, Gujarat | Reliance Intelligence / Jio | None in Epoch | Stretch beyond near-term | T5 |
| Reliance Andhra 1 GW MoU | AP (site undisclosed) | Reliance | None in Epoch | Same program as Digital Connexion Vizag (counted once here) | T5 |
| Digital Connexion Vizag | Visakhapatnam, AP | Digital Connexion JV | None in Epoch | **Excluded — same program as Reliance Andhra MoU** | excluded |
| Google Cloud Jamnagar region | Jamnagar | Google + Reliance | None in Epoch | Cloud anchor, supports Jamnagar capacity | Context |
| Kutch generation + Kutch-Jamnagar transmission | Kutch, Gujarat | RIL New Energy | n/a | Power-readiness, not data-center MW | Context |

## Financing Stack

- **Reliance group capex**: Rs 10 lakh crore / ~$110B over 7 years (group-level, not project-finance close)
- **Digital Connexion AP**: $11B by 2030 (JV-level)
- **Brookfield + Digital Realty**: equity partners in Digital Connexion
- **Reliance Kutch generation**: RIL FY25 investor presentation says execution begun + dedicated transmission line
- **IndiaAI common compute**: PIB context only ($120M scale, 18,693 GPU portfolio, Jio Platforms eligible bidder)

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `reliance_jio_jamnagar` — 0.880 GW facility T5 sovereign (stretch residual after near-term split)
- `reliance_jio_jamnagar_near_term_120mw` — 0.120 GW facility T2 sovereign (Feb 19, 2026 summit)
- `reliance_andhra_1gw_ai_dc_mou` — 1.0 GW facility T5 sovereign (Nov 14, 2025 Reliance/AP MoU) **[Rev-4.3 NEW]**
- `digital_connexion_vizag_1gw_overlap` — **EXCLUDED**, same program as Andhra MoU **[Rev-4.3 NEW]**

## Dedupe Notes

**Andhra Pradesh adjudication (Rev-4.3)**: Reliance/AP government MoU (Nov 14, 2025) and Digital Connexion Vizag campus (Nov 26-27, 2025) are 12 days apart, both Reliance-linked, both AP, both 1 GW. Treated as **same program, counted once** via `reliance_andhra_1gw_ai_dc_mou`. Digital Connexion atom retained for cross-reference, marked `status: excluded`, with `dedupe_adjustment_mw: -1000`.

**Jamnagar split (Rev-4.2)**: 1 GW stretch atom carries 0.880 GW residual; 0.120 GW near-term tranche carved out separately so the H2 2026 evidence is not lost inside the stretch row.

AP state-level ambition is 6 GW data-center capacity by 2030; Reliance/Jio-specific evidence supports only Jamnagar tranches + the AP program. Google/AdaniConneX Visakhapatnam AI hub is separate and not a Reliance row.

## Risk Axes

1. **Counterparty risk** — Reliance balance-sheet credible; offtake/SPV/customer mix opaque; Reliance Intelligence is a newly disclosed entity.
2. **Regulatory risk** — India data localization + IndiaAI sovereign-compute policy + AP/Gujarat data-center incentives + lawful-access requirements. AP MoU still needs land allotment, environmental, coastal, telecom permits.
3. **Power / interconnect risk** — Kutch generation + Kutch-to-Jamnagar dedicated transmission (RIL FY25 IP); 6 GWp solar for AP; no AI data-center grid-connection filing found for any tranche.
4. **Supply chain risk** — No public chip vendor / OEM / liquid-cooling / transformer / switchgear order found for any tranche; Reliance owns no captive accelerator silicon.
5. **Technology risk** — MW basis ambiguous in all primary disclosures (no facility-vs-IT split, no rack density, no accelerator generation). PUE 1.40 used for India hot/humid.
6. **Financing risk** — Rs 10 lakh crore is group-level 7-year, not project-finance close. Digital Connexion $11B by 2030 is JV-level. AP-Reliance project capex undisclosed.
7. **Structural optionality** — Jamnagar phased per Indian demand; Andhra MoU-level; both highly cancellable / scaleable.

## Temporal Logic

- **Earliest**: H2 2026 — *">120 MW will come online"* Jamnagar (ETTelecom + TechCrunch Feb 19, 2026 summit, Mukesh Ambani statement)
- **Central**: 2028–2029 — Jamnagar GW ramp + AP construction
- **Latest**: 2030 — AP 1 GW + Jamnagar GW-scale stretch envelope
- **Critical-path dependency**: Kutch-to-Jamnagar transmission energization; AP land allotment + grid; chip procurement at scale

## Sovereign Sidebar Treatment

Per user direction, this is a **sovereign stretch annex** entry, not Western denominator. All four atoms `scope: sovereign`, all `included_*: false`. Reliance/Jio AI infrastructure is national compute affordability + Indian-language AI + Jio network integration + Reliance-owned green power + India-first compliance. Google Cloud Jamnagar region is dedicated to Reliance — not Western frontier-lab capacity.

Per-row tier: **T2** near-term, **T5** stretch + AP MoU, **excluded** for Vizag (dedupe). **No "floor" language anywhere.**

## Reviewer Findings Addressed

- **Finding #9 (sovereign treatment)**: Per-row tier disclosed; Andhra/Vizag dedupe documented in this page + `dedupe_audit.csv`; Jamnagar 1 GW stretch separated from near-term 120 MW tranche.
- Rev-4.3 added Andhra atom + Digital Connexion exclusion to address the previously-unevaluated Andhra capacity.

## Open Questions / Gaps

- Official Mukesh Ambani Feb 19, 2026 transcript (currently media-cited summit reporting)
- Facility-vs-IT basis for all Reliance/Jio MW/GW disclosures
- Jamnagar coordinates + phasing + interconnect filings
- AP MoU primary text (currently secondary media)
- Reliance vs Digital Connexion same-program adjudication final confirmation
- Chip procurement evidence for any tranche

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [RIL 48th AGM transcript](https://rilstaticasset.akamaized.net/sites/default/files/2025-09/RIL-48th-AGM-Transcripts_2025.pdf) | 2025-08-29 | Primary company | Reliance Intelligence; work begun at Jamnagar; Google Cloud region | "gigawatt-scale AI-ready data centers" |
| [TechCrunch, Reliance $110B AI plan](https://techcrunch.com/2026/02/19/reliance-unveils-110b-ai-investment-plan-as-india-ramps-up-tech-ambitions/) | 2026-02-19 | Secondary media | $110B plan; >120 MW H2 2026 | "Over 120 MW will come online" |
| [Business Standard, Reliance AP 1 GW AI data centre](https://www.business-standard.com/companies/news/reliance-andhra-pradesh-1gw-ai-data-centre-investment-125111401010_1.html) | 2025-11-14 | Secondary media | AP MoU; 1 GW; 6 GWp solar | "1 GW Artificial Intelligence (AI) data centre" |
| [Data Center Dynamics, Digital Connexion AP 1 GW campus](https://www.datacenterdynamics.com/en/news/digital-connexion-signs-mou-to-build-1gw-campus-in-andhra-pradesh-india/) | 2025-11-27 | Specialist secondary | Digital Connexion 1 GW Vizag; $11B by 2030 | "1GW data center campus" |
| [RIL FY25 investor presentation](https://www.ril.com/sites/default/files/2025-07/InvestorPresentation.pdf) | 2025-07-18 | Primary company | Kutch generation; Kutch-Jamnagar transmission | "dedicated transmission line" |
| [PIB / MeitY, IndiaAI common compute](https://psa.gov.in/CMS/web/sites/default/files/publication/India%20all%20set%20to%20launch%20its%20own%20safe%20%26%20secure%20indigenous%20AI%20model%20at%20affordable%20cost%20soon%20Shri%20Ashwini%20Vaishnaw.pdf) | 2025-01-30 | Government | 18,693 GPUs; Jio eligible bidder | "PIF-owned company" (cf. Saudi parallel) |

## Cross-Links

- Research dispatch: `docs/research/D1_reliance_jio.md`
- Atoms: `canonical_capacity_atoms.yaml` (search `reliance_jio_jamnagar`, `reliance_andhra_1gw_ai_dc_mou`, `digital_connexion_vizag_1gw_overlap`)
- Dedupe entries: `dedupe_audit.csv` (groups `reliance_ap_1gw_program`, `reliance_jio_jamnagar`)
- Row delta ledger: `row_delta_ledger.csv` (Rev-4.3 new atom entries)
