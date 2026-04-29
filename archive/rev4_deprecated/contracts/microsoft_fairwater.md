# Microsoft Fairwater — Azure AI Superfactory (US + International)

## TL;DR

Microsoft Fairwater is Microsoft's Azure AI superfactory program, not a single customer contract. The U.S. footprint already counted in Epoch is **Wisconsin (Mount Pleasant) 3.328 GW facility by 2027-10-03**, **Atlanta 0.859 GW facility by 2026-05-14**, and **Goodyear 0.263 GW facility operational**. The international Fairwater leg (Narvik, Norway + Loughton, UK) was reduced in Rev-4.2 from the prior 0.805 GW midpoint to **0.300 GW facility central (range 0.280–0.610)**, anchored by Aker Q3 2025 disclosure of **"230MW secured grid capacity"** at Narvik plus Nscale's UK announcement of **"50MW of AI capacity, scalable to 90MW"** at Loughton. Fairwater workloads are mixed-attribution: Microsoft says they power **"OpenAI, Microsoft AI, Copilot, and other leading AI workloads"** — OpenAI remains a primary cloud partner under the April 27, 2026 amended agreement that makes Microsoft's OpenAI IP license non-exclusive. Microsoft and NVIDIA confirm Vera Rubin deploys at Fairwater Wisconsin and Atlanta, which is the Rev-4.3 basis for the 50% Anthropic-Azure overlap dedupe.

## Counterparties

- **Operator**: Microsoft Corporation (NASDAQ: MSFT). U.S. Fairwater sites Microsoft-owned and operated; Atlanta site reportedly QTS-built per local Epoch notes; Narvik operated by Nscale (Aker-Nscale JV rolled into Nscale per Mar 9, 2026 Series C release); Loughton operated by Nscale.
- **Anchor tenant / user**: OpenAI (primary), Microsoft AI / Copilot (internal), and other leading AI workloads. Anthropic also placed on Azure/Fairwater per Nov 18, 2025 strategic partnership (50% overlap dedupe applied to `anthropic_azure_incremental_capacity`).
- **Financing partner(s)**: Microsoft balance-sheet capex (Wisconsin $7B+ public commitment); Nscale (Series C $2B closed Mar 9, 2026 at $14.6B valuation); Aker (Norway shareholder of formerly named JV); UK Microsoft envelope of $30B announced Sep 16, 2025.

## Structure

- **Type**: Cloud capacity (Microsoft-operated Azure AI infrastructure serving multiple workloads).
- **Term**: U.S. sites Microsoft-owned indefinite; Narvik agreement is **"five-year"** ~$6.2B Microsoft contract per Microsoft Source EMEA (Sep 17, 2025) and Aker Q3 2025 presentation; Loughton tenor not separately disclosed.
- **Announced contract value**: Wisconsin $7B+ public commitment ($3.3B initial + $4B additional); Atlanta capex undisclosed; Narvik USD 6.2B five-year Microsoft contract; UK Microsoft envelope $30B with $15B capex.
- **Equity cross-investments**: None at Fairwater level (Anthropic/NVIDIA/Microsoft equity stack relates to `anthropic_azure_incremental_capacity` separately).
- **Take-or-pay coverage**: Aker Q3 2025 cites take-or-pay model language for Narvik; specific terms not public. U.S. site contracts not disclosed.
- **Optionality**: Multi-year Phase 1/2/3 build cadence at Wisconsin (Microsoft Local Mar 2026: Phase 1 nearing completion, Phase 2 early 2028); Atlanta operational from October 2025; Narvik staged from 2026 with Microsoft Rubin expansion in 2027; Loughton GPU delivery slipped from Q4 2026 to Q1 2027.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2025 | 0.43 (ATL) + 0.555 (WI) + 0.263 (GOD) ≈ 1.25 | T1 | Wisconsin 555 MW operational; Atlanta 433 MW operational from October 2025; Goodyear 263 MW |
| 2026 | 1.5 / 2.0 / 2.5 | T1/T2 | Atlanta full 0.859 GW by May 2026; Narvik 230 MW secured staged from August 2026 |
| 2027 | 2.5 / 3.5 / 4.5 | T2 | Wisconsin late-2027 fourth-building per Epoch; >30,000 Rubin GPUs at Narvik |
| 2028 | 3.5 / 4.5 / 5.5 | T2/T3 | Wisconsin Phase 2 early 2028 per Microsoft Local; full Wisconsin 3.328 GW |
| 2029+ | 4.5 / 5.0 / 5.5 | T3 | Stable Fairwater envelope; international expansion candidate |

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Microsoft Fairwater Wisconsin | Mount Pleasant, WI | Microsoft | Microsoft → OpenAI, Microsoft; 0.555 GW operational + 2.773 GW remaining = 3.328 GW by 2027-10-03 | Direct match | T1/T2 |
| Microsoft Fairwater Atlanta | Fayetteville, GA (QTS-built) | Microsoft | Microsoft → OpenAI; 0.433 GW operational + 0.426 GW remaining = 0.859 GW by 2026-05-14 | Direct match | T1/T2 |
| Microsoft Goodyear | Goodyear, AZ | Microsoft | Microsoft → OpenAI; 0.263 GW operational | Direct match | T1 |
| Fairwater International — Narvik | Kvandal/Narvik, Norway | Nscale (formerly Aker-Nscale JV) | n/a in Epoch | 230 MW secured + 200+90 MW queue; ~$6.2B five-year Microsoft contract | T2 |
| Fairwater International — Loughton | Loughton, UK | Nscale | n/a in Epoch | 50 MW scalable to 90 MW; 23,040 GB300 GPUs Q1 2027 | T2 |

