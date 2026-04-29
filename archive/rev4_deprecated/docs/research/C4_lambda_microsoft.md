# Rev-4.2 Research Dispatch C4: Lambda-Microsoft / NVIDIA

accessed_date: 2026-04-28

## TL;DR

Lambda and Microsoft have a real multi-year, multibillion-dollar AI infrastructure agreement announced by Lambda on November 3, 2025. The public primary-source disclosure says Microsoft gets access to tens of thousands of NVIDIA GPUs, including GB300 NVL72 systems; it does not disclose a 320 MW capacity term, a named site, RPO, take-or-pay mechanics, or delivery tranches.

The repo's current `lambda_microsoft_contract` row should therefore be treated as a candidate overlay, not a primary-verified Microsoft building. Local overlay carries 320 MW facility / 256 MW IT at PUE 1.25 for "Lambda leased, signed, committed capacity"; public evidence supports Lambda's broader leased and planned footprint, including Prime LAX01 Vernon, Kansas City, EdgeConneX Chicago/Atlanta, Aligned DFW-04 Plano, ECL Mountain View, Cologix Columbus, and Allen, Texas. None of the reviewed public sources show Lambda operating an Epoch-counted Microsoft Fairwater, Goodyear, or Crusoe Abilene building.

## Evidence Notes

- Lambda's November 3, 2025 primary announcement says the Microsoft agreement is multibillion-dollar, multi-year, and includes tens of thousands of NVIDIA GPUs, including GB300 NVL72 systems. It gives no MW, site, lease tenor, or public contract value.
- Lambda's November 18, 2025 Series E announcement says it raised over $1.5B led by TWG Global with USIT and existing investors, and that the funding supports gigawatt-scale AI factories. This supports financing capacity, not a Microsoft-specific 320 MW term.
- Named Lambda site evidence is fragmented: Prime says Lambda will initially lease 21 MW at LAX01 Vernon; Lambda says Kansas City launches in early 2026 with 24 MW and can scale above 100 MW; EdgeConneX says 30+ MW across Chicago and Atlanta with a 23 MW Chicago RFS 2026 build-to-density facility; Aligned says Lambda will occupy DFW-04 in Plano but does not disclose MW in the release.
- DCD secondary reporting says Lambda operates out of 15 U.S. data centers, targets more than one million NVIDIA GPUs and 3 GW of liquid-cooled data center capacity, and lists known/expected Lambda locations. DCD also says the exact value and GPU count of the Microsoft deal were not shared.
- The 320 MW capacity basis appears to be a local Rev-4.2 overlay estimate from `neocloud_overlay.yaml` / `row_level_audit.csv`, not a public Lambda/Microsoft disclosure. Keep it as a research candidate for adjudication.

