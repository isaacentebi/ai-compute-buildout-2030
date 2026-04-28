# Rev-4.2 Research Dispatch D2: HUMAIN / xAI / AMD Saudi Sovereign AI Capacity

```yaml
counterparty: HUMAIN / xAI / AMD
contract_overview:
  type: cloud capacity / chip procurement / JV
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2026-01-01, central: 2028-01-01, latest: 2030-12-31}
  exclusivity_or_optionality: >
    HUMAIN has multiple Saudi sovereign AI capacity tracks that should not be
    silently summed without adjudication. The two local 500 MW rows map to:
    (1) a November 2025 xAI/HUMAIN Saudi data-center and Grok framework,
    where xAI's official source confirms the framework but DCD/Bloomberg carry
    the 500 MW size; and (2) a May 2025 AMD/HUMAIN $10B collaboration for
    500 MW over five years, later deepened into an AMD/Cisco/HUMAIN JV aiming
    for up to 1 GW by 2030 with a 100 MW Saudi first phase.
atoms:
  - id: atom:d2_humain_xai_saudi_500mw
    site: "Saudi Arabia, exact first site undisclosed"
    operator: "HUMAIN; xAI partner/user; Nvidia hardware context"
    user_or_anchor: xAI / Grok
    gw_facility: [0.4, 0.5, 0.6]
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: null, latest: null}
    operational_status: T4
    exact_quote: "build a 500MW data center in Saudi Arabia"
    source_url: https://www.datacenterdynamics.com/en/news/xai-humain-data-center-elon-musk/
    source_publisher: Data Center Dynamics
    source_publication_date: 2025-11-20
    accessed_date: 2026-04-28
    source_notes:
      - "DCD is the accessible source for the 500 MW figure; it cites the November 2025 US-Saudi Investment Forum context and reports no first-site location."
      - "xAI's official November 19, 2025 announcement confirms a framework agreement with KSA and HUMAIN to design, build, and operate hyperscale GPU data centers, but does not state 500 MW."
      - "Commerce Department approval for Humain covers the equivalent of up to 35,000 Nvidia GB300s, subject to security/reporting requirements; this is materially below several-hundred-thousand-GPU long-run ambition."
      - "The local canonical row currently carries source_date 2025-05-14; public xAI/HUMAIN 500 MW evidence found here is November 19-20, 2025, so the local date/source should be refreshed during adjudication."
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch Saudi data centers"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch snapshot/report has xAI Colossus 1 and xAI Colossus 2 in
          Memphis only; no HUMAIN, Saudi Arabia, Riyadh, Dammam, or xAI Saudi
          site row was found.
      - epoch_site: "xAI Colossus 1 / xAI Colossus 2"
        epoch_attributed_to: "xAI -> xAI"
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Programmatic xAI compute overlap risk only. The sites are U.S.
          Memphis Epoch rows, so this is not a physical-site dedupe candidate
          unless later evidence says the Saudi facility is replacing or
          reallocating Colossus capacity.
      - epoch_site: "repo atom: xai_humain_saudi"
        epoch_attributed_to: "HUMAIN -> xAI"
        overlap_gw_facility: 0.5
        overlap_evidence: >
          This dispatch atom is the same local sovereign sidebar candidate as
          xai_humain_saudi; use it to refresh evidence, not to add another
          500 MW.
      - epoch_site: "potential repo/NVIDIA-HUMAIN Saudi row if created"
        epoch_attributed_to: "HUMAIN / Nvidia -> xAI or sovereign customers"
        overlap_gw_facility: 0.5
        overlap_evidence: >
          Nvidia's May 2025 HUMAIN release separately says up to 500 MW of
          Saudi AI factories. The November xAI data center appears Nvidia-
          powered in media/forum reports, so adjudication should test whether
          xAI is an anchor/customer for the same Nvidia-HUMAIN Saudi capacity.
    risks:
      counterparty: "xAI/HUMAIN official source is a framework agreement, not a disclosed executed lease, PPA, or take-or-pay contract."
      regulatory: "Advanced U.S. chip exports to Humain are licensed and conditioned on Commerce/BIS security and reporting requirements."
      power_interconnect: "No substation, grid-connection, PPA, utility filing, or exact site found for the 500 MW xAI facility; only HUMAIN's broader Saudi land/fiber strategy is public."
      supply_chain: "Scale depends on Nvidia GB300/Blackwell export approvals, delivery schedules, networking, cooling, and power equipment."
      technology: "Grok nationwide deployment plus training/inference workloads require sovereign-data controls, high-density liquid/cooled infrastructure, and model-service localization."
      financing: "No xAI/HUMAIN project financing terms found; HUMAIN is PIF-backed and has separate Infra financing for 250 MW, but no source ties that facility financing to xAI."
      structural_optionality: "Framework and 'first of a network' language imply optional expansion; count as a candidate sidebar row pending firm site and financing evidence."

  - id: atom:d2_humain_amd_saudi_500mw
    site: "Saudi Arabia and United States network; Saudi first-phase site likely Riyadh or Dammam but not confirmed"
    operator: "HUMAIN / AMD; Cisco added in later JV"
    user_or_anchor: "Saudi sovereign + enterprise/startup/global customers; Luma AI reported first JV customer for first phase"
    gw_facility: [0.3, 0.5, 0.7]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2028-01-01, latest: 2030-12-31}
    operational_status: T4
    exact_quote: "deploy 500 megawatts of AI compute capacity"
    source_url: https://www.amd.com/en/newsroom/press-releases/2025-5-13-amd-and-humain-form-strategic--10b-collaboration-.html
    source_publisher: AMD
    source_publication_date: 2025-05-13
    accessed_date: 2026-04-28
    source_notes:
      - "AMD's May 2025 source says up to $10B and 500 MW over five years, but describes a network from Saudi Arabia to the United States, so the full 500 MW is not necessarily all Saudi physical capacity."
      - "AMD says HUMAIN oversees hyperscale data centers, sustainable power systems, and global fiber interconnects; no site-level interconnect evidence was found."
      - "The November 2025 AMD/Cisco/HUMAIN JV is a later/deepened collaboration for up to 1 GW by 2030, starting with 100 MW in Saudi Arabia and expected to begin operations in 2026."
      - "DCD explicitly flags uncertainty on whether the November 1 GW JV is separate from or part of the earlier May 500 MW AMD agreement."
      - "Local canonical row labels this as Riyadh/Dammam AMD-HUMAIN JV, but primary AMD May evidence does not name Riyadh or Dammam."
    epoch_site_overlap_candidates:
      - epoch_site: "none found in local Epoch Saudi data centers"
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch snapshot/report has no HUMAIN, AMD, Riyadh, Dammam, or
          Saudi AI data-center row. Treat as ex-Epoch sovereign sidebar unless
          a newer Epoch release adds Saudi HUMAIN sites.
      - epoch_site: "repo atom: humain_amd_saudi"
        epoch_attributed_to: "HUMAIN / AMD -> Saudi sovereign + merchant"
        overlap_gw_facility: 0.5
        overlap_evidence: >
          This dispatch atom is the same local sovereign sidebar candidate as
          humain_amd_saudi; use it to refresh evidence, not to add another
          500 MW.
      - epoch_site: "repo/local HUMAIN Riyadh and Dammam 100 MW facilities context"
        epoch_attributed_to: "HUMAIN"
        overlap_gw_facility: 0.2
        overlap_evidence: >
          DCD/Bloomberg context says HUMAIN broke ground on Riyadh and Dammam
          facilities with 100 MW initial capacity each, Q2 2026 target. These
          may host AMD/Cisco first-phase capacity but are not proven to equal
          the full 500 MW AMD row.
      - epoch_site: "potential AMD/Cisco/HUMAIN 1 GW JV row if created"
        epoch_attributed_to: "HUMAIN / AMD / Cisco"
        overlap_gw_facility: 1.0
        overlap_evidence: >
          The November 2025 JV is a direct follow-on to the May collaboration.
          Adjudication should decide whether the local 500 MW row is superseded
          by, nested inside, or separate from the 1 GW by 2030 JV.
    risks:
      counterparty: "AMD provides technology; HUMAIN owns end-to-end delivery; Cisco becomes a critical-infrastructure partner in the later JV. Customer/offtake depth is still thin in public sources."
      regulatory: "AMD explicitly lists export regulations, tariffs, protection measures, and licensing requirements among forward-looking risks."
      power_interconnect: "No primary substation or utility interconnect evidence found; available sources only state sustainable power systems, global fiber interconnects, 100 MW Saudi first phase, and broader Riyadh/Dammam construction context."
      supply_chain: "Depends on AMD Instinct GPU generations, Cisco networking/critical infrastructure, liquid cooling, global fiber, and exportable U.S. AI hardware."
      technology: "AMD ROCm/open-stack positioning reduces Nvidia lock-in but adds platform adoption and software-readiness risk at hyperscale."
      financing: "May AMD/HUMAIN says up to $10B investment; November JV founding-investor sizes are undisclosed; separate Infra $1.2B/250 MW financing is non-binding and not clearly allocated to AMD."
      structural_optionality: "The 500 MW number is 'up to' over five years and cross-border; November 1 GW is an announced plan by 2030 with only 100 MW first phase identified."
contradictions:
  - "xAI official source confirms the HUMAIN/KSA framework and data-center design/build/operate plan but does not state 500 MW; DCD/Bloomberg carry the 500 MW size."
  - "Local xai_humain_saudi row cites a May 2025 DCD source date, but the accessible xAI/HUMAIN 500 MW evidence is November 2025."
  - "AMD May 2025 source says 500 MW over five years across a network from Saudi Arabia to the United States; local atom says Riyadh/Dammam AMD-HUMAIN JV, which is not directly in the May primary source."
  - "AMD/Cisco/HUMAIN November 2025 JV says up to 1 GW by 2030 and a 100 MW Saudi phase 1; DCD says it is unclear whether this is separate from or part of the May 500 MW AMD agreement."
  - "HUMAIN/Nvidia May 2025 also says up to 500 MW of Saudi AI factories; xAI's November 500 MW Nvidia-powered Saudi facility may overlap that Nvidia-HUMAIN capacity, but public sources do not resolve whether it is the same physical row."
gaps:
  - "Executed xAI/HUMAIN contract, lease, offtake, or construction agreement showing firm MW, term, site, and payment obligations."
  - "Exact Saudi site for the xAI 500 MW facility, plus utility interconnect/substation/PPA evidence."
  - "Whether the xAI 500 MW is a new facility, an anchor tenancy in HUMAIN/Nvidia capacity, or part of HUMAIN's first Riyadh/Dammam facilities."
  - "Executed AMD/HUMAIN or AMD/Cisco/HUMAIN JV documents allocating the May 500 MW between Saudi Arabia and the U.S."
  - "Whether the November 2025 AMD/Cisco 1 GW JV supersedes, expands, or nests the May 2025 500 MW AMD/HUMAIN row."
  - "Which customers lease the AMD/Cisco first 100 MW and how much space Luma AI committed."
  - "Definitive financing allocation: PIF equity, Aramco minority-stake completion, Infra $1.2B framework, vendor financing, and customer prepayments."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [xAI, "Grok goes Global with KSA"](https://x.ai/news/grok-goes-global) | 2025-11-19 | Primary company announcement | Confirms xAI/HUMAIN/KSA framework, data-center build/operate language, and Grok nationwide deployment; does not disclose MW. | "hyperscale GPU data centers" | 2026-04-28 |
| [DCD, "xAI and Humain to build 500MW Saudi Arabia data center"](https://www.datacenterdynamics.com/en/news/xai-humain-data-center-elon-musk/) | 2025-11-20 | Secondary media | Accessible support for xAI 500 MW size, no first-site location, first-of-network framing, PIF/HUMAIN 6.6 GW ambition. | "build a 500MW data center" | 2026-04-28 |
| [AMD, "AMD and HUMAIN Form Strategic, $10B Collaboration"](https://www.amd.com/en/newsroom/press-releases/2025-5-13-amd-and-humain-form-strategic--10b-collaboration-.html) | 2025-05-13 | Primary company announcement | 500 MW AMD/HUMAIN capacity, up to $10B, five-year window, KSA-to-U.S. network, HUMAIN delivery role. | "deploy 500 megawatts" | 2026-04-28 |
| [HUMAIN, AMD & Cisco launch AI infrastructure collaboration](https://humain.ai/en/news/humain-and-amd-and-cisco/) | 2025-05-13 | Primary company announcement | HUMAIN says it will oversee hyperscale data centers, sustainable power systems, and global fiber interconnects; no 500 MW figure in accessible page text. | "global fiber interconnects" | 2026-04-28 |
| [AMD, Cisco and HUMAIN to form JV](https://www.amd.com/en/newsroom/press-releases/2025-11-19-amd-cisco-and-humain-to-form-joint-venture.html) | 2025-11-19 | Primary company announcement | Later AMD/Cisco/HUMAIN JV: up to 1 GW by 2030, phase 1 100 MW, expected operations in 2026, AMD MI450 and Cisco infrastructure. | "phase 1 deployment of 100 MW" | 2026-04-28 |
| [DCD, "AMD, Cisco, and Humain set up JV"](https://www.datacenterdynamics.com/en/news/amd-cisco-and-humain-set-up-jv-for-1gw-of-ai-infrastructure-in-saudi-arabia/) | 2025-11-20 | Secondary media | Notes possible Riyadh/Dammam host sites and explicitly says unclear whether 1 GW JV is separate from earlier 500 MW AMD deal. | "unclear whether today's announcement is separate" | 2026-04-28 |
| [NVIDIA, "HUMAIN and NVIDIA Announce Strategic Partnership"](https://nvidianews.nvidia.com/news/humain-and-nvidia-announce-strategic-partnership-to-build-ai-factories-of-the-future-in-saudi-arabia) | 2025-05-13 | Primary company announcement | Separate HUMAIN/Nvidia 500 MW Saudi AI-factory program and 18,000 GB300 first phase; possible overlap with xAI 500 MW. | "up to 500 megawatts" | 2026-04-28 |
| [U.S. Commerce, "Statement on UAE and Saudi Chip Exports"](https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports) | 2025-11-19 | Primary government release | Humain export approval for up to 35,000 Nvidia GB300 equivalents, with security/reporting conditions. | "up to 35,000 Nvidia Blackwell chips" | 2026-04-28 |
| [PIF, "HRH Crown Prince launches HUMAIN"](https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/hrh-crown-prince-launches-humain-as-global-ai-powerhouse/?_bhlid=8975d7e9f7d2b5c40c2133b351af7c584a4b6148) | 2025-05-12 | Primary PIF release | HUMAIN launch, PIF ownership, next-generation data centers/cloud/model mandate, hardware procurement coordination. | "PIF-owned company" | 2026-04-28 |
| [PIF HUMAIN portfolio page](https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/) | 2026 site page | Primary PIF portfolio page | Current PIF description of HUMAIN as full-stack AI platform with NVIDIA, Microsoft, AMD, AWS, Google Cloud, Groq partnerships. | "build the entire AI stack" | 2026-04-28 |
| [PIF / Aramco HUMAIN term sheet](https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/pif-and-aramco-agree-for-aramco-to-acquire-a-significant-minority-stake-in-humain-with-pif-retaining-majority-ownership/) | 2025-10-28 | Primary PIF release | Financing/ownership context: Aramco planned minority stake, PIF retains majority, subject to definitive agreements and approvals. | "non-binding term sheet" | 2026-04-28 |
| [DCD, "Humain breaks ground two data centers"](https://www.datacenterdynamics.com/en/news/humain-breaks-ground-two-data-centers-with-first-facilities-expected-to-go-live-in-q2-2026/) | 2025-08-26 | Secondary media citing Bloomberg | Riyadh and Dammam facilities, 100 MW initial capacity each, Q2 2026 target, U.S. chip-procurement dependency. | "initial capacity of 100MW each" | 2026-04-28 |
| [DCD, "Humain secures 211 plots"](https://www.datacenterdynamics.com/en/news/humain-secures-211-plots-of-land-in-saudi-arabia-for-data-centers/) | 2026-03-12 | Secondary media | Land-bank/fiber-route context; reiterates Riyadh/Dammam 100 MW sites, xAI 500 MW, and Infra financing. | "211 plots of land" | 2026-04-28 |
| [DCD, "Humain and Infra set up $1.2bn financing"](https://www.datacenterdynamics.com/en/news/humain-and-infra-set-up-12bn-financing-package-to-fund-250mw-of-data-center-space-in-saudi-arabia/) | 2026-01-22 | Secondary media | Non-binding $1.2B financing framework for up to 250 MW Saudi hyperscale AI data-center capacity. | "non-binding financing terms" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 local snapshot | Local dataset context | Local Epoch has xAI Colossus 1 and Colossus 2 in Memphis, no HUMAIN/Saudi/Riyadh/Dammam rows. | "xAI Colossus 2" | 2026-04-28 |

## Research Notes

- DCD blocked URL replacement: the local `xai_humain_saudi` source URL remains accessible as of this dispatch, but its date in the local atom appears stale. If a future DCD URL blocks or moves, replace the size support with Bloomberg/CNBC/AP-derived reporting only after finding an accessible source that explicitly says 500 MW.
- Tier evidence: both 500 MW rows remain candidate T4-style announced sovereign sidebar rows from this dispatch's perspective. I did not adjudicate final tier, denominator inclusion, probability, or dedupe.
- xAI row: strongest primary evidence is the official xAI framework agreement; strongest accessible MW evidence is DCD/Bloomberg-style secondary reporting. No first-site, power, financing, or firm-term evidence found.
- AMD row: strongest primary evidence is AMD's May 2025 500 MW / $10B announcement, but it is cross-border and "up to" language. The November 2025 AMD/Cisco/HUMAIN 1 GW by 2030 JV is likely related but not resolved.
- Site/timing: Riyadh and Dammam 100 MW initial facilities with Q2 2026 targets are the only named HUMAIN Saudi sites found, but no source ties either site to the full xAI 500 MW or AMD 500 MW row.
- Export controls: U.S. Commerce's November 19, 2025 approval for Humain's GB300-equivalent purchases materially improves near-term chip deliverability but remains conditional on security/reporting compliance.
- Power/interconnect: public sources mention "sustainable power systems," "global fiber interconnects," geographic diversity, and multiple fiber routes; no utility interconnect, substation, or PPA evidence was found.
- Financing: PIF ownership is primary; Aramco minority stake is non-binding pending definitive agreements; Infra $1.2B/250 MW framework is non-binding and not allocated to xAI or AMD rows.
- Dedupe posture: do not sum xAI 500 MW, Nvidia-HUMAIN 500 MW, AMD-HUMAIN 500 MW, AMD/Cisco-HUMAIN 1 GW, and Riyadh/Dammam 200 MW initial facilities without site/tenant allocation. The xAI and Nvidia rows are the highest-overlap risk; AMD May and AMD/Cisco November are the next-highest-overlap risk.
