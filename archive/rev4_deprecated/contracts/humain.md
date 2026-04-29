# HUMAIN — Saudi Sovereign AI Capacity (xAI / AMD / Cisco / NVIDIA tracks)

## TL;DR

HUMAIN is PIF's full-stack Saudi AI vehicle, launched May 12, 2025. Two atoms in the canonical sovereign sidebar — `xai_humain_saudi` (0.500 GW T4) and `humain_amd_saudi` (0.500 GW T4) — both **excluded from the Western denominator**. Four overlapping HUMAIN capacity tracks exist and **must not be silently summed**: (a) xAI / HUMAIN November 2025 framework for "build a 500MW data center in Saudi Arabia"; (b) NVIDIA / HUMAIN May 2025 partnership for "up to 500 megawatts" of Saudi AI factories; (c) AMD / HUMAIN May 2025 $10B collaboration for "deploy 500 megawatts of AI compute capacity"; (d) AMD / Cisco / HUMAIN November 2025 JV for "up to 1 GW by 2030" with 100 MW Saudi phase 1. Two named ground-broken HUMAIN sites (Riyadh, Dammam, 100 MW initial each, Q2 2026 target) likely host the first phases of one or more of those tracks. BIS export approval (Commerce, Nov 19, 2025) covers up to 35,000 GB300-equivalents — a material near-term constraint relative to several-hundred-thousand-GPU long-run ambition. Sovereign sidebar only — T4 announced framework, not T3 executed contract.

## Counterparties

- **Operator**: HUMAIN (PIF-owned full-stack AI company)
- **Anchor tenants / users**: xAI / Grok (xAI track); Saudi sovereign + enterprise/startup customers; Luma AI named first JV-phase customer (AMD/Cisco JV)
- **Government partner**: Kingdom of Saudi Arabia / PIF (majority owner); HRH Crown Prince launch May 12, 2025
- **Financing partner(s)**: PIF (equity); Aramco non-binding minority-stake term sheet (Oct 28, 2025); Infra non-binding $1.2B / 250 MW financing framework (Jan 22, 2026)

## Structure

- **Type**: Multi-track — chip procurement (NVIDIA GB300, AMD MI450), JV (AMD / Cisco / HUMAIN), framework agreement (xAI), ground lease / colo (Riyadh + Dammam HUMAIN sites)
- **Term**: Five years for AMD May 2025; "by 2030" for AMD/Cisco JV; xAI undisclosed
- **Announced contract value**: AMD May "up to $10B"; AMD/Cisco JV founding-investor sizes undisclosed; xAI / HUMAIN financing not disclosed
- **Take-or-pay coverage**: None disclosed in any track
- **Sovereign-AI policy framing**: PIF launches HUMAIN as "global AI powerhouse" (May 12, 2025); BIS-approved Saudi sovereign chip pipeline (Nov 19, 2025)
- **Optionality**: All four tracks use "up to" / "first of a network" / "phase 1" language. High structural optionality.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.10 / 0.20 / 0.30 | T2/T4 | Riyadh + Dammam initial 100 MW each (DCD Aug 26, 2025); AMD/Cisco JV phase 1 100 MW |
| 2027 | 0.20 / 0.40 / 0.60 | T4 | xAI Nov 2025 framework operational ramp begins |
| 2028 | 0.30 / 0.50 / 0.80 | T4 | AMD May 5-year midpoint; central case ≈ AMD May 500 MW envelope |
| 2029 | 0.40 / 0.70 / 1.00 | T4/T5 | AMD/Cisco JV ramp toward 1 GW; some xAI tranche operational |
| 2030 | 0.50 / 1.00 / 1.50 | T4/T5 | High = AMD/Cisco JV 1 GW envelope; **rows are not summed across xAI 500 / NVIDIA 500 / AMD 500 / AMD-Cisco 1000 candidates** |