```yaml
counterparty: Lambda / Microsoft / NVIDIA
contract_overview:
  type: cloud capacity
  term_years: null
  announced_capex_usd_b: null
  announced_contract_value_usd_b: null
  delivery_window: {earliest: 2026-01-01, central: 2026-12-31, latest: null}
  exclusivity_or_optionality: >
    Multi-year Microsoft access to Lambda-deployed NVIDIA GPU infrastructure.
    Public primary sources do not disclose exclusivity, minimum take-or-pay,
    RPO, fixed MW, or site allocation. The 320 MW row is a local overlay
    candidate for Lambda leased/signed/committed capacity with Microsoft/NVIDIA
    anchors, not a primary-source contract term.
atoms:
  - id: atom:lambda_microsoft_contract_candidate_2025_11_03
    site: "Lambda leased/signed/committed capacity; sites not allocated to Microsoft publicly"
    operator: Lambda
    user_or_anchor: "Microsoft / NVIDIA"
    gw_facility: 0.320
    gw_it: 0.256
    basis: facility_MW
    pue_assumed: 1.25
    energization_window: {earliest: 2026-01-01, central: 2026-12-31, latest: null}
    operational_status: T4
    exact_quote: "tens of thousands of NVIDIA GPUs"
    source_url: https://lambda.ai/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus
    source_publisher: Lambda
    source_publication_date: 2025-11-03
    accessed_date: 2026-04-28
    source_notes:
      - "Primary source supports multibillion-dollar, multi-year Microsoft/Lambda GPU infrastructure; it does not disclose MW, site, RPO, or take-or-pay mechanics."
      - "320 MW facility / 256 MW IT is carried from local `neocloud_overlay.yaml` and `row_level_audit.csv`, where the row is described as Lambda leased/signed/committed capacity."
      - "Earliest 2026 timing is inferred from named Lambda facilities with early-2026/RFS-2026 language; not from the Microsoft contract itself."
    named_site_candidates:
      - site: "Kansas City, MO AI Factory"
        operator_or_landlord: "Lambda sole tenant / local partners"
        user_or_anchor: "single Lambda customer; not publicly named"
        gw_facility: [0.024, 0.100]
        evidence: "Lambda says launch in early 2026 with 24 MW and potential to scale above 100 MW; not tied publicly to Microsoft."
      - site: "Prime Data Centers LAX01, Vernon, CA"
        operator_or_landlord: Prime Data Centers
        user_or_anchor: Lambda
        gw_facility: 0.021
        evidence: "Prime/Lambda release says Lambda will initially lease 21 MW at LAX01; Prime datasheet says LAX01 has 33 MW critical IT load and is operational/leased."
      - site: "EdgeConneX Chicago / Atlanta"
        operator_or_landlord: EdgeConneX
        user_or_anchor: Lambda
        gw_facility: 0.030
        evidence: "EdgeConneX says 30+ MW across Chicago and Atlanta; Chicago 23 MW single-tenant site RFS 2026."
      - site: "Aligned DFW-04, Plano, TX"
        operator_or_landlord: Aligned Data Centers
        user_or_anchor: Lambda
        gw_facility: null
        evidence: "Aligned says Lambda will occupy DFW-04, a liquid-cooled AI/cloud data center under construction; MW not disclosed in release."
      - site: "ECL Mountain View, CA"
        operator_or_landlord: ECL
        user_or_anchor: Lambda
        gw_facility: null
        evidence: "DCD says first Lambda GB300 NVL72 systems came online at ECL Mountain View in September 2025; MW not disclosed in reviewed public sources."
    epoch_site_overlap_candidates:
      - epoch_site: Microsoft Fairwater Wisconsin
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: 3.328
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Wisconsin to 3.328 GW facility
          by 2027-10-03. Candidate only because Microsoft is the anchor in the
          Lambda deal and Microsoft uses Fairwater for AI workloads; no reviewed
          source says Lambda operates or leases Fairwater Wisconsin.
      - epoch_site: Microsoft Fairwater Atlanta
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.859
        overlap_evidence: >
          Local Epoch snapshot carries Fairwater Atlanta to 0.859 GW facility
          by 2026-05-14. Weak geography/name candidate only: Lambda/EdgeConneX
          references Atlanta/ATL02, while Epoch's Fairwater Atlanta is the
          QTS-built Fayetteville Microsoft AI WAN site. No source connects
          Lambda to the Fairwater Atlanta building.
      - epoch_site: Microsoft Goodyear
        epoch_attributed_to: "Microsoft -> OpenAI"
        overlap_gw_facility: 0.263
        overlap_evidence: >
          Local Epoch snapshot has Microsoft Goodyear at 0.263 GW facility
          operational. Candidate only as generic Microsoft AI capacity; no
          Lambda/Microsoft source names Goodyear.
      - epoch_site: Crusoe Abilene Expansion
        epoch_attributed_to: "Microsoft -> Microsoft"
        overlap_gw_facility: 0.941
        overlap_evidence: >
          Local Epoch snapshot carries Microsoft-attributed Crusoe Abilene
          Expansion buildout to 0.941 GW facility by 2027-11-11. Candidate only
          because Microsoft also contracts with neocloud/datacenter providers;
          no reviewed Lambda source names Crusoe or Abilene.
      - epoch_site: Coreweave Helios
        epoch_attributed_to: "CoreWeave -> Microsoft (speculative)"
        overlap_gw_facility: 0.800
        overlap_evidence: >
          Local Epoch snapshot carries CoreWeave Helios buildout to 0.800 GW
          facility with Microsoft as speculative user. This is a same-anchor
          Microsoft neocloud overlap candidate, not a Lambda site candidate.
    risks:
      counterparty: "Medium: Microsoft/NVIDIA anchor quality is high, but Lambda is private and pre-IPO with limited public financial disclosure."
      regulatory: "Medium: named Lambda sites span multiple local jurisdictions; public Microsoft contract source does not identify the permitting path."
      power_interconnect: "High: Microsoft and Lambda both frame power/warm-shell availability as the bottleneck; named sites depend on local utility readiness."
      supply_chain: "Medium-high: contract depends on NVIDIA GB300 NVL72 and future high-density liquid-cooled deployments."
      technology: "Medium: dense GB300/NVL72, photonics, liquid cooling, and future Rubin/Vera systems create integration and refresh-cycle risk."
      financing: "Medium: $1.5B Series E supports growth, but no project-finance package, debt terms, or Microsoft prepayment mechanics were found."
      structural_optionality: "High: no public MW, no site allocation, and no take-or-pay schedule; the local 320 MW may be absorbed by multiple Lambda sites or overlap with NVIDIA leaseback capacity."
contradictions:
  - "Local overlay carries 320 MW facility as Lambda Microsoft/NVIDIA contracted capacity; public Lambda/Microsoft primary announcement discloses GPUs and a multi-year agreement but no MW."
  - "Local overlay marks Lambda operational at 50 MW; DCD says Lambda operates out of 15 U.S. data centers and targets 3 GW, but the reviewed primary sources give only named-site slices such as 21 MW at LAX01 and 24 MW initial at Kansas City."
  - "Kansas City is dedicated to a single Lambda customer under a multi-year agreement, but Lambda does not name that customer; do not assume it is Microsoft without contract/source confirmation."
gaps:
  - "Contract or filing showing whether Microsoft is reserving exactly 320 MW, a GPU count, an IT-load amount, or a dollar-denominated cloud-service commitment."
  - "Site allocation for the Microsoft contract: Kansas City, LAX01, EdgeConneX Chicago/Atlanta, Aligned Plano, ECL Mountain View, Cologix Columbus, Allen Texas, or another site."
  - "Whether the NVIDIA leaseback and Microsoft contract use the same GPUs/capacity or separate tranches."
  - "Whether any Lambda-operated capacity is physically inside an Epoch-counted Microsoft site; current public evidence says no."
  - "Delivery schedule, payment terms, cancellation rights, utilization guarantees, and Microsoft prepayment or balance-sheet treatment."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [Lambda, Microsoft agreement announcement](https://lambda.ai/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus) | 2025-11-03 | Primary company announcement | Multiyear Microsoft/Lambda deal; NVIDIA GB300 NVL72; no MW/site/contract value disclosed. | "multi-year contract" | 2026-04-28 |
| [Lambda, Series E announcement](https://lambda.ai/blog/lambda-raises-over-1.5b-from-twg-global-usit-to-build-superintelligence-cloud-infrastructure) | 2025-11-18 | Primary company announcement | $1.5B+ financing led by TWG Global/USIT; supports gigawatt-scale AI factory ambitions. | "raised over $1.5B" | 2026-04-28 |
| [Lambda / Prime Data Centers LAX01 announcement](https://lambda.ai/blog/prime-data-centers-and-lambda-partner-to-power-the-next-era-of-superintelligence-with-ai-optimized-infrastructure-in-southern-california) | 2025-11-13 | Primary company announcement | LAX01 Vernon site; 33 MW facility, 21 MW Lambda initial lease, VPU power availability. | "21 MW of power" | 2026-04-28 |
| [Prime LAX01 technical sheet](https://primedatacenters.com/wp-content/uploads/2025/10/PDC_LosAngeles_TechSheet_LAX01_01.pdf) | 2025-10 | Primary operator datasheet | LAX01 capacity, utility, operational/leased status. | "CRITICAL IT LOAD 33MW" | 2026-04-28 |
| [Lambda Kansas City announcement](https://lambda.ai/blog/lambda-to-build-a-100mw-ai-factory-in-kansas-city-mo) | 2025-10-28 | Primary company announcement | Kansas City 24 MW initial, >100 MW potential, early-2026 launch, single unnamed Lambda customer. | "24MW of capacity" | 2026-04-28 |
| [EdgeConneX / Lambda announcement](https://www.edgeconnex.com/news/press-releases/edgeconnex-and-lambda-to-build-ai-factory-in-chicago-with-industry-leading-high-density-data-center-infrastructure/) | 2025-08-21 | Primary operator announcement | 30+ MW Chicago/Atlanta, Chicago 23 MW RFS 2026, EdgeConneX operates ATL02/Chicago sites for Lambda. | "30+ Megawatts" | 2026-04-28 |
| [Aligned / Lambda announcement](https://www.globenewswire.com/de/news-release/2025/05/07/3076210/0/en/Aligned-and-Lambda-Partner-to-Power-Next-Generation-AI-Infrastructure.html) | 2025-05-07 | Primary operator announcement | Lambda will occupy Aligned DFW-04 in Plano; liquid-cooled AI/cloud data center; no MW disclosed. | "occupy Aligned's newest" | 2026-04-28 |
| [DCD, Microsoft-Lambda deal](https://www.datacenterdynamics.com/en/news/microsoft-signs-multi-billion-dollar-cloud-capacity-deal-with-lambda/) | 2025-11-04 | Secondary trade press | Microsoft access to Lambda GPUs; no exact value/GPU count; named Lambda facility footprint; 3 GW target. | "not been shared" | 2026-04-28 |
| [DCD, Lambda Series E](https://www.datacenterdynamics.com/en/news/ai-cloud-company-lambda-raises-more-than-15bn-in-series-e-funding-round/) | 2025-11-18 | Secondary trade press | Confirms 15 data centers, >1M GPU/3GW target, Microsoft contract context. | "3GW of liquid-cooled" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Candidate overlaps: Fairwater Wisconsin, Fairwater Atlanta, Goodyear, Crusoe Abilene Expansion, CoreWeave Helios. | "Microsoft Fairwater Wisconsin" | 2026-04-28 |

## Research Notes

- Capacity basis: carry the repo's 320 MW as facility MW because `neocloud_overlay.yaml` says Lambda uses facility basis and PUE 1.25. This is not independently verified by public Lambda/Microsoft sources.
- Microsoft building question: no public evidence found that Lambda operates a Microsoft Fairwater, Goodyear, or Crusoe Abilene building counted by Epoch. The only Atlanta overlap is name/metro confusion: Lambda/EdgeConneX ATL02 is not the Epoch Microsoft Fairwater Atlanta/Fayetteville QTS site based on current public evidence.
- Timing: early 2026/RFS 2026 comes from Kansas City and EdgeConneX site releases, not the Microsoft contract announcement.
- Financing: Series E is corporate equity financing, not project-level financing for a specific Microsoft building. No debt package, prepayment, or customer guarantee was found.
- Dedupe posture: do not adjudicate. Candidate low bound is zero incremental Microsoft physical GW if the 320 MW is already embedded in named Lambda site rows or NVIDIA leaseback capacity; candidate high bound is 0.320 GW facility if the local overlay is retained as ex-Epoch Lambda/Microsoft capacity.
