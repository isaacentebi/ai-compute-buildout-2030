# A2 Research Dispatch: Anthropic-Azure / Microsoft-NVIDIA-Anthropic

```yaml
counterparty: Anthropic / Microsoft Azure / NVIDIA
contract_overview:
  type: cloud capacity
  term_years: null
  announced_capex_usd_b: null
  announced_contract_value_usd_b: 30
  delivery_window: {earliest: null, central: null, latest: null}
  exclusivity_or_optionality: >
    Non-exclusive cloud-capacity commitment. Anthropic says Amazon remains its
    primary cloud provider and training partner; the Microsoft/NVIDIA agreement
    adds Azure capacity, Microsoft Foundry/Copilot distribution, NVIDIA
    co-engineering, and up-to-$15B equity investment. The 1 GW language is an
    "up to" compute-capacity ceiling, with no named site and no primary-source
    term length.
atoms:
  - id: atom:anthropic_azure_2025_11_18
    site: "Azure sites not disclosed"
    operator: Microsoft Azure
    user_or_anchor: Anthropic
    gw_facility: [0, 1.18]
    gw_it: 1.0
    basis: ambiguous_compute
    pue_assumed: 1.18
    energization_window: {earliest: null, central: 2026-12-31, latest: null}
    operational_status: unknown
    exact_quote: "up to one gigawatt of compute capacity"
    source_url: https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/
    source_publisher: Microsoft
    source_publication_date: 2025-11-18
    accessed_date: 2026-04-28
    source_notes:
      - "Microsoft says Anthropic committed to purchase '$30 billion of Azure compute capacity' and to contract additional capacity up to 1 GW."
      - "Microsoft/Anthropic identify NVIDIA Grace Blackwell and Vera Rubin systems; they do not disclose the site, region, utility, PPA, or contract tenor."
      - "2026-12-31 central energization is an inference from NVIDIA's Jan. 5, 2026 Rubin release saying Microsoft is among first cloud providers to deploy Vera Rubin-based instances in 2026; it is not in the Nov. 18 agreement."
    contract_structure:
      cloud_purchase_commitment_usd_b: 30
      microsoft_equity_commitment_usd_b: 5
      nvidia_equity_commitment_usd_b: 10
      nvidia_systems: ["Grace Blackwell", "Vera Rubin"]
      distribution: ["Microsoft Foundry", "GitHub Copilot", "Microsoft 365 Copilot", "Copilot Studio"]
      co_engineering: "Anthropic and NVIDIA model/workload optimization plus future NVIDIA architecture optimization."
    epoch_site_overlap_candidates:
      - epoch_site: Microsoft Fairwater Wisconsin
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: 3.328
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Wisconsin buildout to 3.328 GW
          facility by 2027-10-03. Microsoft says Fairwater powers OpenAI,
          Microsoft AI, Copilot and other leading AI workloads; NVIDIA says
          Microsoft will deploy Vera Rubin systems in future Fairwater sites.
          Candidate only because Anthropic's Azure sites are undisclosed.
      - epoch_site: Microsoft Fairwater Atlanta
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.859
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Atlanta buildout to 0.859 GW
          facility by 2026-05-14. Microsoft says Atlanta is the second
          Fairwater site and shares the Wisconsin architecture; candidate only
          because Anthropic's 1 GW is Azure/NVIDIA compute with no site named.
      - epoch_site: Microsoft Goodyear
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.263
        overlap_evidence: >
          Local Epoch snapshot has 0.263 GW facility operational at Microsoft
          Goodyear. Plausible only as generic Azure AI capacity; no primary
          source ties Goodyear, Anthropic, Grace Blackwell, or Vera Rubin.
      - epoch_site: Crusoe Abilene Expansion
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Local Epoch snapshot carries a Microsoft-attributed 0.941 GW facility
          buildout by 2027-11-11 at Crusoe Abilene Expansion. Candidate is weak:
          the Anthropic announcement says Azure powered by NVIDIA, but does not
          name Crusoe, Abilene, or third-party colocation.
    risks:
      counterparty: "Anthropic is diversifying across AWS, Google/Broadcom TPUs, and Azure/NVIDIA; Azure is not primary cloud per Anthropic."
      regulatory: "No site disclosed, so local permitting, utility tariff, and state/local opposition risk cannot be assessed."
      power_interconnect: "No interconnection queue, utility, or region disclosed; if the 1 GW maps to Fairwater, grid risk is already embedded in Microsoft Epoch sites."
      supply_chain: "Depends on NVIDIA Grace Blackwell and Vera Rubin systems; NVIDIA cautions availability/timing statements are forward-looking."
      technology: "Vera Rubin is next-generation rack-scale infrastructure; deployment depends on liquid cooling, power density, and AI WAN readiness."
      financing: "The $30B is a customer compute-purchase commitment, not a disclosed site capex budget; Microsoft/NVIDIA equity commitments may be circular with cloud/GPU spend."
      structural_optionality: "'Up to' 1 GW and no named sites create high optionality; low bound is zero incremental physical GW if capacity is carved from existing Microsoft/Epoch sites."
contradictions:
  - "Microsoft/Anthropic primary announcement gives 1 GW of compute capacity but no site or delivery date; local canonical overlay currently records a 2028 expected-online year that is not primary-verified."
  - "Official sources frame this as additional Azure/NVIDIA capacity, while Anthropic's later Apr. 2026 posts continue to describe AWS as the primary cloud/training partner and Google/Broadcom as its most significant compute commitment to date."
gaps:
  - "Named Azure region/site allocation for the 1 GW."
  - "Whether the $30B cloud purchase and the up-to-1 GW compute capacity are the same commitment, overlapping tranches, or separate reservations."
  - "Contract tenor, minimum take-or-pay language, termination rights, and ramp schedule."
  - "Power basis: official language says compute capacity, not facility MW or IT MW."
  - "Whether any portion is served from Fairwater Wisconsin, Fairwater Atlanta, Goodyear, Crusoe Abilene Expansion, CoreWeave/Nebius/Nscale, or a future undisclosed Microsoft site."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [Microsoft Official Blog, "Microsoft, NVIDIA and Anthropic announce strategic partnerships"](https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/) | 2025-11-18 | Primary company announcement | $30B Azure compute purchase, up-to-1 GW additional compute, NVIDIA/Microsoft equity commitments, Grace Blackwell/Vera Rubin basis. | "purchase $30 billion of Azure compute capacity" | 2026-04-28 |
| [Anthropic, "Microsoft, NVIDIA, and Anthropic announce strategic partnerships"](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships) | 2025-11-18 | Primary company announcement | Same transaction; confirms AWS remains primary cloud/training partner. | "Amazon remains Anthropic's primary cloud provider" | 2026-04-28 |
| [NVIDIA Investor Relations, "NVIDIA Kicks Off the Next Generation of AI With Rubin"](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx) | 2026-01-05 | Primary company announcement | Rubin deployment timing and Microsoft/Fairwater link. | "deploy Vera Rubin-based instances in 2026" | 2026-04-28 |
| [Microsoft Azure Blog, "Microsoft's strategic AI datacenter planning enables seamless, large-scale NVIDIA Rubin deployments"](https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/) | 2026-01-05 | Primary company announcement | Fairwater Wisconsin/Atlanta and future sites are designed for Vera Rubin NVL72. | "current Fairwater sites in Wisconsin and Atlanta" | 2026-04-28 |
| [Microsoft Official Blog, "Inside the world's most powerful AI datacenter"](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/) | 2025-09-18 | Primary company announcement | Fairwater Wisconsin role, scale, workloads, and multiple identical U.S. Fairwater sites. | "multiple identical Fairwater datacenters under construction" | 2026-04-28 |
| [Microsoft Source, "From Wisconsin to Atlanta: Microsoft connects datacenters..."](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | 2025-11-12 | Primary company feature | Atlanta Fairwater operational timing, AI WAN, and distributed AI superfactory. | "began operation in October" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Microsoft Epoch overlap candidates: Fairwater Wisconsin 3.328 GW facility, Fairwater Atlanta 0.859 GW, Goodyear 0.263 GW, Crusoe Abilene Expansion 0.941 GW. | "Microsoft Fairwater Wisconsin" | 2026-04-28 |

## Research Notes

- Capacity basis: the official wording is "compute capacity" and "NVIDIA Grace Blackwell and Vera Rubin systems." I carry the disclosed figure as 1.0 GW IT-equivalent only because the repo's current canonical row uses that convention; the evidence itself is ambiguous_compute.
- Facility conversion: 1.0 GW IT x 1.18 PUE = 1.18 GW facility is a repo convention, not a primary disclosure.
- Delivery window: no primary source gives a Microsoft-Anthropic delivery date. The only primary timing anchor found is NVIDIA/Microsoft saying Vera Rubin deployments/instances begin in 2026, including Microsoft and future Fairwater sites.
- Incremental/dedupe posture: do not adjudicate. The low-bound overlap case is zero net-new physical GW if Azure allocates Anthropic onto already-counted Microsoft Epoch capacity; the high-bound case is 1.0 GW IT / 1.18 GW facility at undisclosed net-new Azure sites.