The central column reflects ~50% probability that the four tracks collapse into a single Saudi capacity envelope rather than four additive rows. Low column assumes near-complete subsumption (only Riyadh + Dammam phase 1 + JV phase 1 deliver). High column assumes maximum independence.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Riyadh facility | Riyadh, KSA | HUMAIN | None in Epoch | Likely host AMD/Cisco JV phase 1 (100 MW) | T4 |
| Dammam facility | Dammam, KSA | HUMAIN | None in Epoch | Likely host xAI or AMD initial phase | T4 |
| xAI 500 MW (undisclosed first site) | KSA | HUMAIN / xAI partner | None in Epoch | Same canonical row as `xai_humain_saudi` | T4 |
| AMD 500 MW (KSA + US network) | KSA + US | HUMAIN / AMD | None in Epoch | Same canonical row as `humain_amd_saudi`; subsumed-risk vs AMD/Cisco JV | T4 |
| HUMAIN 211-plot land bank | KSA | HUMAIN | None in Epoch | Future site optionality (DCD Mar 12, 2026) | Context |

## Financing Stack

- **PIF equity**: HUMAIN 100% PIF-owned at launch (May 12, 2025)
- **Aramco minority**: Non-binding term sheet (Oct 28, 2025); PIF retains majority pending definitive agreements
- **Infra framework**: Non-binding $1.2B for up to 250 MW (Jan 22, 2026); not allocated to any specific row
- **AMD May commitment**: "up to $10B" over 5 years (AMD primary release, May 13, 2025)
- **AMD / Cisco JV founding-investor sizes**: Undisclosed
- **xAI / HUMAIN financing**: Not disclosed
- **Vendor financing**: Implied via NVIDIA / AMD / Cisco hardware payment terms; not formalized

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `xai_humain_saudi` — 500 MW facility (370.37 IT @ PUE 1.35); T4 sovereign; source DCD Nov 20, 2025 + xAI framework Nov 19, 2025; **Rev-4.3 source date refresh** from stale 2025-05-14
- `humain_amd_saudi` — 500 MW facility (370.37 IT @ PUE 1.35); T4 sovereign; source AMD primary May 13, 2025; documented subsumption-risk vs AMD/Cisco JV

## Dedupe Notes

This contract is the structural example of why sovereign-cluster pairwise overlap matters.

**xAI 500 MW vs NVIDIA-HUMAIN 500 MW**: high overlap risk. xAI's November 2025 facility appears NVIDIA-powered per media context (DCD: "build a 500MW data center"); NVIDIA-HUMAIN May 13, 2025 release also says "up to 500 megawatts" of Saudi AI factories with first 18,000 GB300 phase. Both rows would not be additive without site/tenant allocation. **Not summed.** NVIDIA-HUMAIN row is not created in canonical to avoid silent double-count.

**AMD 500 MW (May) vs AMD/Cisco JV 1 GW (Nov)**: high subsumption risk. DCD: *"unclear whether today's announcement is separate from earlier 500 MW AMD deal"*. The November JV is positioned as a deepened collaboration with Cisco joining and an expanded "up to 1 GW by 2030" envelope; the May 500 MW likely lands inside that envelope. **Not summed.** AMD/Cisco JV 1 GW row is not created in canonical.

**Riyadh + Dammam 100 MW each (Q2 2026)**: likely host first phases of one or more of the four candidate tracks; not a fifth standalone capacity row.

**Net sovereign-sidebar inclusion**: 1.0 GW facility (xAI 500 + AMD 500), counted once each, with documented `double_count_risk: high (documented Rev-4.3)`.

## Risk Axes

