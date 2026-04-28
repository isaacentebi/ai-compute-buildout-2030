# Rev-4.2 Research Dispatch B4: Microsoft Fairwater

accessed_date: 2026-04-28

## TL;DR

Microsoft Fairwater is a real Azure AI superfactory program, not a single
customer contract. The U.S. sites are already represented in local Epoch context:
Fairwater Wisconsin at 0.555 GW facility operational plus 2.773 GW remaining
buildout to 3.328 GW by 2027-10-03, and Fairwater Atlanta at 0.433 GW
operational plus 0.426 GW remaining buildout to 0.859 GW by 2026-05-14.
Microsoft primary sources do not disclose site MW for either U.S. site; the MW
figures are Epoch estimates using site evidence and Microsoft disclosures.

The international Fairwater / Nscale question should be carried as an overlap
candidate, not resolved here. Primary sources name Narvik and Loughton, but the
strongest current primary MW anchors are narrower than the current canonical
0.805 GW facility midpoint for `openai_microsoft_fairwater_international`:
Narvik has 230 MW secured grid/campus capacity with another 290 MW in queue or
ambition, and Loughton has 50 MW of AI capacity scalable to 90 MW. That implies
about 0.280 GW named near-term facility/AI capacity and up to about 0.610 GW if
Narvik's queued/ambition expansion and Loughton's scale-up are counted. Do not
adjudicate the canonical row here; flag the mismatch for adjudication.

Attribution is mixed by design. Microsoft says Fairwater powers OpenAI,
Microsoft AI, Copilot, and other workloads. OpenAI's April 27, 2026 partnership
update says Microsoft remains OpenAI's primary cloud partner but OpenAI can serve
products across any cloud. Narvik is especially attribution-sensitive: OpenAI
announced Stargate Norway in July 2025 as an OpenAI for Countries site with an
initial offtake option; Microsoft/Nscale/Aker later announced a Microsoft
five-year agreement, and Nscale's April 14, 2026 update says Narvik will add more
than 30,000 NVIDIA Rubin GPUs for Microsoft in 2027.

## Evidence Notes

- Microsoft introduced Wisconsin Fairwater on September 18, 2025 as its newest
  U.S. AI datacenter, with multiple identical U.S. Fairwater datacenters under
  construction; it also named Narvik and Loughton as related AI datacenter
  projects.
- Microsoft says Wisconsin covers 315 acres and three buildings totaling 1.2
  million square feet, and separately says it was on track in September 2025 to
  bring the initial Wisconsin AI datacenter online in early 2026. Microsoft Local
  said in March 2026 that Phase 1 was nearing completion and Phase 2 was
  scheduled for early 2028.
- Microsoft unveiled Atlanta on November 12, 2025 as the next Fairwater Azure AI
  datacenter site; Microsoft Source says the Atlanta site began operation in
  October 2025 and connects to Wisconsin through the AI WAN.
- Microsoft describes Fairwater workloads as OpenAI, Microsoft AI, Copilot, and
  other leading AI workloads; this supports shared attribution, not a clean
  OpenAI-only allocation.
- Nscale's October 15, 2025 Microsoft release says the broader Microsoft/Nscale
  package spans four countries and two continents: Texas 240 MW with a Microsoft
  700 MW second-phase option, Portugal/Sines GPUs from Q1 2026, Loughton
  50 MW scalable to 90 MW from Q1 2027, and Narvik about 52,000 GB300 GPUs under
  the Aker-Nscale JV.
- Aker's Q3 2025 investor presentation is the strongest primary-like Narvik
  capacity source found: 230 MW secured grid capacity at Kvandal/Narvik,
  construction ongoing, 200+90 MW in queue, 100% hydropower, a USD 6.2 billion
  five-year Microsoft contract, and first deployment phases targeted from August
  2026 onward.
