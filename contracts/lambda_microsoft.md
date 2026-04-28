# Lambda / Microsoft / NVIDIA — Multibillion-Dollar Multi-Year AI Cloud Capacity

## TL;DR

Lambda's November 3, 2025 primary release announces a multibillion-dollar, multi-year Microsoft AI infrastructure agreement powered by **"tens of thousands of NVIDIA GPUs"** including GB300 NVL72 systems. **The release does not disclose MW, named site allocation, RPO, take-or-pay mechanics, or contract value.** The local overlay carries `lambda_microsoft_contract` at **0.320 GW facility / 0.256 GW IT (PUE 1.25), T4** as a leased/signed/committed capacity convention rather than a primary-disclosed Microsoft building. Lambda's November 18, 2025 Series E announcement raises over $1.5B led by TWG Global with USIT, supporting "gigawatt-scale AI factories" but providing no Microsoft-specific MW allocation. Named Lambda site evidence is fragmented across Prime LAX01 Vernon (21 MW initial / 33 MW critical IT), Kansas City (24 MW initial scalable above 100 MW), EdgeConneX Chicago/Atlanta (30+ MW with 23 MW Chicago RFS 2026), Aligned DFW-04 Plano (no MW disclosed), ECL Mountain View (no MW disclosed), Cologix Columbus (no MW disclosed), and Allen TX (no MW disclosed). DCD reports Lambda operates 15 U.S. data centers and targets >1M GPUs and 3 GW liquid-cooled. **No reviewed source ties any Lambda site to Fairwater Wisconsin, Fairwater Atlanta, Goodyear, Crusoe Abilene Expansion, or CoreWeave Helios** — overlap with Epoch Microsoft sites is medium-confidence customer-demand overlap only.

## Counterparties

- **Operator:** Lambda (private; pre-IPO; AI cloud and GPU infrastructure provider).
- **Anchor tenant:** Microsoft (named in November 3, 2025 release); NVIDIA (named as platform supplier and previously as leaseback counterparty).
- **Financing partners:**
  - TWG Global (Series E lead, November 18, 2025).
  - USIT (Series E participant).
  - Existing Lambda investors.
  - NVIDIA (separate leaseback / GPU supply relationship; specific terms not publicly detailed).
  - Site-level lessors: Prime Data Centers (LAX01 Vernon); EdgeConneX (Chicago, Atlanta); Aligned Data Centers (DFW-04 Plano); ECL (Mountain View); Cologix (Columbus); local Kansas City partners; Allen TX partner.

## Structure

- **Type:** Cloud capacity (multi-year, multibillion-dollar AI infrastructure-as-a-service).
- **Term:** Multi-year per Lambda release; specific tenor not disclosed.
- **Announced contract value:** Multibillion-dollar (Lambda press release) — exact value not shared. DCD says "the exact value and GPU count of the Microsoft deal were not shared."
- **RPO/backlog:** None disclosed (Lambda is private and pre-IPO).
- **Take-or-pay coverage:** Not publicly disclosed.
- **Exclusivity:** Not disclosed.
- **Optionality:** Lambda Kansas City announcement says the site is dedicated to a single unnamed Lambda customer under a multi-year agreement; the customer is not publicly named as Microsoft. Site allocation between Microsoft and NVIDIA leaseback capacity is not publicly resolved.

## GW Shape Over Time

