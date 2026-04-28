# Anthropic / Microsoft Azure / NVIDIA — Up to 1 GW Compute Capacity

## TL;DR

Microsoft, NVIDIA, and Anthropic announced a tripartite strategic partnership on November 18, 2025 in which Anthropic committed to **"purchase $30 billion of Azure compute capacity"** and to contract **"additional capacity up to one gigawatt of compute capacity"** running on NVIDIA Grace Blackwell and Vera Rubin systems. Microsoft separately committed up to $5B and NVIDIA up to $10B equity into Anthropic. The Rev-4.3 canonical row carries 0.590 GW facility central (range 0–1.180 GW) — a partial 50% Fairwater overlap dedupe applied because Microsoft and NVIDIA both confirm Vera Rubin (Anthropic's chip class on Azure) deploys at Fairwater Wisconsin and Atlanta. AWS remains Anthropic's primary cloud and training partner; the Azure relationship is non-exclusive. T5 evidence tier — magnitude and counterparty disclosed, but no Azure region, site, utility, PPA, or contract tenor is public, and source language is "compute capacity" not facility MW.

## Counterparties

- **Operator**: Microsoft Azure (Microsoft Corporation, NASDAQ: MSFT). Operates the Fairwater AI superfactory program (Wisconsin, Atlanta, plus international Narvik/Loughton candidates).
- **Anchor tenant / user**: Anthropic, PBC. $30B Azure compute purchase commitment and up-to-1 GW additional capacity reservation.
- **Financing partner(s)**: Microsoft equity into Anthropic up to $5B; NVIDIA equity into Anthropic up to $10B; Microsoft balance-sheet capex underwrites Azure/Fairwater site delivery.

## Structure

- **Type**: Cloud capacity (compute purchase) with NVIDIA chip/architecture co-engineering overlay.
- **Term**: Not disclosed in the Microsoft Nov 18, 2025 release. Anthropic's parallel statement says AWS remains primary cloud/training partner; tenor of Azure spend commitment is undisclosed.
- **Announced contract value**: $30B Azure compute purchase commitment. Up to $15B combined Microsoft/NVIDIA equity into Anthropic (separate from cloud spend).
- **Equity cross-investments**: Microsoft up to $5B + NVIDIA up to $10B into Anthropic. Circular-funding optics: Anthropic equity dollars from chip/cloud vendors recycle into Azure/NVIDIA spend.
- **Take-or-pay coverage**: Not disclosed. Microsoft frames the $30B as a "purchase" commitment; no public termination, minimum-utilization, or RPO disclosure.
- **Optionality**: High. "Up to" 1 GW; "compute capacity" not facility MW; no named Azure region; future NVIDIA architecture optimization included as forward-looking.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.0 / 0.10 / 0.30 | T5 | Vera Rubin instances begin 2026 per NVIDIA Jan 5, 2026; first Anthropic capacity could go live mid-late 2026 |
| 2027 | 0.0 / 0.30 / 0.80 | T5 | Mid-window ramp into Fairwater Wisconsin/Atlanta or net-new sites |
| 2028 | 0.0 / 0.59 / 1.18 | T5 | Central case full 1 GW envelope with 50% Fairwater overlap |
| 2029 | 0.0 / 0.59 / 1.18 | T5 | Stable central; high case requires net-new Microsoft sites beyond Fairwater |
| 2030+ | 0.0 / 0.59 / 1.18 | T5 | Carries forward unless new disclosure |

The canonical residual is 0.590 GW central with low=0 (full Fairwater carve-out) and high=1.180 GW (no overlap, full net-new Microsoft sites).

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Microsoft Fairwater Wisconsin | Mount Pleasant, WI | Microsoft | Microsoft → OpenAI, Microsoft; 3.328 GW facility by 2027-10-03 | 0.295 GW (50% overlap central case) | T1/T2 |
| Microsoft Fairwater Atlanta | Fayetteville, GA | Microsoft / QTS-built | Microsoft → OpenAI; 0.859 GW facility by 2026-05-14 | 0.295 GW (50% overlap central case) | T1/T2 |
| Microsoft Goodyear | Goodyear, AZ | Microsoft | Microsoft → OpenAI; 0.263 GW operational | Candidate Azure capacity pool only | T1 |
| Crusoe Abilene Expansion | Abilene, TX | Crusoe / Microsoft | Microsoft → Microsoft; 0.941 GW by 2027-11-11 | Candidate only — Crusoe Mar 27, 2026 release ties to Microsoft AI infrastructure, not Anthropic | T2 |
| Net-new Microsoft Azure sites | undisclosed | Microsoft | Not in Epoch | High case 1.180 GW residual | T5 |

## Financing Stack

- **Capex envelope**: Not disclosed at the Anthropic-Azure level; absorbed in Microsoft's standalone Fairwater capex (Wisconsin $7B+ public commitment).
- **Equity / debt / RPO**: Microsoft up-to-$5B equity into Anthropic; NVIDIA up-to-$10B equity into Anthropic; Anthropic side $30B Azure compute purchase commitment.
- **Public disclosures**: Microsoft Official Blog 2025-11-18; Anthropic mirror 2025-11-18; NVIDIA Rubin Vera press release 2026-01-05; Microsoft Azure Blog Vera Rubin deployment plans 2026-01-05; Microsoft Fairwater Wisconsin announcement 2025-09-18; Atlanta unveil 2025-11-12.

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `anthropic_azure_incremental_capacity` — 0.590 GW facility central (range 0–1.180), T5, 50% Fairwater overlap dedupe applied; included in raw-horizon and probability-weighted totals (excluded from non-stretch and conservative T1/T2/T3 totals).
- Cross-references: `epoch_microsoft_fairwater_wisconsin_*`, `epoch_microsoft_fairwater_atlanta_*` (overlap candidates).

## Dedupe Notes

Rev-4.3 introduces a partial Fairwater overlap dedupe (Reviewer #3 fix). Microsoft Azure Blog (2026-01-05) states current Fairwater Wisconsin and Atlanta sites are designed for Vera Rubin NVL72 deployments. NVIDIA IR (2026-01-05) confirms Microsoft will deploy Vera Rubin instances in 2026. Anthropic-Azure 1 GW commitment is explicitly Vera Rubin/Grace Blackwell. Central case allocates 50% (0.590 GW facility) to Fairwater overlap split equally between Wisconsin (0.295 GW) and Atlanta (0.295 GW), with the remaining 50% (0.590 GW) treated as net-new Microsoft sites. Low case (0 GW) assumes full Fairwater carve-out — all Anthropic Azure capacity allocated inside Wisconsin's 3.328 GW or Atlanta's 0.859 GW envelope; high case (1.180 GW) assumes no overlap and full net-new physical capacity. Documented as judgmental — sources do not disclose an Anthropic-specific Azure site list. Dedupe direction: `partial_fairwater_overlap_50pct_central`.

## Risk Axes

1. **Counterparty risk** — Anthropic remains AWS-primary per April 20, 2026 release; Azure is non-exclusive. Microsoft commitment is a customer compute purchase, not site take-or-pay; no public termination rights or minimum payment. Anthropic also has Google/Broadcom 4.5 GW TPU exposure and AWS 5 GW exposure simultaneously, raising same-customer demand-allocation risk across overlays.
2. **Regulatory risk** — No Azure region disclosed; local permitting, utility tariff, state-level moratoria risk cannot be assessed without site disclosure. If allocated to Wisconsin Fairwater, WE Energies/PSC scrutiny applies; if Atlanta, Georgia Power and Fayette County land-use; if net-new, undisclosed.
3. **Power / interconnect risk** — 1 GW compute capacity implies multi-GW power delivery if net-new. If Fairwater-allocated, grid risk is already embedded in Microsoft Epoch sites (LPSC-equivalent Wisconsin PSC, Georgia PSC dockets). Vera Rubin NVL576 at ~600 kW per rack class is power-density-extreme.
4. **Supply chain risk** — Depends on NVIDIA Grace Blackwell and Vera Rubin systems; NVIDIA explicitly forward-looking-disclaims availability/timing. Liquid-cooling, AI WAN readiness, transformer/switchgear gating. HBM/CoWoS capacity underpins Vera Rubin ramp.
5. **Technology obsolescence risk** — Vera Rubin is next-generation rack-scale infrastructure (NVL576, ~600 kW/rack class); deployment depends on liquid-cooling, power-density, and AI WAN execution. If Vera Rubin yield/timing slips, fallback to Grace Blackwell may degrade contracted compute economics.
6. **Financing risk** — $30B is Anthropic compute-purchase commitment; Microsoft $5B + NVIDIA $10B equity create circular funding optics. SEC and policy reviewers (House AI Task Force, antitrust attention) increasingly focused on AI-vendor-equity-into-customer arrangements. Not site-level capex risk.
7. **Structural optionality** — "Up to" language and no named sites create high optionality; if Microsoft allocates Anthropic onto existing Fairwater capacity (no net-new), incremental Western GW = 0 (low-case canonical floor). High case requires Microsoft to deliver net-new sites by 2028.

## Temporal Logic

- **Earliest**: 2026-01-01 (NVIDIA Jan 5, 2026 release: Microsoft will **"deploy Vera Rubin-based instances in 2026"**).
- **Central**: 2027-06-30 — mid-window allocation across Fairwater Wisconsin/Atlanta and net-new sites; aligned with Vera Rubin NVL576 rollout cadence.
- **Latest**: 2028-12-31 — full 1 GW envelope plausible by year-end 2028 if Microsoft delivers net-new sites; Microsoft Local Phase 2 Wisconsin schedule is early 2028.
- **Critical-path dependency**: Vera Rubin/NVL576 rack delivery; Microsoft Fairwater Phase 2/3 build-out at Wisconsin and Atlanta; AI WAN throughput readiness; Anthropic enterprise demand absorption to support $30B spend cadence.

## Reviewer Findings Addressed

- **Rev-4.3 Reviewer #3 fix**: Replaced prior 0 GW Class B treatment with partial 50% Fairwater overlap dedupe. Central 0.590 GW facility with 0–1.180 GW range. Documented as `partial_fairwater_overlap_50pct_central`. Microsoft and NVIDIA confirm Vera Rubin deploys at Fairwater Wisconsin/Atlanta; the chip class is Anthropic's Azure stack.
- **Tier rationale**: T5 because counterparty named, GW magnitude stated, and broad delivery window inferable; not T4 because no named Azure region/site, utility, PPA, or contract tenor; not T6 because GW figure is source-disclosed not analyst-inferred.

## Open Questions / Gaps

- Named Azure region/site allocation for the 1 GW.
- Whether the $30B cloud purchase and the up-to-1 GW compute capacity are the same commitment, overlapping tranches, or separate reservations.
- Contract tenor, take-or-pay language, termination rights, ramp schedule.
- Power basis adjudication: source language is "compute capacity," not facility MW or IT MW.
- Whether any portion is served from Fairwater Wisconsin, Fairwater Atlanta, Goodyear, Crusoe Abilene Expansion, CoreWeave, Nebius, Nscale, or a future undisclosed Microsoft site.
- Whether Microsoft $5B and NVIDIA $10B equity into Anthropic are committed or milestone-conditional.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Microsoft Official Blog, "Microsoft, NVIDIA and Anthropic announce strategic partnerships"](https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/) | 2025-11-18 | Primary company announcement | $30B Azure compute purchase; up-to-1 GW; Microsoft $5B + NVIDIA $10B equity; Vera Rubin/Grace Blackwell basis | "purchase $30 billion of Azure compute capacity"; "additional compute capacity up to one gigawatt" |
| [Anthropic, "Microsoft, NVIDIA, and Anthropic announce strategic partnerships"](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships) | 2025-11-18 | Primary company announcement | AWS remains primary cloud/training partner | "Amazon remains Anthropic's primary cloud provider" |
| [NVIDIA IR, "NVIDIA Kicks Off the Next Generation of AI With Rubin"](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx) | 2026-01-05 | Primary company announcement | Rubin deployment timing; Microsoft/Fairwater link | "deploy Vera Rubin-based instances in 2026" |
| [Microsoft Azure Blog, "Strategic AI datacenter planning enables seamless, large-scale NVIDIA Rubin deployments"](https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/) | 2026-01-05 | Primary company announcement | Fairwater Wisconsin/Atlanta designed for Vera Rubin NVL72 | "current Fairwater sites in Wisconsin and Atlanta" |
| [Microsoft Official Blog, "Inside the world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Fairwater Wisconsin scope; multiple identical U.S. Fairwater sites | "multiple identical Fairwater datacenters under construction" |
| [Microsoft Source, "From Wisconsin to Atlanta"](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | 2025-11-12 | Primary company feature | Atlanta operational from October 2025; AI WAN | "began operation in October" |
| [Anthropic, "Anthropic and Amazon expand collaboration"](https://www.anthropic.com/news/anthropic-amazon-compute) | 2026-04-20 | Primary company announcement | AWS-primary status post-Azure deal | "Amazon remains Anthropic's primary cloud provider and training partner" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Fairwater Wisconsin 3.328 GW, Atlanta 0.859 GW, Goodyear 0.263 GW, Crusoe Abilene 0.941 GW | "Microsoft Fairwater Wisconsin" |

## Cross-Links

- Research dispatch: `docs/research/A2_anthropic_azure.md`
- Atoms: `canonical_capacity_atoms.yaml` (`anthropic_azure_incremental_capacity`)
- Dedupe entries: `dedupe_audit.csv` (rows for `anthropic_azure_incremental_capacity`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
- Related: `contracts/anthropic_nvidia.md`, `contracts/microsoft_fairwater.md`
