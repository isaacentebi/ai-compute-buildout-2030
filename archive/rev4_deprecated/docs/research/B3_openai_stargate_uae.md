# Rev-4.2 Research Dispatch B3: OpenAI Stargate UAE / UAE-US AI Campus

accessed_date: 2026-04-28

## TL;DR

Stargate UAE belongs in the sovereign stretch annex, not the Western denominator. Primary sources frame it as OpenAI's first "OpenAI for Countries" deployment, built under a U.S.-UAE government-to-government AI Acceleration Partnership, built by G42/Khazna in Abu Dhabi, and operated by OpenAI and Oracle for UAE/regional sovereign-AI use. Commerce also says UAE compute access is reserved for U.S. hyperscalers and approved cloud providers with KYC, security, reporting, and export-control conditions. That is a sovereign/allied deployment surface, not a U.S./Western site serving the denominator for OpenAI/Anthropic/Google/Meta/Microsoft/xAI capex.

The most defensible row is the 1 GW Stargate UAE cluster, with a 200 MW first tranche expected in 2026. Local Epoch context already carries this as `epoch_openai_stargate_uae_buildout_remaining`: 1.400 GW facility, 1.207 GW IT bridge, T4, scope sovereign, excluded from raw/weighted Western totals. G42's October 2025 construction update is stronger than announcement-only evidence for the first 200 MW tranche, but it is still not an operational row as of the local snapshot: Epoch has 0 MW current, partly constructed first buildings, first operational date 2026-12-01, and full buildout 2028-01-01.

Flag, do not adjudicate: the broader 5 GW UAE-US AI Campus is a real official site-level plan, but OpenAI's named Stargate tranche is 1 GW. The remaining 4 GW is campus/country/hyperscaler capacity, not OpenAI-specific capacity. It should be carried, if at all, as a sovereign stretch candidate with high allocation and export-control risk.

## Evidence Notes

- OpenAI says Stargate UAE is the first international Stargate deployment and the first OpenAI for Countries partnership to help governments build sovereign AI capability in coordination with the U.S. government.
- OpenAI's capacity language is a "1GW Stargate UAE cluster in Abu Dhabi" with "200MW expected to go live in 2026"; G42 separately says the cluster will be built by G42 and operated by OpenAI and Oracle.
- The U.S. Department of Commerce describes the larger campus as a 5 GW UAE-US AI Campus in Abu Dhabi, built by G42, operated in partnership with U.S. companies, and subject to security guarantees, KYC controls, and approved-provider restrictions.
- G42/PRNewswire's October 2025 construction update says Khazna is developing the 1 GW cluster, the first 200 MW is on an accelerated timeline, civil/structural/architectural construction is well advanced, long-lead equipment procurement is complete, and first mechanical deliveries have reached the site.
- Commerce's November 2025 chip-export statement says G42 received approval to purchase the equivalent of up to 35,000 Nvidia Blackwell GB300 chips, conditioned on rigorous security and reporting requirements. G42 frames that approval as moving Stargate UAE from planning to deployment.
- Financing is not cleanly disclosed at the Stargate UAE project level. Primary sources say G42/Khazna builds the UAE campus, OpenAI/Oracle operate the Stargate cluster, SoftBank participates, NVIDIA supplies Grace Blackwell GB300 systems, Cisco supplies networking/security/observability, and UAE entities will invest in U.S. digital infrastructure. OpenAI's January Stargate release separately names MGX as an initial equity funder for Stargate, but the UAE project-specific cap table/debt stack is not public in the sources reviewed here.

