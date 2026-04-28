# Nscale / Microsoft — 200,000 GB300 GPU Multi-Country Deployment

## TL;DR

Nscale's October 15, 2025 primary release announces an expanded Microsoft deal for **approximately 200,000 NVIDIA GB300 GPUs** across four countries: Texas (104,000 GPUs at Ward County / Cedarvale, Barstow), Sines (Portugal, 12,600 GPUs), Loughton (UK, 23,040 GPUs at 50 MW scalable to 90 MW), and Narvik (Norway, 52,000 GPUs at the 230 MW secured campus). Aker disclosed a $6.2B five-year Microsoft contract for Narvik, and an April 14, 2026 Nscale release adds more than 30,000 NVIDIA Rubin GPUs to the Narvik footprint in 2027. Microsoft holds a **700 MW Texas second-phase option** starting late 2027 toward Nscale's 1.2 GW Texas footprint plan, but the option is not the same as firm contracted capacity. The **Rev-4.2 fix reduces the Nscale-Microsoft atom from 0.900 GW to 0.240 GW** (Ward County / Cedarvale floor of approximately 234 MW per the Ionic Digital lease, ~240 MW per Nscale rounding) because Narvik and Loughton MW sit in the Microsoft Fairwater International overlay row (`openai_microsoft_fairwater_international`, 0.805 GW facility) and would otherwise be double-counted (`nscale_fairwater_overlap_adjustment` removes 0.600 GW). Sines MW is not disclosed in any primary source.

## Counterparties

- **Operator:**
  - Texas: Nscale (AI infrastructure operator); Ionic Digital (facility owner / lessor at Cedarvale, Ward County, Barstow, TX).
  - Norway: Nscale, with Aker-Nscale JV history rolled into Nscale via the March 9, 2026 Series C announcement.
  - UK (Loughton): Nscale.
  - Portugal (Sines): Start Campus partner-run.
- **Anchor tenant:** Microsoft (sole disclosed anchor for the 200k-GPU agreement).
- **Financing partners:**
  - Aker ASA (publicly listed; disclosed $6.2B five-year Microsoft contract for Narvik with cash flow supporting capex).
  - Ionic Digital (10-year triple-net Cedarvale lease with approximately $2B contracted revenue).
  - Nscale equity: $2B Series C (March 9, 2026) at $14.6B valuation; previous Aker JV roll-up.

## Structure

- **Type:** Cloud capacity / AI infrastructure-as-a-service, multi-country, GB300 (with Rubin expansion 2027).
- **Term:** Aker discloses Narvik as binding **five-year** customer agreement (~$6.2B). Ionic discloses Cedarvale as **10-year** triple-net lease with approximately $2B contracted revenue. Nscale-Microsoft top-level term not separately disclosed.
- **Announced contract value:** Aker $6.2B for Narvik five-year; Ionic ~$2B Cedarvale lease revenue (separate from Microsoft contract value). Microsoft-Nscale aggregate contract value **not primary-disclosed**.
- **RPO/backlog:** Nscale has no public RPO/SEC-style backlog disclosure.
- **Take-or-pay coverage:** Aker Q3 2025 presentation references a 3-5 year take-or-pay model on roughly 120 MW contracted with Microsoft/OpenAI at Kvandal (Narvik). Texas / Sines / Loughton take-or-pay terms not specifically disclosed.
- **Exclusivity:** None disclosed.
- **Optionality:** **Microsoft's 700 MW Texas second-phase option (starts late 2027)** is the principal optional tranche. Nscale's 1.2 GW Texas footprint plan exceeds the firm Ionic 234 MW lease. Loughton is 50 MW scalable to 90 MW. Narvik secured 230 MW with 200+90 MW in queue at Kvandal.

## GW Shape Over Time

| Year | Facility GW low | Facility GW central | Facility GW high | Operational status | Notes |
|---|---:|---:|---:|---|---|
| 2026 | 0.05 | 0.10 | 0.15 | T4 | Sines GPU delivery Q1 2026; Texas Microsoft services begin Q3 2026; Narvik staged services begin 2026 |
| 2027 | 0.30 | 0.50 | 0.80 | T4 | Loughton GB300 Q1 2027; Narvik Rubin expansion 2027; Texas full 240 MW; option exercise window opens late 2027 |
| 2028 | 0.40 | 0.60 | 1.20 | T4 | If Microsoft exercises 700 MW Texas option, full footprint approaches 1.2 GW Texas plan |
| 2029 | 0.50 | 0.70 | 1.40 | T4 | Continued expansion subject to option exercise |
| 2030 | 0.50 | 0.70 | 1.50 | T4 | Steady-state if all options exercised |