| Year | Facility GW low | Facility GW central | Facility GW high | Operational status | Notes |
|---|---:|---:|---:|---|---|
| 2025 | 0.05 | 0.05 | 0.10 | T1 | Lambda operational seed; LAX01 Vernon 21 MW Lambda lease; ECL Mountain View first GB300 NVL72 systems online September 2025 |
| 2026 | 0.10 | 0.20 | 0.32 | T4 | Kansas City 24 MW launch early 2026; EdgeConneX Chicago 23 MW RFS 2026 |
| 2027 | 0.20 | 0.30 | 0.45 | T4 | Continued site-level expansion; Aligned DFW-04 occupancy |
| 2028 | 0.25 | 0.35 | 0.60 | T4 | Local 320 MW overlay convention as committed midpoint |
| 2029 | 0.30 | 0.40 | 0.70 | T4 | DCD 3 GW liquid-cooled target trajectory |
| 2030 | 0.32 | 0.50 | 1.00 | T4 | Long-tail toward DCD-reported 3 GW ambition |

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|---|---|---|---|---:|---|
| Prime LAX01 | Vernon, CA | Prime Data Centers (landlord); Lambda (tenant) | Not in Epoch | 21 MW Lambda lease at 33 MW critical-IT facility | T1/T2 |
| Kansas City AI Factory | Kansas City, MO | Lambda (sole tenant) | Not in Epoch | 24 MW initial; scalable above 100 MW; early-2026 launch | T4 |
| EdgeConneX Chicago | Chicago, IL | EdgeConneX (landlord); Lambda (tenant) | Not in Epoch | 23 MW single-tenant; RFS 2026 | T4 |
| EdgeConneX Atlanta (ATL02) | Atlanta, GA | EdgeConneX (landlord); Lambda (tenant) | Not in Epoch | Part of "30+ MW combined" Chicago/Atlanta | T4 |
| Aligned DFW-04 | Plano, TX | Aligned (landlord); Lambda (tenant) | Not in Epoch | MW not disclosed in release | T4 |
| ECL Mountain View | Mountain View, CA | ECL (landlord); Lambda (tenant) | Not in Epoch | First GB300 NVL72 systems online September 2025; MW not disclosed | T1 |
| Cologix Columbus | Columbus, OH | Cologix (landlord); Lambda (tenant) | Not in Epoch | MW not disclosed | T4 |
| Allen TX | Allen, TX | Lambda / partner | Not in Epoch | MW not disclosed | T4 |

## Financing Stack

- **Capex envelope:** Not publicly disclosed at top level; DCD reports >1M GPU and 3 GW liquid-cooled target ambition.
- **Equity:** Lambda Series E over $1.5B led by TWG Global with USIT (November 18, 2025).
- **Project finance / debt:** No project-finance package or asset-level debt disclosed in primary sources. NVIDIA leaseback structure mentioned by trade press; specific terms not publicly detailed.
- **RPO / prepaid:** None disclosed.
- **Public disclosures:** Lambda Microsoft agreement announcement (2025-11-03); Lambda Series E announcement (2025-11-18); Lambda/Prime LAX01 announcement (2025-11-13); Prime LAX01 technical sheet (October 2025); Lambda Kansas City announcement (2025-10-28); EdgeConneX/Lambda Chicago announcement (2025-08-21); Aligned/Lambda DFW-04 announcement (2025-05-07); DCD Microsoft-Lambda coverage (2025-11-04); DCD Series E coverage (2025-11-18).

## Atoms Sourced

- `atom:lambda_microsoft_contract` (0.320 GW T4) — local overlay convention for Lambda leased/signed/committed capacity with Microsoft/NVIDIA anchors (PUE 1.25). **Not primary-disclosed** as Microsoft contract MW.
- `atom:lambda_operational` — Lambda operational seed capacity.

## Dedupe Notes

