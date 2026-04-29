# CoreWeave Counterparty Stack

## TL;DR

CoreWeave's FY2025 Form 10-K (filed 2026-03-02) discloses **43 data centers with over 850 MW of active power** and **approximately 3.1 GW of total contracted power capacity** as of December 31, 2025. **The 850 MW active fleet is a subset of the 3.1 GW contracted total, not additive** — this is the headline reviewer #5 fix in Rev-4.3 and is the load-bearing arithmetic for ex-Epoch attribution. CoreWeave reports $60.7B of remaining performance obligations (RPO) and $66.8B of total revenue backlog with a five-year weighted-average remaining contract term. The customer stack is concentrated but diversifying: Microsoft was 67% of FY2025 revenue, OpenAI agreements total up to approximately $22.4B, Meta is committed via a September 2025 $14.2B order plus an April 2026 $21B expansion through December 2032, and IBM is a named GB200 NVL72 supercomputer customer with no MW disclosure. Local ex-Epoch counted capacity is 2.300 GW (= 3.100 GW contracted − 0.800 GW Galaxy Helios already attributed to the Epoch row), with `coreweave_operational_disclosed` retained for T1 tier-table visibility but excluded from incremental totals.

## Counterparties

- **Operator:** CoreWeave, Inc. (NYSE: CRWV; SEC CIK 1769628). Operates 43 data centers across the United States and Europe per the FY2025 10-K. Acts as both colocation lessee (Galaxy Helios; Applied Digital Polaris Forge 1) and hyperscaler/AI cloud capacity provider.
- **Anchor tenants:**
  - **Microsoft** — 67% of FY2025 revenue per CoreWeave 10-K; MSA filed as SEC exhibit 2025-03-03 specifying U.S. default geography, dedicated fiber, and customer hardware requirements.
  - **OpenAI** — total contract value up to approximately $22.4B (initial $11.9B March 2025 plus up-to-$6.5B September 2025 expansion); $350M OpenAI stock issuance to CoreWeave under the March 2025 agreement.
  - **Meta** — September 2025 order for up to approximately $14.2B through December 2031 under the December 2023 MSA; April 9, 2026 expansion of approximately $21B through December 2032 across multiple locations including initial Vera Rubin deployments.
  - **IBM** — GB200 Grace Blackwell supercomputer for IBM Granite model training, January 15, 2025 announcement; **MW not disclosed in any public source.**
- **Financing partners:**
  - Galaxy Digital — $1.4B Helios project financing close (August 15, 2025).
  - Applied Digital — $2B 10-year triple-net lease structure for Polaris Forge 1.
  - Public debt and asset-level project finance backed by customer take-or-pay contracts; specific lenders redacted in primary filings.

## Structure

- **Type:** Cloud capacity (hyperscaler/AI customer take-or-pay style) over leased and developed colocation footprint.
- **Term:** Five-year weighted-average remaining contract duration per FY2025 10-K. OpenAI contract structured to 2031-05-31 latest; Meta expansion through December 2032; Galaxy Helios financing on a 15-year revenue basis.
- **Announced contract value (named):** $57.6B disclosed customer-order stack (OpenAI ~$22.4B + Meta $14.2B initial + Meta $21B expansion). This is named-customer aggregate, not additive capacity.
- **Aggregate filed obligations:** $60.7B RPO; $66.8B total revenue backlog (FY2025 results, 2026-02-27).
- **Take-or-pay coverage:** CoreWeave 10-K describes customer contracts generally as multi-year committed, take-or-pay capacity purchases. Order forms are heavily redacted; Microsoft, OpenAI, Meta, and IBM do not disclose MW allocations by site.
- **Exclusivity:** None disclosed. Microsoft MSA is non-exclusive. OpenAI and Meta agreements are stated as "complementary" to other compute relationships (Microsoft, Oracle/Stargate).
- **Optionality:** Order-form structure permits expansion (illustrated by OpenAI September 2025 $6.5B add-on and Meta April 2026 $21B expansion). Termination/walk-away provisions are redacted in SEC exhibits.

## GW Shape Over Time

