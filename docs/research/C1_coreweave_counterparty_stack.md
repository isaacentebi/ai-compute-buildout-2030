# Rev-4.2 Research Dispatch C1: CoreWeave Counterparty Stack

accessed_date: 2026-04-28

## TL;DR

CoreWeave is now primary-source verifiable as a large, public neocloud with 43 data centers, over 850 MW of active power, approximately 3.1 GW of total contracted power capacity, $60.7B of RPO, and $66.8B of broader revenue backlog as of December 31, 2025. The commercial stack is concentrated but diversifying: Microsoft was 67% of FY2025 revenue, OpenAI has agreements totaling up to about $22.4B, Meta had an initial $14.2B order and a newer April 2026 expansion for about $21B, and IBM is a named GB200/NVL72 supercomputer customer.

For Rev-4.2, the strongest site-level overlap candidate is Galaxy Helios in West Texas: Galaxy discloses CoreWeave has committed to the full 800 MW gross approved capacity, while local Epoch already carries `epoch_coreweave_helios_buildout_remaining` as 0.800 GW facility by 2029-01-01 with Microsoft as speculative user. Polaris Forge 1 is not in the local Epoch snapshot, but it is a material leaseback/double-count candidate because Applied Digital discloses 400 MW of critical IT capacity leased to CoreWeave. Customer-level overlaps with Microsoft/OpenAI/Meta sites remain weak without site allocations, but should be carried as candidates because the same demand pools also appear in Epoch-attributed Fairwater, Stargate, Hyperion/Prometheus, and other hyperscaler rows.

