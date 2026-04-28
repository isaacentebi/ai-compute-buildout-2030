# Reliance Jio

## TL;DR

This Rev-4.2 contract drilldown is generated from the research dispatch pending final adjudication into atoms, dedupe, and row deltas.

## Research Source

- `docs/research/D1_reliance_jio.md`

## Dispatch Content

# Rev-4.2 Research Dispatch D1: Reliance-Jio / Jamnagar / Andhra India AI Capacity

accessed_date: 2026-04-28

## TL;DR

Reliance/Jio should remain in the sovereign/India AI sidebar, not the Western denominator. The evidence has strengthened since the stale canonical row: Reliance's 2025 AGM transcript says work has already begun on gigawatt-scale AI-ready data centers in Jamnagar, and 2026 India AI Impact Summit reporting attributes to Mukesh Ambani a first Jamnagar tranche of more than 120 MW coming online in H2 2026. That near-term >120 MW tranche is the best candidate for an evidenced row, but its public basis is still not clean: the 120 MW figure is reported by media from the summit rather than found in an RIL filing, and sources do not state facility load versus IT load.

The existing 1 GW Jamnagar atom is still better treated as a stretch candidate. Reliance's own wording is "gigawatt scale" or "multi-gigawatt", with phased delivery aligned to Indian demand, not a public 1 GW commissioning contract. Andhra adds a second Reliance-linked India AI capacity candidate: a 1 GW AI data center MoU announced with the Andhra Pradesh government in November 2025, plus a separate Digital Connexion/Reliance-Brookfield-Digital Realty 1 GW Visakhapatnam campus announced for 2030. These may be the same AP capacity, adjacent program capacity, or overlapping Reliance-related disclosures; this dispatch flags them for adjudication rather than deduping them.

No local Epoch Reliance/Jamnagar or Andhra Reliance row was found in the 2026-04-20 / retrieved 2026-04-22 Epoch snapshot. Local canonical currently has only `reliance_jio_jamnagar` at 1.000 GW facility, T5, sovereign, secondary-only, no Epoch overlap.

## Evidence Notes

- RIL's 47th AGM presentation says it is building large-scale AI infrastructure and names "Gigawatt scale AI ready Data Centers in Jamnagar powered by green energy."
- RIL's 48th AGM transcript creates stronger status evidence: Reliance Intelligence will build gigawatt-scale AI-ready data centers and "work has already begun" at Jamnagar.
- Google CEO Sundar Pichai's RIL AGM remarks say Google and Reliance are establishing a Jamnagar cloud region dedicated to Reliance, powered by clean energy and connected by Jio's network. This supports the Jamnagar cloud/AI use case, but not a MW quantum.
- TechCrunch and ETTelecom report from the February 19, 2026 India AI Impact Summit that Reliance/Jio will invest about Rs 10 lakh crore / $110 billion over seven years, with multi-gigawatt Jamnagar construction underway and more than 120 MW expected online in H2 2026. Treat this as credible secondary reporting of a public speech until an official transcript is pulled.
- RIL's July 2025 investor presentation says Reliance has begun execution of Kutch generation projects and is setting up a dedicated transmission line from Kutch to Jamnagar. This is useful for power-readiness context, not an AI data-center interconnect filing.
- Andhra Pradesh evidence is MoU-level. Business Standard/IBEF report Reliance signed a 1 GW AI data center deal with AP on November 14, 2025, backed by a 6 GWp solar project and described as a twin to Jamnagar.
- Digital Connexion evidence appears to be a separate November 26, 2025 company-statement/MoU surface: $11 billion by 2030 for 1 GW of AI-native purpose-built data centers over 400 acres in Visakhapatnam. Because Digital Connexion is a Reliance/Brookfield/Digital Realty JV, this is an overlap candidate with the AP Reliance 1 GW MoU.
- IndiaAI common compute is material sovereign-AI context but not a MW data-center atom. PIB says the common compute facility has 18,693 GPUs, about 10,000 initially available, with Jio Platforms one of ten eligible bidders.