- **Epoch overlap:** None confirmed. Local Epoch Microsoft sites (Fairwater Wisconsin 3.328 GW; Fairwater Atlanta 0.859 GW; Goodyear 0.263 GW; Crusoe Abilene Expansion 0.941 GW; CoreWeave Helios 0.800 GW with Microsoft as #speculative user) are customer-anchor candidates only — **no reviewed Lambda source places Lambda at any of these Epoch buildings.**
- **Cross-overlay overlap:** **Medium overlap risk** because Microsoft is an anchor tenant in multiple overlay rows (CoreWeave, Nscale, Lambda). The 320 MW Lambda-Microsoft basis is a local overlay convention; if Microsoft has consolidated demand into Fairwater/Stargate, some Lambda overlay capacity could be customer-fungible with those Epoch rows. No primary-source allocation supports MW subtraction.
- **Atlanta name confusion:** Lambda/EdgeConneX ATL02 is not the Epoch Microsoft Fairwater Atlanta/Fayetteville QTS site based on current public evidence. Do not merge.
- **NVIDIA leaseback:** Lambda's NVIDIA leaseback footprint may overlap with Microsoft contract capacity at the GPU level; primary sources do not disambiguate.
- **Residual incremental GW:** 0.320 GW retained as ex-Epoch local overlay convention; could be zero if all 320 MW is embedded in Lambda's named-site footprint already-counted elsewhere.

## Risk Axes

1. **Counterparty:** Microsoft and NVIDIA anchor quality is high, but **Lambda is private and pre-IPO with limited public financial disclosure**, no RPO, and no SEC backlog visibility. The Microsoft contract value is undisclosed (DCD: "not been shared"), and **MW is not published** in either the November 3, 2025 Lambda release or the November 18, 2025 Series E release.
2. **Regulatory:** Named Lambda sites span California (Vernon, Mountain View), Texas (Plano, Allen), Illinois (Chicago), Georgia (Atlanta), Missouri (Kansas City), and Ohio (Columbus). Each carries separate utility, planning, environmental, and tax permitting paths; the Microsoft contract source does not identify the regulatory path or specific permits required.
3. **Power / interconnect:** Microsoft and Lambda both frame power/warm-shell availability as the bottleneck. Site delivery depends on local utility readiness: LAX01 Vernon at 33 MW already operational/leased; Kansas City 24 MW initial early 2026 with 100 MW scaling target; EdgeConneX Chicago 23 MW RFS 2026.
4. **Supply chain:** Contract depends on NVIDIA GB300 NVL72 systems and future high-density liquid-cooled deployments. ECL Mountain View first GB300 NVL72 came online September 2025; further GB300 ramp and Vera/Rubin successor platforms are the principal supply gates.
5. **Technology obsolescence:** Dense GB300/NVL72, photonics, liquid cooling, and future Rubin/Vera systems create integration and refresh-cycle risk over a multi-year contract.
6. **Financing:** **$1.5B Series E supports growth, but no project-finance package, debt terms, or Microsoft prepayment mechanics were found.** Series E concentration in TWG Global / USIT is a structural concentration to track. Lambda has no public RPO or SEC backlog.
7. **Structural optionality:** **No public MW, no site allocation, and no take-or-pay schedule.** The local 320 MW may be absorbed by multiple Lambda sites already counted in named-site lists (LAX01, KC, EdgeConneX, Aligned, ECL, Cologix, Allen) or overlap with NVIDIA leaseback capacity. **Medium overlap risk** with Fairwater/CoreWeave/Crusoe Microsoft demand.

## Temporal Logic

- **Earliest plausible energization:** Already partially energized — 21 MW LAX01 Vernon active; ECL Mountain View first GB300 NVL72 online September 2025.
- **Central case:** 0.20–0.30 GW facility by year-end 2026 across named sites (Kansas City, EdgeConneX Chicago/Atlanta, LAX01, DFW-04, Mountain View, Columbus, Allen).
- **Latest plausible:** 0.32 GW local overlay convention retained as midpoint; DCD 3 GW liquid-cooled target is a stretch ambition through 2030.
- **Critical-path dependency:** GB300 NVL72 supply at ECL/EdgeConneX; Kansas City 24 MW commissioning early 2026; EdgeConneX Chicago 23 MW RFS 2026; Aligned DFW-04 commissioning.

## Reviewer Findings Addressed

- **Local overlay basis disclosed plainly:** **0.320 GW T4 is local overlay convention, not primary-disclosed.** Lambda's November 3, 2025 release verbatim — "tens of thousands of NVIDIA GPUs", "multibillion-dollar", "multi-year" — provides no MW.
- **Series E concentration:** Documented TWG Global / USIT as Series E lead/participant.
- **Named sites enumerated** with MW where disclosed and "MW not disclosed" stated plainly where the operator release omits the figure (Aligned, ECL, Cologix, Allen).
- **No Fairwater/Crusoe overlap claim:** Documented absence of evidence linking Lambda to those Epoch rows; medium overlap risk acknowledged via customer-anchor commonality.
- **Atlanta name disambiguation:** Lambda/EdgeConneX ATL02 ≠ Epoch Microsoft Fairwater Atlanta (Fayetteville QTS).

## Open Questions / Gaps

- Contract or filing showing whether Microsoft is reserving exactly 320 MW, a GPU count, an IT-load amount, or a dollar-denominated cloud-service commitment.
- Site allocation for the Microsoft contract: Kansas City, LAX01, EdgeConneX Chicago/Atlanta, Aligned Plano, ECL Mountain View, Cologix Columbus, Allen TX, or another site.
- Whether the NVIDIA leaseback and Microsoft contract use the same GPUs/capacity or separate tranches.
- Whether any Lambda-operated capacity is physically inside an Epoch-counted Microsoft site; current public evidence says no.
- Delivery schedule, payment terms, cancellation rights, utilization guarantees, and Microsoft prepayment or balance-sheet treatment.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote (verbatim) |
|---|---|---|---|---|
| [Lambda Microsoft agreement](https://lambda.ai/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus) | 2025-11-03 | Primary release | Multibillion-dollar multi-year Microsoft/Lambda; GB300 NVL72; no MW/site/value | "tens of thousands of NVIDIA GPUs"; "multi-year contract" |
| [Lambda Series E](https://lambda.ai/blog/lambda-raises-over-1.5b-from-twg-global-usit-to-build-superintelligence-cloud-infrastructure) | 2025-11-18 | Primary release | $1.5B+ TWG/USIT; supports gigawatt-scale | "raised over $1.5B" |
| [Lambda / Prime LAX01](https://lambda.ai/blog/prime-data-centers-and-lambda-partner-to-power-the-next-era-of-superintelligence-with-ai-optimized-infrastructure-in-southern-california) | 2025-11-13 | Primary release | LAX01 Vernon 33 MW facility, 21 MW Lambda lease | "21 MW of power" |
| [Prime LAX01 technical sheet](https://primedatacenters.com/wp-content/uploads/2025/10/PDC_LosAngeles_TechSheet_LAX01_01.pdf) | 2025-10 | Primary datasheet | 33 MW critical IT load | "CRITICAL IT LOAD 33MW" |
| [Lambda Kansas City](https://lambda.ai/blog/lambda-to-build-a-100mw-ai-factory-in-kansas-city-mo) | 2025-10-28 | Primary release | KC 24 MW initial, >100 MW potential, early-2026 launch | "24MW of capacity" |
| [EdgeConneX / Lambda Chicago](https://www.edgeconnex.com/news/press-releases/edgeconnex-and-lambda-to-build-ai-factory-in-chicago-with-industry-leading-high-density-data-center-infrastructure/) | 2025-08-21 | Primary release | 30+ MW Chicago/Atlanta combined; Chicago 23 MW RFS 2026 | "30+ Megawatts" |
| [Aligned / Lambda DFW-04](https://www.globenewswire.com/de/news-release/2025/05/07/3076210/0/en/Aligned-and-Lambda-Partner-to-Power-Next-Generation-AI-Infrastructure.html) | 2025-05-07 | Primary release | Lambda occupies DFW-04 Plano; MW not disclosed | "occupy Aligned's newest" |
| [DCD Microsoft-Lambda](https://www.datacenterdynamics.com/en/news/microsoft-signs-multi-billion-dollar-cloud-capacity-deal-with-lambda/) | 2025-11-04 | Secondary trade press | Value/GPU count not disclosed; named Lambda footprint; 3 GW target | "not been shared" |
| [DCD Lambda Series E](https://www.datacenterdynamics.com/en/news/ai-cloud-company-lambda-raises-more-than-15bn-in-series-e-funding-round/) | 2025-11-18 | Secondary trade press | 15 DCs, >1M GPU, 3 GW liquid-cooled target | "3GW of liquid-cooled" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Microsoft Epoch sites for customer-anchor overlap | "Microsoft Fairwater Wisconsin" |

## Cross-Links

- Research dispatch: `docs/research/C4_lambda_microsoft.md`
- Canonical atoms: `canonical_capacity_atoms.yaml` rows for `lambda_microsoft_contract`, `lambda_operational`.
- Dedupe ledger: `dedupe_audit.csv` rows for the above atom IDs.
- Schema: `contracts/_schema.md`.
