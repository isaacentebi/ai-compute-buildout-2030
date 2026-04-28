# Rev-4.2 Research Dispatch D3: UK Culham AI Growth Zone

accessed_date: 2026-04-28

## TL;DR

Primary sources do not support 300 MW as a source-stated Culham figure. The canonical public formulation is an initial 100 MW AI data centre at UKAEA's Culham Campus, with plans/aspirations to scale to 500 MW. The repo's current `uk_culham_ai_growth_zone` atom carries 250 MW IT / 300 MW facility, with a 100-500 MW IT range; that should be treated as an internal analyst central case, not as the official project size.

Tier candidates: the first 100 MW is the strongest candidate, likely T4 because UK Government/UKAEA have designated the site, UKAEA has run an investment-partner EOI, and UKAEA states spare dual-resilient power for roughly 100 MW. It is not T3 because no signed private partner, anchor tenant, term, RPO/take-or-pay contract, or binding customer allocation was found. The 500 MW maximum is a T5 stretch candidate until there is a named partner, planning consent, allocated land envelope, grid/interconnect schedule, and customer/sovereign-use split. Local canonical T5 treatment for the 300 MW central row is therefore directionally conservative.

Sovereign stretch annex treatment remains appropriate. Culham is domestic UK sovereign/public compute infrastructure, framed around UKAEA, fusion R&D, AI Research Resource/public-sector capacity, and the UK's sovereign AI/compute strategy. It should not enter the Western denominator unless adjudication changes the scope policy. There is no local Epoch site overlap found; this is a repo-side sovereign sidebar atom rather than an upstream Epoch frontier data-centre row.

## Evidence Notes

- The January 2025 government response says Culham is the first AI Growth Zone, subject to a public-private partnership, with a private-sector partner sought to build a large AI data centre "beginning with 100MW" and scaling to 500 MW.
- The February 2025 AI Growth Zone press release generalizes the programme target: government will work with network operators to scale each zone to 500MW+, and sites should have 500+ MW existing capacity or a credible plan to get there. This is programme/site-readiness language, not proof of a 500 MW Culham contract.
- UKAEA's Culham EOI says the first released plot has 132 kV and 400 kV grid connections with approximately 100 MW of steady-state, dual-resilient power available for a mission-led AI data centre. It also says UKAEA is exploring larger acreage to permit proposals above 100 MW, potentially up to 500 MW.
- UKAEA's strategic investment materials say the broader campus has 600 MW peak capacity when combining National Grid and SSE infrastructure. That is not the same as committed data-centre load.
- A South Oxfordshire procurement notice says a 100 MW data centre is being developed, with aspirations up to 500 MW longer term, but explicitly says completion timing is uncertain and subject to planning permission; it cites an ambitious April 2028 completion date.
- Sunrise, the 1.4 MW fusion AI supercomputer announced in March 2026, is a first step for the AI Growth Zone but should not be counted as the 100 MW data centre tranche.
- No source reviewed names a hyperscaler, frontier lab, neocloud, data-centre operator, contract value, lease term, or anchor tenant for the Culham 100/500 MW project. UKAEA is still framed as seeking a long-term strategic investment partner.