## Financing Stack

- **Capex envelope**: Wisconsin $7B+ public commitment; Atlanta undisclosed; Goodyear undisclosed; Narvik USD 6.2B five-year Microsoft contract (Aker Q3 2025); UK Microsoft envelope $30B with $15B capex.
- **Equity / debt / RPO**: Microsoft balance-sheet absorption; Nscale $2B Series C (Mar 9, 2026); Aker shareholder financing; Aker presentation references GPU/data-center leverage targets.
- **Public disclosures**: Microsoft Wisconsin announcement Sep 18, 2025; Microsoft Source Atlanta feature Nov 12, 2025; Microsoft Local Mount Pleasant update Mar 1, 2026; Microsoft Norway feature Sep 17, 2025; Aker Q3 2025 presentation Nov 4, 2025; Aker-Nscale JV Microsoft agreement Sep 17, 2025; Nscale UK release Sep 16, 2025; Nscale Series C Mar 9, 2026; Nscale Microsoft Norway expanded Apr 14, 2026.

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `epoch_microsoft_fairwater_wisconsin_operational` — 0.555 GW facility (T1).
- `epoch_microsoft_fairwater_wisconsin_buildout_remaining` — 2.773 GW facility to 3.328 GW by 2027-10-03 (T2).
- `epoch_microsoft_fairwater_atlanta_operational` — 0.433 GW facility (T1).
- `epoch_microsoft_fairwater_atlanta_buildout_remaining` — 0.426 GW facility to 0.859 GW by 2026-05-14 (T2).
- `epoch_microsoft_goodyear_operational` — 0.263 GW facility (T1).
- `openai_microsoft_fairwater_international` — 0.300 GW facility central (range 0.280–0.610), T2, Rev-4.2 source replacement from prior 0.805 GW midpoint to named Narvik 230 MW + Loughton 50–90 MW anchors.

## Dedupe Notes

The international Fairwater atom (`openai_microsoft_fairwater_international`) was reduced in Rev-4.2 from the prior 0.805 GW facility midpoint to **0.300 GW facility central** (range 0.280–0.610) because current primary sources (Aker Q3 2025; Nscale UK Sep 16, 2025) support 230 MW Narvik plus 50–90 MW Loughton. Dedupe direction: `source_replace_named_narvik_loughton_mw`. Narvik and Loughton are also Nscale operating sites, creating overlap risk against `nscale_microsoft_contract_capacity`; that overlap is excluded via `nscale_fairwater_overlap_adjustment` (-0.600 GW facility, status `excluded`, `dedupe_direction: attribute_to_openai_microsoft_fairwater`). The Narvik attribution is itself layered: OpenAI announced Stargate Norway Jul 31, 2025 with OpenAI as initial offtaker option; Microsoft/Nscale/Aker subsequently announced the $6.2B five-year Microsoft contract (Sep 17, 2025); and Nscale's April 14, 2026 update confirms Narvik will add >30,000 Rubin GPUs for Microsoft in 2027. Anchor allocation may continue to evolve. The Anthropic-Azure 1 GW commitment (`anthropic_azure_incremental_capacity`) carries a 50% Fairwater overlap dedupe (Reviewer #3 fix Rev-4.3) because Microsoft and NVIDIA both confirm Vera Rubin (Anthropic's chip class) deploys at Fairwater Wisconsin and Atlanta.

## Risk Axes