- Nscale's March 9, 2026 Series C release says the Aker-Nscale JV is being
  rolled fully into Nscale, with projects continuing. Nscale's April 14, 2026
  Norway release says the 230 MW Narvik campus will add more than 30,000 NVIDIA
  Rubin GPUs for Microsoft in 2027 and will be solely managed by Nscale.

```yaml
counterparty: "Microsoft / OpenAI / Nscale / Aker"
contract_overview:
  type: cloud capacity
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2025-10-01, central: 2027-01-01, latest: 2028-12-31}
  exclusivity_or_optionality: >
    Fairwater is Microsoft-operated Azure AI infrastructure serving multiple
    workloads. OpenAI remains a primary Microsoft cloud partner, but the April
    27, 2026 amended agreement makes Microsoft's OpenAI IP license non-exclusive
    and allows OpenAI products to be served across any cloud. Nscale sites add
    operator/tenant overlap and Microsoft option language, especially Texas and
    Narvik.
atoms:
  - id: atom:microsoft_fairwater_wisconsin_epoch_overlap
    site: "Microsoft Fairwater Wisconsin, Mount Pleasant, WI"
    operator: Microsoft
    user_or_anchor: "OpenAI / Microsoft"
    gw_facility: 3.328
    gw_it: 2.869
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2026-04-16, central: 2027-10-03, latest: 2028-03-31}
    operational_status: "T1 operational 0.555 GW; T2 buildout candidate 2.773 GW"
    exact_quote: "largest and most sophisticated AI factory we've built yet"
    source_url: https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
    source_publisher: Microsoft
    source_publication_date: 2025-09-18
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Microsoft Fairwater Wisconsin"
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: 3.328
        overlap_evidence: >
          Local canonical atoms carry 0.555 GW operational and 2.773 GW
          remaining buildout to 3.328 GW facility by 2027-10-03. Epoch's public
          note says Fairwater Wisconsin is projected to consume 3.3 GW by late
          2027. Candidate should be counted once as the Epoch site, not again as
          a generic OpenAI/Microsoft commitment.
    risks:
      counterparty: "Low Microsoft credit risk; attribution between OpenAI and Microsoft internal workloads remains mixed."
      regulatory: "Medium: local construction/community scrutiny and phase changes; Caledonia work is separate but shows regional siting sensitivity."
      power_interconnect: "High: multi-GW WE Energies/MISO load; Microsoft says it prepays energy/electrical infrastructure and will match fossil generation with carbon-free energy."
      supply_chain: "High: hundreds of thousands of NVIDIA GPUs, liquid cooling, transformers, switchgear, and fiber."
      technology: "Medium: Fairwater is dense two-story Blackwell-era design; future Rubin-era changes may affect later buildings."
      financing: "Low for Microsoft-funded U.S. site; exact site-level capex beyond $7B Wisconsin public commitment is not fully disclosed."
      structural_optionality: "Medium: Microsoft Local Phase 2 early-2028 schedule differs from Epoch late-2027 estimate."
  - id: atom:microsoft_fairwater_atlanta_epoch_overlap
    site: "Microsoft Fairwater Atlanta, GA"
    operator: "Microsoft / QTS-built campus per local Epoch notes"
    user_or_anchor: "OpenAI / Microsoft"
    gw_facility: 0.859
    gw_it: 0.741
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2025-10-01, central: 2026-05-14, latest: 2026-12-31}
    operational_status: "T1 operational 0.433 GW; T2 buildout candidate 0.426 GW"
    exact_quote: "began operation in October"
    source_url: https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/
    source_publisher: Microsoft Source
    source_publication_date: 2025-11-12
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Microsoft Fairwater Atlanta"
        epoch_attributed_to: "Microsoft -> OpenAI #speculative"
        overlap_gw_facility: 0.859
        overlap_evidence: >
          Local canonical atoms carry 0.433 GW operational and 0.426 GW
          remaining buildout to 0.859 GW facility by 2026-05-14. Microsoft
          primary confirms Atlanta is the next Fairwater site and began
          operation in October 2025, but does not disclose MW.
    risks:
      counterparty: "Low Microsoft credit risk; QTS/operator ownership mechanics should be checked before assigning operator economics."
      regulatory: "Medium: Atlanta power/land constraints are not documented in Microsoft primary source."
      power_interconnect: "Medium-high: Microsoft says Atlanta was selected for resilient utility power, but no interconnection filing was extracted here."
      supply_chain: "Medium: Blackwell GPU and liquid-cooling supply chain."
      technology: "Medium: same Fairwater architecture as Wisconsin."
      financing: "Medium-low: Microsoft primary does not disclose Atlanta capex or lease structure."
      structural_optionality: "Medium: Microsoft primary gives operational status but no per-building MW."
  - id: atom:fairwater_narvik_nscale_microsoft_candidate
    site: "Kvandal/Narvik, Norway"
    operator: "Nscale; formerly Aker-Nscale JV, Aker shareholder"
    user_or_anchor: "Microsoft; OpenAI initial offtake option / Stargate Norway candidate"
    gw_facility: [0.230, 0.230, 0.520]
    gw_it: null
    basis: facility_MW
    pue_assumed: null
    energization_window: {earliest: 2026-08-01, central: 2027-01-01, latest: null}
    operational_status: "T2/T3 candidate; not final-adjudicated"
    exact_quote: "230MW secured grid capacity"
    source_url: https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/11/04/658641_Aker_ASA_3Q_2025_Presentation.pdf?VersionId=SRe3eE4FHa.5Qjn31MKeyHvs7kD5nUMN
    source_publisher: Aker ASA Q3 2025 presentation
    source_publication_date: 2025-11-04
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "openai_microsoft_fairwater_international"
        epoch_attributed_to: "Microsoft -> OpenAI / Microsoft"
        overlap_gw_facility: 0.805
        overlap_evidence: >
          Current canonical international Fairwater row groups Narvik and
          Loughton at 0.805 GW facility midpoint, with 0.460-1.725 GW range.
          Newer primary sources disclose 230 MW secured at Narvik and 50 MW
          scalable to 90 MW at Loughton; this is a candidate contradiction, not
          adjudicated here.
      - epoch_site: "Nscale/Fairwater overlap adjustment"
        epoch_attributed_to: "Nscale / Microsoft"
        overlap_gw_facility: 0.600
        overlap_evidence: >
          Local canonical atom excludes 0.600 GW Nscale Narvik/Loughton overlap
          and attributes it to Fairwater. Primary Nscale sources confirm Nscale
          is the Narvik operator and Microsoft anchor; exact dedupe amount needs
          adjudication.
    risks:
      counterparty: "Medium: private Nscale execution, though Microsoft anchor and Aker shareholder support are strong."
      regulatory: "Medium: Norway sovereign/renewable positioning is favorable, but local permitting and grid expansion beyond 230 MW remain open."
      power_interconnect: "Medium-low for 230 MW secured; high for 200+90 MW queued expansion."
      supply_chain: "High: GB300 and Rubin GPU rollout, direct-liquid cooling, and grid equipment."
      technology: "Medium-high: April 2026 update shifts part of deployment to NVIDIA Rubin in 2027."
      financing: "Medium: Aker presentation references GPU/data-center leverage targets and possible customer prepayments; Nscale raised $2B Series C."
      structural_optionality: "High: OpenAI initial offtake option, Microsoft expansion, Aker JV roll-up, and queued power create nontrivial allocation optionality."
  - id: atom:fairwater_loughton_nscale_microsoft_candidate
    site: "Nscale Loughton AI Campus, UK"
    operator: Nscale
    user_or_anchor: Microsoft Azure
    gw_facility: [0.050, 0.050, 0.090]
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2027-01-01, central: 2027-03-31, latest: 2027-12-31}
    operational_status: "T2 candidate; not final-adjudicated"
    exact_quote: "50MW of AI capacity, scalable to 90MW"
    source_url: https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement
    source_publisher: Nscale
    source_publication_date: 2025-09-16
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "openai_microsoft_fairwater_international"
        epoch_attributed_to: "Microsoft -> OpenAI / Microsoft"
        overlap_gw_facility: 0.805
        overlap_evidence: >
          Loughton is one of the two sites grouped in the current international
          Fairwater atom. Nscale and Microsoft primary sources support 23,000+
          GPUs at Loughton but only 50 MW scalable to 90 MW, not a 100-500 MW
          primary-disclosed site.
      - epoch_site: "Stargate UK / OpenAI-Nscale candidate"
        epoch_attributed_to: "OpenAI / Nscale / NVIDIA"
        overlap_gw_facility: null
        overlap_evidence: >
          Nscale's same UK announcement separately describes Stargate UK with
          OpenAI exploring offtake up to 8,000 GPUs in Q1 2026 and up to 31,000
          over time at UK sites including Cobalt Park. Keep distinct from
          Microsoft Loughton unless later evidence merges the workloads.
    risks:
      counterparty: "Medium: private Nscale, but Microsoft anchor and UK sovereign AI policy support."
      regulatory: "Medium-high: UK grid/planning constraints; current site scale is small versus global Fairwater sites."
      power_interconnect: "Medium for 50 MW; high for expansion beyond 90 MW or any broader UK Stargate allocation."
      supply_chain: "Medium-high: 23,040 GB300 GPUs delivered in Q1 2027 per Nscale."
      technology: "Medium: direct-liquid cooling and high-density GPU campus."
      financing: "Medium: Nscale private financing; Microsoft $30B UK envelope includes $15B capex but does not isolate Loughton."
      structural_optionality: "Medium-high: Q4 2026 live target in Jan. 2025 became Q1 2027 GPU delivery in Sep./Oct. 2025 sources."
contradictions:
  - "Microsoft primary sources name Wisconsin, Atlanta, Narvik, and Loughton but do not disclose U.S. site MW; local Epoch assigns Wisconsin 3.328 GW facility and Atlanta 0.859 GW facility."
  - "Current canonical international Fairwater row is 0.805 GW facility midpoint for Narvik+Loughton; current primary sources found here support 0.280 GW named near-term capacity and up to 0.610 GW if stated scale-ups/queues are counted."
  - "OpenAI July 2025 says Stargate Norway is OpenAI's first European AI data center initiative with OpenAI as an initial offtaker option; Microsoft/Nscale/Aker sources later describe a USD 6.2B five-year Microsoft contract and April 2026 Microsoft Rubin expansion at the same Narvik campus."
  - "Microsoft Local March 2026 says Mount Pleasant Phase 2 is scheduled for early 2028; local Epoch context estimates the fourth Wisconsin building operational by 2027-10-03."
  - "Nscale January 2025 said Loughton was scheduled to be live in Q4 2026 and could house up to 45,000 GB200 GPUs; September/October 2025 Microsoft/Nscale disclosures say 23,040/23,000 GB300 GPUs from Q1 2027."
gaps:
  - "Pull Wisconsin utility/MISO/WE Energies load-service documents that underpin Epoch's 3.3 GW estimate and map Phase 1/2/3 to Microsoft Local construction phases."
  - "Extract Atlanta/QTS permits, substation filings, or utility load requests to validate the 0.859 GW Epoch estimate."
  - "Resolve Narvik allocation among OpenAI Stargate Norway, Microsoft 52,000 GB300 GPUs, and Microsoft >30,000 Rubin GPUs: additive, replacement, or phased within the same 230 MW."
  - "Classify Narvik tier strength after deciding whether Aker's USD 6.2B five-year Microsoft contract plus generic take-or-pay slide language is sufficient for T3 or should remain T2/T4."
  - "Confirm whether the current `openai_microsoft_fairwater_international` 0.805 GW facility midpoint should be revised to named primary MW anchors or retained as a broader Fairwater-style estimate."
  - "Check Nscale Texas/Sines capacity against `nscale_microsoft_contract_capacity`; these are Nscale/Microsoft neocloud overlaps, but not Fairwater sites based on current primary naming."
```