```yaml
counterparty: "G42 / Khazna Data Centers / OpenAI / Oracle / UAE-US AI Acceleration Partnership"
contract_overview:
  type: JV
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2026-01-01, central: 2026-12-01, latest: 2028-01-01}
  exclusivity_or_optionality: "OpenAI names a 1 GW Stargate UAE cluster with 200 MW expected in 2026; Commerce/G42 name a broader 5 GW UAE-US campus. No take-or-pay, lease term, ownership split, or OpenAI-exclusive share is disclosed."
atoms:
  - id: atom:openai_stargate_uae_phase1_200mw_candidate
    site: "Stargate UAE / UAE-US AI Campus, Abu Dhabi, United Arab Emirates"
    operator: "G42 / Khazna builds; OpenAI and Oracle operate"
    user_or_anchor: "OpenAI; Oracle; UAE sovereign users; approved U.S. cloud providers"
    gw_facility: [0.20, 0.28, 0.28]
    gw_it: 0.20
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2026-12-01, latest: 2026-12-31}
    operational_status: T4
    exact_quote: "first 200MW"
    source_url: "https://www.prnewswire.com/news-releases/g42-provides-update-on-construction-of-stargate-uae-ai-infrastructure-cluster-302586401.html"
    source_publisher: "G42 via PRNewswire"
    source_publication_date: 2025-10-16
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate UAE"
        epoch_attributed_to: "G42 -> OpenAI"
        overlap_gw_facility: 0.28
        overlap_evidence: "Local Epoch timeline carries Building 1 and 2 as 280 MW facility by 2026-12-01; current_power_mw is 0 and timeline_now says Building 1 and 2 are partly constructed."
    risks:
      counterparty: "Medium: G42/Khazna is UAE state-linked infrastructure; OpenAI/Oracle are operators, but project-level binding economics are not disclosed."
      regulatory: "High: U.S. advanced-chip exports are licensed and conditioned on security/reporting controls; future U.S. policy or compliance findings can slow deployment."
      power_interconnect: "Medium-high: Commerce says the full campus will use nuclear, solar, and gas; no primary utility interconnect schedule or plant-by-plant COD was found."
      supply_chain: "Medium: G42 says long-lead equipment is procured and first mechanical deliveries arrived, but GB300/export availability remains gating."
      technology: "Medium: source language is AI cluster / infrastructure capacity, not a clean facility-vs-IT power basis."
      financing: "Medium: capex and debt/equity stack are undisclosed; likely backed by G42/Khazna/UAE capital plus partner vendor contributions."
      structural_optionality: "High: 200 MW is the only construction-progress tranche; remaining 800 MW remains a named plan."
  - id: atom:openai_stargate_uae_1gw_cluster_candidate
    site: "Stargate UAE / UAE-US AI Campus, Abu Dhabi, United Arab Emirates"
    operator: "G42 / Khazna builds; OpenAI and Oracle operate"
    user_or_anchor: "OpenAI"
    gw_facility: [1.00, 1.40, 1.40]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2028-01-01, latest: null}
    operational_status: T4
    exact_quote: "1-gigawatt compute cluster"
    source_url: "https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae"
    source_publisher: "G42"
    source_publication_date: 2025-05-22
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate UAE"
        epoch_attributed_to: "G42 -> OpenAI"
        overlap_gw_facility: 1.40
        overlap_evidence: "Local canonical atom `epoch_openai_stargate_uae_buildout_remaining` carries 1400 MW facility, pue_assumed 1.16, 1206.897 MW IT, T4, scope sovereign, excluded from Western raw/weighted totals."
    risks:
      counterparty: "Medium: multi-party consortium includes G42, OpenAI, Oracle, NVIDIA, Cisco, and SoftBank; role boundaries are public but economics are not."
      regulatory: "High: U.S. export-control approval is a continuing condition, not a one-time risk removal."
      power_interconnect: "Medium-high: primary sources disclose 5 GW campus power mix but not the interconnection queue or exact substation/generation phasing."
      supply_chain: "Medium-high: NVIDIA GB300 systems and networking/security gear are named; export licenses and delivery cadence govern realization."
      technology: "Medium: primary statements do not identify whether 1 GW is IT load, facility load, or contractual compute capacity."
      financing: "Medium: project capex is undisclosed; broader Stargate names MGX/SoftBank/OpenAI/Oracle, but UAE-specific funding shares are not disclosed."
      structural_optionality: "Medium-high: 1 GW is a named cluster, yet only 200 MW has construction-progress detail."
  - id: atom:uae_us_ai_campus_5gw_sovereign_stretch_candidate
    site: "5 GW UAE-US AI Campus, Abu Dhabi, United Arab Emirates"
    operator: "G42 with U.S. company partners"
    user_or_anchor: "U.S. hyperscalers, approved cloud service providers, UAE/regional users"
    gw_facility: 5.00
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: null, latest: null}
    operational_status: T4
    exact_quote: "5GW of capacity"
    source_url: "https://www.commerce.gov/news/press-releases/2025/05/uae-and-us-presidents-attend-unveiling-phase-1-new-5gw-ai-campus-abu"
    source_publisher: "U.S. Department of Commerce"
    source_publication_date: 2025-05-15
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "OpenAI Stargate UAE"
        epoch_attributed_to: "G42 -> OpenAI"
        overlap_gw_facility: 1.40
        overlap_evidence: "Stargate UAE is the named 1 GW OpenAI tranche inside the 5 GW campus; local Epoch carries the OpenAI tranche only."
      - epoch_site: "Microsoft/G42 UAE Khazna expansion"
        epoch_attributed_to: "Khazna Data Centers / G42 -> Microsoft Azure sovereign cloud"
        overlap_gw_facility: 0.26
        overlap_evidence: "Local canonical atom `microsoft_g42_uae_khazna` carries 200 MW IT / 260 MW facility, sovereign scope, based on Microsoft's November 2025 primary announcement."
    risks:
      counterparty: "Medium-high: the 5 GW campus is a bilateral sovereign program with hyperscaler allocation not disclosed."
      regulatory: "High: Commerce describes controlled access, KYC, approved-provider restrictions, and anti-diversion safeguards."
      power_interconnect: "High: 5 GW requires nuclear/solar/gas power coordination; no complete primary COD schedule was found."
      supply_chain: "High: multi-GW advanced accelerator imports into UAE remain policy-sensitive."
      technology: "Medium: campus capacity is not allocated by chip generation, model workload, or customer."
      financing: "Medium: G42 leads build/investment and UAE entities invest in U.S. digital infrastructure, but no campus-level financing stack is public."
      structural_optionality: "High: 5 GW is broader campus capacity, not a signed OpenAI capacity commitment."
contradictions:
  - "OpenAI and G42 name a 1 GW Stargate UAE cluster with 200 MW in 2026; Commerce and G42 also name a 5 GW UAE-US AI Campus. Treat the 5 GW as broader sovereign campus capacity, not OpenAI-specific capacity."
  - "Primary sources use MW/GW cluster, compute, and AI data-center capacity language interchangeably. Local Epoch converts the 1 GW cluster to 1.4 GW facility, but the primary sources do not disclose PUE or basis."
  - "G42 says chip licensing moves the project from planning into execution; Commerce's November 2025 approval is only up to 35,000 GB300-equivalent chips for G42 and Humain, not enough by itself to evidence the full 1 GW or 5 GW buildout."
gaps:
  - "Project-level capex, ownership, debt/equity split, and take-or-pay obligations for Stargate UAE."
  - "Whether OpenAI has exclusive, priority, or partial rights to the 1 GW cluster, and whether Oracle is cloud operator, capacity reseller, or co-operator."
  - "Facility-vs-IT basis for the 200 MW and 1 GW figures; local Epoch facility conversion should remain a candidate, not a primary-source fact."
  - "Primary power/interconnection schedule for the Abu Dhabi site, including substations, gas/nuclear/solar supply contracts, and COD milestones."
  - "Export-license cadence beyond the November 2025 35,000 GB300-equivalent approval, and whether approvals are allocated to Stargate UAE versus other G42/UAE facilities."
  - "Physical verification refresh after the local Epoch 2025-11-16 imagery note and G42's October 2025 construction update."
```

