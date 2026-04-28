# Rev-4.2 Research Dispatch B2: OpenAI Stargate US

```yaml
counterparty: OpenAI / Oracle / SoftBank / Crusoe / Vantage / Related Digital
contract_overview:
  type: JV
  term_years: null
  announced_capex_usd_b: 500.0
  delivery_window: {earliest: 2025-06-01, central: 2028-12-31, latest: 2029-12-31}
  exclusivity_or_optionality: >
    Stargate is a multi-party infrastructure platform rather than one clean
    signed site lease. January 2025 launch language makes SoftBank and OpenAI
    lead partners, with SoftBank holding financial responsibility and OpenAI
    operational responsibility; Oracle, NVIDIA, Microsoft, Arm, and OpenAI were
    named initial technology partners. Later disclosures split the surface into
    Oracle capacity, SoftBank/OpenAI fast-build sites, CoreWeave capacity, and
    Microsoft-provided OpenAI cloud capacity. Treat all site and GW claims as
    overlap candidates, not additive adjudications.
atoms:
  - id: atom:b2_openai_stargate_us_program_envelope
    site: "United States Stargate program, multi-site"
    operator: "Stargate JV / Oracle / SoftBank / developers"
    user_or_anchor: OpenAI
    gw_facility: [7.0, 8.0, 10.0]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2025-06-01, central: 2028-12-31, latest: 2029-12-31}
    operational_status: T4
    exact_quote: "$500 billion, 10-gigawatt commitment"
    source_url: https://openai.com/index/five-new-stargate-sites/
    source_publisher: OpenAI
    source_publication_date: 2025-09-23
    accessed_date: 2026-04-28
    source_notes:
      - "Jan. 21, 2025 launch: $500B over four years, $100B immediate deployment, starting in Texas."
      - "Jul. 22, 2025 Oracle agreement: 4.5 GW additional U.S. capacity; with Abilene, over 5 GW under development."
      - "Sep. 23, 2025: five new U.S. sites plus Abilene and CoreWeave bring Stargate to nearly 7 GW and over $400B over three years."
      - "Oct. 30, 2025 Michigan announcement: over 8 GW planned capacity and more than $450B over three years."
      - "Jan. 20, 2026 OpenAI community page: U.S. AI infrastructure target stated as 10 GW by 2029, with multiple sites under development."
    epoch_site_overlap_candidates:
      - epoch_site: OpenAI Stargate Abilene
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.180
        overlap_evidence: >
          Local Epoch atoms carry 0.200 GW operational plus 0.980 GW remaining
          facility buildout by 2026-07-01. Direct site/program match.
      - epoch_site: OpenAI Stargate Shackelford
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.960
        overlap_evidence: >
          Local Epoch atom carries 1.960 GW facility by 2028-12-31. Direct
          match to OpenAI's Shackelford County site and Vantage Frontier campus.
      - epoch_site: OpenAI Stargate New Mexico
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 2.210
        overlap_evidence: >
          Local Epoch atom carries 2.210 GW facility by 2028-12-31. Direct
          match to OpenAI's Dona Ana County site; public/local sources also use
          Project Jupiter naming.
      - epoch_site: OpenAI Stargate Wisconsin
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.300
        overlap_evidence: >
          Local Epoch atom carries 1.300 GW facility by 2028-12-31. Direct
          match to the Port Washington/Lighthouse site announced as the Midwest
          Stargate site.
      - epoch_site: OpenAI Stargate Michigan
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.383
        overlap_evidence: >
          Local Epoch atom carries 1.383 GW facility by 2028-12-31. Direct
          match to OpenAI/Oracle/Related Digital Saline Township announcement
          and MPSC 1,383 MW approval.
      - epoch_site: OpenAI Stargate Milam
        epoch_attributed_to: "SoftBank -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.200
        overlap_evidence: >
          Local Epoch atom carries 1.200 GW facility by 2028-12-31. Direct
          match to OpenAI/SoftBank/SB Energy Milam County site.
      - epoch_site: OpenAI Stargate Lordstown
        epoch_attributed_to: "SoftBank -> OpenAI, Stargate #confident"
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch data_centers.csv has a Stargate Lordstown row with zero
          MW because no visible construction/capacity atom is yet carried; OpenAI
          and SoftBank name Lordstown as a site that can scale within the
          SoftBank/OpenAI 1.5 GW tranche.
      - epoch_site: Crusoe Abilene Expansion
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Candidate contradiction/adjacency only. Local Epoch treats the former
          Abilene expansion as Microsoft, not OpenAI. Crusoe's Mar. 27, 2026
          primary release says the adjacent 900 MW campus supports Microsoft AI
          infrastructure.
      - epoch_site: Microsoft Fairwater Mount Pleasant / Fairwater Wisconsin
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: 3.328
        overlap_evidence: >
          OpenAI's Jan. 2026 community page refers to a latest AI campus with
          Microsoft in Mount Pleasant, Wisconsin. Candidate only: it is not one
          of the Oracle/SoftBank Stargate sites and is already a Microsoft AI WAN
          Epoch site.
    risks:
      counterparty: "OpenAI is committing across Oracle, Microsoft, SoftBank, CoreWeave, AWS, NVIDIA, AMD, and Broadcom surfaces; obligation seniority and cancellation rights are not public."
      regulatory: "Named sites face state/local utility, zoning, environmental, water, air, and bond approvals; Michigan and New Mexico already show public-opposition and cost-allocation scrutiny."
      power_interconnect: "The public GW figures mix data-center capacity, IT/load, site potential, and power commitments; power-delivery responsibility varies by site."
      supply_chain: "GB200/Rubin racks, HBM, liquid cooling, switchgear, turbines, substations, transformers, and skilled labor remain gating items."
      technology: "OpenAI may change accelerator mix across NVIDIA, AMD, Broadcom/OpenAI ASICs, and Microsoft/Oracle cloud designs before all sites energize."
      financing: "January JV language assigns SoftBank financial responsibility, but Abilene is separately project-financed; Oracle has major RPO/lease/capex exposure."
      structural_optionality: "The same OpenAI demand can appear as Stargate, Oracle RPO, Microsoft capacity, CoreWeave capacity, and chip procurement; high double-count risk."

  - id: atom:b2_stargate_abilene_flagship
    site: "Stargate I, Abilene, Texas"
    operator: "Crusoe developer / Oracle Cloud Infrastructure"
    user_or_anchor: OpenAI
    gw_facility: [0.200, 1.180, 1.200]
    gw_it: null
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2025-06-01, central: 2026-07-01, latest: 2026-12-31}
    operational_status: T2
    exact_quote: "first phase of Stargate's flagship data center campus"
    source_url: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
    source_publisher: Crusoe
    source_publication_date: 2025-09-30
    accessed_date: 2026-04-28
    source_notes:
      - "Crusoe says construction began in June 2024; first two buildings were energized within a year; Oracle began delivering NVIDIA GB200 racks in June 2025."
      - "Crusoe/Blue Owl/Primary Digital May 2025 release describes a $15B JV, 1.2 GW AI data center, two-building first phase of 200+ MW, and six-building second phase expected in mid-2026."
      - "Mortenson describes a 200 MW 138 kV substation, an expansion, and a Phase 2 1 GW 345 kV substation with five main power transformers."
    epoch_site_overlap_candidates:
      - epoch_site: OpenAI Stargate Abilene
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.180
        overlap_evidence: >
          Direct site match. Local Epoch 2026-04-22 revision treats roughly
          0.200 GW operational by the April 2026 cutoff and pushes prior 0.590
          GW milestone back into under-construction pending commissioning.
      - epoch_site: Crusoe Abilene Expansion
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Adjacent/former expansion candidate. AP reports OpenAI declined to
          pursue further Abilene expansion; Crusoe primary source now assigns
          the new 900 MW campus to Microsoft.
    risks:
      counterparty: "Crusoe develops and Oracle provides OCI to OpenAI; financing involves Blue Owl and Primary Digital rather than a single OpenAI-owned asset."
      regulatory: "Air, substation, turbine, and local construction approvals must be checked building-by-building."
      power_interconnect: "Mortenson documents 200 MW existing substation plus 1 GW 345 kV phase; AP reports grid draw with on-site gas backup/plant complexity."
      supply_chain: "Eight-building completion depends on GB200 rack delivery, electrical gear, direct-to-chip liquid cooling, and construction labor."
      technology: "Early workload status is credible, but full eight-building commissioning and GPU installation can lag shell energization."
      financing: "The $15B JV funds construction; OpenAI/Oracle lease/payment terms are not fully public."
      structural_optionality: "The Abilene 1.2 GW campus and the adjacent Microsoft 900 MW campus should not be merged without adjudication."

  - id: atom:b2_oracle_stargate_4_5gw_us_tranche
    site: "Oracle-led Stargate sites: Shackelford TX, Dona Ana NM, Port Washington WI, Saline MI, Abilene-area expansion candidate"
    operator: "Oracle / Vantage / Related Digital / other developers"
    user_or_anchor: OpenAI
    gw_facility: [4.5, 5.5]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2028-12-31, latest: 2029-12-31}
    operational_status: T4
    exact_quote: "4.5 gigawatts of additional Stargate capacity"
    source_url: https://openai.com/index/stargate-advances-with-partnership-with-oracle/
    source_publisher: OpenAI
    source_publication_date: 2025-07-22
    accessed_date: 2026-04-28
    source_notes:
      - "Sep. 2025 OpenAI/SoftBank source says the Oracle/OpenAI partnership exceeds $300B over five years."
      - "OpenAI later says Michigan is part of the 4.5 GW Oracle partnership and brings Stargate over 8 GW planned capacity."
      - "Oracle Q1 FY26 RPO was $455B; Q3 FY26 RPO was $553B, with large-scale AI contracts and a $50B financing program disclosed."
    epoch_site_overlap_candidates:
      - epoch_site: OpenAI Stargate Shackelford
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.960
        overlap_evidence: "Direct match to OpenAI's Shackelford County site; Epoch buildout by 2028-12-31."
      - epoch_site: OpenAI Stargate New Mexico
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 2.210
        overlap_evidence: "Direct match to OpenAI's Dona Ana County site; Epoch buildout by 2028-12-31."
      - epoch_site: OpenAI Stargate Wisconsin
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.300
        overlap_evidence: "Direct match to Port Washington/Lighthouse; Vantage says close to 1 GW AI capacity by 2028."
      - epoch_site: OpenAI Stargate Michigan
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.383
        overlap_evidence: "Direct match to Saline Township; MPSC approved 1,383 MW supply contracts."
      - epoch_site: OpenAI Stargate Abilene
        epoch_attributed_to: "Oracle -> OpenAI, Stargate #confident"
        overlap_gw_facility: null
        overlap_evidence: >
          Sep. 2025 language included a potential 600 MW expansion near Abilene.
          March 2026 evidence suggests the adjacent 900 MW campus is Microsoft,
          so the 600 MW Abilene expansion component requires adjudication.
    risks:
      counterparty: "Oracle is central to the 4.5 GW tranche and to OpenAI's cloud RPO, but developers differ by site."
      regulatory: "Michigan MPSC special-contract approval is conditional; New Mexico bond/permit litigation and environmental concerns remain open."
      power_interconnect: "Large-load contracts and site power basis are not consistently public; Michigan has explicit curtailment/load-shed conditions."
      supply_chain: "Oracle buildouts reportedly face labor/material delays; primary Oracle says AI contracts are funded by prepayments/customer-supplied GPUs or financing."
      technology: "Accelerator generation could shift from GB200 to Rubin or other OpenAI-designed silicon across the delivery window."
      financing: "Oracle RPO and financing disclosures do not isolate OpenAI/Stargate, but they are a material overlap surface."
      structural_optionality: "The public 4.5 GW claim can overlap the same named sites already counted in Epoch's Stargate atoms."

  - id: atom:b2_softbank_openai_fast_build_sites
    site: "Lordstown, Ohio and Milam County, Texas"
    operator: "SoftBank / SB Energy / OpenAI"
    user_or_anchor: OpenAI
    gw_facility: 1.5
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2028-12-31, latest: 2029-12-31}
    operational_status: T4
    exact_quote: "can scale to 1.5 gigawatts"
    source_url: https://group.softbank/en/news/press/20250924
    source_publisher: SoftBank Group
    source_publication_date: 2025-09-24
    accessed_date: 2026-04-28
    source_notes:
      - "SoftBank says Lordstown had broken ground and was on track to be operational next year as of Sep. 23/24, 2025."
      - "SoftBank says Milam County will be developed with SB Energy, providing powered infrastructure for a fast-build site."
    epoch_site_overlap_candidates:
      - epoch_site: OpenAI Stargate Milam
        epoch_attributed_to: "SoftBank -> OpenAI, Stargate #confident"
        overlap_gw_facility: 1.200
        overlap_evidence: "Direct match; local Epoch carries 1.200 GW facility by 2028-12-31."
      - epoch_site: OpenAI Stargate Lordstown
        epoch_attributed_to: "SoftBank -> OpenAI, Stargate #confident"
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch has the named Lordstown row but no nonzero capacity atom
          yet; public capacity is only paired with Milam in a combined 1.5 GW
          SoftBank/OpenAI tranche.
    risks:
      counterparty: "SoftBank is a lead Stargate funder but the public site economics and lease/payments to OpenAI are opaque."
      regulatory: "Lordstown is an industrial retrofit/manufacturing/data-center candidate; Milam depends on Texas local and power approvals."
      power_interconnect: "SB Energy powered-infrastructure plan is not yet enough to validate delivered load or facility MW."
      supply_chain: "Fast-build designs still depend on grid equipment, modular data center gear, AI racks, and labor."
      technology: "SoftBank design may use Arm ecosystem assets or NVIDIA systems; site-level chip mix is undisclosed."
      financing: "SoftBank's January financial-responsibility role does not specify how the Lordstown/Milam tranche is funded."
      structural_optionality: "Combined 1.5 GW cannot be allocated between Lordstown and Milam without more evidence."

contradictions:
  - "Launch framing says Stargate is a new company with SoftBank financial responsibility and OpenAI operational responsibility; later site evidence shows Oracle, Crusoe/Blue Owl/Primary Digital, Vantage, Related Digital, SB Energy, and Microsoft-controlled surfaces with different economics."
  - "OpenAI July 2025 says over 5 GW under development with Abilene plus Oracle's 4.5 GW; OpenAI September says nearly 7 GW with five new sites plus Abilene and CoreWeave; OpenAI October Michigan says over 8 GW. These are milestones in one program, not automatically additive."
  - "The September 2025 five-site announcement named one Midwest site later updated to Wisconsin; Michigan was announced separately on October 30, 2025 as part of the Oracle 4.5 GW partnership, creating a site-count mismatch against the phrase 'five new sites.'"
  - "OpenAI September included a potential 600 MW expansion near Abilene; AP/Crusoe March 2026 evidence says an adjacent 900 MW Abilene campus is for Microsoft after OpenAI declined further expansion, while existing OpenAI/Oracle Abilene remains under construction."
  - "Local Epoch treats Abilene operational capacity as 0.200 GW facility after a 2026-04-22 revision, while older public reporting and local timeline rows referenced 0.590 GW or 1.2 GW milestones; use the revision as local context, not final adjudication."
  - "OpenAI community language calls Microsoft Mount Pleasant an AI campus built for OpenAI alongside Stargate campuses, but Microsoft Fairwater is a separate Microsoft AI WAN Epoch surface and should remain a candidate overlap, not folded into Stargate."
gaps:
  - "Definitive Stargate JV capitalization table, debt stack, guarantees, recourse, and site-by-site ownership."
  - "OpenAI payment obligations versus Oracle RPO, including how much of Oracle's $455B/$553B RPO is OpenAI/Stargate-specific."
  - "Site-level facility MW versus IT MW basis for every public GW claim."
  - "Whether the 600 MW Abilene expansion in September 2025 survives separately from the March 2026 Microsoft 900 MW campus."
  - "Allocation of the SoftBank/OpenAI 1.5 GW between Lordstown and Milam."
  - "Primary permits/interconnection filings for Shackelford, Dona Ana, Milam, Lordstown, and Wisconsin sufficient to validate delivered power and timing."
  - "CoreWeave contribution to the September 2025 nearly-7-GW Stargate total and whether it overlaps separate neocloud/CoreWeave atoms."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [OpenAI/SoftBank, "Announcing The Stargate Project"](https://openai.com/index/announcing-the-stargate-project/) | 2025-01-21 | Primary company announcement | $500B/4-year program, $100B immediate deployment, initial equity funders, SoftBank/OpenAI roles, initial technology partners. | "SoftBank having financial responsibility" | 2026-04-28 |
| [OpenAI, "Stargate advances with 4.5 GW partnership with Oracle"](https://openai.com/index/stargate-advances-with-partnership-with-oracle/) | 2025-07-22 | Primary company announcement | Oracle 4.5 GW U.S. Stargate capacity; Abilene parts up and running; first GB200 racks delivered June 2025. | "4.5 gigawatts of additional" | 2026-04-28 |
| [OpenAI, "five new Stargate sites"](https://openai.com/index/five-new-stargate-sites/) | 2025-09-23 | Primary company announcement | Five new U.S. sites, nearly 7 GW planned, over $400B investment, $300B+ Oracle partnership, site list and Wisconsin update. | "nearly 7 gigawatts" | 2026-04-28 |
| [SoftBank Group, five-site Stargate release](https://group.softbank/en/news/press/20250924) | 2025-09-24 | Primary company announcement | Same five-site announcement; SoftBank language for Lordstown/Milam 1.5 GW and Oracle/OpenAI $300B+ partnership. | "can scale to 1.5 gigawatts" | 2026-04-28 |
| [OpenAI, "Expanding Stargate to Michigan"](https://openai.com/index/expanding-stargate-to-michigan/) | 2025-10-30 | Primary company announcement | Saline Township Michigan, more than 1 GW, part of Oracle 4.5 GW partnership, over 8 GW planned capacity. | "over 8 gigawatts" | 2026-04-28 |
| [Crusoe, Abilene flagship live](https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live) | 2025-09-30 | Primary company announcement | First phase live on OCI; construction began June 2024; first two buildings energized; eight-building campus. | "first two buildings were energized" | 2026-04-28 |
| [Crusoe/Blue Owl/Primary Digital Abilene JV](https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture) | 2025-05-21 | Primary company announcement | $15B JV; 1.2 GW; first two buildings 200+ MW; six-building second phase expected mid-2026. | "1.2 gigawatt AI data center" | 2026-04-28 |
| [Mortenson Abilene data center development](https://www.mortenson.com/projects/abilene-data-center-development) | n.d. | Primary contractor project page | 200 MW substation, AEP interconnect, Phase 2 1 GW 345 kV substation, Oct. 2026 estimated completion. | "1GW, 345kV Substation" | 2026-04-28 |
| [Crusoe 900 MW Microsoft Abilene campus](https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure) | 2026-03-27 | Primary company announcement | Adjacent 900 MW Microsoft campus, first building mid-2027, total Abilene projected capacity 2.1 GW. | "support Microsoft AI Infrastructure" | 2026-04-28 |
| [AP, Microsoft takes over Texas AI data center expansion](https://apnews.com/article/ai-stargate-microsoft-openai-crusoe-oracle-f4f74c3a4617d8cfab5b933fc31ccc6e) | 2026-03-27 | Secondary reporting | Reports OpenAI declined further Abilene expansion; Microsoft takes adjacent project; existing OpenAI/Oracle campus remains. | "OpenAI declined to pursue it" | 2026-04-28 |
| [Vantage/Choose Milwaukee Wisconsin Stargate announcement](https://mkeregion.com/news/2025/10/22/press-releases/openai-oracle-and-vantage-data-centers-announce-stargate-data-center-site-in-wisconsin/) | 2025-10-22 | Primary/partner release | Port Washington/Lighthouse, close to 1 GW AI capacity, construction soon, scheduled completion 2028. | "close to a gigawatt" | 2026-04-28 |
| [Related Digital Michigan Stargate announcement](https://www.related-digital.com/news/openai-oracle-and-related-digital-announce-stargate-data-center-site-in-michigan) | 2025-10-30 | Primary/partner release | Saline Township, more than 1 GW, construction expected early 2026, funded by private investors/financial institutions. | "more than a gigawatt" | 2026-04-28 |
| [Michigan Public Service Commission DTE contract approval](https://www.michigan.gov/mpsc/commission/news-releases/2025/12/18/mpsc-approves-dte-electric-energy-contracts-for-data-center) | 2025-12-18 | Government/regulatory | 1,383 MW Saline data center, Green Chile Ventures/Oracle, 19-year minimum term and 80% minimum billing demand. | "1,383- megawatt" | 2026-04-28 |
| [Oracle Q1 FY26 results](https://investor.oracle.com/investor-news/news-details/2025/Oracle-Announces-Fiscal-Year-2026-First-Quarter-Financial-Results/) | 2025-09-09 | Primary financial release | RPO $455B after four multibillion-dollar contracts; OCI revenue growth forecast. | "RPO contract backlog" | 2026-04-28 |
| [Oracle Q3 FY26 results](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Fiscal-Year-2026-Third-Quarter-Financial-Results/default.aspx) | 2026-03-10 | Primary financial release | RPO $553B; AI contracts funded by prepayments/customer-supplied GPUs; $50B financing plan and $30B raised. | "large scale AI contracts" | 2026-04-28 |
| [OpenAI, "Stargate Community"](https://openai.com/index/stargate-community/) | 2026-01-20 | Primary company announcement | Current site-list language across Texas, New Mexico, Wisconsin, Michigan and Microsoft Mount Pleasant mention. | "well beyond halfway" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Local overlap candidates from `epoch_data_centers/compiled.json`, `epoch_data_centers/data_centers.csv`, `epoch_data_centers/data_center_timelines.csv`, and `canonical_capacity_atoms.yaml`; repo snapshot retrieved 2026-04-22, reviewed 2026-04-28. | "OpenAI Stargate Abilene" | 2026-04-28 |

## Research Notes

- Site list as of this dispatch: Abilene TX, Shackelford County TX, Dona Ana County NM, Port Washington WI, Saline Township MI, Milam County TX, Lordstown OH. The Abilene-adjacent Microsoft/Crusoe campus and Microsoft Mount Pleasant/Fairwater are candidate overlaps, not Stargate-US additions in this dispatch.
- GW shape over time: January 2025 launch set the 10 GW/$500B U.S. target; July Oracle deal took Abilene plus 4.5 GW to over 5 GW; September five-site release took the program to nearly 7 GW plus CoreWeave; October Michigan took planned capacity to over 8 GW; January 2026 community page restated the 10 GW by 2029 target.
- Epoch posture: local Epoch already carries most active Stargate site capacity. Summed U.S. Epoch Stargate candidates excluding UAE and excluding Microsoft/Fairwater are 9.233 GW facility before Lordstown's zero-MW row; adding the Microsoft Abilene expansion would be a separate 0.941 GW candidate only.
- Capacity basis: public claims generally say "capacity" or "AI capacity" rather than facility MW. Local Epoch rows are facility MW with PUE 1.16. Do not mix these bases without adjudication.
- Financing structure: public primary sources support (1) SoftBank/OpenAI lead-partner role, (2) Oracle/OpenAI 4.5 GW partnership exceeding $300B over five years, (3) Abilene project finance through Crusoe/Blue Owl/Primary Digital, and (4) Oracle RPO/financing exposure. They do not expose site-level OpenAI take-or-pay terms.