```yaml
counterparty: "UK Government / UKAEA / TBD strategic investment partner"
contract_overview:
  type: unknown
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2028-04-01, central: null, latest: 2030-12-31}
  exclusivity_or_optionality: "Official sources describe a public-private partnership and partner-selection process, not an executed offtake. Primary figures are 100 MW initial capacity and up to 500 MW scale target; the repo's 300 MW facility point is an internal central estimate."
atoms:
  - id: atom:d3_uk_culham_initial_100mw_candidate
    site: "Culham Campus, Oxfordshire, United Kingdom"
    operator: "TBD strategic investment partner; UKAEA sponsor/landlord"
    user_or_anchor: "UKAEA fusion/R&D allocation; public sector/sovereign compute; commercial users TBD"
    gw_facility: 0.100
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2028-04-01, central: null, latest: 2030-12-31}
    operational_status: T4
    exact_quote: "100MW of steady state"
    source_url: "https://culham.org.uk/invest-at-culham-campus/expression-of-interest/"
    source_publisher: "UKAEA / Culham Campus"
    source_publication_date: 2025-08-12
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "Local searches of `epoch_data_centers` and repo Epoch context found no Culham/UKAEA/Culham Campus data-centre row."
      - epoch_site: "repo atom: uk_culham_ai_growth_zone"
        epoch_attributed_to: "UK Government / UKAEA"
        overlap_gw_facility: 0.300
        overlap_evidence: "Local canonical atom carries 250 MW IT / 300 MW facility, T5, sovereign, excluded from Western raw and probability-weighted totals."
    risks:
      counterparty: "High: strategic investment partner, operator, and anchor tenant are not named in reviewed primary sources."
      regulatory: "Medium-high: project remains subject to planning permission; local development order and adjacent No. 1 site planning issues remain live."
      power_interconnect: "Medium: UKAEA identifies 132 kV/400 kV access and roughly 100 MW spare steady-state dual-resilient power, but no executed interconnection or energization milestone was found."
      supply_chain: "Medium: no public GPU, server, cooling, or EPC procurement for the 100 MW facility was found; Sunrise suppliers are for a separate 1.4 MW supercomputer."
      technology: "Medium: official MW basis is not cleanly IT versus facility; NESO notes market confusion when MW figures omit cooling/non-IT loads."
      financing: "High: no capex, lease economics, debt/equity stack, or government support package was found."
      structural_optionality: "Medium-high: 100 MW is a designated initial opportunity, but still dependent on partner selection, planning, and final proposal parameters."

  - id: atom:d3_uk_culham_500mw_stretch_candidate
    site: "Culham Campus and potential adjacent Culham development land, Oxfordshire, United Kingdom"
    operator: "TBD strategic investment partner; UKAEA / DSIT policy support"
    user_or_anchor: "UK sovereign/public-sector compute and commercial AI users TBD"
    gw_facility: 0.500
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: null, central: 2030-12-31, latest: null}
    operational_status: T5
    exact_quote: "scale up to 500MW"
    source_url: "https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response/ai-opportunities-action-plan-government-response"
    source_publisher: "UK Government / DSIT"
    source_publication_date: 2025-01-13
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "No Culham, UKAEA, or AI Growth Zone site appears in local Epoch data-center files."
      - epoch_site: "repo atom: uk_culham_ai_growth_zone"
        epoch_attributed_to: "UK Government / UKAEA"
        overlap_gw_facility: 0.300
        overlap_evidence: "The repo central point is below the official 500 MW maximum and appears to be an analyst central case, not a source-stated capacity."
    risks:
      counterparty: "High: no private developer, operator, hyperscaler, or AI-lab anchor has been announced for the 500 MW scale-out."
      regulatory: "High: 500 MW depends on final development parameters, planning route, local land allocation, environmental review, and community/local-benefit commitments."
      power_interconnect: "High: programme criteria expect at least 500 MW by 2030, but Culham-specific available spare power is stated at roughly 100 MW initially; scale-up requires further grid/network arrangements."
      supply_chain: "High: no 500 MW equipment procurement, construction contract, or GPU allocation was found."
      technology: "Medium-high: official sources use capacity/power language without identifying IT load, facility load, PUE, redundancy topology, or usable AI accelerator power."
      financing: "High: the 500 MW case is an aspiration/plan with no public project-finance package."
      structural_optionality: "High: UKAEA says proposals could be above 100 MW and potentially up to 500 MW, depending on expanded acreage and final parameters."

  - id: atom:d3_uk_culham_repo_300mw_central_flag
    site: "Culham AI Growth Zone, Oxfordshire, United Kingdom"
    operator: "UK Government / UKAEA"
    user_or_anchor: "UK sovereign + TBD tenant"
    gw_facility: 0.300
    gw_it: 0.250
    basis: IT_MW
    pue_assumed: 1.2
    energization_window: {earliest: null, central: null, latest: null}
    operational_status: T5
    exact_quote: "UK sovereign AI Growth Zone"
    source_url: "file:///Users/isaacentebi/Desktop/ai-compute-buildout-2030/canonical_capacity_atoms.yaml"
    source_publisher: "Local canonical_capacity_atoms.yaml"
    source_publication_date: 2026-04-27
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "Local Epoch searches found no Culham site; this atom is a repo sovereign sidebar row."
    risks:
      counterparty: "High: local atom uses TBD tenant; web research found no named anchor."
      regulatory: "High: source-stated capacity remains subject to PPP agreement and planning."
      power_interconnect: "Medium-high: 300 MW central exceeds UKAEA's initially available 100 MW spare power and is below the 500 MW policy scale target."
      supply_chain: "High: no supply-chain evidence specific to 300 MW was found."
      technology: "High: 250 MW IT / 300 MW facility is an analyst conversion, not a primary-source capacity basis."
      financing: "High: no financing evidence specific to 300 MW was found."
      structural_optionality: "High: keep as a central scenario flag only unless adjudication chooses a different canonical row."
contradictions:
  - "Primary sources repeatedly state 100 MW initial capacity and scale/aspiration up to 500 MW; no reviewed primary source states 300 MW for Culham."
  - "Local canonical data carries 250 MW IT / 300 MW facility with a 100-500 MW IT range; that is internally coherent as a central estimate but not source-canonical."
  - "UKAEA's EOI says roughly 100 MW available spare steady-state dual-resilient power for the first opportunity; UKAEA's strategic investor PDF says the campus has 600 MW peak capacity combining National Grid and SSE infrastructure. These are different power concepts."
  - "Find a Tender says a 100 MW data centre is being developed and suggests an ambitious April 2028 completion date, but also says timing is uncertain and subject to planning permission."
  - "Sunrise is a 1.4 MW supercomputer and a first step for the Culham AI Growth Zone; it should not be conflated with the 100 MW or 500 MW data-centre project."
gaps:
  - "Name of the strategic investment partner, data-centre operator, cloud provider, hyperscaler, AI-lab tenant, or public-sector anchor."
  - "Executed PPP, lease, concession, power-purchase, or take-or-pay terms."
  - "Whether official MW figures are IT load, facility load, grid import capacity, or another basis; PUE and redundancy assumptions."
  - "Planning application/consent for the AI data centre itself, final land acreage, and status of the Local Development Order."
  - "Culham-specific National Grid/NESO connection milestones for scaling beyond the initial roughly 100 MW."
  - "Whether the 500 MW scale target should replace the repo's 300 MW central point, or be carried only as high/stretch while preserving 300 MW as an analyst midpoint."
```

