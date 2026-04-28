# A1 Research Dispatch: Anthropic-AWS 5 GW Project Rainier Expansion

```yaml
counterparty: Anthropic / Amazon Web Services
contract_overview:
  type: cloud capacity
  term_years: 10
  announced_capex_usd_b: null
  announced_contract_value_usd_b: 100+
  announced_equity_usd_b: {immediate: 5, possible_future: 20, prior: 8}
  delivery_window: {earliest: 2026-04-20, central: 2026-12-31, latest: null}
  exclusivity_or_optionality: >
    Non-exclusive cloud-capacity commitment. Anthropic says AWS remains its
    primary training and cloud provider, but Claude is also available through
    Google Cloud and Microsoft Azure. The 5 GW figure is an "up to" capacity
    ceiling across Trainium2, Trainium3, Trainium4, and optional future
    Trainium generations; the full 5 GW delivery date and site allocation are
    not disclosed. Amazon's equity investment is separate from Anthropic's
    AWS spend commitment and includes future milestone-linked optionality.
atoms:
  - id: atom:anthropic_aws_2026_04_20_total_5gw
    site: "Project Rainier expansion / AWS sites not disclosed"
    operator: Amazon Web Services
    user_or_anchor: Anthropic
    gw_facility: [5.0, 6.0]
    gw_it: 5.0
    basis: ambiguous_compute
    pue_assumed: 1.20
    energization_window: {earliest: 2026-04-20, central: null, latest: null}
    operational_status: T4
    exact_quote: "securing up to 5GW of new capacity"
    source_url: https://www.anthropic.com/news/anthropic-amazon-compute
    source_publisher: Anthropic
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "Anthropic gives the strongest 'new capacity' wording, but does not name sites or distinguish facility MW from IT/chip capacity."
      - "Amazon's parallel release describes 'up to 5 gigawatts (GW) of capacity' and ties it to Trainium generations, reinforcing ambiguous_compute rather than facility-power basis."
      - "The 6.0 GW facility high is only the current repo convention of treating 5.0 GW as IT-equivalent at 1.20 PUE; it is not a primary-source facility disclosure."
      - "The 10-year term is from Anthropic's 'more than $100 billion over the next ten years' AWS-technology commitment."
    contract_structure:
      cloud_spend_commitment_usd_b: 100+
      term_years: 10
      chips: ["Trainium2", "Trainium3", "Trainium4", "future Trainium generations"]
      includes_inference_regions: ["Asia", "Europe"]
      aws_role: "Primary training and cloud provider for mission-critical Anthropic workloads."
      amazon_equity: "Amazon invests $5B immediately, with up to $20B future milestone-linked investment, separate from prior $8B."
      take_or_pay_status: "Not disclosed in public sources; treat as cloud capacity / spend commitment, not confirmed take-or-pay."
    epoch_site_overlap_candidates:
      - epoch_site: Anthropic-Amazon New Carlisle
        epoch_attributed_to: "Amazon -> Anthropic; Project Rainier #confident"
        overlap_gw_facility: 1.229
        overlap_evidence: >
          AWS publicly identifies St. Joseph County, Indiana as one Project
          Rainier site, and the local Epoch snapshot carries New Carlisle to
          1.229 GW facility by 2026-06-21. Candidate is strongest for existing
          Rainier context, but Anthropic's Apr. 20 release frames the 5 GW as
          "new" relative to Rainier already using over one million Trainium2
          chips, so this may be pre-existing rather than overlap.
      - epoch_site: Amazon Madison Mega Site
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 0.819
        overlap_evidence: >
          Local Epoch snapshot tags Madison as speculative Rainier and carries
          0.819 GW facility by 2026-09-18. Amazon's Mississippi releases
          confirm a large Madison County/Canton AWS campus, but do not tie it
          to Anthropic or Project Rainier; overlap remains a candidate only.
      - epoch_site: Amazon Ridgeland
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 1.008
        overlap_evidence: >
          Local Epoch snapshot tags Ridgeland as speculative Rainier and carries
          1.008 GW facility by 2027-09-21. Mississippi Today and Amazon confirm
          an Amazon data-center expansion/event at Ridgeland in April 2026, but
          public primary sources do not name Anthropic.
    risks:
      counterparty: "Anthropic is buying from AWS while also expanding Google/Broadcom TPU and Azure/NVIDIA capacity; AWS remains primary but not exclusive."
      regulatory: "No public April 20 site list; each candidate site has separate local permitting, water, tax, and community-opposition exposure."
      power_interconnect: "5 GW of compute capacity would require multi-GW utility commitments; Mississippi and Indiana sources discuss grid upgrades but not a full 5 GW interconnect schedule."
      supply_chain: "Capacity depends on Trainium2/3/4 ramps; Trainium4 is future-generation silicon, and Amazon explicitly forward-looking-disclaims delivery timing."
      technology: "Trainium3/4 fleet-scale training and inference performance remains less externally benchmarked than NVIDIA GPU capacity."
      financing: "$100B is Anthropic cloud spend, not Amazon facility capex; Amazon's $5B/+20B equity support creates circular funding optics."
      structural_optionality: "'Up to' 5 GW, optional future silicon, no named sites, and no full delivery date create high optionality."

  - id: atom:anthropic_aws_2026_04_20_2026_tranche_1gw
    site: "Project Rainier expansion / 2026 tranche, sites not disclosed"
    operator: Amazon Web Services
    user_or_anchor: Anthropic
    gw_facility: [1.0, 1.2]
    gw_it: 1.0
    basis: ambiguous_compute
    pue_assumed: 1.20
    energization_window: {earliest: 2026-04-20, central: 2026-12-31, latest: 2026-12-31}
    operational_status: T3
    exact_quote: "nearly 1GW in total before the end of the year"
    source_url: https://www.anthropic.com/news/anthropic-amazon-compute
    source_publisher: Anthropic
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "This is a nested delivery tranche inside the 5 GW headline, not additive to the 5 GW total atom."
      - "Anthropic also says significant Trainium2 capacity is coming online in Q2 and scaled Trainium3 capacity later in 2026."
      - "Amazon's release confirms significant Trainium3 capacity expected this year, but does not quantify the 2026 tranche."
    contract_structure:
      tranche_type: "Near-term Trainium2/Trainium3 capacity under the broader 10-year AWS commitment."
      take_or_pay_status: "Not disclosed."
    epoch_site_overlap_candidates:
      - epoch_site: Anthropic-Amazon New Carlisle
        epoch_attributed_to: "Amazon -> Anthropic; Project Rainier #confident"
        overlap_gw_facility: 0.137
        overlap_evidence: >
          Local Epoch snapshot shows 0.137 GW facility remaining buildout at
          New Carlisle by 2026-06-21, which overlaps Anthropic's first-half
          2026 Trainium2 language. It is unclear whether this is part of
          already-existing Rainier or the April 20 "new" tranche.
      - epoch_site: Amazon Madison Mega Site
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 0.819
        overlap_evidence: >
          Epoch's 2026-09-18 Madison buildout date is close to Anthropic's
          year-end 2026 tranche; however the Rainier/Anthropic attribution is
          speculative and not confirmed by the April 20 announcement.
      - epoch_site: Amazon Ridgeland
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 0.273
        overlap_evidence: >
          Epoch's timeline has 0.273 GW facility operational by 2026-05-19
          and 1.008 GW by 2027-09-21. The 2026 portion could overlap the
          near-term tranche, but no public source ties Ridgeland to Anthropic.
    risks:
      counterparty: "Near-term demand pressure is explicit; Anthropic says consumer and enterprise growth strained reliability."
      regulatory: "If the tranche maps to Mississippi, water/recycled-water and air-permit conditions remain relevant; if Indiana, I&M/NIPSCO service terms matter."
      power_interconnect: "Fast 2026 delivery likely depends on already-permitted or already-energized AWS sites."
      supply_chain: "Trainium3 capacity later in 2026 is a ramp risk."
      technology: "Scaled Trainium3 deployment is new production infrastructure."
      financing: "No tranche-level price or minimum payment disclosed."
      structural_optionality: "Nested in the 5 GW headline; must not be counted as additional capacity."

  - id: atom:epoch_context_anthropic_aws_candidate_sites
    site: "New Carlisle IN; Canton/Madison County MS; Ridgeland MS"
    operator: Amazon Web Services
    user_or_anchor: Anthropic
    gw_facility: 3.056
    gw_it: 2.635
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2026-05-19, central: 2026-09-18, latest: 2027-09-21}
    operational_status: unknown
    exact_quote: "Project Rainier #speculative"
    source_url: https://epoch.ai/data/data-centers
    source_publisher: Epoch AI Frontier Data Centers local snapshot
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "This context atom is not a new commitment. It sums candidate Epoch facility buildout relevant to dedupe review: New Carlisle remaining 0.137 GW, Madison total 0.819 GW, Ridgeland total 1.008 GW, plus New Carlisle already-operational 1.092 GW."
      - "New Carlisle is #confident Rainier/Anthropic; Madison and Ridgeland are #speculative Rainier/Anthropic in the local Epoch snapshot."
      - "Do not adjudicate headline dedupe from this atom; it exists only to surface overlap candidates."
    epoch_site_overlap_candidates:
      - epoch_site: Anthropic-Amazon New Carlisle
        epoch_attributed_to: "Amazon -> Anthropic; Project Rainier #confident"
        overlap_gw_facility: 1.229
        overlap_evidence: "Epoch current 1.092 GW facility plus 0.137 GW remaining buildout by 2026-06-21."
      - epoch_site: Amazon Madison Mega Site
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 0.819
        overlap_evidence: "Epoch current 0.341 GW facility plus 0.478 GW remaining buildout by 2026-09-18."
      - epoch_site: Amazon Ridgeland
        epoch_attributed_to: "Amazon -> Anthropic #speculative; Project Rainier #speculative"
        overlap_gw_facility: 1.008
        overlap_evidence: "Epoch 1.008 GW facility buildout by 2027-09-21, including 0.273 GW by 2026-05-19."
    risks:
      counterparty: "Epoch's user attribution differs by site confidence: New Carlisle is confident; Mississippi sites are speculative."
      regulatory: "MDEQ permits and Madison County water/wastewater agreements show physical projects, not Anthropic tenant identity."
      power_interconnect: "Mississippi expansion depends on Entergy/grid buildout; New Carlisle depends on Indiana utility arrangements."
      supply_chain: "Physical shells can be ahead of Trainium allocations."
      technology: "Epoch facility-MW estimates are not the same unit as Amazon/Anthropic chip-capacity language."
      financing: "Amazon Mississippi and Indiana capex announcements are site/program capex, not necessarily Anthropic-specific spend."
      structural_optionality: "Candidate set could be inside existing AWS growth rather than the April 20 new-capacity envelope."
contradictions:
  - "Anthropic calls the 5 GW 'new capacity'; Amazon's release says 'current and future generations' of Trainium capacity and does not use 'new' in the same headline claim."
  - "Anthropic says it currently uses over one million Trainium2 chips in Project Rainier, while AWS's Project Rainier launch article described nearly half a million chips and more than one million by year-end; this appears to be timing progression, not necessarily inconsistent."
  - "The local overlay treats Madison + Ridgeland as likely overlap and New Carlisle as existing/non-overlap; the 2026 tranche could still include New Carlisle's 0.137 GW remaining buildout."
  - "Amazon's Mississippi releases confirm large AWS campuses at Canton/Madison County and Ridgeland/Hinds-area expansion, but do not publicly connect those campuses to Anthropic or Project Rainier."
gaps:
  - "Named site allocation for the 5 GW headline and the 2026 near-term tranche."
  - "Contract language: minimum spend, take-or-pay terms, termination rights, and remedies for delayed capacity."
  - "Power basis: whether 5 GW means facility MW, IT load, chip/TDP envelope, or commercial compute-capacity convention."
  - "Ramp schedule after year-end 2026; no source found with a full 5 GW COD date."
  - "Whether Madison and Ridgeland are truly Anthropic/Rainier, generic AWS cloud capacity, or a mix."
  - "Utility/interconnection documents tying a specific MW quantity to Anthropic at each candidate site."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [Anthropic, "Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute"](https://www.anthropic.com/news/anthropic-amazon-compute) | 2026-04-20 | Primary company announcement | 5 GW headline, 10-year $100B AWS commitment, 2026 near-term tranche, Trainium generations, AWS primary-provider status, Amazon equity. | "up to 5GW of new capacity" | 2026-04-28 |
| [Amazon, "Amazon and Anthropic expand strategic collaboration"](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai) | 2026-04-20 | Primary company announcement | Confirms >$100B AWS spend, up-to-5 GW capacity, Trainium2/3/4 and future Trainium, $5B plus up-to-$20B equity. | "up to 5 gigawatts (GW) of capacity" | 2026-04-28 |
| [Amazon, "AWS activates Project Rainier"](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) | 2025-06-24 | Primary company announcement | Existing Rainier context: St. Joseph County site, nearly half-million Trainium2 chips at launch, Anthropic workloads, water/cooling notes. | "one of the world's largest AI compute clusters" | 2026-04-28 |
| [Amazon, "Amazon plans to invest $25 billion in Mississippi data centers"](https://www.aboutamazon.com/news/company-news/amazon-25-billion-mississippi-data-centers) | 2026-04-09 | Primary company announcement | Confirms Mississippi AWS campus expansion, $25B statewide plan, additional Madison County/Hinds County investments, grid/water claims. | "total statewide planned investment has reached $25 billion" | 2026-04-28 |
| [Amazon, "AWS plans to invest $10 billion in Mississippi"](https://www.aboutamazon.com/news/aws/aws-10-billion-investment-mississippi/) | 2024-01-25 | Primary company announcement | Original Madison County AWS two-complex announcement; confirms two industrial-park data-center complexes but not Anthropic tenant. | "two data center complexes" | 2026-04-28 |
| [MDEQ enSearch, Amazon Data Services / Madison Mega Site](https://opcgis.deq.state.ms.us/ensearchonline/ai_info.aspx?ai=86219) | 2026-04-28 | Government database | Confirms Amazon Data Services Madison Mega Site air-construction permit records and Canton address. | "Amazon Data Services Inc, Madison Mega Site" | 2026-04-28 |
| [MDEQ Permit 1720-00098, Madison Mega Site](https://opc.deq.state.ms.us/get_doc.aspx?dt=dpermit&id=1815201) | 2024-12-04 | Government permit | Air construction permit for Amazon Data Services Inc, Madison Mega Site, Nissan Parkway and Highway 22, Canton. | "Nissan Parkway and Highway 22" | 2026-04-28 |
| [MDEQ Permit 1720-00099, Ridgeland](https://opc.deq.state.ms.us/get_doc.aspx?dt=finalp&id=1791725) | 2026-04-24 | Government permit | Air construction permit for Amazon Data Services Inc, JAN200, 1626 County Line Road, Ridgeland. | "1626 County Line Road" | 2026-04-28 |
| [Madison County / ADS water and wastewater service agreement](https://tools.madison-co.net/images/agenda_files/342/JAN100%20WSA%20-%204-18-2025%20Redacted%20Exhibits%20%5B103808541%20V1%5D.pdf) | 2025-04-08 | Local government agreement | Confirms Madison Mega Site project location and water/wastewater infrastructure serving Amazon Data Services. | "JAN100/Madison Mega Site" | 2026-04-28 |
| [Mississippi Today, "Amazon investing $12 billion to build more data centers in Mississippi"](https://mississippitoday.org/2026/04/09/data-centers-amazon-investments/) | 2026-04-09 | Secondary local reporting | Ridgeland event, $25B statewide total, Entergy power context, recycled-water statements, local concerns. | "held at the site in Ridgeland" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Candidate overlap sites: New Carlisle 1.229 GW facility, Madison 0.819 GW facility, Ridgeland 1.008 GW facility. | "Project Rainier #speculative" | 2026-04-28 |

## Research Notes

- Capacity basis: official sources use "capacity," "compute," and "Trainium chips," not facility MW. I kept the repo's 1.20 PUE convention visible but treated the source basis as `ambiguous_compute`.
- Delivery timing: only the near-term tranche is dated: meaningful compute in three months, Trainium2 in Q2, scaled Trainium3 later in 2026, and nearly 1 GW by 2026-12-31. No full 5 GW delivery date was found.
- Epoch overlap posture: New Carlisle is a confirmed existing Rainier site and strongest context candidate, but likely pre-announcement capacity. Madison and Ridgeland are physically real AWS Mississippi sites, but Anthropic/Rainier attribution remains speculative in local Epoch data and unconfirmed in primary public releases.
- Dedupe posture: do not finalize subtraction here. Plausible interpretations range from "5 GW fully net-new beyond all three Epoch sites" to "near-term/new tranche partly repackages New Carlisle/Madison/Ridgeland already in Epoch."
