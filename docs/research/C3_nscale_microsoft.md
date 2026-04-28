# Rev-4.2 Research Dispatch C3: Nscale / Microsoft

```yaml
counterparty: Nscale / Microsoft
contract_overview:
  type: cloud capacity
  term_years: null
  announced_capex_usd_b: null
  announced_contract_value_usd_b: null
  delivery_window: {earliest: 2026-01-01, central: 2027-01-01, latest: null}
  exclusivity_or_optionality: >
    Nscale announced an expanded Microsoft deal for approximately 200,000
    NVIDIA GB300 GPUs across Europe and the U.S. The public primary sources do
    not disclose a single 900 MW Microsoft contract. The repo's current 900 MW
    Nscale atom is best treated as a candidate/inference after excluding
    Fairwater Narvik/Loughton overlap, with strongest primary support for
    Ward County/Cedarvale 234-240 MW, Loughton 50 MW scalable to 90 MW, Narvik
    230 MW campus capacity, Sines GPU delivery with no MW, and Microsoft's
    option on a 700 MW second Texas phase from late 2027.
atoms:
  - id: atom:c3_nscale_microsoft_200k_gpu_multisite
    site: "Ward County/Cedarvale Texas; Sines Portugal; Loughton UK; Narvik Norway"
    operator: "Nscale; Ionic Digital site lease in Texas; Aker-Nscale JV rolled into Nscale in Norway; Start Campus partner-run in Portugal"
    user_or_anchor: Microsoft
    gw_facility: [0.52, 0.59, 1.29]
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2027-01-01, latest: 2027-12-31}
    operational_status: T4
    exact_quote: "approximately 200,000 NVIDIA GB300 GPUs"
    source_url: https://www.nscale.com/press-releases/nscale-microsoft-2025
    source_publisher: Nscale
    source_publication_date: 2025-10-15
    accessed_date: 2026-04-28
    source_notes:
      - "Low/central/high are dispatch ranges, not Nscale-disclosed aggregate MW."
      - "Low includes primary-disclosed named-site capacity: Ward County ~240 MW, Loughton 50 MW, Narvik 230 MW, and an inferred Sines placeholder from GPU density."
      - "Central uses Loughton scalable 90 MW plus Sines inferred MW; high adds Microsoft's 700 MW Texas second-phase option but not Nscale's full 1.2 GW Texas footprint."
      - "Nscale says the 200k-GPU agreement covers four countries and two continents; the listed deployments are Texas, Sines, Loughton, and Narvik."
    contract_structure:
      microsoft_total_gpus: 200000
      texas_gpus: 104000
      texas_initial_mw: 240
      texas_site_lease_mw_ionic: 234
      texas_second_phase_option_mw: 700
      texas_total_footprint_plan_mw: 1200
      sines_gpus: 12600
      sines_mw_disclosed: null
      loughton_gpus: 23040
      loughton_mw: [50, 90]
      narvik_gb300_gpus_previous: 52000
      narvik_campus_mw: 230
      narvik_rubin_gpus_added_2026_04: 30000
      narvik_contract_value_usd_b: 6.2
      narvik_contract_term_years: 5
    epoch_site_overlap_candidates:
      - epoch_site: Microsoft Fairwater Wisconsin
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: 3.328
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Wisconsin buildout to 3.328 GW
          by 2027-10-03. Microsoft's Fairwater article groups Wisconsin with
          Narvik and Loughton as AI datacenter investments connected to the
          Microsoft Cloud; candidate only because Nscale's 200k-GPU contract
          does not allocate workloads to U.S. Fairwater.
      - epoch_site: Microsoft Fairwater Atlanta
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.859
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Atlanta buildout to 0.859 GW by
          2026-05-14. It is part of the same Microsoft AI WAN/Fairwater context,
          but no Nscale source ties the 200k-GPU deal to Atlanta.
      - epoch_site: Microsoft Goodyear
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.263
        overlap_evidence: >
          Local Epoch snapshot has Microsoft Goodyear at 0.263 GW full buildout.
          Treat only as generic Microsoft/OpenAI AI capacity overlap risk, not
          a site-level match.
      - epoch_site: Crusoe Abilene Expansion
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Local Epoch snapshot carries a Microsoft-attributed 0.941 GW buildout
          at Crusoe Abilene Expansion. No source links Nscale to Abilene, but
          adjudication should avoid adding all Microsoft neocloud capacity on
          top of Microsoft-attributed Epoch sites without end-user separation.
      - epoch_site: "repo overlay: openai_microsoft_fairwater_international"
        epoch_attributed_to: "Microsoft / OpenAI; Fairwater Narvik and Loughton"
        overlap_gw_facility: 0.805
        overlap_evidence: >
          This is not an upstream Epoch row but is local atom context. The repo
          already carries Narvik/Loughton as a Fairwater-international overlay
          with 0.805 GW facility point and 0.46-1.725 GW range. Nscale is the
          operator/developer partner at both sites, so these MW should be
          flagged for dedupe against any Nscale row.
    risks:
      counterparty: "Nscale is private, recently founded, and scaling quickly; execution depends on private funding, debt, vendors, and hyperscaler demand."
      regulatory: "Four-country rollout exposes the contract to UK, EU/Portugal, Norway, and U.S. data-center, planning, grid, and AI-sovereignty regimes."
      power_interconnect: "Primary evidence is strongest for powered-site capacity at Ward County and secured/queued capacity at Narvik; Sines MW is not disclosed and Texas expansion beyond the initial phase is optional."
      supply_chain: "Delivery depends on large NVIDIA GB300 and later Rubin deployments plus Dell/Nokia/networking/cooling supply chains."
      technology: "Sites require dense liquid-cooled AI infrastructure; Ward County is a crypto-to-AI conversion and Narvik/Loughton depend on high-density GPU campus delivery."
      financing: "Aker says Narvik cash flow supports capex and Ionic has a 10-year lease, but Nscale has no public RPO/SEC-style backlog disclosure and the total Microsoft deal value is not primary-disclosed."
      structural_optionality: "The 700 MW Texas second phase is an option; the 1.2 GW Texas footprint is a plan; the 900 MW repo atom is an analyst construct rather than a primary contract figure."

  - id: atom:c3_nscale_ward_county_cedarvale_microsoft
    site: "Cedarvale / Ward County, Barstow, Texas"
    operator: "Nscale lessee; Ionic Digital facility owner"
    user_or_anchor: Microsoft
    gw_facility: [0.234, 0.240, 0.940]
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-07-01, central: 2026-09-30, latest: 2027-12-31}
    operational_status: T4
    exact_quote: "The site is leased from Ionic Digital"
    source_url: https://www.nscale.com/press-releases/nscale-microsoft-2025
    source_publisher: Nscale
    source_publication_date: 2025-10-15
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: none found in local Epoch snapshot
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch data_centers/report context has no Nscale, Ionic,
          Cedarvale, Ward County, or Barstow Microsoft row. This appears
          ex-Epoch unless a newer Epoch release adds it.
      - epoch_site: "repo atom: nscale_microsoft_contract_capacity"
        epoch_attributed_to: "Nscale -> Microsoft / Google"
        overlap_gw_facility: 0.900
        overlap_evidence: >
          The current canonical atom carries 900 MW facility for Nscale after
          subtracting Fairwater overlap. Ward County's primary-supported
          234-240 MW plus Microsoft's optional 700 MW second phase equals
          roughly 0.94 GW, which may explain the 900 MW candidate, but the
          option is not the same as firm contracted capacity.
    risks:
      counterparty: "Ionic is the real-estate/powered-site lessor; Nscale is the AI infrastructure service provider; Microsoft is the compute customer."
      regulatory: "Texas crypto-to-AI conversion still depends on local permitting, equipment installation, and operating compliance."
      power_interconnect: "Ionic discloses full 234 MW lease capacity; Nscale discloses ~240 MW and a 1.2 GW footprint plan. The 700 MW second phase starts late 2027 only if Microsoft exercises the option."
      supply_chain: "104,000 GB300 GPUs must be installed with direct-liquid cooling, power distribution, networking, and commissioning from Q3 2026."
      technology: "Cedarvale must move from mining infrastructure into high-density AI service operations."
      financing: "Ionic's 10-year triple-net lease has approximately $2B of contracted revenue, but that is Ionic-Nscale lease revenue, not a disclosed Microsoft-Nscale RPO."
      structural_optionality: "0.234-0.240 GW is strongest; 0.94 GW includes the option; 1.2 GW is a footprint plan."

  - id: atom:c3_nscale_fairwater_narvik_loughton_overlap
    site: "Narvik, Norway and Loughton, UK"
    operator: "Nscale; Aker-Nscale JV for Narvik until roll-up into Nscale"
    user_or_anchor: Microsoft
    gw_facility: [0.280, 0.320, 0.610]
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-08-01, central: 2027-01-01, latest: 2027-12-31}
    operational_status: T4
    exact_quote: "Narvik, Norway, Microsoft announced plans with nScale and Aker JV"
    source_url: https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
    source_publisher: Microsoft
    source_publication_date: 2025-09-18
    accessed_date: 2026-04-28
    source_notes:
      - "Narvik low/central/high: 230 MW secured campus; possible expansion by additional 290 MW per Nscale/Stargate Norway/Aker context."
      - "Loughton low/central: 50 MW initial; 90 MW scalable."
      - "This atom is primarily a dedupe flag against the repo's Fairwater-international overlay, not a recommendation to count new GW twice."
    epoch_site_overlap_candidates:
      - epoch_site: "repo overlay: openai_microsoft_fairwater_international"
        epoch_attributed_to: "Microsoft / OpenAI"
        overlap_gw_facility: 0.805
        overlap_evidence: >
          Local canonical atom already attributes Narvik and Loughton to
          Fairwater international at 0.805 GW facility. Nscale primary releases
          identify the same sites as Microsoft customer capacity.
      - epoch_site: Microsoft Fairwater Wisconsin / Atlanta
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: null
        overlap_evidence: >
          Microsoft describes Narvik and Loughton in the same global AI
          datacenter/Fairwater context as Wisconsin. Upstream Epoch only tracks
          the U.S. Fairwater sites, but program-level overlap is high.
    risks:
      counterparty: "Narvik has moved from Aker-Nscale/OpenAI Stargate Norway framing to Microsoft-anchored and Nscale-managed framing; anchor allocation may still evolve."
      regulatory: "Norway hydropower/grid approvals and UK planning/power constraints remain relevant."
      power_interconnect: "Aker discloses 230 MW secured capacity and 200+90 MW in queue at Kvandal; Loughton is 50 MW scalable to 90 MW."
      supply_chain: "Narvik initially used GB300 language, then April 2026 expansion adds more than 30,000 Rubin GPUs in 2027."
      technology: "High-density Arctic/UK liquid-cooled AI campuses need commissioning and network integration into Microsoft Cloud."
      financing: "Aker discloses a $6.2B five-year Microsoft contract for Narvik, but not the full site-level capex stack or Microsoft take-or-pay terms."
      structural_optionality: "Strong candidate overlap with local Fairwater row; do not treat as incremental until adjudication resolves ownership of Narvik/Loughton MW."
contradictions:
  - "The local canonical atom says 900 MW Nscale/Microsoft facility capacity, but no primary source found states a standalone 900 MW contract. The closest primary arithmetic is Ward County 234-240 MW plus a 700 MW Microsoft option, or a broader ex-Fairwater inference."
  - "Nscale's site language says Ward County is ~240 MW with plans to expand to 1.2 GW; Ionic says Cedarvale lease covers full 234 MW capacity. Use 234 MW as lease-document floor and ~240 MW as Nscale rounded site capacity."
  - "Narvik was announced in July 2025 as Stargate Norway with OpenAI as an initial offtaker; in September 2025 Aker/Nscale announced a $6.2B five-year Microsoft agreement; in April 2026 Nscale announced an expanded Microsoft/Narvik Rubin deployment. Anchor allocation is therefore shared/evolving, not cleanly Microsoft-only from inception."
  - "The repo's Fairwater-international atom estimates 0.805 GW facility for Narvik/Loughton, while primary sources disclose 230 MW Narvik campus capacity and 50-90 MW Loughton capacity. The local 0.805 GW point appears higher than directly disclosed initial site capacity."
gaps:
  - "Executed Microsoft-Nscale master services agreement or public filing showing total value, take-or-pay terms, termination rights, and per-site MW/GPU allocation."
  - "Whether Microsoft exercised, or must exercise, the 700 MW Texas second-phase option."
  - "Sines MW/power allocation and whether Start Campus capacity is dedicated to Microsoft or shared."
  - "How many Narvik MW remain OpenAI/Stargate Norway versus Microsoft after the Aker-Nscale JV roll-up and April 2026 Microsoft expansion."
  - "Whether adjudication should revise the current 900 MW Nscale atom to a smaller firm figure plus an optional Texas tranche, and separately dedupe Narvik/Loughton against Fairwater international."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [Nscale, "Nscale Contracts Approximately 200,000 NVIDIA GB300 GPUs with Microsoft"](https://www.nscale.com/press-releases/nscale-microsoft-2025) | 2025-10-15 | Primary company announcement | 200k GPU Microsoft deal, four-country structure, Texas 104k GPUs/~240 MW/Q3 2026, Sines 12.6k GPUs/Q1 2026, Loughton 23k GPUs/50-90 MW/Q1 2027, Narvik 52k GPUs, Texas 700 MW option. | "approximately 200,000 NVIDIA GB300 GPUs" | 2026-04-28 |
| [Microsoft Official Blog, "Inside the world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Microsoft identifies Narvik with Nscale/Aker and Loughton with Nscale in the global AI datacenter/Fairwater context. | "plans with nScale and Aker JV" | 2026-04-28 |
| [Microsoft Source EMEA, "The port town in Norway emerging as an AI hub"](https://news.microsoft.com/source/emea/features/the-port-town-in-norway-emerging-as-an-ai-hub/) | 2025-09-17 | Primary company article | Narvik agreement is $6.2B, five years, staged services from 2026, renewable/secured grid capacity. | "five-year agreement" | 2026-04-28 |
| [Aker / PRNewswire, "Aker-Nscale JV signs Multi-Billion Dollar AI infrastructure agreement with Microsoft"](https://www.prnewswire.com/news-releases/aker-nscale-jv-signs-multi-billion-dollar-ai-infrastructure-agreement-with-microsoft-302559403.html) | 2025-09-17 | Primary company / regulated announcement | Binding five-year customer agreement, ~$6.2B, staged deployments beginning 2026; cash flow supports capex. | "binding five-year customer agreement" | 2026-04-28 |
| [Aker ASA Q3 2025 presentation](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/11/04/658641_Aker_ASA_3Q_2025_Presentation.pdf?VersionId=SRe3eE4FHa.5Qjn31MKeyHvs7kD5nUMN) | 2025-11-04 | Public-company investor presentation | Narvik/Kvandal 230 MW secured capacity, 200+90 MW queue, 52k Microsoft GPUs, ~120 MW contracted with Microsoft/OpenAI, 3-5 year take-or-pay model. | "230MW secured capacity" | 2026-04-28 |
| [Ionic Digital, "Cedarvale Facility with Nscale"](https://ionicdigital.com/uncategorized/ionic-digital-secures-transformational-lease-agreement-of-cedarvale-facility-with-nscale-2/) | 2025-10-14 | Primary company announcement | Nscale leases full 234 MW Cedarvale facility under 10-year triple-net lease with ~$2B contracted revenue. | "full 234 MW capacity" | 2026-04-28 |
| [Nscale, "UK AI infrastructure commitment"](https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement) | 2025-09-16 | Primary company announcement | Loughton Microsoft campus: 50 MW scalable to 90 MW, 23,040 GB300 GPUs in Q1 2027; separate Stargate UK/OpenAI platform. | "50MW of AI capacity" | 2026-04-28 |
| [Microsoft On the Issues, "$30 billion in UK"](https://blogs.microsoft.com/on-the-issues/2025/09/16/microsoft-30-billion-uk-ai-future/) | 2025-09-16 | Primary company announcement | Microsoft UK investment includes largest UK supercomputer with more than 23k NVIDIA GPUs in partnership with Nscale. | "partnership with Nscale" | 2026-04-28 |
| [UK Government, "US-UK pact"](https://www.gov.uk/government/news/us-uk-pact-will-boost-advances-in-drug-discovery-create-tens-of-thousands-of-jobs-and-transform-lives) | 2025-09-16 | Government announcement | Confirms UK Microsoft/Nscale supercomputer and broader UK-US AI infrastructure context. | "more than 23,000 advanced GPUs" | 2026-04-28 |
| [Nscale, "Nscale announces expanded deal with Microsoft in Norway"](https://www.nscale.com/press-releases/nscale-microsoft-norway) | 2026-04-14 | Primary company announcement | Latest Narvik update: Nscale-managed project adds >30k NVIDIA Rubin GPUs in 2027. | "more than 30,000 NVIDIA Rubin GPUs" | 2026-04-28 |
| [Nscale AI Infrastructure page](https://www.nscale.com/ai-infrastructure) | 2026 site page | Primary company site page | Current site capacities: Glomfjord 30 MW operational, Narvik 230+290 MW, Ward County ~240 MW to 1.2 GW, Loughton up to 90 MW. | "roughly 240MW AI data center" | 2026-04-28 |
| [Nscale Series C announcement](https://www.nscale.com/press-releases/nscale-series-c) | 2026-03-09 | Primary company announcement | $2B Series C, $14.6B valuation, Aker JV roll-up into Nscale, governance/funding context. | "roll the Aker Nscale joint venture" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 local snapshot | Local dataset context | Relevant Microsoft overlap candidates: Fairwater Wisconsin 3.328 GW, Fairwater Atlanta 0.859 GW, Goodyear 0.263 GW, Crusoe Abilene Expansion 0.941 GW; no local Nscale site rows. | "Microsoft Fairwater Wisconsin" | 2026-04-28 |

## Research Notes

- Evidence strength: the reviewer concern is valid for the current canonical 900 MW atom because it cites SiliconANGLE and treats a constructed capacity figure as if it were directly contracted. Primary sources now support the underlying Nscale/Microsoft relationship and named sites, but still do not directly support "900 MW" as a firm Microsoft contract.
- Best candidate interpretation of 900 MW: Ward County 234-240 MW plus Microsoft's 700 MW second-phase option equals about 0.94 GW. That is a strong explanation for the order of magnitude, but it should be labeled optional until exercise evidence appears.
- Dedupe posture: Narvik and Loughton should be flagged against `openai_microsoft_fairwater_international`; Ward County/Cedarvale appears ex-Epoch in the local snapshot; Sines has no disclosed MW and should not be converted without adjudication.
- Delivery timing: Sines begins Q1 2026; Narvik staged services begin 2026 and expanded Rubin deployment is 2027; Texas Microsoft services begin Q3 2026; Loughton GB300 delivery is Q1 2027; Texas option starts late 2027.
- Basis: primary sources use a mix of facility MW, site capacity, GPU counts, and service-delivery timing. This dispatch carries facility MW only where sources disclose site power; Sines remains GPU-only except for a clearly marked inference in the aggregate range.