| Year | Facility GW low | Facility GW central | Facility GW high | Operational status | Notes |
|---|---:|---:|---:|---|---|
| 2025 | 0.850 | 0.850 | 0.850 | T1 | 10-K discloses "over 850 MW of active power" at 43 data centers as of 2025-12-31 |
| 2026 | 1.30 | 1.50 | 1.80 | T2/T3 | PF1 building 1 RFS Q4 2025; PF1 building 2 mid-2026; Helios Phase I 200 MW gross 1H 2026 |
| 2027 | 2.10 | 2.40 | 2.70 | T2/T3 | Helios Phase II 400 MW gross commencing 2027; PF1 building 3 RFS 2027 |
| 2028 | 2.80 | 3.00 | 3.10 | T3 | Helios Phase III 200 MW gross commencing 2028 |
| 2029 | 3.10 | 3.10 | 3.10 | T3 | Full contracted envelope per 10-K ($60.7B RPO supports five-year delivery) |
| 2030 | 3.10 | 3.10 | 3.30 | T3/T4 | Galaxy 830 MW additional ERCOT approval is optional; Meta/OpenAI Vera Rubin expansions |

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|---|---|---|---|---:|---|
| Galaxy Helios | Dickens County, West Texas | Galaxy Digital (landlord); CoreWeave (AI/HPC operator) | Epoch row "Coreweave Helios" 0 MW current / 0.800 GW buildout by 2029-01-01 | 0.800 GW (excluded from coreweave_contracted_ex_epoch) | T3 |
| Applied Digital Polaris Forge 1 | Ellendale, North Dakota | Applied Digital (landlord); CoreWeave (tenant) | Not in local Epoch snapshot | 0.400 GW critical IT (3 buildings under 10-yr lease) | T3 |
| Other 41 disclosed data centers | U.S. + Europe (sites not fully disclosed) | CoreWeave / various lessors | Not individually mapped in Epoch | Embedded in 850 MW active fleet | T1 |
| Lancaster / Kenilworth / European sites | Various | CoreWeave | Not in local Epoch snapshot | Subsumed under fleet 850 MW | T1 |

## Financing Stack

- **Capex envelope:** Not disclosed as single figure. CoreWeave operates an asset-light/leased model; site-level capex is borne by lessors (Galaxy at Helios, Applied Digital at PF1) or financed via project debt.
- **Equity:** Public-company common equity; OpenAI received $350M of CoreWeave stock under the March 2025 agreement.
- **Project finance / debt:** $1.4B Galaxy Helios project financing closed August 15, 2025 (15-year revenue basis); CoreWeave 10-K discloses asset-level debt supported by customer take-or-pay contracts but redacts specific facilities.
- **RPO / prepaid:** $60.7B remaining performance obligations; $66.8B total revenue backlog as of December 31, 2025; five-year weighted-average remaining contract duration.
- **Public disclosures:** CoreWeave FY2025 Form 10-K (2026-03-02); Q4/FY2025 results press release (2026-02-27); SEC-filed Microsoft MSA exhibit (2025-03-03); SEC-filed Meta MSA exhibit (2025-09-30); company press releases for OpenAI March 2025 and September 2025 agreements, Meta April 2026 expansion, and IBM January 2025 supercomputer.

## Atoms Sourced