1. **Counterparty risk** — Low Microsoft credit risk (investment-grade); attribution between OpenAI and Microsoft internal workloads remains mixed. The April 27, 2026 amended OpenAI/Microsoft agreement makes Microsoft's OpenAI IP license non-exclusive and allows OpenAI products to be served across any cloud, raising future workload-allocation flexibility. Nscale is private; Aker shareholder support and Nscale Series C close at $14.6B valuation underpin international leg.
2. **Regulatory risk** — Medium. Wisconsin local construction/community scrutiny and phase changes (Caledonia work separate but regional siting sensitive). Atlanta power/land constraints not documented in Microsoft primary source. Norway hydropower/grid approvals favorable; UK Loughton planning constraints active. Nordic data-residency and EU AI Act compliance applicable to international leg.
3. **Power / interconnect risk** — High at Wisconsin (multi-GW WE Energies/MISO load; Microsoft prepays energy/electrical infrastructure and matches fossil generation with carbon-free energy). Medium-high at Atlanta. Medium-low at Narvik for 230 MW secured; high for 200+90 MW queued expansion. Medium for 50 MW Loughton; high for >90 MW expansion or broader UK Stargate allocation.
4. **Supply chain risk** — High. Hundreds of thousands of NVIDIA GPUs (Grace Blackwell + Vera Rubin), liquid cooling, transformers, switchgear, fiber. GB300 and Rubin GPU rollout, direct-liquid cooling, grid equipment all in parallel.
5. **Technology obsolescence risk** — Medium. Fairwater is dense two-story Blackwell-era design; future Rubin-era changes may affect later buildings. April 2026 update shifts part of Narvik deployment to NVIDIA Rubin in 2027.
6. **Financing risk** — Low for Microsoft-funded U.S. sites; exact site-level capex beyond Wisconsin $7B not fully disclosed. Medium for Nscale international leg; Series C and Aker shareholder support are positive but private-company disclosure remains limited.
7. **Structural optionality** — Medium. Microsoft Local Mar 2026 Phase 2 early-2028 schedule differs from Epoch late-2027 estimate; OpenAI initial offtake option, Microsoft expansion, and Aker JV roll-up create allocation optionality for Narvik. Nscale Loughton Q4 2026 live target slipped to Q1 2027 GPU delivery.

## Temporal Logic

- **Earliest**: 2025-10 — Atlanta began operation in October 2025 per Microsoft Source feature.
- **Central**: 2027-01-01 — mid-Fairwater rollout combining Wisconsin Phase 1/Phase 2 transition, Atlanta full buildout (May 2026), and Narvik staged services from August 2026.
- **Latest**: 2028-12-31 — Wisconsin Phase 2 early 2028 per Microsoft Local; Loughton Q1 2027 GPU delivery; Narvik Rubin expansion 2027.
- **Critical-path dependency**: Wisconsin WE Energies/MISO transmission and substation commissioning; Atlanta utility delivery; Narvik 230 MW secured grid capacity execution by Aker/Nscale; NVIDIA Vera Rubin platform delivery; AI WAN throughput.

## Reviewer Findings Addressed

- **Rev-4.2 international source replacement**: Reduced `openai_microsoft_fairwater_international` from prior 0.805 GW midpoint to 0.300 GW facility central (range 0.280–0.610), anchored by named primary MW (Narvik 230 MW Aker Q3 2025; Loughton 50–90 MW Nscale Sep 2025). Dedupe direction: `source_replace_named_narvik_loughton_mw`.
- **Nscale overlap excluded**: `nscale_fairwater_overlap_adjustment` (-0.600 GW, status `excluded`) prevents double-count between Fairwater International and Nscale neocloud rows.
- **Vera Rubin Fairwater deployment confirmed**: Microsoft Azure Blog (2026-01-05) and NVIDIA IR (2026-01-05) confirm Vera Rubin at Fairwater; this is the basis for the Rev-4.3 50% Fairwater overlap on `anthropic_azure_incremental_capacity`.

## Open Questions / Gaps

