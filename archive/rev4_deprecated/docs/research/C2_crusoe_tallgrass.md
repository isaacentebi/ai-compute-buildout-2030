# Rev-4.2 Research Dispatch C2: Crusoe / Tallgrass

accessed_date: 2026-04-28

## TL;DR

Crusoe/Tallgrass Cheyenne is a real southeast Wyoming development candidate with primary-source support for a 1.8 GW initial AI data center campus, a design path to 10 GW, local site-plan approval, and a co-located Tallgrass power/gas strategy. It is not yet evidenced as a firm hyperscaler take-or-pay capacity contract in public sources. The best Rev-4.2 treatment is a Cheyenne candidate atom at 1.8 GW facility/site-plan capacity, with the 10 GW language carried only as stretch optionality.

Abilene is different. Crusoe has primary-source support for the original Stargate/Oracle/OpenAI campus, a 1.2 GW existing Abilene buildout, and a new adjacent 900 MW Microsoft campus. Local Epoch already carries `OpenAI Stargate Abilene` at 1.18 GW facility full buildout and `Crusoe Abilene Expansion` at 0.941 GW facility full buildout. Do not adjudicate final tiers or subtraction here, but flag the full 2.121 GW Abilene capacity as an Epoch overlap candidate. Also flag nearby `OpenAI Stargate Shackelford` separately because OpenAI's September 2025 Stargate site announcement names Shackelford County, Texas; it is not the same address as Crusoe's Spinks Road Abilene campus in the local Epoch snapshot.

## Evidence Notes

- Tallgrass' July 24, 2025 company release says Crusoe and Tallgrass announced a strategic partnership to develop a 1.8 GW AI data center campus in southeast Wyoming, "designed to scale up to 10 gigawatts." It also says the campus will use power sources fueled by natural gas and future renewables, with proximity to Tallgrass CO2 sequestration, natural gas, and water assets.
- Laramie County File 26-023 shows the Project Jade site plan and BFC Power / Cheyenne Power Hub site plan were "approved with conditions" on January 6, 2026. The county planning memo says Project Jade is a 600-acre data center site with five data center buildings and two support buildings, while Tallgrass' power project is a 659-acre site with two power-generation facilities.
- The full county site-plan package identifies WY DC 1, LLC, an indirect Crusoe subsidiary, as Project Jade applicant/owner. It says Project Jade is about eight miles south of Cheyenne, west of US-85 and about one mile south of Terry Ranch Road; construction is planned in six continuous phases, with five data center buildings and 40 BESS units.
- The Tallgrass site-plan application identifies Tallgrass Integrated Logistics Solutions as applicant/owner and describes BFC Power / Cheyenne Power Hub as a power cogeneration facility for the planned co-located data center. Major components include a fuel-cell yard, two combined-cycle turbines, temporary aeroderivative/light-duty turbines, and permanent aeroderivative/light-duty simple-cycle turbines.
- DCD's January 8, 2026 report, secondary but consistent with the county record, identifies the site as Project Jade near Terry Ranch Road south of Cheyenne, says Tallgrass will build BFC Power and Cheyenne Power Hub adjacent to the campus, cites a $7B Tallgrass energy-infrastructure investment, and says first data center buildings are hoped to be electrified in 2027.
- Crusoe's March 27, 2026 Abilene/Microsoft release says the new 900 MW site has two buildings plus an on-site power plant, sits adjacent to existing Abilene infrastructure, brings total projected Abilene capacity to approximately 2.1 GW, and expects first building energization in mid-2027.
- Crusoe's same Abilene release discloses the basis tension: the 900 MW power plant is facility/generation language, but each of the two Microsoft buildings is designed for 336 MW of critical IT load, implying 672 MW critical IT for the two buildings before support load / generation reserve treatment.
- Crusoe's September 30, 2025 release says the first phase of Stargate's Abilene campus is live on OCI, construction began in June 2024, the first two buildings were energized within a year, and the planned eight-building campus will support hundreds of thousands of GPUs.
- OpenAI's September 23, 2025 Stargate release says new Oracle sites plus a potential 600 MW expansion near flagship Abilene can deliver over 5.5 GW; by March 2026, AP reported OpenAI chose to put that incremental Abilene expansion capacity in other locations, while Crusoe announced the adjacent Microsoft campus.

