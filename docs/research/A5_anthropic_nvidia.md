# Rev-4.2 Research Dispatch A5: Anthropic-NVIDIA

accessed_date: 2026-04-28

## Bottom Line

The public Anthropic-NVIDIA relationship is not a standalone NVIDIA-owned data-center capacity atom. The capacity-bearing candidate is a Microsoft Azure commitment: Anthropic committed to purchase $30B of Azure compute and to contract up to 1 GW of additional compute on NVIDIA Grace Blackwell and Vera Rubin systems. NVIDIA's direct role is equity plus architecture/model co-design; Microsoft is the cloud/operator counterparty.

This candidate should remain flagged, not adjudicated. It has no disclosed site, no explicit energization date, and high overlap risk with Microsoft AI WAN / Fairwater capacity already in Epoch. It also sits alongside larger Anthropic capacity programs with AWS Trainium, Google/Broadcom TPUs, and Fluidstack-built U.S. data centers, so NVIDIA/Azure should not be treated as Anthropic's only or primary scaling path.

```yaml
counterparty: Anthropic-NVIDIA via Microsoft Azure
contract_overview:
  type: cloud capacity + chip/architecture support
  term_years: null
  announced_capex_usd_b: null
  announced_compute_capacity_usd_b: 30.0
  delivery_window: {earliest: null, central: null, latest: null}
  exclusivity_or_optionality: >
    Non-exclusive. Anthropic says it uses AWS Trainium, Google TPUs, and
    NVIDIA GPUs, while Amazon remains its primary cloud provider and
    training partner. NVIDIA and Microsoft also committed to invest up to
    $10B and $5B respectively in Anthropic, but the public source does
    not make NVIDIA the site owner or cloud operator.
atoms:
  - id: atom:anthropic_microsoft_nvidia_azure_1gw_candidate
    site: Azure sites not disclosed
    operator: Microsoft Azure
    user_or_anchor: Anthropic
    gw_facility: [0.00, 1.18, 1.18]
    gw_it: 1.00
    basis: ambiguous_compute
    pue_assumed: 1.18
    energization_window: {earliest: null, central: null, latest: null}
    operational_status: T5
    exact_quote: "up to one gigawatt of compute capacity"
    source_url: https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/
    source_publisher: Microsoft
    source_publication_date: 2025-11-18
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: Microsoft Fairwater Wisconsin
        epoch_attributed_to: Microsoft / OpenAI / Microsoft AI WAN
        overlap_gw_facility: 3.328
        overlap_evidence: >
          Local Epoch snapshot shows Microsoft-owned Fairwater Wisconsin
          at 555 MW current and 3.328 GW full buildout by 2027-10-03.
          Because the Azure-Anthropic release names no sites, this capacity
          could be carved from Microsoft's already-counted AI WAN footprint.
      - epoch_site: Microsoft Fairwater Atlanta
        epoch_attributed_to: Microsoft / OpenAI / Microsoft AI WAN
        overlap_gw_facility: 0.859
        overlap_evidence: >
          Local Epoch snapshot shows Microsoft-owned Fairwater Atlanta at
          433 MW current and 859 MW full buildout by 2026-05-14. The
          site uses the same Microsoft/NVIDIA AI-superfactory pattern, but
          no public source ties Anthropic specifically to this site.
      - epoch_site: Microsoft Goodyear
        epoch_attributed_to: Microsoft / OpenAI
        overlap_gw_facility: 0.263
        overlap_evidence: >
          Local Epoch snapshot shows Microsoft Goodyear at 263 MW full
          buildout as of 2025-11-12. It is a possible Azure capacity pool,
          not an evidenced Anthropic site.
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: Fluidstack / Anthropic, G42
        overlap_gw_facility: 0.509
        overlap_evidence: >
          Not a Microsoft overlap, but a same-customer overlap risk. Local
          Epoch shows Fluidstack Lake Mariner at 509 MW full buildout, and
          the repo overlay treats Anthropic/Fluidstack and Anthropic
          Google/Broadcom as potentially the same physical TPU program.
    risks:
      counterparty: >
        Public source does not disclose whether Anthropic has take-or-pay
        obligations, minimum utilization, cancellation rights, or whether
        NVIDIA's $10B investment is conditioned on deployment milestones.
      regulatory: >
        Circular AI financing and cross-investment scrutiny risk: NVIDIA
        and Microsoft invest in Anthropic while Anthropic buys compute
        capacity powered by NVIDIA systems on Microsoft Azure.
      power_interconnect: >
        No site, utility, interconnect queue position, or power procurement
        disclosed for the 1 GW. Treat as cloud allocation until physical
        site evidence appears.
      supply_chain: >
        Capacity depends on Microsoft receiving and integrating Grace
        Blackwell and Vera Rubin systems at scale. Microsoft separately
        said Vera Rubin NVL72 would roll into modern liquid-cooled Azure
        datacenters over the next few months, but that statement is not
        Anthropic-specific.
      technology: >
        Anthropic is explicitly multi-platform. NVIDIA co-optimization may
        improve performance/TCO, but Anthropic can shift workloads across
        AWS Trainium, Google TPUs, and NVIDIA GPUs.
      financing: >
        The headline combines $30B Azure purchase capacity with up to $15B
        supplier/cloud equity commitments; the release does not publish a
        cash-flow schedule.
      structural_optionality: >
        "Up to" 1 GW and no site disclosure make the atom option-like. The
        low case is zero incremental physical GW if it is an allocation
        inside existing Microsoft AI capacity.
contradictions:
  - >
    Microsoft frames the Azure/NVIDIA commitment as up to 1 GW, while
    Anthropic's later AWS announcement says Amazon remains its primary
    training and cloud provider and secures up to 5 GW of AWS capacity.
    This is not a contradiction in contract terms, but it argues against
    treating NVIDIA/Azure as exclusive or as Anthropic's primary capacity
    path.
  - >
    Anthropic's Google/Broadcom TPU release says multiple GW starting in
    2027 and calls the U.S. siting a major expansion of the November 2025
    $50B Fluidstack infrastructure commitment. That creates same-customer
    capacity overlap risk if the Azure/NVIDIA 1 GW is added without
    checking physical sites.
  - >
    The local canonical ledger already carries anthropic_azure_incremental_capacity
    as 1.0 GW IT / 1.18 GW facility, but its own range floors at zero
    because no sites are named.
gaps:
  - >
    Need contract terms or Microsoft/Anthropic filings showing whether
    $30B is committed spend, cancellable cloud credits, take-or-pay, or
    a framework agreement.
  - >
    Need site-level Azure evidence: region, data-center campus, utility
    filings, delivery schedule, or whether the 1 GW is a carve-out from
    Fairwater/Goodyear capacity.
  - >
    Need NVIDIA investment term sheet or closing disclosure to determine
    whether equity funds recycle into Azure/NVIDIA system purchases.
  - >
    Need workload allocation split across AWS Trainium, Google TPUs,
    NVIDIA GPUs, and Fluidstack-built sites to avoid double counting
    Anthropic demand as multiple independent physical GW commitments.
```