- `atom:coreweave_operational_disclosed` (0.850 GW T1) — 850 MW active power across 43 data centers per FY2025 10-K. **Excluded from all totals as subset of `coreweave_contracted_ex_epoch` (Rev-4.3 reviewer #5 fix).**
- `atom:coreweave_contracted_ex_epoch` (2.300 GW T3) — 3.100 GW total contracted per 10-K minus 0.800 GW Helios already attributed in Epoch.
- `atom:coreweave_epoch_overlap_helios` (−0.800 GW) — Galaxy Helios subtraction; Helios sits in the Epoch row (`epoch_coreweave_helios_buildout_remaining`).
- `atom:coreweave_applied_digital_pf1_overlap_adjustment` (−0.400 GW critical IT, dedupe_direction: attribute_to_coreweave_end_user) — PF1 leaseback; Applied Digital ground-lease counted under Applied Digital primary row, dedupe sends MW to CoreWeave end-user.
- `atom:epoch_coreweave_helios_buildout_remaining` (0.800 GW; Epoch row, attributed_to: CoreWeave/Microsoft #speculative).

## Dedupe Notes

- **Epoch overlap:** Galaxy Helios 0.800 GW is the only direct CoreWeave/Epoch site overlap. The local Epoch row carries Helios as 800 MW facility buildout by 2029-01-01; Galaxy primary disclosure says CoreWeave has committed to the full 800 MW approved power capacity. Subtracted via `coreweave_epoch_overlap_helios` to avoid double-counting.
- **Cross-overlay overlap:** Applied Digital PF1 is not in Epoch but is a leaseback against the Applied Digital primary row in this overlay. Resolved via `coreweave_applied_digital_pf1_overlap_adjustment` (−0.400 MW critical IT) attributing the lease to CoreWeave end-use.
- **Customer-level overlap (not site-level):** Microsoft/OpenAI/Meta also appear at Fairwater Wisconsin (3.328 GW Epoch), Fairwater Atlanta (0.859 GW Epoch), Stargate Abilene (1.18 GW Epoch), Hyperion/Prometheus/Temple. No primary source allocates CoreWeave physical capacity to these Epoch-attributed campuses; carried as customer-demand candidates only, no MW subtraction applied.
- **Residual incremental GW:** 2.300 GW = 3.100 GW contracted − 0.800 GW Helios. The 850 MW active fleet is excluded from totals as a subset of the 3.1 GW contracted envelope.

## Risk Axes

1. **Counterparty:** Microsoft 67% FY2025 revenue concentration is the binding credit-and-renewal risk per the 10-K's explicit risk-factor language ("loss or reduction in spend by a top customer would materially affect us"). OpenAI ~$22.4B contract is private-counterparty risk; CoreWeave 10-K specifically flags OpenAI credit exposure. Meta's $14.2B + $21B is investment-grade but technology-strategy-sensitive.
2. **Regulatory:** Multi-state data-center, export-control, privacy/security, and local power/tax scrutiny. Helios depends on ERCOT/Texas interconnection milestones; Galaxy discloses 830 MW additional ERCOT approval and 2.7 GW under load study, both contingent on grid/load-study progress. PF1 (Ellendale, ND) requires North Dakota site approvals and local power arrangements per Applied Digital filings.
3. **Power / interconnect:** $1.4B Galaxy Helios financing covers initial retrofit/expansion; Phase I/II/III delivery runs 2026–2028 and depends on substation, transmission, commissioning, and retrofit execution. PF1 three-building delivery schedule spans Q4 2025, mid-2026, and 2027. Active fleet growth from 360 MW (FY2024) to 850+ MW in one year depends on leased-DC provider delivery cadence.
4. **Supply chain:** CoreWeave 10-K cites dependency on latest GPUs, networking, storage, liquid cooling, chillers, and HVAC systems. GB200 Blackwell supply (IBM Granite supercomputer) and Vera Rubin deployment for the April 2026 Meta expansion create platform-readiness risk in 2026–2027.
5. **Technology obsolescence:** Five-year weighted-average contract life vs faster accelerator generation cycles (H100 to GB200 to B300 to Vera Rubin) can strand or reprice older clusters before contract amortization.
6. **Financing:** $1.4B Galaxy Helios project finance and CoreWeave's asset-level debt are supported by customer take-or-pay contracts; delayed site delivery can push revenue recognition. Galaxy flags financing-covenant and construction risks in Q4 2025 results. Applied Digital flags construction, financing, and principal-customer risks.
7. **Structural optionality:** Take-or-pay reduces demand risk, but order forms are redacted and customer/site fungibility is high. Galaxy's 2.7 GW additional load-study pipeline is optional and unleased in primary sources. Meta April 2026 expansion adds contract value but no new MW disclosure.

## Temporal Logic

- **Earliest plausible energization:** Already energized — 850 MW active as of 2025-12-31.
- **Central case:** 2.40 GW facility by year-end 2027 as Helios Phase II and PF1 buildings 2–3 deliver.
- **Latest plausible:** 3.10 GW contracted envelope substantially delivered by 2029–2030, matching Helios Phase III 2028 commencement and Meta-expansion December 2032 contract end.
- **Critical-path dependency:** Galaxy Helios ERCOT interconnect Phase II commissioning (260 MW critical IT, 2027); PF1 building 3 RFS 2027; GB200/Vera Rubin platform supply for IBM and Meta order forms.

## Reviewer Findings Addressed

- **Reviewer #5 (Rev-4.3 headline fix):** "850 MW active is additive to 3.1 GW contracted." Resolved. The 10-K verbatim quote — "We had 43 data centers with over 850 MW of active power… our total contracted power capacity was approximately 3.1 GW" — establishes the 850 MW active is a subset of the 3.1 GW contracted total. `coreweave_operational_disclosed` is retained for T1 tier-table visibility and explicitly excluded from all incremental totals. Net incremental ex-Epoch is `coreweave_contracted_ex_epoch` = 2.300 GW = 3.100 − 0.800 (Helios already in Epoch).
- **Galaxy Helios attribution:** Galaxy primary disclosure of "full 800 MW of approved power capacity" for CoreWeave matches Epoch's Helios row (0.800 GW buildout by 2029-01-01); subtracted via `coreweave_epoch_overlap_helios`.
- **PF1 leaseback double-count risk:** Resolved via `coreweave_applied_digital_pf1_overlap_adjustment` (−0.400 GW critical IT, attribute_to_coreweave_end_user); PF1 not in Epoch.
- **Meta April 2026 expansion ($21B) MW:** Verified no new MW disclosure; $21B figure does not increase the 3.1 GW contracted-power atom.
- **IBM MW disclosure:** Confirmed not disclosed; IBM January 2025 release describes platform ("one of the first NVIDIA GB200 Grace Blackwell Superchip-enabled AI supercomputers") and workload (IBM Granite model training) without facility/site/MW.

## Open Questions / Gaps

- Named site allocation by customer for Microsoft, OpenAI, Meta, and IBM (order-form schedules redacted in SEC exhibits).
- Whether any Helios capacity is specifically assigned to Microsoft, OpenAI, Meta, IBM, or another customer (Epoch's Microsoft user attribution at Helios is marked #speculative).
- CoreWeave Q1 2026 filing/results to update 850 MW active and 3.1 GW contracted power as of 2026-03-31.
- Primary SEC 8-K text for the April 2026 Meta order form, including exact relationship to the September 2025 $14.2B order.
- Polaris Forge 1 current RFS/energized status by building as of 2026-04-28 (Applied Digital 10-Q cadence).
- Full CoreWeave site list and crosswalk to Epoch rows beyond Helios and PF1 (Lancaster, Kenilworth, European sites).
- Power-basis reconciliation among CoreWeave "active/contracted power" (10-K), Galaxy gross power vs critical IT load (Q4 2025 results), Applied Digital critical IT capacity (press releases), and Epoch facility MW.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote (verbatim) |
|---|---|---|---|---|
| [CoreWeave FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) | 2026-03-02 | SEC filing | 43 DCs, 850+ MW active, 3.1 GW contracted, $60.7B RPO, 5-yr WAL | "43 data centers with over 850 MW of active power"; "total contracted power capacity was approximately 3.1 GW" |
| [CoreWeave Q4/FY2025 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results/) | 2026-02-27 | Primary release | Revenue backlog | "$66.8 billion" |
| [CoreWeave-Microsoft MSA exhibit](https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798dex1023.htm) | 2025-03-03 | SEC exhibit | U.S. default geography | "provided within the United States" |
| [CoreWeave OpenAI March 2025 agreement](https://coreweave.com/news/coreweave-announces-agreement-with-openai-to-deliver-ai-infrastructure) | 2025-03-10 | Primary release | Initial $11.9B + $350M stock | "up to $11.9 billion" |
| [CoreWeave OpenAI September 2025 expansion](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx) | 2025-09-25 | Primary release | OpenAI total ~$22.4B | "total contract value with OpenAI up to approximately $22.4 billion" |
| [CoreWeave Meta April 2026 expansion](https://investors.coreweave.com/news/news-details/2026/CoreWeave-and-Meta-Announce-21-Billion-Expanded-AI-Infrastructure-Agreement/default.aspx) | 2026-04-09 | Primary release | $21B Meta expansion through 2032 | "AI cloud capacity through December 2032"; "approximately $21 billion" |
| [CoreWeave-Meta MSA exhibit](https://www.sec.gov/Archives/edgar/data/1769628/000176962825000050/redactedmetamsa929finald.htm) | 2025-09-30 | SEC exhibit | Existing Meta MSA effective Dec 2023 | "Meta Platforms, Inc." |
| [IBM/CoreWeave Granite supercomputer](https://newsroom.ibm.com/2025-01-15-coreweave-partners-with-ibm-to-deliver-new-ai-supercomputer-for-ibm-granite-models) | 2025-01-15 | Primary release | GB200 NVL72; Granite training; MW not disclosed | "one of the first NVIDIA GB200 Grace Blackwell Superchip-enabled AI supercomputers" |
| [Galaxy Helios project financing](https://www.galaxy.com/newsroom/galaxy-closes-helios-project-financing) | 2025-08-15 | Primary release | $1.4B financing; full 800 MW commitment | "full 800 MW of approved power capacity" |
| [Galaxy Q4/FY2025 results](https://investor.galaxy.com/news-releases/news-release-details/galaxy-announces-fourth-quarter-and-full-year-2025-financial) | 2026-02-03 | Primary release | 526 MW critical IT; 800 MW gross; phasing | "526MW" |
| [Applied Digital PF1 lease](https://ir.applieddigital.com/news-events/press-releases/detail/128/applied-digital-finalizes-additional-150mw-lease-with) | 2025-08-29 | Primary release | 400 MW critical IT in 3 leases | "400MW in Total Critical IT Capacity" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Helios 0.800 GW buildout 2029-01-01 | "Coreweave Helios" |

## Cross-Links

- Research dispatch: `docs/research/C1_coreweave_counterparty_stack.md`
- Canonical atoms: `canonical_capacity_atoms.yaml` rows for `coreweave_operational_disclosed`, `coreweave_contracted_ex_epoch`, `coreweave_epoch_overlap_helios`, `coreweave_applied_digital_pf1_overlap_adjustment`, `epoch_coreweave_helios_buildout_remaining`.
- Dedupe ledger: `dedupe_audit.csv` rows for the above atom IDs.
- Schema: `contracts/_schema.md`.