1. **Counterparty risk** — Frameworks/MoUs only; no executed lease/PPA/take-or-pay in any of the four tracks. xAI Nov 2025 confirmed *"design, build, and operate hyperscale GPU data centers"* but stops short of an executed commercial contract.
2. **Regulatory risk** — **BIS export controls are the binding near-term constraint**. Commerce Nov 19, 2025 approved up to 35,000 GB300-equivalents for HUMAIN, conditioned on security/reporting compliance. This is materially below several-hundred-thousand-GPU long-run ambition; further allocations require ongoing BIS review.
3. **Power / interconnect risk** — No substation, PPA, utility filing, or grid-connection schedule found for any 500 MW HUMAIN facility. Available evidence: "sustainable power systems" + "global fiber interconnects" (HUMAIN press) + Riyadh/Dammam ground-breaking (DCD Bloomberg). Saudi grid integration at 500 MW class typically takes 18-30 months past first concrete.
4. **Supply chain risk** — Chip export licensing is the binding constraint. AMD MI450 + NVIDIA GB300 + Cisco networking + liquid cooling at hot-arid PUE 1.35 amplify thermal/electrical equipment risk. No public commitments for transformers, switchgear, or HVAC vendors.
5. **Technology risk** — Grok requires sovereign-data localization; Saudi data residency rules may constrain cross-border training. AMD ROCm at hyperscale carries adoption risk vs. NVIDIA CUDA lock-in.
6. **Financing risk** — **PIF equity is firm; Aramco term sheet is non-binding pending definitive agreements; Infra $1.2B / 250 MW framework is non-binding and unallocated.** The "$10B AMD up to" is a vendor commitment, not project capex.
7. **Structural optionality** — *"first of a network"* + *"phase 1 of 1 GW"* + *"up to"* — every disclosure carries scale-up and walk-away optionality. Low-bound case is that only Riyadh + Dammam initial 100 MW each + AMD/Cisco JV phase 1 (100 MW) operationalize by 2030.

## Temporal Logic

- **Earliest plausible energization**: Q2 2026 — Riyadh + Dammam 100 MW initial each. Source: DCD, Aug 26, 2025: *"initial capacity of 100MW each"*.
- **Central case**: 2027–2028 — AMD May 5-year window midpoint; xAI Nov framework operational ramp.
- **Latest plausible**: 2030 — AMD/Cisco JV "up to 1 GW by 2030" envelope. Source: AMD primary release, Nov 19, 2025.
- **Critical-path dependency**: BIS chip export licensing cadence; Saudi grid/substation buildout for site-by-site interconnect; Aramco minority-stake definitive close.

## Sovereign Sidebar Treatment

Per user direction, this is a **sovereign stretch annex** entry, not Western denominator. Both atoms carry `scope: sovereign` and `included_*: false`. HUMAIN is PIF-owned; the customer base is Saudi sovereign + enterprise + Luma AI. No Western frontier-lab take-or-pay disclosed. Sidebar treatment is correct.

Per-row tier: **T4** (announced framework, magnitude + counterparty + broad timing all disclosed). Not T3 because no executed lease/PPA. Not T5 because xAI confirmed and HUMAIN broke ground on two named sites.

**No "floor" language used anywhere on this page.**

## Reviewer Findings Addressed

- **Finding #9 (sovereign treatment)**: This page documents per-row tier, dedupe-once policy across four overlap candidates, and explicit Western-denominator exclusion. Aligned with `dedupe_audit.csv` `double_count_risk: high (documented Rev-4.3)` for both atoms.
- **Reviewer's manual verification list**:
  - `xai_humain_saudi` — Rev-4.3 source date refresh from stale 2025-05-14 to 2025-11-20; primary xAI framework + DCD secondary size; explicit overlap-risk documentation against NVIDIA-HUMAIN.
  - `humain_amd_saudi` — Rev-4.3 primary AMD May 13, 2025 release replaces secondary DCD; subsumption-risk against AMD/Cisco JV documented.

## Open Questions / Gaps