## Evidence Notes

- Microsoft primary source, 2025-11-18: Anthropic committed to purchase "$30 billion of Azure compute capacity" and "additional compute capacity up to one gigawatt"; the same post says the compute commitment initially uses NVIDIA Grace Blackwell and Vera Rubin systems and that NVIDIA/Microsoft would invest up to $10B/$5B in Anthropic.
- NVIDIA direct role: the Microsoft source describes a first deep technology partnership for NVIDIA and Anthropic to optimize Anthropic models and future NVIDIA architectures. It does not identify NVIDIA as the data-center operator, lessor, power buyer, or capacity seller.
- Microsoft/NVIDIA infrastructure context: Microsoft said on 2026-03-16 that it had deployed hundreds of thousands of liquid-cooled Grace Blackwell GPUs and was rolling Vera Rubin NVL72 into modern liquid-cooled Azure datacenters over the next few months. This supports Azure platform readiness, not Anthropic-specific energization.
- Anthropic AWS overlap: Anthropic's 2026-04-20 source says Amazon secures up to 5 GW for Claude, nearly 1 GW total by end-2026, more than $100B over ten years, and that AWS remains Anthropic's primary training/cloud provider.
- Anthropic Google/Broadcom/Fluidstack overlap: Anthropic's 2025-10-23 Google TPU source says up to one million TPUs and well over 1 GW online in 2026. Its 2026-04-06 Google/Broadcom source says multiple GW starting in 2027 and that most new compute is a major expansion of the November 2025 $50B U.S. infrastructure commitment. Anthropic's 2025-11-12 Fluidstack source says $50B of data centers in Texas and New York with sites online throughout 2026, but no MW.