Note: GW figures above are *gross* Nscale-Microsoft footprint. The dedupe-adjusted incremental ex-overlay atom is 0.240 GW (Ward County floor). Narvik/Loughton MW already attributed to `openai_microsoft_fairwater_international`.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|---|---|---|---|---:|---|
| Cedarvale / Ward County | Barstow, TX | Nscale (lessee); Ionic Digital (owner) | None in local Epoch snapshot | 0.234–0.240 GW firm; 0.700 GW second-phase option (late 2027) | T4 |
| Narvik / Kvandal | Narvik, Norway | Nscale (Aker-JV roll-up) | Not in Epoch directly; 0.805 GW in `openai_microsoft_fairwater_international` overlay | 230 MW secured + 200+90 MW queue (excluded; Fairwater International) | T4 |
| Loughton | Essex, UK | Nscale | Not in Epoch directly; subsumed in Fairwater International overlay | 50 MW scalable to 90 MW (excluded; Fairwater International) | T4 |
| Sines | Portugal | Start Campus | None in Epoch | 12,600 GPUs; **MW not disclosed** | T4 |
| Glomfjord | Norway | Nscale | Operational seed | 30 MW operational | T1 |

## Financing Stack

- **Capex envelope:** Not disclosed at top level. Aker discloses Narvik capex supported by Microsoft contract cash flow. Ionic Digital Cedarvale lease backed by Microsoft service obligations.
- **Equity:** Nscale Series C $2B at $14.6B valuation (2026-03-09); rolled up Aker-Nscale JV. Aker ASA public-company equity at parent level.
- **Project finance / debt:** Aker references binding five-year customer agreement supporting Narvik project finance; specific lenders/terms not detailed in public release.
- **RPO / prepaid:** None publicly disclosed for Nscale-Microsoft. Aker discloses $6.2B Microsoft contract value for Narvik as primary cash-flow visibility.
- **Public disclosures:** Nscale October 15, 2025 200k GPU release; Microsoft Official Blog "world's most powerful AI datacenter" (2025-09-18); Microsoft Source EMEA Narvik feature (2025-09-17); Aker PRNewswire $6.2B Microsoft release (2025-09-17); Aker ASA Q3 2025 investor presentation (2025-11-04); Ionic Digital Cedarvale release (2025-10-14); Nscale UK release (2025-09-16); Microsoft On the Issues UK $30B (2025-09-16); UK Government US-UK pact (2025-09-16); Nscale Norway expansion release (2026-04-14); Nscale Series C (2026-03-09).

## Atoms Sourced

- `atom:nscale_microsoft_contract_capacity` (0.240 GW T4) — Ward County / Cedarvale floor; Texas-only attribution after Fairwater International dedupe.
- `atom:nscale_fairwater_overlap_adjustment` (−0.600 GW) — removes Narvik + Loughton from Nscale-Microsoft to avoid double-count with `openai_microsoft_fairwater_international`.
- `atom:nscale_operational_seed_capacity` — Glomfjord ~30 MW operational.
- Reference: `openai_microsoft_fairwater_international` (0.805 GW; carries Narvik/Loughton MW).

## Dedupe Notes

- **Epoch overlap:** No direct Nscale row in Epoch. Microsoft sites in Epoch (Fairwater Wisconsin 3.328 GW; Fairwater Atlanta 0.859 GW; Goodyear 0.263 GW; Crusoe Abilene Expansion 0.941 GW) are customer-anchor candidates only — no Nscale primary source ties Nscale capacity to those Microsoft Epoch campuses.
- **Cross-overlay overlap:** **Narvik (230 MW) and Loughton (50–90 MW) sit in the local `openai_microsoft_fairwater_international` overlay row at 0.805 GW facility point.** Microsoft's "world's most powerful AI datacenter" blog explicitly groups Wisconsin with Narvik and Loughton in the global Fairwater AI WAN context. To prevent double-counting, `nscale_fairwater_overlap_adjustment` (−0.600 GW) removes Narvik/Loughton from the Nscale-Microsoft atom; the Fairwater International overlay retains the MW.
- **Residual incremental GW:** 0.240 GW Ward County floor (Texas-only), with 0.700 GW Texas option recognized separately as T4 optionality.
- **Sines:** GPU-only disclosure (12,600 GB300 GPUs); no MW assigned. Carried as gap, not converted.

## Risk Axes