```yaml
counterparty: "Reliance Industries / Jio Platforms / Reliance Intelligence / Digital Connexion"
contract_overview:
  type: unknown
  term_years: null
  announced_capex_usd_b: 110
  delivery_window: {earliest: 2026-07-01, central: 2026-12-31, latest: 2030-12-31}
  exclusivity_or_optionality: >
    Reliance/Jio announced a seven-year India AI infrastructure plan and
    Jamnagar data centers delivered in phases. Public sources disclose no
    take-or-pay tenant, lease term, utility interconnection agreement, or
    facility-vs-IT basis. Andhra 1 GW evidence is MoU / JV-campus disclosure
    and may overlap with the Reliance AP announcement.
atoms:
  - id: atom:d1_reliance_jio_jamnagar_phase1_120mw_candidate
    site: "Jamnagar, Gujarat, India"
    operator: "Reliance Intelligence / Jio / Reliance Industries"
    user_or_anchor: "Reliance, Jio, Indian enterprise and sovereign-AI users; Google Cloud partnership for Reliance cloud region"
    gw_facility: [0.120, 0.120, 0.180]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-07-01, central: 2026-12-31, latest: 2027-06-30}
    operational_status: T2
    exact_quote: "Over 120 MW will come online"
    source_url: "https://telecom.economictimes.indiatimes.com/news/industry/reliance-and-jio-to-invest-10-lakh-crore-in-ai-infrastructure-by-2033/128545747"
    source_publisher: "ETTelecom"
    source_publication_date: 2026-02-19
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "Local Epoch `epoch_data_centers/report.txt`, `epoch_data_centers/compiled.json`, and `canonical_capacity_atoms.yaml` have no Reliance/Jio/Jamnagar site row as of the 2026-04-20 / retrieved 2026-04-22 snapshot."
    risks:
      counterparty: "Medium: Reliance/Jio is a large balance-sheet counterparty, but public customer/offtake economics are not disclosed."
      regulatory: "Medium: India sovereign compute and data-localization policy support the program, but cloud/data-center incentives and lawful-access requirements can affect tenant mix."
      power_interconnect: "Medium-high: RIL discloses Kutch generation and a dedicated Kutch-Jamnagar transmission line, but no AI data-center grid-connection filing was found."
      supply_chain: "High: no public chip vendor, server OEM, liquid-cooling, transformer, or switchgear order was found for the 120 MW tranche."
      technology: "Medium-high: the MW basis is ambiguous; sources do not state critical IT load, facility load, rack density, or accelerator generation."
      financing: "Medium: Rs 10 lakh crore is a seven-year group-level plan, not a project-finance close for Jamnagar."
      structural_optionality: "Medium: company says construction has begun and names H2 2026, but the public schedule is not tied to a permitting/interconnect milestone."

  - id: atom:d1_reliance_jio_jamnagar_1gw_stretch_candidate
    site: "Jamnagar, Gujarat, India"
    operator: "Reliance Intelligence / Jio / Reliance Industries"
    user_or_anchor: "Reliance-owned demand; Indian enterprise and sovereign-AI users"
    gw_facility: 1.0
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-07-01, central: null, latest: null}
    operational_status: T5
    exact_quote: "gigawatt-scale AI-ready data centers"
    source_url: "https://rilstaticasset.akamaized.net/sites/default/files/2025-09/RIL-48th-AGM-Transcripts_2025.pdf"
    source_publisher: "Reliance Industries Limited"
    source_publication_date: 2025-08-29
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "No Jamnagar/Reliance row appears in local Epoch context; canonical currently carries `reliance_jio_jamnagar` as a non-Epoch sovereign T5 row."
    risks:
      counterparty: "Medium: Reliance is credible, but the AI infrastructure entity, Reliance Intelligence, is newly announced and project-level obligations are opaque."
      regulatory: "Medium: sovereign AI policy is supportive, while data residency, cloud certification, telecom integration, and government access rules remain design constraints."
      power_interconnect: "High: 1 GW+ data-center power requires major dedicated transmission, substations, storage, and round-the-clock green power; only broad Kutch-to-Jamnagar transmission evidence was found."
      supply_chain: "High: no public accelerator allocation supports a full 1 GW Jamnagar compute buildout."
      technology: "High: 'gigawatt scale' is not a clean facility-MW or IT-MW disclosure."
      financing: "Medium-high: the $110B/Rs 10 lakh crore plan is group-level and seven-year, not Jamnagar-specific capex."
      structural_optionality: "High: 1 GW is a scaling envelope beyond the >120 MW near-term tranche."

  - id: atom:d1_reliance_andhra_1gw_ai_dc_mou_candidate
    site: "Andhra Pradesh, India; exact site not disclosed in Reliance AP MoU reports"
    operator: "Reliance Industries / Jio or Reliance-controlled developer"
    user_or_anchor: "Indian AI infrastructure users; possibly Reliance/Jio ecosystem"
    gw_facility: 1.0
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: null, central: 2030-12-31, latest: null}
    operational_status: T4
    exact_quote: "1 GW Artificial Intelligence (AI) data centre"
    source_url: "https://www.business-standard.com/companies/news/reliance-andhra-pradesh-1gw-ai-data-centre-investment-125111401010_1.html"
    source_publisher: "Business Standard"
    source_publication_date: 2025-11-14
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Digital Connexion Visakhapatnam 1 GW candidate"
        epoch_attributed_to: "Reliance Industries / Brookfield / Digital Realty"
        overlap_gw_facility: 1.0
        overlap_evidence: "Digital Connexion later announced $11B by 2030 for 1 GW across 400 acres in Visakhapatnam; Reliance AP MoU reporting also describes a 1 GW AP AI data center. Treat as possible same program until adjudicated."
      - epoch_site: "Google / AdaniConneX Visakhapatnam AI hub"
        epoch_attributed_to: "Google / AdaniConneX"
        overlap_gw_facility: null
        overlap_evidence: "Separate AP gigawatt AI hub in/near Visakhapatnam; AP's 6 GW state target increases site/power overlap risk but no Reliance-Google capacity match is shown."
    risks:
      counterparty: "Medium: Reliance is named, but reports do not identify the project SPV, tenant, or commercial offtake."
      regulatory: "Medium: MoU signed with AP government; land allotment, permits, and data-center policy incentives remain to be verified."
      power_interconnect: "High: a 6 GWp solar project is announced for support, but no substation/interconnect schedule was found."
      supply_chain: "High: no chip, cooling, or electrical procurement is disclosed."
      technology: "Medium-high: described as modular and GPU/TPU/AI-processor capable, but no rack density or basis."
      financing: "Medium-high: no AP Reliance capex total is disclosed in the MoU reporting."
      structural_optionality: "High: MoU-level 1 GW plan; delivery phasing not disclosed."

  - id: atom:d1_digital_connexion_vizag_1gw_overlap_candidate
    site: "Visakhapatnam, Andhra Pradesh, India"
    operator: "Digital Connexion (Reliance Industries / Brookfield / Digital Realty JV)"
    user_or_anchor: "Hyperscalers and enterprises"
    gw_facility: 1.0
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: null, central: 2030-12-31, latest: null}
    operational_status: T4
    exact_quote: "1GW data center campus"
    source_url: "https://www.datacenterdynamics.com/en/news/digital-connexion-signs-mou-to-build-1gw-campus-in-andhra-pradesh-india/"
    source_publisher: "Data Center Dynamics"
    source_publication_date: 2025-11-27
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Reliance Andhra 1 GW AI data center MoU candidate"
        epoch_attributed_to: "Reliance Industries / Jio"
        overlap_gw_facility: 1.0
        overlap_evidence: "Both candidates are Reliance-linked, Andhra Pradesh 1 GW AI/data-center disclosures within twelve days; one cites Reliance Industries, the other its Digital Connexion JV."
      - epoch_site: "none found in local Epoch snapshot"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: "Local Epoch snapshot has no Andhra Reliance/Digital Connexion row."
    risks:
      counterparty: "Medium-low: JV combines Reliance, Brookfield, and Digital Realty, but the exact tenant mix is not public."
      regulatory: "Medium: MoU with Andhra Pradesh Economic Development Board; land, environmental, coastal, and telecom permits still need primary extraction."
      power_interconnect: "High: 1 GW across 400 acres requires robust substations and redundant feeds; public statement language is design intent, not interconnect approval."
      supply_chain: "High: AI-native design implies high-density equipment, but no accelerator/electrical procurement was found."
      technology: "Medium: AI-native, high-rack-density language is stronger than generic DC language but still not a facility-vs-IT basis."
      financing: "Medium: $11B by 2030 is disclosed, but project financing terms are not."
      structural_optionality: "Medium-high: site and capex are named, but construction and customer phasing are unresolved."
contradictions:
  - "The existing canonical atom carries Jamnagar as 1.000 GW facility, T5, secondary-only. Current evidence supports adding or separating a near-term >120 MW Jamnagar tranche, but not upgrading the whole 1 GW stretch."
  - "RIL primary sources say gigawatt-scale/multi-gigawatt Jamnagar data centers; secondary summit reporting says more than 120 MW in H2 2026. The latter is the only near-term MW disclosure found."
  - "Reliance AP 1 GW MoU and Digital Connexion Vizag 1 GW campus may describe the same Reliance-linked AP capacity, two coordinated tranches, or overlapping media retellings. Do not sum without adjudication."
  - "AP state-level ambition is 6 GW data-center capacity by 2030, but Reliance/Jio-specific public evidence supports only the Jamnagar near-term tranche plus 1 GW stretch candidates."
gaps:
  - "Official transcript or video timestamp for Mukesh Ambani's February 19, 2026 India AI Impact Summit 120 MW statement."
  - "Facility-vs-IT basis for all Reliance/Jio MW/GW disclosures."
  - "Jamnagar site coordinates, building count, phase schedule, substation/interconnect filings, and Kutch-to-Jamnagar transmission capacity."
  - "Primary Reliance or AP government MoU text for the November 2025 Andhra 1 GW announcement."
  - "Whether the Reliance AP MoU is the same as, upstream of, or separate from Digital Connexion's 1 GW Visakhapatnam campus."
  - "Chip/server procurement evidence for the 120 MW tranche and for any 1 GW scale-up."
```