- Wisconsin utility/MISO/WE Energies load-service documents that underpin Epoch's 3.3 GW estimate; Phase 1/2/3 mapping to Microsoft Local construction phases.
- Atlanta/QTS permits, substation filings, or utility load requests to validate the 0.859 GW Epoch estimate.
- Narvik allocation among OpenAI Stargate Norway, Microsoft 52,000 GB300 GPUs, and Microsoft >30,000 Rubin GPUs: additive, replacement, or phased within the same 230 MW.
- Whether Aker's USD 6.2B five-year Microsoft contract plus generic take-or-pay slide language is sufficient for T3 or should remain T2/T4.
- Nscale Texas/Sines capacity against `nscale_microsoft_contract_capacity` — not Fairwater sites per current primary naming, but operator overlap.
- Caledonia / future Wisconsin expansion beyond current Phase 2.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Microsoft Official Blog, "Inside the world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Wisconsin scope; multiple identical U.S. Fairwater sites; Narvik/Loughton named | "power OpenAI, Microsoft AI" |
| [Microsoft On the Issues, "Made in Wisconsin"](https://blogs.microsoft.com/on-the-issues/2025/09/18/made-in-wisconsin-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | $3.3B initial + $4B additional Wisconsin investment | "online in early 2026" |
| [Microsoft Local, "Mount Pleasant datacenter project update"](https://local.microsoft.com/blog/mount-pleasant-datacenter-project-update/) | 2026-03-01 | Primary local project update | Phase 1 nearing completion; Phase 2 early-2028 schedule | "Phase 1 is anticipated" |
| [Microsoft Source, "From Wisconsin to Atlanta"](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | 2025-11-12 | Primary company feature | Atlanta operational from October 2025; AI WAN | "began operation in October" |
| [Microsoft Source EMEA, "The port town in Norway emerging as an AI hub"](https://news.microsoft.com/source/emea/features/the-port-town-in-norway-emerging-as-an-ai-hub/) | 2025-09-17 | Primary company feature | Microsoft/Nscale/Aker Narvik $6.2B five-year agreement | "five-year agreement" |
| [Aker ASA Q3 2025 presentation](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/11/04/658641_Aker_ASA_3Q_2025_Presentation.pdf?VersionId=SRe3eE4FHa.5Qjn31MKeyHvs7kD5nUMN) | 2025-11-04 | Public-company investor presentation | Narvik/Kvandal 230 MW secured; 200+90 MW queue; Microsoft $6.2B; take-or-pay model language | "230MW secured capacity" |
| [Nscale, "UK AI infrastructure commitment"](https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement) | 2025-09-16 | Primary company announcement | Loughton 50 MW scalable to 90 MW; 23,040 GB300 GPUs Q1 2027 | "50MW of AI capacity" |
| [Nscale Series C announcement](https://www.nscale.com/press-releases/nscale-series-c) | 2026-03-09 | Primary company announcement | $2B Series C; $14.6B valuation; Aker JV roll-up | "roll the Aker Nscale joint venture" |
| [Nscale, "Expanded deal with Microsoft in Norway"](https://www.nscale.com/press-releases/nscale-microsoft-norway) | 2026-04-14 | Primary company announcement | Narvik adds >30,000 Rubin GPUs in 2027; solely Nscale-managed | "230 MW Nscale Narvik campus" |
| [OpenAI, "Introducing Stargate Norway"](https://openai.com/index/introducing-stargate-norway/) | 2025-07-31 | Primary company announcement | Narvik OpenAI initial offtaker; 230 MW + 290 MW ambition | "230MW of capacity" |
| [OpenAI, "Next phase of Microsoft OpenAI partnership"](https://openai.com/index/next-phase-of-microsoft-partnership/) | 2026-04-27 | Primary company announcement | Non-exclusive IP; primary cloud partner status | "primary cloud partner" |
| [Epoch AI, "Fairwater power usage"](https://epoch.ai/data-insights/fairwater-power-usage) | 2025-11-26 | Local/Epoch public context | 3.3 GW Wisconsin estimate; late-2027 fourth building | "3.3 GW of power" |
| [Microsoft Azure Blog, "NVIDIA Rubin deployments"](https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/) | 2026-01-05 | Primary company announcement | Fairwater Wisconsin/Atlanta designed for Vera Rubin | "current Fairwater sites in Wisconsin and Atlanta" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Wisconsin/Atlanta/Goodyear MW + dates | "Microsoft Fairwater Wisconsin" |

## Cross-Links

- Research dispatch: `docs/research/B4_microsoft_fairwater.md`
- Atoms: `canonical_capacity_atoms.yaml` (`epoch_microsoft_fairwater_wisconsin_*`, `epoch_microsoft_fairwater_atlanta_*`, `epoch_microsoft_goodyear_operational`, `openai_microsoft_fairwater_international`)
- Dedupe entries: `dedupe_audit.csv` (rows for `openai_microsoft_fairwater_international`, `nscale_fairwater_overlap_adjustment`, `anthropic_azure_incremental_capacity`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
- Related: `contracts/anthropic_azure.md` (50% Fairwater overlap dedupe), `contracts/nscale_microsoft.md` (Narvik/Loughton operator overlap), `contracts/openai_stargate_us.md` (separate Stargate surface)