1. **Counterparty:** Microsoft is investment-grade and explicitly named, but **Nscale is private, recently founded, scaled rapidly, and has no public RPO/SEC backlog disclosure.** Aker disclosed $6.2B / 5-yr Microsoft contract value at Narvik anchors counterparty visibility for that site only; the broader 200k-GPU Microsoft contract value is not primary-disclosed.
2. **Regulatory:** Four-country rollout exposes the contract to UK planning/power regimes (Loughton), EU/Portugal grid (Sines via Start Campus), Norway sovereign and hydropower/grid approvals (Narvik), and U.S. ERCOT/Texas permitting (Ward County). Norway sovereign-AI considerations and EU-UK data-residency rules add layered jurisdictional risk.
3. **Power / interconnect:** Strongest evidence at Ward County (Ionic discloses full 234 MW lease capacity; Nscale rounds to ~240 MW) and Narvik (Aker discloses 230 MW secured + 200+90 MW queue at Kvandal). **Sines MW is not disclosed**, and Texas expansion beyond initial phase requires Microsoft to exercise the 700 MW second-phase option.
4. **Supply chain:** Delivery depends on 200,000 GB300 GPUs and 30,000+ Rubin GPUs (April 2026 expansion), plus Dell servers, Nokia networking, and direct-liquid cooling at all four sites. GB300 ramp and Rubin platform readiness in 2027 are the principal supply gates.
5. **Technology obsolescence:** Sites require dense liquid-cooled AI infrastructure; **Ward County is a crypto-to-AI conversion** and Narvik/Loughton depend on greenfield high-density GPU campus delivery. Rubin platform refresh in 2027 may require electrical/cooling re-spec.
6. **Financing:** Aker says Narvik cash flow supports capex and Ionic has a 10-year lease with ~$2B contracted revenue, but **Nscale has no public RPO/SEC-style backlog disclosure** and the total Microsoft deal value is not primary-disclosed. The `siliconangle.com` 200,000-GPU coverage is the principal trade-press support for the canonical atom; primary Nscale release confirms GPU count and country split but not aggregate contract value.
7. **Structural optionality:** **The 700 MW Texas second phase is an option, the 1.2 GW Texas footprint is a plan, and the prior 900 MW canonical atom was an analyst construct rather than a primary contract figure.** Rev-4.2 fix replaces 900 MW with 240 MW Ward County floor and removes Narvik/Loughton via Fairwater International dedupe.

## Temporal Logic

- **Earliest plausible energization:** Sines Q1 2026 (GPU delivery); Texas Microsoft services begin Q3 2026.
- **Central case:** Texas 240 MW + Loughton 50 MW + Narvik 230 MW operational by year-end 2027 with Rubin GPUs deploying 2027.
- **Latest plausible:** Microsoft's 700 MW Texas second-phase option exercise window opens late 2027; full 1.2 GW Texas footprint by 2029–2030 if exercised.
- **Critical-path dependency:** Ionic Cedarvale RFS/commissioning; Aker Kvandal grid connection and queue conversion (200+90 MW); UK Loughton power readiness; Sines MW disclosure / Start Campus delivery cadence.

## Reviewer Findings Addressed

- **Rev-4.2 fix (atom reduction):** Resolved. **Nscale-Microsoft atom reduced from 0.900 GW to 0.240 GW** (Ward County floor). The 0.900 GW figure was an analyst construct (closest reconstruction: Ward County ~240 MW + 700 MW Microsoft Texas option ≈ 0.94 GW), which is not the same as firm contracted capacity. Texas-only attribution applied.
- **Narvik / Loughton dedupe:** Resolved via `nscale_fairwater_overlap_adjustment` (−0.600 GW). Narvik and Loughton sit in `openai_microsoft_fairwater_international` overlay (0.805 GW); Nscale-Microsoft kept Texas-only.
- **Sines MW disclosure:** Confirmed not disclosed. Carried as gap; no MW assigned.
- **Aker contract evidence:** Verified $6.2B / 5-yr binding agreement for Narvik in Aker PRNewswire release and Aker ASA Q3 2025 presentation.
- **Texas 700 MW option:** Verified as option starting late 2027, not firm. 1.2 GW Texas footprint is plan, not commitment.

## Open Questions / Gaps