## Sovereign Treatment

Use sovereign sidebar treatment because the controlling evidence is government-to-government and country-capability language:

- OpenAI calls this an OpenAI for Countries partnership to help governments build sovereign AI capability in coordination with the U.S. government.
- Commerce says the campus is built under the U.S.-UAE AI Acceleration Partnership, built by G42, and reserved for U.S. hyperscalers and approved cloud providers with KYC controls.
- G42 says the campus will deliver sovereign, AI-grade compute and that the cluster is part of a UAE-U.S. AI corridor.
- Local canonical data already marks `epoch_openai_stargate_uae_buildout_remaining` as `scope: sovereign`, `included_raw_horizon: false`, and `included_probability_weighted: false`.

Do not put this in the Western denominator unless the paper's scope policy changes. The Western denominator is for Western-aligned operator/user capacity; this is UAE territory, UAE-led buildout, sovereign-AI policy infrastructure, and export-controlled regional compute even though OpenAI/Oracle operate the named cluster.

## Tier Evidence Candidates

| Candidate row | Evidence | Candidate tier note |
|---|---|---|
| First 200 MW Stargate UAE tranche | G42 construction update: well underway, civil/structural/architectural work advanced, long-lead equipment procured, first mechanical deliveries on site, planned 2026 delivery. | Could justify T2 for this tranche if physical-construction evidence is accepted; local canonical still carries the site as T4 announced because no operational MW is in Epoch. |
| Full 1 GW Stargate UAE cluster | OpenAI/G42/Cisco primary announcements name 1 GW and 200 MW in 2026; G42 later says the first 200 MW is in build. | T4 is appropriate for full 1 GW until more of the remaining 800 MW has physical evidence or a binding utility/generation schedule. |
| Broader 5 GW UAE-US campus | Commerce/G42 official May 2025 announcement names 5 GW, 10 square miles, G42 build, U.S. partner operations, nuclear/solar/gas power. | T4 site-level plan or T5 sovereign stretch candidate; not OpenAI-specific and not Western-denominator capacity. |
| Microsoft/G42 Khazna 200 MW | Microsoft primary November 2025 announcement names a 200 MW Khazna expansion coming online before end-2026 for Azure sovereign cloud services. | Separate sovereign overlap candidate; do not double count inside the 5 GW campus unless adjudication confirms it is part of the same campus. |

