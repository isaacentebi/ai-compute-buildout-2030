# Anthropic / AWS — Project Rainier Expansion (up to 5 GW)

## TL;DR

Anthropic and Amazon Web Services announced on April 20, 2026 an expansion of Project Rainier under which Anthropic secures **"up to 5GW of new capacity"** for Claude training and inference, anchored by Amazon's Trainium2/Trainium3/Trainium4 (and future-Trainium) generations, supported by Anthropic's existing **"more than $100 billion over the next ten years"** AWS technology commitment plus Amazon's incremental $5B equity investment with up-to-$20B milestone-linked future investment. The Rev-4.3 canonical row carries 1.973 GW facility (range 0–3.800 GW) — a Rev-4.2 partial dedupe that subtracts 0.819 GW Madison Mega Site and 1.008 GW Ridgeland from the prior 3.800 GW residual; New Carlisle's 1.229 GW (1.092 GW operational + 0.137 GW remaining) is treated as pre-existing Rainier capacity per Anthropic's "new capacity" framing rather than as overlap with the April 20 headline. The 2026 near-term tranche of **"nearly 1GW in total before the end of the year"** is nested inside the 5 GW envelope and not additive. AWS remains Anthropic's primary cloud and training partner under the Apr 20 release.

## Counterparties

- **Operator**: Amazon Web Services (Amazon.com, Inc., NASDAQ: AMZN). Public cloud operator; owner-operator of the Rainier site footprint including New Carlisle, Indiana and Mississippi candidate sites.
- **Anchor tenant / user**: Anthropic, PBC. Up to 5 GW of compute capacity for Claude training and inference; AWS framed as primary training/cloud provider.
- **Financing partner(s)**: Amazon balance sheet (site capex); Anthropic cloud-spend commitment ("more than $100 billion over the next ten years") underwrites AWS revenue. Amazon's prior $8B equity, plus $5B immediate and up-to-$20B milestone-linked future Anthropic investments, are separate from cloud spend.

## Structure