## Sovereign / India Sidebar Treatment

Reliance/Jio capacity is best treated as India sovereign/strategic AI capacity. The public rationale is not a Western lab take-or-pay cloud contract; it is national compute affordability, Indian-language AI, Jio network integration, Reliance-owned green power, India-first compliance, and domestic sovereign compute. PIB's IndiaAI common compute facility reinforces the national direction: government-backed GPU access for academia, startups, governments, public-sector agencies, and approved users, with Jio Platforms listed among the eligible providers.

Do not move Reliance/Jio Jamnagar or Andhra capacity into the Western denominator unless adjudication changes the scope rule. Google Cloud's Jamnagar region is dedicated to Reliance, not disclosed as Western frontier-lab capacity.

## Tier Evidence Candidates

| Candidate row | Evidence | Candidate tier note |
|---|---|---|
| Jamnagar first >120 MW | RIL says work has begun; summit reporting says >120 MW in H2 2026. | T2/T4 boundary. T2 if company "work begun" plus H2 2026 phase is accepted as physical evidence; otherwise T4 until official transcript/interconnect evidence is pulled. |
| Jamnagar 1 GW / multi-GW | RIL primary sources say gigawatt-scale or multi-gigawatt, phased. | T5 stretch candidate beyond the near-term tranche. |
| Reliance AP 1 GW MoU | AP/Reliance MoU reporting; 6 GWp solar support; no exact site or phasing. | T4 MoU/site-plan candidate, with high overlap risk against Digital Connexion. |
| Digital Connexion Vizag 1 GW | JV/MoU reporting names Visakhapatnam, 400 acres, $11B by 2030. | T4 candidate, possible duplicate of the Reliance AP 1 GW announcement. |
| IndiaAI common compute | PIB and IndiaAI portal show GPU access program, not data-center MW. | Context only; not a facility-GW atom without physical-site allocation. |