```yaml
counterparty: "Crusoe / Tallgrass"
contract_overview:
  type: unknown
  term_years: null
  announced_capex_usd_b: 50
  delivery_window: {earliest: 2027-01-01, central: 2027-12-31, latest: null}
  exclusivity_or_optionality: >
    Cheyenne is publicly evidenced as a Crusoe/Tallgrass strategic partnership,
    approved site plan, and power-campus development. Public sources do not name
    a hyperscaler tenant, lease term, take-or-pay obligation, or RPO. The 10 GW
    language is scale optionality, not firm counted capacity. Abilene has named
    Oracle/OpenAI and Microsoft customer surfaces, but those physical sites are
    already represented in local Epoch candidate rows.
atoms:
  - id: atom:c2_crusoe_tallgrass_cheyenne_project_jade
    site: "Project Jade / Switchgrass Industrial Park, south of Cheyenne, Laramie County, WY"
    operator: "WY DC 1, LLC / Crusoe data center; Tallgrass BFC Power and Cheyenne Power Hub"
    user_or_anchor: "Undisclosed"
    gw_facility: 1.8
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2027-01-01, central: 2027-12-31, latest: null}
    operational_status: T4
    exact_quote: "develop a 1.8 gigawatt (GW) AI data center campus"
    source_url: "https://tallgrass.com/newsroom/press-releases/Crusoe"
    source_publisher: "Tallgrass"
    source_publication_date: 2025-07-24
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local `epoch_data_centers/compiled.json` and `canonical_capacity_atoms.yaml`
          include no Cheyenne/Project Jade row as of the local snapshot reviewed
          2026-04-28. This is a candidate ex-Epoch site unless a newer Epoch
          update has added it.
      - epoch_site: "OpenAI Stargate sites, unspecified future candidates"
        epoch_attributed_to: "Oracle / SoftBank -> OpenAI"
        overlap_gw_facility: null
        overlap_evidence: >
          OpenAI is still evaluating additional Stargate sites, but no primary
          source names Cheyenne/Project Jade as Stargate. Carry only as a
          speculative overlap check, not a site match.
    risks:
      counterparty: "Medium-high: Crusoe and Tallgrass are credible named developers, but no public hyperscaler tenant or take-or-pay contract is disclosed."
      regulatory: "Medium: Laramie County approved site plans with conditions on 2026-01-06; further air, water, generation, pipeline, and construction permits remain execution gates."
      power_interconnect: "High: project depends on behind-the-meter gas/cogeneration, BESS, Tallgrass gas/CO2/water assets, and county/federal/state approvals; 10 GW stretch would need power beyond the initial plant."
      supply_chain: "High: multi-GW gas turbines/fuel cells, transformers, switchgear, liquid-cooling equipment, and AI racks face constrained delivery windows."
      technology: "Medium: public sources do not identify chip stack, rack density, or critical IT load for Cheyenne."
      financing: "High: DCD reports $7B Tallgrass energy infrastructure and up to $50B total project cost; no public project-finance close or anchor lease has been found."
      structural_optionality: "High: 1.8 GW is a site-plan/development target; 10 GW is explicitly scale-up optionality."

  - id: atom:c2_crusoe_tallgrass_cheyenne_stretch_to_10gw
    site: "Project Jade stretch beyond initial 1.8 GW"
    operator: "Crusoe / Tallgrass"
    user_or_anchor: "Undisclosed"
    gw_facility: 8.2
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: null, central: null, latest: null}
    operational_status: T5
    exact_quote: "Designed to scale up to 10 gigawatts"
    source_url: "https://tallgrass.com/newsroom/press-releases/Crusoe"
    source_publisher: "Tallgrass"
    source_publication_date: 2025-07-24
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "No local Epoch Cheyenne/Project Jade row found; stretch is below firm-count threshold absent additional permits, power, tenant, and financing evidence."
    risks:
      counterparty: "High: no tenant or commercial obligation found for the stretch."
      regulatory: "High: county-approved materials support the initial Project Jade/BFC scope, not a fully evidenced 10 GW buildout."
      power_interconnect: "Very high: DCD reports the on-site station will only generate 2.7 GW, so a 10 GW campus would need other power sources."
      supply_chain: "Very high: 8.2 GW incremental capacity would require enormous electrical, thermal, and compute supply."
      technology: "High: future rack density and architecture could materially alter GW-to-compute translation."
      financing: "Very high: no public financing package for the stretch has been found."
      structural_optionality: "Very high: this is expansion language, not a firm capacity commitment."

  - id: atom:c2_crusoe_abilene_stargate_epoch_overlap
    site: "Crusoe / Oracle / OpenAI Stargate Abilene, 5502 Spinks Rd, Abilene, TX"
    operator: "Crusoe developer; Oracle Cloud Infrastructure operator"
    user_or_anchor: OpenAI
    gw_facility: 1.18
    gw_it: 1.017
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2025-06-28, central: 2026-07-01, latest: 2026-12-31}
    operational_status: T2
    exact_quote: "first phase of Stargate's flagship data center campus"
    source_url: "https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live"
    source_publisher: "Crusoe"
    source_publication_date: 2025-09-30
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate Abilene"
        epoch_attributed_to: "Oracle -> OpenAI"
        overlap_gw_facility: 1.18
        overlap_evidence: >
          Local Epoch snapshot shows 200 MW current facility power and 1.180 GW
          full buildout by 2026-07-01 at 5502 Spinks Rd, Abilene, TX.
    risks:
      counterparty: "Medium: Oracle/OpenAI/Crusoe remain named, but March 2026 reporting separated the main 1.2 GW campus from the abandoned additional expansion."
      regulatory: "Medium: existing construction and operations reduce risk, but local tax, water, emissions, and community impacts remain active."
      power_interconnect: "Medium-high: Crusoe says Abilene primarily connects to ERCOT and uses GE Vernova gas turbines for backup/grid stability; AP cites a 350 MW existing gas plant."
      supply_chain: "Medium: first two buildings live; remaining six buildings still depend on rack, cooling, electrical, and commissioning schedule."
      technology: "Medium: OpenAI/Oracle Blackwell-era deployment may change as new accelerator generations arrive."
      financing: "Medium: the 1.2 GW campus has reported $15B JV/development financing, but Oracle/OpenAI expansion negotiations show financing sensitivity."
      structural_optionality: "Medium: main Stargate I is live/under construction; further Abilene expansion was optional and shifted away."

  - id: atom:c2_crusoe_abilene_microsoft_epoch_overlap
    site: "Crusoe Abilene Microsoft campus, adjacent to 5502 Spinks Rd, Abilene, TX"
    operator: Crusoe
    user_or_anchor: Microsoft
    gw_facility: 0.941
    gw_it: 0.672
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2027-06-01, central: 2027-09-17, latest: 2027-11-11}
    operational_status: T2
    exact_quote: "900 MW site includes two new buildings"
    source_url: "https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure"
    source_publisher: "Crusoe"
    source_publication_date: 2026-03-27
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Crusoe Abilene Expansion"
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Local Epoch snapshot shows `Crusoe Abilene Expansion` at 0 MW
          current and 0.941 GW full facility buildout by 2027-11-11. The local
          row's Microsoft owner/user and address match Crusoe's March 2026
          Microsoft expansion announcement.
      - epoch_site: "OpenAI Stargate Abilene"
        epoch_attributed_to: "Oracle -> OpenAI"
        overlap_gw_facility: null
        overlap_evidence: >
          Same broader Abilene tract and adjacent campus, but separate named
          Microsoft buildings and on-site power plant. Flag for physical-campus
          dedupe only; do not merge with the OpenAI/Oracle row here.
    risks:
      counterparty: "Low-medium: Microsoft is named in Crusoe's primary release and quoted, but public lease term/RPO details are not disclosed."
      regulatory: "Medium: land clearing and site preparation are underway; local permitting and plant approvals remain delivery gates."
      power_interconnect: "Medium-high: 900 MW on-site power plant plus MV BESS is planned; first building not expected until mid-2027."
      supply_chain: "High: two 336 MW critical-IT buildings require very high-density power, cooling, and accelerator supply."
      technology: "Medium: designed for next-generation GPU architectures; exact silicon not disclosed."
      financing: "Medium-high: AP/Bloomberg context suggests this capacity followed OpenAI/Oracle expansion changes; no dedicated Microsoft project-finance close found."
      structural_optionality: "Medium: named Microsoft support is stronger than Cheyenne, but basis differs between 900 MW generation/site capacity and 672 MW critical IT."

  - id: atom:c2_openai_stargate_shackelford_regional_overlap_candidate
    site: "OpenAI Stargate Shackelford, 175 Private Road 1604, Abilene, Shackelford County, TX"
    operator: Oracle
    user_or_anchor: OpenAI
    gw_facility: 1.96
    gw_it: 1.69
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2027-01-01, central: 2028-12-31, latest: 2028-12-31}
    operational_status: T2
    exact_quote: "located in Shackelford County, Texas"
    source_url: "https://openai.com/index/five-new-stargate-sites/"
    source_publisher: "OpenAI"
    source_publication_date: 2025-09-23
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate Shackelford"
        epoch_attributed_to: "Oracle -> OpenAI"
        overlap_gw_facility: 1.96
        overlap_evidence: >
          Local Epoch snapshot has a separate Stargate Shackelford row at 175
          Private Road 1604, Abilene, Shackelford County, with 1.960 GW full
          buildout by 2028-12-31. It is a regional Stargate/Abilene-area
          overlap candidate, not the same address as Crusoe's 5502 Spinks Rd
          Abilene campus.
    risks:
      counterparty: "Medium: OpenAI/Oracle are named at portfolio level; local operator detail comes from Epoch."
      regulatory: "Medium-high: separate county/site approvals need primary extraction."
      power_interconnect: "High: 1.96 GW local Epoch buildout implies large power procurement not resolved in this dispatch."
      supply_chain: "High: large Stargate site with multi-year completion risk."
      technology: "Medium: OpenAI/Oracle chip mix may shift over the 2027-2028 buildout."
      financing: "Medium-high: Oracle/OpenAI broader 4.5 GW partnership is large and financing-intensive."
      structural_optionality: "Medium: OpenAI names Shackelford as a new site, but this dispatch does not adjudicate the site-specific firm tier."
contradictions:
  - "Cheyenne primary release supports 1.8 GW and scale to 10 GW; county/DCD materials describe a 2.7 GW adjacent power project. The 10 GW data-center stretch is not matched by the initial on-site generation scope."
  - "Crusoe's Abilene Microsoft announcement says 900 MW site capacity and 900 MW on-site power, while the same release says the two buildings are designed for 336 MW of critical IT load each. Treat 900 MW as facility/generation capacity and 672 MW as disclosed critical IT, not interchangeable units."
  - "OpenAI's September 2025 release described a potential 600 MW expansion near Abilene; AP reported on 2026-03-27 that OpenAI chose to put that additional capacity elsewhere, while Crusoe announced a 900 MW adjacent Microsoft campus."
  - "Local `canonical_capacity_atoms.yaml` has an existing `crusoe_cheyenne_or_other_future_capacity` atom at 1.98 GW contracted capacity. This dispatch does not edit/adjudicate that row; it flags that public Cheyenne evidence supports 1.8 GW site-plan capacity plus optional stretch, while the extra 0.18 GW appears to be residual/ex-Epoch accounting rather than a named Cheyenne primary-source increment."
gaps:
  - "Pull full Laramie County Project Jade and BFC Power/Cheyenne Power Hub site-plan sheets into a structured table: building count, square footage, generation units, phasing, conditions of approval, and water/emissions assumptions."
  - "Find primary air permit, water permit, and any Wyoming PSC/FERC interconnect or pipeline filings for BFC Power and Cheyenne Power Hub."
  - "Confirm whether any hyperscaler tenant, lease term, take-or-pay, or project-finance close has been publicly filed for Cheyenne."
  - "Resolve Cheyenne capacity basis: 1.8 GW appears to be data-center campus/facility capacity; county materials found so far do not disclose critical IT MW."
  - "For Abilene, reconcile Crusoe's 2.1 GW public site total, Epoch's 1.180 + 0.941 = 2.121 GW facility buildout, and the Microsoft 672 MW critical-IT disclosure."
  - "Check whether the local Epoch `OpenAI Stargate Shackelford` row should be grouped with Abilene-area Stargate discussions or kept fully separate by address/county."
```