- Executed xAI / HUMAIN contract showing firm MW, term, site, payment obligations.
- Exact Saudi site for the xAI 500 MW facility, plus utility interconnect / substation / PPA evidence.
- Whether the xAI 500 MW is a new facility, an anchor tenancy in NVIDIA-HUMAIN capacity, or a phase of HUMAIN's first Riyadh / Dammam facilities.
- Executed AMD / HUMAIN or AMD / Cisco / HUMAIN JV documents allocating the May 500 MW between Saudi Arabia and the US.
- Whether the November 2025 AMD / Cisco 1 GW JV supersedes, expands, or nests the May 2025 500 MW AMD / HUMAIN row.
- Definitive financing allocation: PIF equity, Aramco minority-stake completion, Infra $1.2B framework, vendor financing.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [xAI, "Grok goes Global with KSA"](https://x.ai/news/grok-goes-global) | 2025-11-19 | Primary company | xAI/HUMAIN/KSA framework | "hyperscale GPU data centers" |
| [DCD, "xAI and Humain to build 500MW Saudi Arabia data center"](https://www.datacenterdynamics.com/en/news/xai-humain-data-center-elon-musk/) | 2025-11-20 | Secondary media | xAI 500 MW size | "build a 500MW data center" |
| [AMD, "AMD and HUMAIN Form Strategic, $10B Collaboration"](https://www.amd.com/en/newsroom/press-releases/2025-5-13-amd-and-humain-form-strategic--10b-collaboration-.html) | 2025-05-13 | Primary company | 500 MW AMD/HUMAIN; up to $10B | "deploy 500 megawatts of AI compute capacity" |
| [HUMAIN / AMD / Cisco JV release](https://www.amd.com/en/newsroom/press-releases/2025-11-19-amd-cisco-and-humain-to-form-joint-venture.html) | 2025-11-19 | Primary company | Up to 1 GW by 2030; phase 1 100 MW | "phase 1 deployment of 100 MW" |
| [DCD, "AMD, Cisco, and Humain set up JV"](https://www.datacenterdynamics.com/en/news/amd-cisco-and-humain-set-up-jv-for-1gw-of-ai-infrastructure-in-saudi-arabia/) | 2025-11-20 | Secondary media | Subsumption flag | "unclear whether today's announcement is separate" |
| [NVIDIA, "HUMAIN and NVIDIA Announce Strategic Partnership"](https://nvidianews.nvidia.com/news/humain-and-nvidia-announce-strategic-partnership-to-build-ai-factories-of-the-future-in-saudi-arabia) | 2025-05-13 | Primary company | NVIDIA-HUMAIN 500 MW; first 18,000 GB300 | "up to 500 megawatts" |
| [US Commerce, UAE/Saudi Chip Exports](https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports) | 2025-11-19 | Government release | HUMAIN export approval up to 35,000 GB300 | "up to 35,000 Nvidia Blackwell chips" |
| [PIF, "HRH Crown Prince launches HUMAIN"](https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/hrh-crown-prince-launches-humain-as-global-ai-powerhouse/) | 2025-05-12 | PIF release | HUMAIN launch; PIF ownership | "PIF-owned company" |
| [PIF / Aramco HUMAIN term sheet](https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/pif-and-aramco-agree-for-aramco-to-acquire-a-significant-minority-stake-in-humain-with-pif-retaining-majority-ownership/) | 2025-10-28 | PIF release | Non-binding term sheet | "non-binding term sheet" |
| [DCD, "Humain breaks ground two data centers"](https://www.datacenterdynamics.com/en/news/humain-breaks-ground-two-data-centers-with-first-facilities-expected-to-go-live-in-q2-2026/) | 2025-08-26 | Secondary media | Riyadh + Dammam 100 MW initial each | "initial capacity of 100MW each" |

## Cross-Links

- Research dispatch: `docs/research/D2_humain.md`
- Atoms: `canonical_capacity_atoms.yaml` (search `xai_humain_saudi`, `humain_amd_saudi`)
- Dedupe entries: `dedupe_audit.csv` (groups `xai_humain_saudi_500mw`, `humain_amd_saudi_500mw_subsumed_by_amd_cisco_jv_1gw`)
- Row delta ledger: `row_delta_ledger.csv` (Rev-4.3 source-date refresh entries for both atoms)
- Audit response: `RESPONSE_TO_AUDIT.md` (Finding #9)