- Executed Microsoft-Nscale master services agreement or public filing showing total value, take-or-pay terms, termination rights, and per-site MW/GPU allocation.
- Whether Microsoft has exercised, or must exercise, the 700 MW Texas second-phase option.
- Sines MW/power allocation and whether Start Campus capacity is dedicated to Microsoft or shared.
- How many Narvik MW remain OpenAI/Stargate Norway versus Microsoft after the Aker-Nscale JV roll-up and April 2026 Microsoft expansion.
- Whether the 0.805 GW Fairwater International point should be revised given primary disclosure of 230 MW Narvik secured + 50–90 MW Loughton.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote (verbatim) |
|---|---|---|---|---|
| [Nscale 200,000 GB300 GPU release](https://www.nscale.com/press-releases/nscale-microsoft-2025) | 2025-10-15 | Primary release | 200k GPU multi-country contract; Texas 104k/~240 MW; Sines 12.6k; Loughton 23k/50–90 MW; Narvik 52k; Texas 700 MW option | "approximately 200,000 NVIDIA GB300 GPUs" |
| [Microsoft "world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary release | Narvik with Nscale/Aker; Loughton with Nscale; Fairwater context | "plans with nScale and Aker JV" |
| [Microsoft Source EMEA Narvik feature](https://news.microsoft.com/source/emea/features/the-port-town-in-norway-emerging-as-an-ai-hub/) | 2025-09-17 | Primary article | Narvik agreement $6.2B, five years, staged 2026 | "five-year agreement" |
| [Aker / PRNewswire Microsoft release](https://www.prnewswire.com/news-releases/aker-nscale-jv-signs-multi-billion-dollar-ai-infrastructure-agreement-with-microsoft-302559403.html) | 2025-09-17 | Primary regulated release | Binding five-year ~$6.2B; cash flow supports capex | "binding five-year customer agreement" |
| [Aker ASA Q3 2025 presentation](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/11/04/658641_Aker_ASA_3Q_2025_Presentation.pdf?VersionId=SRe3eE4FHa.5Qjn31MKeyHvs7kD5nUMN) | 2025-11-04 | Investor presentation | Narvik 230 MW secured; 200+90 MW queue; 52k Microsoft GPUs; ~120 MW Microsoft/OpenAI; 3-5 yr take-or-pay | "230MW secured capacity" |
| [Ionic Digital Cedarvale release](https://ionicdigital.com/uncategorized/ionic-digital-secures-transformational-lease-agreement-of-cedarvale-facility-with-nscale-2/) | 2025-10-14 | Primary release | Full 234 MW Cedarvale 10-yr triple-net ~$2B revenue | "full 234 MW capacity" |
| [Nscale UK announcement](https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement) | 2025-09-16 | Primary release | Loughton 50 MW scalable to 90 MW; 23,040 GB300 GPUs Q1 2027 | "50MW of AI capacity" |
| [Microsoft On the Issues UK $30B](https://blogs.microsoft.com/on-the-issues/2025/09/16/microsoft-30-billion-uk-ai-future/) | 2025-09-16 | Primary release | UK supercomputer with >23k GPUs partnership with Nscale | "partnership with Nscale" |
| [UK Government US-UK pact](https://www.gov.uk/government/news/us-uk-pact-will-boost-advances-in-drug-discovery-create-tens-of-thousands-of-jobs-and-transform-lives) | 2025-09-16 | Government announcement | Confirms UK Microsoft/Nscale supercomputer | "more than 23,000 advanced GPUs" |
| [Nscale Norway expansion](https://www.nscale.com/press-releases/nscale-microsoft-norway) | 2026-04-14 | Primary release | >30,000 Rubin GPUs added 2027 | "more than 30,000 NVIDIA Rubin GPUs" |
| [Nscale AI infrastructure page](https://www.nscale.com/ai-infrastructure) | 2026 site page | Primary site | Glomfjord 30 MW operational; Narvik 230+290 MW; Ward County ~240 MW to 1.2 GW; Loughton up to 90 MW | "roughly 240MW AI data center" |
| [Nscale Series C](https://www.nscale.com/press-releases/nscale-series-c) | 2026-03-09 | Primary release | $2B Series C; $14.6B valuation; Aker JV roll-up | "roll the Aker Nscale joint venture" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Microsoft Epoch sites for customer-anchor overlap | "Microsoft Fairwater Wisconsin" |

## Cross-Links

- Research dispatch: `docs/research/C3_nscale_microsoft.md`
- Canonical atoms: `canonical_capacity_atoms.yaml` rows for `nscale_microsoft_contract_capacity`, `nscale_fairwater_overlap_adjustment`, `nscale_operational_seed_capacity`, `openai_microsoft_fairwater_international`.
- Dedupe ledger: `dedupe_audit.csv` rows for the above atom IDs.
- Schema: `contracts/_schema.md`.