## Local Atom Context Used

- `canonical_capacity_atoms.yaml`: `anthropic_azure_incremental_capacity` already exists as 1.0 GW IT / 1.18 GW facility, T5, with low/high facility range 0-1.18 GW and note "no sites named, so range floors at zero."
- `compute_commitments_overlay.yaml`: Anthropic-Azure is Class A because GW is disclosed, but no site is named. Anthropic-Google/Broadcom is Class B chip procurement and overlaps the Fluidstack infrastructure envelope. Anthropic-AWS is a separate 5 GW physical-capacity commitment with partial Epoch overlap.
- `epoch_data_centers/compiled.json`: relevant overlap candidates include Microsoft Fairwater Wisconsin (3.328 GW buildout), Microsoft Fairwater Atlanta (0.859 GW), Microsoft Goodyear (0.263 GW), Anthropic-Amazon New Carlisle (1.229 GW), Amazon Madison Mega Site (0.819 GW), Amazon Ridgeland (1.008 GW), and Fluidstack Lake Mariner (0.509 GW).

## Source Register

| Publisher | Date | URL | Use |
| --- | --- | --- | --- |
| Microsoft | 2025-11-18 | https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/ | Primary source for Azure/NVIDIA/Anthropic 1 GW candidate, $30B Azure capacity, NVIDIA/Microsoft equity commitments. |
| Microsoft | 2026-03-16 | https://blogs.microsoft.com/blog/2026/03/16/microsoft-at-nvidia-gtc-new-solutions-for-microsoft-foundry-azure-ai-infrastructure-and-physical-ai/ | Azure Grace Blackwell / Vera Rubin readiness context; not Anthropic-specific. |
| Anthropic | 2026-04-20 | https://www.anthropic.com/news/anthropic-amazon-compute | Primary source for AWS 5 GW overlap/context and AWS primary-provider language. |
| Anthropic | 2025-10-23 | https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services | Primary source for up to 1M TPUs, well over 1 GW in 2026, and multi-platform strategy. |
| Anthropic | 2026-04-06 | https://www.anthropic.com/news/google-broadcom-partnership-compute | Primary source for Google/Broadcom multiple-GW TPU capacity starting 2027 and connection to the $50B U.S. infrastructure commitment. |
| Google Cloud | 2026-04-06 | https://www.googlecloudpresscorner.com/2026-04-06-Anthropic-Expands-Use-of-Google-Cloud-and-TPUs | Primary corroboration for multiple GW of TPU capacity starting 2027. |
| Anthropic | 2025-11-12 | https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure | Primary source for $50B Fluidstack-built Texas/New York infrastructure and 2026 online language. |
| Fluidstack | 2025-11-12 | https://www.fluidstack.io/about-us/blog/fluidstack-selected-by-anthropic-to-deliver-custom-data-centers-in-the-us | Primary corroboration for Fluidstack custom data centers and rapid delivery/gigawatts language. |
| Epoch AI local snapshot | 2026-04-20 | https://epoch.ai/data/data-centers | Local Epoch overlap candidates from `epoch_data_centers/compiled.json`; repo snapshot retrieved 2026-04-22, reviewed 2026-04-28. |