## Source Pointers

| Source | Date | Type | Use | Accessed |
|---|---:|---|---|---:|
| [RIL 47th AGM key highlights presentation](https://www.ril.com/sites/default/files/2024-08/Presentation-on-key-highlights-of-47th-AGM.pdf) | 2024-08-29 | Primary company | Jamnagar "gigawatt scale AI ready" statement. | 2026-04-28 |
| [RIL 47th AGM transcript](https://www.ril.com/sites/default/files/2024-09/RIL-47th-AGM-Transcripts.pdf) | 2024-08-29 | Primary company | Green power, Kutch generation, Kutch-Jamnagar transmission context. | 2026-04-28 |
| [RIL FY25 investor presentation](https://www.ril.com/sites/default/files/2025-07/InvestorPresentation.pdf) | 2025-07-18 | Primary company | New Energy commissioning in 4-6 quarters, Kutch projects, dedicated transmission line to Jamnagar. | 2026-04-28 |
| [RIL 48th AGM transcript](https://rilstaticasset.akamaized.net/sites/default/files/2025-09/RIL-48th-AGM-Transcripts_2025.pdf) | 2025-08-29 | Primary company | Reliance Intelligence, work begun at Jamnagar, Google Cloud Jamnagar region. | 2026-04-28 |
| [TechCrunch, Reliance $110B AI plan](https://techcrunch.com/2026/02/19/reliance-unveils-110b-ai-investment-plan-as-india-ramps-up-tech-ambitions/) | 2026-02-19 | Secondary media | $110B plan; >120 MW H2 2026; multi-GW Jamnagar construction. | 2026-04-28 |
| [ETTelecom, Reliance/Jio Rs 10 lakh crore AI infrastructure](https://telecom.economictimes.indiatimes.com/news/industry/reliance-and-jio-to-invest-10-lakh-crore-in-ai-infrastructure-by-2033/128545747) | 2026-02-19 | Secondary media | Independent report of the >120 MW H2 2026 statement and 10 GW green-power surplus. | 2026-04-28 |
| [Business Standard, Reliance AP 1 GW AI data centre](https://www.business-standard.com/companies/news/reliance-andhra-pradesh-1gw-ai-data-centre-investment-125111401010_1.html) | 2025-11-14 | Secondary media | AP MoU, 1 GW AI data center, twin to Jamnagar, 6 GWp solar. | 2026-04-28 |
| [IBEF, RIL to build 1 GW AI data centre in Andhra Pradesh](https://www.ibef.org/news/ril-to-build-1-gw-ai-data-centre-in-andhra-pradesh-deepen-investment-footprint) | 2025-11-17 | Government-linked secondary | AP/Reliance 1 GW and 6 GWp solar summary. | 2026-04-28 |
| [Data Center Dynamics, Digital Connexion AP 1 GW campus](https://www.datacenterdynamics.com/en/news/digital-connexion-signs-mou-to-build-1gw-campus-in-andhra-pradesh-india/) | 2025-11-27 | Specialist secondary citing company statement | Digital Connexion 1 GW, 400 acres, $11B by 2030, Visakhapatnam. | 2026-04-28 |
| [PIB / MeitY, IndiaAI common compute facility](https://psa.gov.in/CMS/web/sites/default/files/publication/India%20all%20set%20to%20launch%20its%20own%20safe%20%26%20secure%20indigenous%20AI%20model%20at%20affordable%20cost%20soon%20Shri%20Ashwini%20Vaishnaw.pdf) | 2025-01-30 | Primary government | 18,693 GPUs, 10,000 initial GPUs, eligible bidders including Jio Platforms. | 2026-04-28 |
| [IndiaAI Compute Capacity portal](https://indiaai.gov.in/hub/indiaai-compute-capacity) | 2026 page access | Primary/government portal | Current compute allocation context and user categories. | 2026-04-28 |
| Local Epoch context: `epoch_data_centers/report.txt`, `epoch_data_centers/compiled.json`, `canonical_capacity_atoms.yaml` | 2026-04-20 / retrieved 2026-04-22 | Local dataset context | No Reliance/Jamnagar/AP Reliance Epoch overlap; current canonical Reliance row is T5 sovereign 1 GW. | 2026-04-28 |