```yaml
counterparty: "CoreWeave / Microsoft / OpenAI / Meta / IBM"
contract_overview:
  type: cloud capacity
  term_years: 5
  announced_capex_usd_b: null
  announced_contract_value_usd_b: 57.6
  delivery_window: {earliest: 2026-01-01, central: 2027-12-31, latest: 2032-12-31}
  exclusivity_or_optionality: "CoreWeave describes customer contracts generally as multi-year committed, take-or-pay capacity purchases. Customer/site order forms are heavily redacted; Microsoft, OpenAI, Meta, and IBM do not disclose MW allocations by site. The $57.6B value is a named disclosed customer-order stack, not an additive capacity estimate: OpenAI up to ~$22.4B plus Meta $14.2B and ~$21B expansion. CoreWeave's filed aggregate is $60.7B RPO / $66.8B revenue backlog; Microsoft is disclosed by revenue concentration rather than total contract value, and IBM value is undisclosed."
atoms:
  - id: atom:coreweave_fleet_active_power_disclosed
    site: "CoreWeave 43-data-center fleet, United States and Europe; sites not fully disclosed"
    operator: CoreWeave
    user_or_anchor: "Microsoft / OpenAI / Meta / IBM / other AI customers"
    gw_facility: 0.850
    gw_it: 0.680
    basis: facility_MW
    pue_assumed: 1.25
    energization_window: {earliest: 2025-12-31, central: 2025-12-31, latest: 2025-12-31}
    operational_status: T1
    exact_quote: "over 850 MW of active power"
    source_url: "https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm"
    source_publisher: "CoreWeave FY2025 Form 10-K / SEC"
    source_publication_date: 2026-03-02
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Coreweave Helios"
        epoch_attributed_to: "CoreWeave owner; Microsoft user #speculative"
        overlap_gw_facility: 0.0
        overlap_evidence: "Local Epoch Helios row is 0 MW current / 800 MW buildout, so the 850 MW active fleet is likely ex-Epoch Helios unless later data-hall delivery is added."
      - epoch_site: "Applied Digital Polaris Forge 1"
        epoch_attributed_to: "not in local Epoch; local neocloud leaseback candidate"
        overlap_gw_facility: 0.100
        overlap_evidence: "Applied Digital says PF1 building one is scheduled/RFS around Q4 2025 in local context; if included in CoreWeave's active fleet, it should not also be counted under Applied Digital."
    risks:
      counterparty: "Medium: Microsoft remains the dominant revenue customer; OpenAI, Meta and IBM diversify backlog but add customer-concentration and credit exposure."
      regulatory: "Medium: multi-state data center, export-control, privacy/security, and local power/tax scrutiny; individual fleet sites are not all disclosed."
      power_interconnect: "High: active fleet growth from 360 MW to 850+ MW in one year depends on leased data-center providers and utility delivery."
      supply_chain: "High: CoreWeave cites dependency on latest GPUs, networking, storage, liquid cooling, chillers and HVAC systems."
      technology: "Medium-high: rapid transition from H100/GB200 to B300/Vera Rubin can strand or reprice older clusters."
      financing: "High: asset-level debt is supported by customer take-or-pay contracts; delayed site delivery can push revenue."
      structural_optionality: "Medium: committed contracts reduce demand risk, but order forms are redacted and site/customer fungibility is high."
  - id: atom:coreweave_total_contracted_power_disclosed
    site: "CoreWeave contracted fleet, site mix undisclosed"
    operator: CoreWeave
    user_or_anchor: "Microsoft / OpenAI / Meta / IBM / other AI customers"
    gw_facility: 3.100
    gw_it: 2.480
    basis: facility_MW
    pue_assumed: 1.25
    energization_window: {earliest: 2026-01-01, central: 2027-12-31, latest: null}
    operational_status: T3
    exact_quote: "total contracted power capacity was approximately 3.1 GW"
    source_url: "https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm"
    source_publisher: "CoreWeave FY2025 Form 10-K / SEC"
    source_publication_date: 2026-03-02
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Coreweave Helios"
        epoch_attributed_to: "CoreWeave owner; Microsoft user #speculative"
        overlap_gw_facility: 0.800
        overlap_evidence: "Local Epoch carries Helios as 800 MW facility buildout; Galaxy says CoreWeave committed to the full 800 MW approved power capacity."
      - epoch_site: "Microsoft Fairwater Wisconsin"
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: null
        overlap_evidence: "Microsoft is both CoreWeave's largest FY2025 revenue customer and an Epoch hyperscaler anchor; no source ties CoreWeave capacity to Fairwater."
      - epoch_site: "Microsoft Fairwater Atlanta"
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: null
        overlap_evidence: "Customer-level overlap only: Microsoft demand stack could substitute for or complement Azure/Fairwater capacity; no CoreWeave site allocation disclosed."
      - epoch_site: "OpenAI Stargate Abilene / Shackelford / Milam / Michigan / Wisconsin / New Mexico"
        epoch_attributed_to: OpenAI
        overlap_gw_facility: null
        overlap_evidence: "OpenAI says CoreWeave complements Microsoft, Oracle and Stargate; no evidence that CoreWeave physical sites are Stargate sites."
      - epoch_site: "Meta Hyperion / Meta Prometheus / Meta Temple"
        epoch_attributed_to: Meta
        overlap_gw_facility: null
        overlap_evidence: "Meta's CoreWeave orders are cloud capacity at multiple undisclosed CoreWeave locations, not identified with Meta-owned Epoch campuses."
    risks:
      counterparty: "Medium-high: filed 10-K says top-customer loss or reduced spend would materially affect CoreWeave."
      regulatory: "Medium: location opacity prevents project-by-project permitting checks."
      power_interconnect: "High: 3.1 GW contracted includes future deployments over coming years, likely across Helios, PF1 and other undisclosed leased sites."
      supply_chain: "High: GPU, networking, storage, transformer, liquid-cooling and data-center-shell execution risk."
      technology: "High: contract durations average roughly five years while accelerator generations turn faster."
      financing: "High: RPO/backlog are bankable but dependent on delivery and availability requirements."
      structural_optionality: "Medium: take-or-pay lowers optionality, but customer order forms and capacity substitutions are redacted."
  - id: atom:coreweave_helios_galaxy_overlap_candidate
    site: "Galaxy Helios data center campus, Dickens County / West Texas"
    operator: "Galaxy Digital infrastructure; CoreWeave tenant/operator of AI/HPC workloads"
    user_or_anchor: "CoreWeave; downstream user possibly Microsoft per Epoch #speculative"
    gw_facility: 0.800
    gw_it: 0.526
    basis: facility_MW
    pue_assumed: 1.52
    energization_window: {earliest: 2026-06-30, central: 2027-12-31, latest: 2028-12-31}
    operational_status: T3
    exact_quote: "full 800 MW of approved power capacity"
    source_url: "https://www.galaxy.com/newsroom/galaxy-closes-helios-project-financing"
    source_publisher: "Galaxy Digital"
    source_publication_date: 2025-08-15
    accessed_date: 2026-04-28
    source_notes:
      - "Galaxy Q4 2025 results give 526 MW contracted critical IT load and 800 MW gross power: Phase I 133 MW critical / 200 MW gross in 1H26; Phase II 260 MW critical / 400 MW gross in 2027; Phase III 133 MW critical / 200 MW gross commencing 2028."
      - "The pue_assumed field is just 800 gross divided by 526 critical IT. It is a gross-to-critical conversion from Galaxy's lease tables, not a disclosed operating PUE."
      - "Galaxy also discloses 830 MW additional ERCOT approval and 2.7 GW under load study / 3.5 GW potential, but only the 800 MW CoreWeave commitment is counted as this atom's contracted candidate."
    epoch_site_overlap_candidates:
      - epoch_site: "Coreweave Helios"
        epoch_attributed_to: "CoreWeave owner; Microsoft user #speculative"
        overlap_gw_facility: 0.800
        overlap_evidence: "Same Helios site and same 800 MW gross/approved-power scale as local Epoch's Coreweave Helios buildout row."
    risks:
      counterparty: "Medium: Galaxy's revenue depends on CoreWeave lease performance; CoreWeave's downstream user allocation is undisclosed."
      regulatory: "Medium: ERCOT and Texas interconnection milestones are favorable but expansion beyond 800 MW requires further grid/load-study progress."
      power_interconnect: "High: Phase I/II/III delivery runs 2026-2028 and depends on substation, transmission, commissioning and retrofit execution."
      supply_chain: "Medium-high: retrofit from mining to AI/HPC needs dense power, cooling and high-voltage equipment."
      technology: "Medium: site must support rapidly changing accelerator and liquid-cooling requirements."
      financing: "Medium: $1.4B project financing covers initial retrofit/expansion; Galaxy flags financing-covenant and construction risks."
      structural_optionality: "Medium: CoreWeave exercised options to reach 800 MW, but Galaxy's 2.7 GW additional load-study pipeline is optional and unleased in primary sources."
  - id: atom:coreweave_applied_digital_polaris_forge_1_overlap_candidate
    site: "Applied Digital Polaris Forge 1 Campus, Ellendale, North Dakota"
    operator: Applied Digital
    user_or_anchor: CoreWeave
    gw_facility: null
    gw_it: 0.400
    basis: IT_MW
    pue_assumed: null
    energization_window: {earliest: 2025-12-31, central: 2026-12-31, latest: 2027-12-31}
    operational_status: T3
    exact_quote: "400MW in Total Critical IT Capacity"
    source_url: "https://ir.applieddigital.com/news-events/press-releases/detail/128/applied-digital-finalizes-additional-150mw-lease-with"
    source_publisher: "Applied Digital"
    source_publication_date: 2025-08-29
    accessed_date: 2026-04-28
    source_notes:
      - "Applied Digital discloses three long-term leases with CoreWeave: 100 MW ready-for-service target Q4 2025, 150 MW expected mid-2026, and 150 MW expected full capacity/RFS in 2027."
      - "This is a leaseback/dedupe candidate against CoreWeave's fleet, not an Epoch overlap in the local canonical snapshot."
    epoch_site_overlap_candidates:
      - epoch_site: "None in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: null
        overlap_evidence: "Local neocloud overlay explicitly says Polaris Forge 1 is not in Epoch but should be deduped against CoreWeave."
    risks:
      counterparty: "Medium: Applied Digital depends on CoreWeave as anchor tenant for PF1."
      regulatory: "Medium: North Dakota site approvals and local power arrangements need source-level refresh."
      power_interconnect: "High: three-building delivery schedule spans Q4 2025, mid-2026 and 2027."
      supply_chain: "High: high-density AI factory buildout depends on electrical and cooling equipment delivery."
      technology: "Medium: CoreWeave workload density may change before building three is ready."
      financing: "Medium-high: Applied Digital flags construction, financing and principal-customer risks."
      structural_optionality: "Medium: signed leases are firm, but future 1 GW campus scale is not equivalent to the 400 MW CoreWeave commitment."
  - id: atom:coreweave_openai_capacity_stack
    site: "CoreWeave sites not disclosed"
    operator: CoreWeave
    user_or_anchor: OpenAI
    gw_facility: null
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2025-03-10, central: 2027-12-31, latest: 2031-05-31}
    operational_status: T3
    exact_quote: "total contract value with OpenAI up to approximately $22.4 billion"
    source_url: "https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx"
    source_publisher: "CoreWeave"
    source_publication_date: 2025-09-25
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate Abilene"
        epoch_attributed_to: OpenAI
        overlap_gw_facility: null
        overlap_evidence: "OpenAI's March 2025 CoreWeave quote says the deal complements Microsoft, Oracle and Stargate; it does not identify CoreWeave sites as Stargate."
      - epoch_site: "Microsoft Fairwater Wisconsin / Atlanta"
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: null
        overlap_evidence: "OpenAI also uses Microsoft/Fairwater capacity; CoreWeave capacity is a separate cloud agreement unless later site allocation proves otherwise."
    risks:
      counterparty: "Medium-high: OpenAI is private and large relative to CoreWeave; CoreWeave 10-K explicitly flags OpenAI credit exposure."
      regulatory: "Medium: OpenAI model and compute regulation may affect demand, but site-specific permitting is undisclosed."
      power_interconnect: "Unknown-high: no MW or site schedule disclosed."
      supply_chain: "High: frontier training/inference workloads require latest NVIDIA platforms and network scale."
      technology: "High: reserved capacity may need hardware refresh during contract life."
      financing: "Medium-high: contracts support RPO/backlog and asset-level debt but depend on delivery."
      structural_optionality: "Medium: stated as up-to contract values and reserved capacity orders; termination/order details are redacted."
  - id: atom:coreweave_meta_capacity_stack
    site: "CoreWeave multiple locations not disclosed"
    operator: CoreWeave
    user_or_anchor: Meta
    gw_facility: null
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-04-09, central: 2029-12-31, latest: 2032-12-31}
    operational_status: T3
    exact_quote: "AI cloud capacity through December 2032"
    source_url: "https://investors.coreweave.com/news/news-details/2026/CoreWeave-and-Meta-Announce-21-Billion-Expanded-AI-Infrastructure-Agreement/default.aspx"
    source_publisher: "CoreWeave"
    source_publication_date: 2026-04-09
    accessed_date: 2026-04-28
    source_notes:
      - "CoreWeave FY2025 10-K also discloses a September 2025 Meta order under an existing MSA for up to approximately $14.2B through December 2031."
      - "The April 2026 release says dedicated capacity will be across multiple locations and include initial NVIDIA Vera Rubin platform deployments."
    epoch_site_overlap_candidates:
      - epoch_site: "Meta Hyperion"
        epoch_attributed_to: Meta
        overlap_gw_facility: null
        overlap_evidence: "Customer-level overlap only: Meta's own Hyperion campus is already Epoch-attributed; CoreWeave's Meta capacity is at multiple CoreWeave locations."
      - epoch_site: "Meta Prometheus / Meta Temple"
        epoch_attributed_to: Meta
        overlap_gw_facility: null
        overlap_evidence: "No primary source ties the CoreWeave Meta order to these Meta-owned/leased Epoch campuses."
    risks:
      counterparty: "Low-medium: Meta has strong credit, but customer-concentration and AI strategy reprioritization matter."
      regulatory: "Medium: Meta AI/data-center scrutiny may affect both owned and leased AI capacity."
      power_interconnect: "Unknown-high: multiple CoreWeave locations are not named."
      supply_chain: "High: Vera Rubin early deployment creates platform and cooling readiness risk."
      technology: "High: inference workload mix may alter capacity needs through 2032."
      financing: "Medium: large Meta contract improves financing support; exact MW and asset collateral are not disclosed."
      structural_optionality: "Medium: initial commitment and expansion language are firm commercially, but order form terms are redacted."
  - id: atom:coreweave_ibm_granite_supercomputer
    site: "CoreWeave site not disclosed"
    operator: CoreWeave
    user_or_anchor: IBM
    gw_facility: null
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2025-01-15, central: 2025-12-31, latest: null}
    operational_status: T4
    exact_quote: "one of the first NVIDIA GB200 Grace Blackwell Superchip-enabled AI supercomputers"
    source_url: "https://newsroom.ibm.com/2025-01-15-coreweave-partners-with-ibm-to-deliver-new-ai-supercomputer-for-ibm-granite-models"
    source_publisher: "IBM Newsroom / CoreWeave"
    source_publication_date: 2025-01-15
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "No named Epoch overlap"
        epoch_attributed_to: null
        overlap_gw_facility: null
        overlap_evidence: "IBM/CoreWeave disclosed platform and workload but not MW, facility, utility, or location."
    risks:
      counterparty: "Low: IBM is an investment-grade enterprise customer, but contract value is undisclosed."
      regulatory: "Low-medium: enterprise AI and data handling requirements may constrain deployment."
      power_interconnect: "Unknown: no site or MW disclosed."
      supply_chain: "Medium-high: one of the first GB200 NVL72 supercomputers depends on early Blackwell supply."
      technology: "Medium: IBM Granite training stack may shift as IBM evolves hybrid-cloud AI."
      financing: "Low-medium: no disclosed dollar commitment, so financing relevance to CoreWeave RPO is unclear."
      structural_optionality: "High: no term, MW, or minimum payment disclosed."
contradictions:
  - "CoreWeave reports 3.1 GW total contracted power capacity on a fleet basis, while Galaxy and Applied Digital disclose Helios/PF1 in gross power and/or critical IT load. Do not merge these bases without a conversion rule."
  - "Local neocloud overlay subtracts only the 0.800 GW Helios Epoch overlap from CoreWeave's 3.1 GW to get 2.300 GW contracted ex-Epoch, while separately marking Polaris Forge 1 as a CoreWeave/Applied Digital leaseback. That is a local attribution convention, not a primary-source statement."
  - "Epoch attributes Helios user to Microsoft on a speculative basis. CoreWeave primary filings show Microsoft is the largest customer, but no primary source maps Microsoft to Helios."
  - "Galaxy's Helios Phase I/II/III schedule supports 2026-2028 delivery, while local Epoch stores Helios buildout by 2029-01-01. Treat the difference as schedule granularity, not a resolved contradiction."
  - "CoreWeave's April 2026 Meta expansion adds a new $21B commitment but no MW; it should not mechanically increase the 3.1 GW contracted-power atom without a new capacity disclosure."
gaps:
  - "Named site allocation by customer for Microsoft, OpenAI, Meta and IBM."
  - "Whether any Helios capacity is specifically assigned to Microsoft, OpenAI, Meta, IBM, or another customer."
  - "CoreWeave Q1 2026 filing/results, if filed after this dispatch, to update 850 MW active and 3.1 GW contracted power."
  - "Primary SEC 8-K text for the April 2026 Meta order form, including exact relationship to the September 2025 $14.2B order."
  - "Polaris Forge 1 current RFS/energized status by building as of 2026-04-28 from Applied Digital 10-Q or site-specific utility evidence."
  - "Full CoreWeave site list and crosswalk to Epoch rows, including Helios, Core Scientific/CoreWeave sites, Lancaster, Kenilworth, and European sites."
  - "Power-basis reconciliation among CoreWeave 'active/contracted power', Galaxy gross power vs critical IT load, Applied Digital critical IT capacity, and Epoch facility MW."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [CoreWeave FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm) | 2026-03-02 | SEC filing | 43 data centers, 850+ MW active power, 3.1 GW contracted power, $60.7B RPO, five-year weighted-average committed contract duration, Microsoft/OpenAI/Meta concentration. | "43 data centers with over 850 MW" | 2026-04-28 |
| [CoreWeave Q4/FY2025 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results/) | 2026-02-27 | Primary company release | $66.8B revenue backlog and operating update around active/contracted power. | "$66.8 billion" | 2026-04-28 |
| [CoreWeave-Microsoft MSA exhibit](https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798dex1023.htm) | 2025-03-03 | SEC contract exhibit | Microsoft MSA terms, U.S. default geography, dedicated fiber, customer hardware requirements, order-form structure. | "provided within the United States" | 2026-04-28 |
| [CoreWeave OpenAI March 2025 agreement](https://coreweave.com/news/coreweave-announces-agreement-with-openai-to-deliver-ai-infrastructure) | 2025-03-10 | Primary company release | Initial OpenAI contract up to $11.9B and OpenAI $350M stock issuance. | "up to $11.9 billion" | 2026-04-28 |
| [CoreWeave OpenAI September 2025 expansion](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx) | 2025-09-25 | Primary company release | Additional up-to-$6.5B agreement and total OpenAI contract value up to ~$22.4B. | "up to approximately $22.4 billion" | 2026-04-28 |
| [CoreWeave Meta April 2026 expansion](https://investors.coreweave.com/news/news-details/2026/CoreWeave-and-Meta-Announce-21-Billion-Expanded-AI-Infrastructure-Agreement/default.aspx) | 2026-04-09 | Primary company release | Meta expansion for about $21B through December 2032, multiple locations, Vera Rubin. | "approximately $21 billion" | 2026-04-28 |
| [CoreWeave-Meta MSA exhibit](https://www.sec.gov/Archives/edgar/data/1769628/000176962825000050/redactedmetamsa929finald.htm) | 2025-09-30 | SEC contract exhibit | Existing Meta MSA, effective December 2023, under which later order forms were placed. | "Meta Platforms, Inc." | 2026-04-28 |
| [IBM/CoreWeave Granite supercomputer release](https://newsroom.ibm.com/2025-01-15-coreweave-partners-with-ibm-to-deliver-new-ai-supercomputer-for-ibm-granite-models) | 2025-01-15 | Primary company release | IBM GB200 NVL72 supercomputer for Granite models and IBM Storage integration. | "train the next generations of its Granite models" | 2026-04-28 |
| [Galaxy Helios project financing release](https://www.galaxy.com/newsroom/galaxy-closes-helios-project-financing) | 2025-08-15 | Primary company release | $1.4B financing, CoreWeave full 800 MW approved power commitment, 15-year revenue basis, 3.5 GW potential. | "full 800 MW" | 2026-04-28 |
| [Galaxy Q4/FY2025 results](https://investor.galaxy.com/news-releases/news-release-details/galaxy-announces-fourth-quarter-and-full-year-2025-financial) | 2026-02-03 | Primary company release | Helios 526 MW critical IT / 800 MW gross schedule, 1.6 GW approved power after ERCOT approval. | "526MW" | 2026-04-28 |
| [Applied Digital PF1 CoreWeave lease release](https://ir.applieddigital.com/news-events/press-releases/detail/128/applied-digital-finalizes-additional-150mw-lease-with) | 2025-08-29 | Primary company release | PF1 400 MW critical IT capacity leased to CoreWeave across three long-term leases and delivery schedule. | "400MW across" | 2026-04-28 |
| [Applied Digital PF2 hyperscaler lease release](https://ir.applieddigital.com/news-events/press-releases/detail/132/applied-digital-announces-5-billion-ai-factory-lease-with) | 2025-10-22 | Primary company release | PF2 200 MW critical IT lease to undisclosed investment-grade hyperscaler; useful to separate from CoreWeave PF1. | "200 megawatts" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Local overlap rows: Coreweave Helios 0.800 GW facility buildout by 2029-01-01; Microsoft/OpenAI/Meta Epoch site universe. | "Coreweave Helios" | 2026-04-28 |

## Research Notes

- Capacity basis: CoreWeave's 850 MW and 3.1 GW are disclosed as active/contracted power capacity at fleet level; I map them to facility_MW to match local atom convention. Galaxy's Helios disclosure provides both gross power and critical IT load; Applied Digital PF1 is critical IT load only.
- Incremental ex-Epoch candidate: if using local atom convention, the clean mechanical split is 3.1 GW CoreWeave contracted power less 0.8 GW Helios already in Epoch = 2.3 GW contracted ex-Epoch. This dispatch does not adjudicate whether to further adjust for PF1, because PF1 is not an Epoch row but is a leaseback/double-count candidate against Applied Digital.
- Active incremental candidate: the 850 MW active fleet appears incremental to Epoch Helios because local Epoch Helios has 0 MW current. PF1 building one may be embedded in that 850 MW and should not also be counted under Applied Digital.
- Customer-site mapping: Microsoft/OpenAI/Meta/IBM contracts are strong commercially but weak geographically. Without order-form site schedules, overlaps with Fairwater, Stargate, Hyperion, Prometheus and Temple are customer-demand candidates rather than physical site overlaps.
- Latest-source caution: the April 9, 2026 Meta expansion is current as of this dispatch and adds contract value/duration evidence, but not a new MW disclosure.