- **Type**: Cloud capacity (multi-year compute purchase) with chip procurement overlay (Trainium2/3/4 generations).
- **Term**: Ten years (Anthropic's $100B+ AWS-technology commitment is denominated over ten years).
- **Announced contract value**: $100B+ Anthropic AWS spend; $5B + up-to-$20B Amazon equity. No site-level capex disclosed.
- **Equity cross-investments**: Amazon $5B immediate + up to $20B milestone-linked + prior $8B = up to $33B Anthropic equity exposure. Amazon explicitly states equity is separate from spend.
- **Take-or-pay coverage**: Not disclosed. Source language is "up to 5 GW of new capacity" and "$100 billion AWS technology commitment" — capacity ceiling and dollar ceiling, not enforceable take-or-pay.
- **Optionality**: High. "Up to" phrasing on both GW and chip generations; future-Trainium generations explicitly forward-looking. No public site list and no full-5-GW COD date.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 1.0 / 1.0 / 1.2 | T2/T3 | "nearly 1GW in total before the end of the year"; Trainium2 ramp Q2; scaled Trainium3 later in 2026 |
| 2027 | 1.5 / 2.0 / 2.5 | T3/T4 | Mid-window ramp; sites unallocated by primary sources |
| 2028 | 2.0 / 3.0 / 4.0 | T4 | Trainium3/4 fleet scale-up |
| 2029 | 0.0 / 1.973 / 3.800 | T4 | Rev-4.2 canonical residual range; no full 5 GW COD date in any source |
| 2030+ | 0.0 / 1.973 / 3.800 | T4 | Carries 5 GW envelope absent further site disclosure |

The canonical residual is 1.973 GW central (Rev-4.2 partial dedupe), with low=0 (full Madison/Ridgeland/New Carlisle subsumption hypothesis) and high=3.800 GW (no overlap beyond explicit New Carlisle).

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Anthropic-Amazon New Carlisle | St. Joseph County, IN | AWS | Amazon → Anthropic, Project Rainier #confident; 1.092 GW operational + 0.137 GW remaining | Pre-existing Rainier; not subtracted from 5 GW residual per Anthropic "new capacity" framing | T1/T2 |
| Amazon Madison Mega Site | Canton, Madison County, MS | AWS | Amazon → Anthropic #speculative, Project Rainier #speculative; 0.819 GW facility by 2026-09-18 | −0.819 GW deduped to Rev-4.2 residual | T2/T4 |
| Amazon Ridgeland (JAN200) | Ridgeland, Hinds County, MS | AWS | Amazon → Anthropic #speculative, Project Rainier #speculative; 1.008 GW facility by 2027-09-21 | −1.008 GW deduped to Rev-4.2 residual | T3/T4 |
| Unallocated 2026 tranche | undisclosed | AWS | Not in Epoch | Nested in 5 GW headline; ~1 GW by 2026-12-31 | T3 |
| Unallocated 2027–2030 capacity | undisclosed | AWS | Not in Epoch | Carried as 1.973 GW residual | T4 |

## Financing Stack

- **Capex envelope**: Not disclosed at the Anthropic-AWS site level; absorbed in Amazon's standalone capex guidance.
- **Equity / debt / RPO**: Amazon equity into Anthropic ($5B + $20B optional + $8B prior); Anthropic side $100B+ ten-year cloud spend commitment is the load-bearing economic obligation. No site-level project finance disclosed.
- **Public disclosures**: Anthropic and Amazon parallel announcements 2026-04-20; Amazon $25B Mississippi statewide investment release 2026-04-09; AWS Project Rainier launch 2025-06-24; MDEQ permits for Madison Mega Site (1720-00098) and Ridgeland JAN200 (1720-00099).

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `anthropic_aws_incremental_new_capacity` — 1.973 GW facility (range 0–3.800), T4, Rev-4.2 residual after Madison/Ridgeland subtraction, included in raw horizon and probability-weighted totals.
- `epoch_anthropic_amazon_new_carlisle_operational` — 1.092 GW facility, T1.
- `epoch_anthropic_amazon_new_carlisle_buildout_remaining` — 0.137 GW facility, T2 (full buildout 2026-06-21).

## Dedupe Notes

Rev-4.2 reduced the prior 3.800 GW residual to 1.973 GW by subtracting Madison (0.819 GW) and Ridgeland (1.008 GW), both of which Epoch carries with Anthropic/Project Rainier #speculative attribution. New Carlisle (1.229 GW) is treated as **pre-existing Rainier capacity** rather than as an overlap dedupe, consistent with Anthropic's April 20 framing of the 5 GW as **"up to 5GW of new capacity"** distinct from the existing Rainier deployment that already runs **"more than one million Trainium2 chips"**. Primary AWS sources confirm New Carlisle as the launch Rainier site (June 24, 2025 release: "one of the world's largest AI compute clusters"); Mississippi sources confirm Madison and Ridgeland as Amazon AWS campuses but stop short of naming Anthropic. Dedupe direction: `partial_dedupe_epoch_madison_ridgeland`. Double-count risk flagged HIGH because Madison/Ridgeland's Anthropic attribution remains speculative — primary AWS Mississippi releases describe campus expansion without Anthropic tenant identification.

## Risk Axes

1. **Counterparty risk** — Anthropic concentration risk for AWS revenue (>$10B/year run-rate implied by $100B/10yr); Amazon equity-into-Anthropic stack creates circular-funding optics that SEC and policy reviewers (House AI Task Force, FTC) have flagged in the broader "AI compute investment loop" context. Anthropic also expanding Google/Broadcom TPU and Azure/NVIDIA capacity simultaneously — AWS is primary but not exclusive.
2. **Regulatory risk** — Mississippi Madison County MDEQ Permit 1720-00098 and Ridgeland MDEQ Permit 1720-00099 are active; recycled-water and air-permit conditions are relevant. Indiana New Carlisle local water/grid agreements with I&M/NIPSCO. No public April 20 site list, so each candidate site has separate exposure to local opposition, water permitting, and tax-incentive scrutiny.
3. **Power / interconnect risk** — 5 GW of compute requires multi-GW utility commitments; Amazon Mississippi releases reference Entergy grid upgrades but disclose no full 5 GW interconnect schedule. Mississippi Today reports flag local grid and recycled-water opposition. Indiana I&M service terms not fully public.
4. **Supply chain risk** — Trainium2 ramp Q2 2026 confirmed; Trainium3 scaling later 2026 forward-looking-disclaimed; Trainium4 explicitly future-generation silicon with no fab/timing detail. HBM and advanced packaging (TSMC CoWoS) capacity gates the multi-GW deployment. Amazon's parallel release stops short of binding delivery dates.
5. **Technology obsolescence risk** — Trainium3/4 fleet-scale training and inference performance remains less externally benchmarked than NVIDIA Blackwell/Rubin; if benchmark or efficiency gaps emerge, Anthropic can shift workloads to Google TPU or Azure NVIDIA paths. Five-GW envelope spans multiple chip generations.
6. **Financing risk** — $100B is Anthropic cloud-spend commitment, not Amazon facility capex; if Anthropic revenue trajectory slows, take-or-pay enforceability is undisclosed. Amazon $5B/+$20B equity creates circular-funding exposure: equity dollars effectively recycle into Trainium revenue.
7. **Structural optionality** — "Up to" 5 GW, optional future Trainium silicon, no named sites, and no full 5 GW delivery date together create high optionality. Anthropic's September 2025 Google Cloud announcement and April 2026 Google/Broadcom 3.5 GW deal demonstrate Anthropic's willingness to diversify; AWS exclusivity is explicitly disclaimed.

## Temporal Logic

- **Earliest**: 2026-04-20 (announcement). Trainium2 capacity comes online "in three months" per Anthropic Apr 20 release: "**meaningful compute coming online in three months**".
- **Central**: 2026-12-31 for the near-term ~1 GW tranche (Anthropic: **"nearly 1GW in total before the end of the year"**); 2028–2030 for the broader 5 GW envelope as Trainium3/4 ramp.
- **Latest**: No public full-5-GW COD date. Trainium4 is forward-looking-disclaimed as a future generation; latest plausible energization is post-2030.
- **Critical-path dependency**: Trainium3 fab/HBM ramp; Mississippi MDEQ permit conditions and Entergy grid commissioning at Madison/Ridgeland; Indiana I&M/NIPSCO transmission upgrades at New Carlisle; Anthropic enterprise/consumer revenue trajectory to support $100B+ cloud-spend cadence.

## Reviewer Findings Addressed

- **Rev-4.2 partial dedupe**: Reduced prior 3.800 GW residual to 1.973 GW via Madison/Ridgeland subtraction; documented as `partial_dedupe_epoch_madison_ridgeland`. Madison and Ridgeland are Epoch #speculative Rainier candidates.
- **New Carlisle treatment**: Treated as pre-existing Rainier capacity per Anthropic Apr 20 "**up to 5GW of new capacity**" framing, distinct from Rainier already running "more than one million Trainium2 chips". Not subtracted from 5 GW residual to avoid double-deduction; counted once in Epoch row.
- **2026 tranche nesting**: "**nearly 1GW in total before the end of the year**" is nested inside the 5 GW headline, not additive; documented in dispatch and atom notes.

## Open Questions / Gaps

- Named site allocation for the 5 GW headline and the ~1 GW 2026 near-term tranche.
- Whether Madison/Ridgeland speculative Rainier attribution survives a primary-source confirmation; if Anthropic publicly disclaims those sites, the residual reverts toward 3.800 GW.
- Take-or-pay terms, minimum-spend enforceability, termination rights, and remedies for delayed capacity.
- Power basis adjudication: whether 5 GW means facility MW, IT load, chip/TDP envelope, or commercial compute-capacity convention.
- Full 5 GW COD date and delivery curve.
- Utility/interconnection documents tying a specific MW quantity to Anthropic at each candidate site.
- Whether $100B+ ten-year commitment is single-tranche cloud reservation, RPO-style customer obligation, or framework-level reciprocal commitment.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Anthropic, "Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute"](https://www.anthropic.com/news/anthropic-amazon-compute) | 2026-04-20 | Primary company announcement | 5 GW headline; 10-year $100B AWS commitment; 2026 near-term tranche; AWS primary status | "up to 5GW of new capacity"; "nearly 1GW in total before the end of the year"; "more than $100 billion over the next ten years" |
| [Amazon, "Amazon and Anthropic expand strategic collaboration"](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai) | 2026-04-20 | Primary company announcement | $5B + up-to-$20B equity; up-to-5 GW; Trainium2/3/4 generations | "up to 5 gigawatts (GW) of capacity" |
| [Amazon, "AWS activates Project Rainier"](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) | 2025-06-24 | Primary company announcement | New Carlisle launch site; existing Rainier context | "one of the world's largest AI compute clusters" |
| [Amazon, "$25 billion in Mississippi data centers"](https://www.aboutamazon.com/news/company-news/amazon-25-billion-mississippi-data-centers) | 2026-04-09 | Primary company announcement | Mississippi statewide $25B; Madison/Hinds County expansion | "total statewide planned investment has reached $25 billion" |
| [MDEQ Permit 1720-00098, Madison Mega Site](https://opc.deq.state.ms.us/get_doc.aspx?dt=dpermit&id=1815201) | 2024-12-04 | Government permit | Madison Mega Site air construction permit; Canton location | "Nissan Parkway and Highway 22" |
| [MDEQ Permit 1720-00099, Ridgeland JAN200](https://opc.deq.state.ms.us/get_doc.aspx?dt=finalp&id=1791725) | 2026-04-24 | Government permit | Ridgeland JAN200 air construction permit | "1626 County Line Road" |
| [Mississippi Today, "Amazon investing $12 billion to build more data centers in Mississippi"](https://mississippitoday.org/2026/04/09/data-centers-amazon-investments/) | 2026-04-09 | Secondary local reporting | Ridgeland event; Entergy power context; recycled-water statements | "held at the site in Ridgeland" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Site-level facility MW for New Carlisle/Madison/Ridgeland | "Project Rainier #speculative" |

## Cross-Links

- Research dispatch: `docs/research/A1_anthropic_aws.md`
- Atoms: `canonical_capacity_atoms.yaml` (`anthropic_aws_incremental_new_capacity`, `epoch_anthropic_amazon_new_carlisle_operational`, `epoch_anthropic_amazon_new_carlisle_buildout_remaining`)
- Dedupe entries: `dedupe_audit.csv` (rows for `anthropic_aws_incremental_new_capacity`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