## Sovereign Treatment

Keep Culham in the sovereign stretch annex pending adjudication. The core evidence is policy-led and UK sovereign-capability-led:

- The AI Opportunities Action Plan frames AI Growth Zones as a way to crowd in private capital for domestic compute and strategic partnerships.
- The government response says the Culham pilot would deliver "secure, dedicated public sector computing capacity."
- The UK Compute Roadmap says AI Growth Zones strengthen UK security and resilience and are part of sovereign, secure, sustainable capability.
- UKAEA says up to 20 MW, or equivalent services, would be available on demand for fusion and broader R&D research.
- Local canonical data already marks `uk_culham_ai_growth_zone` as `scope: sovereign`, `included_raw_horizon: false`, and `included_probability_weighted: false`.

This is not a Western-denominator hyperscaler row because there is no named Western operator/user capacity commitment, and the project is explicitly designed as a UK sovereign/public-private campus.

## 300 MW vs 500 MW Treatment

Use the following as candidate treatment, not final adjudication:

| Figure | Evidence status | Candidate use |
|---:|---|---|
| 100 MW | Directly supported by UK Government/UKAEA/local procurement sources as the initial facility/opportunity. | Candidate T4 initial Culham atom. |
| 300 MW facility / 250 MW IT | Local repo central estimate only; not found in primary sources. | Candidate internal central scenario, preserve as a flag until adjudication decides whether to revise. |
| 500 MW | Directly supported as the official scale-up target/maximum/aspiration, not as a contracted build. | Candidate T5 stretch/high case, not central unless adjudication changes the convention. |
| 600 MW peak campus power | UKAEA strategic investor material, campus-level combined power infrastructure. | Do not treat as AI data-centre capacity without allocation evidence. |
| 1.4 MW Sunrise | Government-funded fusion AI supercomputer, targeted for June 2026 operation. | Separate public-compute first step; not part of the 100/500 MW data-centre capacity count. |

## Tier Evidence Candidates

| Candidate row | Evidence | Candidate tier note |
|---|---|---|
| Culham initial 100 MW | Government designation, UKAEA EOI, initial available dual-resilient power, heat-network tender saying 100 MW is being developed. | T4 candidate. Strong site-level plan, but not T3 because no partner/tenant/contract economics. |
| Culham full 500 MW scale-out | Government response, AI Growth Zone programme criteria, UKAEA maximum proposal language. | T5 candidate until partner, planning, grid and customer allocation evidence exists. |
| Local 300 MW facility central | Repo atom only; derived from 250 MW IT and PUE 1.2, within the 100-500 MW band. | Keep as a flagged central scenario, not primary-source canonical. |