## Neocloud / Operator Overlap Candidates

- **Nscale:** Strong direct overlap. Nscale operates Loughton and Narvik, is the
  Microsoft counterparty for broader 200,000-GPU capacity, and is already
  represented locally by `nscale_microsoft_contract_capacity` plus
  `nscale_fairwater_overlap_adjustment`. The Fairwater dispatch should flag
  Narvik/Loughton for adjudication against both the Microsoft Fairwater row and
  Nscale neocloud rows.
- **CoreWeave:** No direct Fairwater site overlap found. CoreWeave remains a
  Microsoft neocloud capacity overlap elsewhere in the repo, but not tied by
  primary sources to Wisconsin, Atlanta, Narvik, or Loughton Fairwater.
- **Lambda:** No direct Fairwater site overlap found. Lambda's Microsoft/NVIDIA
  capacity should stay separate unless a later source names Fairwater deployment
  or AI WAN integration.

## International Site Strength Candidates

| Site | Primary MW/GPU anchor | Status / timing | Candidate strength |
| --- | --- | --- | --- |
| Narvik/Kvandal | 230 MW secured grid capacity; 200+90 MW queue; 52,000 GB300 Microsoft GPUs; >30,000 Rubin GPUs in 2027 | Construction ongoing in Aker Q3 2025; staged services from 2026; Microsoft Rubin expansion in 2027 | Strongest international Fairwater candidate; T2/T3 candidate, not final |
| Loughton | 50 MW AI capacity scalable to 90 MW; 23,040 GB300 GPUs in Q1 2027 | Site acquired; Q4 2026 target slipped to Q1 2027 GPU delivery | Named and primary-supported, but much smaller MW anchor |
| Sines / Texas under Nscale-Microsoft | Texas 240 MW with 700 MW Microsoft option; Sines 12,600 GB300 GPUs from Q1 2026 | Nscale/Microsoft primary announcement | Nscale neocloud overlap, not Fairwater-named in primary sources |

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [Microsoft Official Blog, "Inside the world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Names Wisconsin Fairwater, multiple U.S. Fairwaters, Narvik, Loughton, AI WAN, OpenAI/Microsoft/Copilot workload attribution. | "power OpenAI, Microsoft AI" | 2026-04-28 |
| [Microsoft On the Issues, "Made in Wisconsin"](https://blogs.microsoft.com/on-the-issues/2025/09/18/made-in-wisconsin-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Wisconsin construction timing, $3.3B initial plus $4B additional investment, early-2026 online target. | "online in early 2026" | 2026-04-28 |
| [Microsoft Local, "Mount Pleasant datacenter project update"](https://local.microsoft.com/blog/mount-pleasant-datacenter-project-update/) | 2026-03-01 | Primary local project update | March 2026 construction status: Phase 1 nearing completion, Phase 2 early-2028 schedule. | "Phase 1 is anticipated" | 2026-04-28 |
| [Microsoft Official Blog, "Infinite scale"](https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/) | 2025-11-12 | Primary company announcement | Atlanta unveiled as next Fairwater site; Fairwater architecture, AI WAN, GB200/GB300, cooling and power design. | "next Fairwater site" | 2026-04-28 |
| [Microsoft Source, "From Wisconsin to Atlanta"](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | 2025-11-12 | Primary company feature | Atlanta began operation in October 2025; AI WAN 120,000 miles; Fairwater supports OpenAI/Microsoft AI/Copilot. | "began operation in October" | 2026-04-28 |
| [OpenAI, "The next phase of the Microsoft OpenAI partnership"](https://openai.com/index/next-phase-of-microsoft-partnership/) | 2026-04-27 | Primary company announcement | Current OpenAI/Microsoft attribution and cloud rights. | "primary cloud partner" | 2026-04-28 |
| [OpenAI, "Introducing Stargate Norway"](https://openai.com/index/introducing-stargate-norway/) | 2025-07-31 | Primary company announcement | Original Narvik/OpenAI attribution, 230 MW + 290 MW ambition, 100,000 GPUs by end-2026, Nscale/Aker JV. | "230MW of capacity" | 2026-04-28 |
| [Microsoft Source EMEA, "The port town in Norway emerging as an AI hub"](https://news.microsoft.com/source/emea/features/the-port-town-in-norway-emerging-as-an-ai-hub/) | 2025-09-17 | Primary company feature | Microsoft/Nscale/Aker Narvik deal, $6.2B estimate, five-year agreement, staged services commencing 2026. | "five-year agreement" | 2026-04-28 |
| [Nscale, "UK AI infrastructure commitment"](https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement) | 2025-09-16 | Primary company announcement | Loughton 50 MW scalable to 90 MW, 23,040 GB300 GPUs in Q1 2027, Microsoft/Nscale and separate Stargate UK/OpenAI paths. | "50MW of AI capacity" | 2026-04-28 |
| [Microsoft On the Issues, "$30 billion in UK"](https://blogs.microsoft.com/on-the-issues/2025/09/16/microsoft-30-billion-uk-ai-future/) | 2025-09-16 | Primary company announcement | Microsoft UK envelope and Nscale supercomputer partnership with 23,000+ GPUs. | "largest supercomputer" | 2026-04-28 |
| [Nscale, "Nscale Microsoft 2025"](https://www.nscale.com/press-releases/nscale-microsoft-2025) | 2025-10-15 | Primary company announcement | Broader 200,000-GPU Microsoft/Nscale package; Texas 240 MW plus option, Sines, Loughton, Narvik. | "four countries and two continents" | 2026-04-28 |
| [Aker ASA Q3 2025 presentation](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/11/04/658641_Aker_ASA_3Q_2025_Presentation.pdf?VersionId=SRe3eE4FHa.5Qjn31MKeyHvs7kD5nUMN) | 2025-11-04 | Public-company investor presentation | Narvik/Kvandal 230 MW secured, 200+90 MW queue, construction ongoing, Microsoft $6.2B five-year contract, take-or-pay model language. | "USD 6.2billion" | 2026-04-28 |
| [Nscale, "Series C"](https://www.nscale.com/press-releases/nscale-series-c) | 2026-03-09 | Primary company announcement | Nscale $2B Series C, Aker JV roll-up into Nscale, project continuity. | "roll the Aker Nscale joint venture" | 2026-04-28 |
| [Nscale, "expanded deal with Microsoft in Norway"](https://www.nscale.com/press-releases/nscale-microsoft-norway) | 2026-04-14 | Primary company announcement | Narvik 230 MW campus adds >30,000 Rubin GPUs for Microsoft in 2027; solely managed by Nscale. | "230 MW Nscale Narvik campus" | 2026-04-28 |
| [Epoch AI, "Fairwater power usage"](https://epoch.ai/data-insights/fairwater-power-usage) | 2025-11-26 | Local/Epoch public context | Public Epoch support for 3.3 GW Wisconsin estimate and late-2027 fourth-building timing. | "3.3 GW of power" | 2026-04-28 |
| Local repo: `canonical_capacity_atoms.yaml`, `epoch_data_centers/*`, `compute_commitments_overlay.yaml`, `neocloud_overlay.yaml` | 2026-04-20 to 2026-04-25 | Local atom/Epoch context | Current Fairwater and Nscale atom values, dedupe groups, evidence tiers, and overlap adjustments. | "Fairwater Narvik and Loughton" | 2026-04-28 |