## Source Pointers

| Source | Date | Type | Use | Accessed |
|---|---:|---|---|---:|
| [OpenAI, "Introducing Stargate UAE"](https://openai.com/index/introducing-stargate-uae/) | 2025-05-22 | Primary company | First international Stargate, OpenAI for Countries/sovereign framing, 1 GW and 200 MW in 2026. | 2026-04-28 |
| [U.S. Commerce, "UAE and US Presidents attend the unveiling of Phase 1 of new 5GW AI campus in Abu Dhabi"](https://www.commerce.gov/news/press-releases/2025/05/uae-and-us-presidents-attend-unveiling-phase-1-new-5gw-ai-campus-abu) | 2025-05-15 | Primary government | 5 GW campus, G42 build, U.S. company operations, KYC/security guarantees, power mix. | 2026-04-28 |
| [G42, "Global Tech Alliance Launches Stargate UAE"](https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae) | 2025-05-22 | Primary company | G42 build, OpenAI/Oracle operation, NVIDIA GB300, Cisco/SoftBank roles, 1 GW/200 MW. | 2026-04-28 |
| [Cisco, "Cisco Joins Stargate UAE Initiative"](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2025/m05/cisco-joins-stargate-uae-initiative.html) | 2025-05-22 | Primary company | Independent consortium confirmation, target 1 GW and initial 200 MW in 2026. | 2026-04-28 |
| [G42 via PRNewswire, construction update](https://www.prnewswire.com/news-releases/g42-provides-update-on-construction-of-stargate-uae-ai-infrastructure-cluster-302586401.html) | 2025-10-16 | Primary company wire | Construction status, Khazna developer role, long-lead procurement, 2026 first tranche. | 2026-04-28 |
| [U.S. Commerce, "Statement on UAE and Saudi Chip Exports"](https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports) | 2025-11-19 | Primary government | G42 advanced semiconductor export authorization, 35,000 GB300-equivalent chips, security/reporting conditions. | 2026-04-28 |
| [G42, "G42 Receives U.S. Approval for Advanced AI Chip Exports"](https://www.g42.ai/resources/news/g42-receives-us-approval-advanced-ai-chip-exports-enabling-full-scale-deployment-trusted-ai-infrastructure) | 2025-11-20 | Primary company | G42 says approval accelerates Stargate UAE and deployment is governed by RTE/BIS guidelines. | 2026-04-28 |
| [Microsoft, "Microsoft and G42 Accelerate UAE's Digital Future with Major Data Centre Expansion"](https://news.microsoft.com/source/emea/2025/11/microsoft-and-g42-accelerate-uaes-digital-future-with-major-data-centre-expansion/) | 2025-11-05 | Primary company | Separate 200 MW Khazna/Microsoft sovereign cloud overlap candidate. | 2026-04-28 |
| [G42 statement on House Select Committee / NYT allegations](https://www.g42.ai/resources/news/Statement-on-the-New-York-Times-article-and-the-letter-from-the-United-States-Congress-House-Select-Committee-on-the-CCP) | 2024-01-11 | Primary company | Counterparty/regulatory risk context: G42 denies allegations and says it aligned with U.S. partners from 2022. | 2026-04-28 |
| Local Epoch context: `epoch_data_centers/compiled.json`, `epoch_data_centers/data_centers.csv`, `epoch_data_centers/data_center_timelines.csv`, `canonical_capacity_atoms.yaml` | 2026-04-20 / retrieved 2026-04-22 | Local dataset context | Stargate UAE overlap: 0 MW current, 280 MW facility first tranche by 2026-12-01, 1.4 GW facility full buildout by 2028-01-01, sovereign scope. | 2026-04-28 |