## Source Pointers

| Source | Date | Type | Use | Accessed |
|---|---:|---|---|---:|
| [UK Government, AI Opportunities Action Plan government response](https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response/ai-opportunities-action-plan-government-response) | 2025-01-13 | Primary government | Culham first AIGZ; PPP condition; 100 MW initial and 500 MW scale plan; secure public-sector compute framing. | 2026-04-28 |
| [UK Government, "Government fires starting gun on AI Growth Zones"](https://www.gov.uk/government/news/government-fires-starting-gun-on-ai-growth-zones-to-turbocharge-plan-for-change) | 2025-02-10 | Primary government | Programme-level 500MW+ scale target; 500+ MW site-readiness criterion; Culham as testing ground. | 2026-04-28 |
| [UKAEA / Culham Campus, Invitation to Express Interest](https://culham.org.uk/invest-at-culham-campus/expression-of-interest/) | 2025-08-12 | Primary UKAEA/Culham | Partner process; first plot; 132 kV/400 kV connections; roughly 100 MW initial; possible up to 500 MW; up to 20 MW R&D availability. | 2026-04-28 |
| [UKAEA / Culham Campus, Strategic Investment Partner Opportunity](https://culham.org.uk/wp-content/uploads/downloads/Strategic_Investment_Partner_Opportunity.pdf) | 2025 | Primary UKAEA/Culham | 600 MW peak campus power context; National Grid/SSE infrastructure; strategic investor framing; Local Development Order. | 2026-04-28 |
| [South Oxfordshire District Council, Find a Tender heat-network feasibility notice](https://www.find-tender.service.gov.uk/Notice/074444-2025) | 2025-11-17 | Primary local procurement | 100 MW being developed; aspirations up to 500 MW; timing uncertain; ambitious April 2028 date; planning-permission caveat. | 2026-04-28 |
| [South Oxfordshire/Vale of White Horse, Statement of Common Ground for land adjacent to Culham Campus](https://www.southandvale.gov.uk/app/uploads/2026/04/LPA50-AS2-Statement-of-Common-Ground-for-Land-adjacent-to-Culham-Campus.pdf) | 2026-03 | Local planning document | Repeats 100 MW initial / 500 MW scale language; adjacent land/planning context and No. 1 site application. | 2026-04-28 |
| [UK Government, UK Compute Roadmap](https://www.gov.uk/government/publications/uk-compute-roadmap/uk-compute-roadmap) | 2025-07, updated 2026-04-23 | Primary government | 6 GW UK AI-capable capacity by 2030; each AIGZ at least 500 MW by 2030; sovereign/secure framing. | 2026-04-28 |
| [UK Government, Delivering AI Growth Zones](https://www.gov.uk/government/publications/delivering-ai-growth-zones/delivering-ai-growth-zones) | 2025-11-13 | Primary government | Grid/planning reform; 500 MW data-centre cost example; AIGZ Delivery Unit and investment environment. | 2026-04-28 |
| [National Grid DSO / Regen, Data Centre Impact Study](https://dso.nationalgrid.co.uk/downloads/15083/data-centre-impact-study2.pdf) | 2025-11 | Grid/distribution study | 500 MW by 2030 criterion; Culham 100 to 500 MW summary; grid/network implications. | 2026-04-28 |
| [NESO, Options for optimising GB Data Centres](https://www.neso.energy/about/innovation/our-innovation-projects/options-optimising-gb-data-centres) | 2025-07 close-down | System operator research | Data-centre forecast use in FES/SSEP; warns that quoted MW may be IT power and exclude cooling/non-IT loads. | 2026-04-28 |
| [UK Government / UKAEA, Sunrise supercomputer announcement](https://www.gov.uk/government/news/45m-for-uks-first-ai-supercomputer-to-accelerate-fusion-energy) | 2026-03-16 | Primary government | Separate 1.4 MW fusion AI supercomputer; first step for Culham AIGZ, not 100/500 MW data-centre evidence. | 2026-04-28 |
| Local context: `canonical_capacity_atoms.yaml`, `row_level_audit.csv`, `source_claim_map.csv` | 2026-04-27 local repo | Local atom context | Current row is 250 MW IT / 300 MW facility, T5, sovereign, excluded from Western totals; no local Epoch site overlap found. | 2026-04-28 |