## Source Pointers

- Tallgrass / Crusoe Cheyenne announcement: https://tallgrass.com/newsroom/press-releases/Crusoe
- Laramie County File 26-023, Project Jade / BFC Power site-plan approval: https://laramiecounty.legistar.com/LegislationDetail.aspx?GUID=1623FD5B-974F-4551-9E2F-53A415151CCE&ID=7792288
- Laramie County planning memo attachment: https://laramiecounty.legistar.com/View.ashx?GUID=0946D063-8DEE-42DD-B75C-867B3A63027D&ID=15061112&M=F
- Laramie County Tall Grass/Crusoe press release: https://www.laramiecountywy.gov/files/sharedassets/public/v/1/county/press-release/tall-grasscrusoe-energy-and-data-center-project-in-southern-laramie-county.pdf
- DCD Cheyenne approval report: https://www.datacenterdynamics.com/en/news/crusoe-gets-go-ahead-for-18gw-data-center-campus-and-power-plant-in-cheyenne-wyoming/
- Crusoe Abilene Microsoft 900 MW announcement: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- Crusoe Abilene Stargate live announcement: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
- OpenAI Stargate five-site announcement: https://openai.com/index/five-new-stargate-sites/
- OpenAI Oracle 4.5 GW Stargate partnership: https://openai.com/index/stargate-advances-with-partnership-with-oracle/
- AP on Microsoft taking over Abilene expansion after OpenAI backed away: https://apnews.com/article/ai-stargate-microsoft-openai-crusoe-oracle-f4f74c3a4617d8cfab5b933fc31ccc6e
- GE Vernova / Crusoe 29 gas turbine package announcement: https://www.crusoe.ai/resources/newsroom/ge-vernova-and-crusoe-announce-major-29-unit-gas-turbine-deal
- Kirkland on Blue Owl / Crusoe $15B Abilene JV financing: https://www.kirkland.com/news/press-release/2025/05/kirkland-advises-blue-owl-on-data-center-development
- Local Epoch context reviewed: `epoch_data_centers/compiled.json`, `epoch_data_centers/report.txt`, `canonical_capacity_atoms.yaml`, and `neocloud_overlay.yaml` from this repo snapshot.
