# Anthropic Google Broadcom

## TL;DR

This Rev-4.2 contract drilldown is generated from the research dispatch pending final adjudication into atoms, dedupe, and row deltas.

## Research Source

- `docs/research/A3_anthropic_google_broadcom.md`

## Dispatch Content

# Rev-4.2 Research Dispatch A3: Anthropic-Google/Broadcom TPU Capacity

```yaml
counterparty: Anthropic / Google Cloud / Broadcom
contract_overview:
  type: cloud capacity + chip procurement
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2026-01-01, central: 2027-07-01, latest: 2031-12-31}
  exclusivity_or_optionality: >
    Non-exclusive Anthropic compute path. Anthropic says it also uses AWS
    Trainium and NVIDIA GPUs, and that Amazon remains its primary cloud and
    training partner. Google Cloud is the service channel; Broadcom is the
    TPU / rack-component supply channel. Broadcom's 2026 8-K makes actual
    consumption conditional on Anthropic's continued commercial success.
atoms:
  - id: atom:anthropic_google_cloud_tpu_2025_1gw_2026
    site: unspecified Google Cloud / TPU capacity
    operator: Google Cloud
    user_or_anchor: Anthropic
    gw_facility: null
    gw_it: [1.0, 1.1, 1.3]
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2026-07-01, latest: 2026-12-31}
    operational_status: unknown
    exact_quote: "well over a gigawatt"
    source_url: https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services
    source_publisher: Anthropic
    source_publication_date: 2025-10-23
    accessed_date: 2026-04-28
    source_notes:
      - >
        Anthropic announced planned access to up to one million Google Cloud
        TPUs and described the expansion as worth tens of billions of dollars.
        Google Cloud's same-day press release says Anthropic will have access
        to the capacity coming online in 2026.
      - >
        Treat as chip/cloud capacity, not site-level facility MW. The source
        does not name a campus, colo operator, utility, or interconnection.
    epoch_site_overlap_candidates:
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: Fluidstack; users Anthropic, G42
        overlap_gw_facility: 0.509
        overlap_evidence: >
          Local Epoch context has 68 MW current and 509 MW full buildout by
          2027-03-31. It is the only local Epoch site explicitly carrying
          Anthropic under Fluidstack, but the October Google Cloud source does
          not name Fluidstack or Lake Mariner.
      - epoch_site: Google New Albany
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.543
        overlap_evidence: >
          Local Epoch context has a Google-owned TPU-suitable campus with 407
          MW current and 543 MW buildout by 2026-12-18. Candidate only because
          the deal is delivered via Google Cloud; Epoch attributes users to
          Google DeepMind, not Anthropic.
      - epoch_site: Google Council Bluffs (East)
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.284
        overlap_evidence: >
          Local Epoch context has 190 MW current and 284 MW buildout by
          2026-06-10. Candidate Google Cloud site; no Anthropic site evidence.
      - epoch_site: Google Pryor (North)
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.454
        overlap_evidence: >
          Local Epoch context has 65 MW current and 454 MW buildout by
          2026-05-17. Candidate Google Cloud site; no Anthropic site evidence.
      - epoch_site: Google Omaha
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.474
        overlap_evidence: >
          Local Epoch context has 189 MW current and 474 MW buildout by
          2027-07-26. Candidate Google Cloud site; no Anthropic site evidence.
      - epoch_site: Google Cedar Rapids
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.627
        overlap_evidence: >
          Local Epoch context has 105 MW current and 627 MW buildout by
          2028-11-18. Candidate Google Cloud site; timing is later than the
          2026 Anthropic capacity window.
    risks:
      counterparty: >
        Anthropic demand has to absorb a very large cloud/TPU reservation while
        it is also committing to AWS, NVIDIA, and Microsoft Azure paths.
      regulatory: >
        No named campus or permit record is attached to this atom, so local
        land-use, air-permit, and water constraints cannot be checked.
      power_interconnect: >
        Source discloses capacity but no utility queue, substation, or PPA
        evidence. Treat power deliverability as unresolved.
      supply_chain: >
        Depends on Google TPU availability and Broadcom/TSMC execution for
        custom ASIC and networking components.
      technology: >
        "Up to one million TPUs" does not disclose TPU generation mix, power
        per chip, rack density, or how much is training versus inference.
      financing: >
        Primary sources disclose "tens of billions" but not RPO, lease
        structure, prepayment, or Alphabet/Google Cloud backlog.
      structural_optionality: >
        "Up to" chip language implies optionality; the capacity may be staged,
        cancellable, or workload-dependent.

  - id: atom:anthropic_google_broadcom_tpu_2026_35gw_2027
    site: unspecified, vast majority in United States
    operator: Google Cloud / Broadcom / undisclosed operational partners
    user_or_anchor: Anthropic
    gw_facility: null
    gw_it: 3.5
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2027-01-01, central: 2028-07-01, latest: 2031-12-31}
    operational_status: unknown
    exact_quote: "approximately 3.5 gigawatts"
    source_url: https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/0001193125-26-144028-index.htm
    source_publisher: Broadcom / SEC Form 8-K
    source_publication_date: 2026-04-06
    accessed_date: 2026-04-28
    corroborating_sources:
      - url: https://www.anthropic.com/news/google-broadcom-partnership-compute
        publisher: Anthropic
        publication_date: 2026-04-06
        accessed_date: 2026-04-28
        claim: Multiple gigawatts of next-generation TPU capacity expected online starting in 2027.
      - url: https://www.googlecloudpresscorner.com/2026-04-06-Anthropic-Expands-Use-of-Google-Cloud-and-TPUs
        publisher: Google Cloud
        publication_date: 2026-04-06
        accessed_date: 2026-04-28
        claim: Capacity delivered through Google Cloud services and Google-built TPUs supplied through Broadcom.
    source_notes:
      - >
        Broadcom says Google and Broadcom have a long-term TPU and supply
        assurance agreement through up to 2031, and separately that Anthropic
        will access 3.5 GW through Broadcom beginning in 2027.
      - >
        Anthropic says the vast majority of the new compute will be in the
        United States and frames the deal as an expansion of its November 2025
        $50B American infrastructure commitment.
      - >
        Google Cloud says delivery is through both Google Cloud services and
        Google-built TPUs supplied through Broadcom. This supports a mixed
        cloud-capacity / chip-procurement classification, not a standalone
        colo atom.
    epoch_site_overlap_candidates:
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: Fluidstack; users Anthropic, G42
        overlap_gw_facility: 0.509
        overlap_evidence: >
          Strongest named local overlap candidate because Anthropic's April
          source links the 2027 TPU expansion to the November 2025 US
          infrastructure commitment, and that commitment names Fluidstack,
          New York, and Texas. However, Lake Mariner alone is far smaller than
          3.5 GW and the Broadcom/Google sources do not name it.
      - epoch_site: Fluidstack / Anthropic Texas and New York sites, unspecified
        epoch_attributed_to: Fluidstack / Anthropic
        overlap_gw_facility: null
        overlap_evidence: >
          Anthropic and Fluidstack both announced $50B of custom Anthropic data
          centers in Texas and New York, "with more sites to come," coming
          online through 2026. Candidate envelope; not a specific Epoch site.
      - epoch_site: Goodnight
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 1.0876
        overlap_evidence: >
          Local Epoch context has the largest Google buildout candidate:
          1,087.6 MW by 2027-10-01 in Claude, Texas. Candidate only; Epoch
          attributes the site to Google DeepMind, not Anthropic.
      - epoch_site: Google Cedar Rapids
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.627
        overlap_evidence: >
          Local Epoch context buildout date of 2028-11-18 fits the broader
          2027-2031 Broadcom window, but no source ties Anthropic to the site.
      - epoch_site: Google New Albany
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.543
        overlap_evidence: >
          Existing 407 MW current and 543 MW buildout could host Google Cloud
          TPU capacity; no Anthropic-specific evidence.
      - epoch_site: Google Omaha
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.474
        overlap_evidence: >
          Buildout to 474 MW by 2027-07-26 overlaps the 2027 start window; no
          Anthropic-specific evidence.
      - epoch_site: Google Pryor (North)
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.454
        overlap_evidence: >
          Buildout to 454 MW by 2026-05-17 could support existing Google Cloud
          TPU capacity, but the 2027 expansion is not site-linked.
      - epoch_site: Google Council Bluffs (East)
        epoch_attributed_to: Google / Google DeepMind
        overlap_gw_facility: 0.284
        overlap_evidence: >
          Candidate Google Cloud TPU site by ownership and timing, but too
          small to explain much of the 3.5 GW and not Anthropic-attributed.
    risks:
      counterparty: >
        Broadcom explicitly conditions consumption on Anthropic's continued
        commercial success; this is a demand and credit risk.
      regulatory: >
        Site anonymity prevents checking whether the "vast majority" US
        footprint already has local approvals.
      power_interconnect: >
        3.5 GW of TPU-based compute implies multi-GW power delivery; no named
        interconnects, utilities, or energization milestones are disclosed.
      supply_chain: >
        Depends on Broadcom custom TPU/rack component supply, Google TPU
        architecture, TSMC fabrication capacity, HBM/advanced packaging, and
        networking optics.
      technology: >
        Next-generation TPU capacity is not mapped to TPU generation, server
        density, cluster topology, or utilization.
      financing: >
        Broadcom says the parties are discussing operational and financial
        partners, indicating the deployment financing stack is not fully
        public or may not be finalized.
      structural_optionality: >
        Multi-party structure may allow staging across Google-owned regions,
        Fluidstack shells, or other operational partners; physical capacity is
        not assignable from public sources alone.
contradictions:
  - >
    Anthropic frames the April 2026 deal as a major expansion of its November
    2025 $50B US infrastructure commitment; Google frames delivery through
    Google Cloud services and TPUs supplied through Broadcom; Broadcom frames
    it as access through Broadcom plus operational/financial partners. These
    descriptions are compatible, but they do not resolve whether the physical
    shells are Google-owned, Fluidstack-built, or a mix.
  - >
    The October 2025 atom is "up to one million TPUs" and "well over" 1 GW;
    the April 2026 atom is approximately 3.5 GW beginning in 2027. Secondary
    reports often summarize total Anthropic TPU exposure as roughly 4.5 GW,
    but primary sources do not provide a clean additive site-level bridge.
  - >
    Local overlay context treats the TPU/Broadcom row as Class B chip
    procurement that may flow into Fluidstack shells. Primary Google/Broadcom
    sources do not name Fluidstack, so this should remain an overlap candidate,
    not an adjudicated dedupe.
  - >
    Local Epoch Google sites are attributed to Google DeepMind, while the
    Anthropic deal is Google Cloud customer capacity. Epoch attribution does
    not distinguish internal Google model use from cloud capacity sold to
    Anthropic.
gaps:
  - Site list for the 2026 one-million-TPU tranche and the 2027+ 3.5 GW tranche.
  - Whether the 3.5 GW is IT load, facility load, contractual compute nameplate, or another capacity convention.
  - Whether Anthropic's November 2025 $50B Fluidstack commitment includes physical shells for Google/Broadcom TPUs.
  - Identity of Broadcom's "operational and financial partners" and whether they include Fluidstack, Google-owned campuses, utilities, SPVs, or colocation lessors.
  - Alphabet/Google Cloud or Anthropic contract accounting: RPO, minimum take-or-pay, prepayment, cancellation, and term.
  - Utility interconnection evidence for any candidate site that would support multi-GW incremental TPU load.
```

## Dispatch Notes

Do not add these atoms as incremental site-level facility GW without a separate
site assignment. The strongest public inference is that this is Anthropic cloud
capacity plus TPU/custom-silicon procurement. The physical capacity may overlap
with Fluidstack's Anthropic buildout, Google-owned Epoch sites, or both. The
research handoff should flag all candidates and leave tiering/dedupe to
adjudication.

Primary sources used:

- [Anthropic, Oct. 23, 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- [Google Cloud, Oct. 23, 2025](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services)
- [Anthropic, Apr. 6, 2026](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [Google Cloud, Apr. 6, 2026](https://www.googlecloudpresscorner.com/2026-04-06-Anthropic-Expands-Use-of-Google-Cloud-and-TPUs)
- [Broadcom Form 8-K, Apr. 6, 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/0001193125-26-144028-index.htm)
- [Anthropic $50B Fluidstack announcement, Nov. 12, 2025](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure)
- [Fluidstack $50B Anthropic announcement, Nov. 12, 2025](https://www.fluidstack.io/about-us/blog/fluidstack-selected-by-anthropic-to-deliver-custom-data-centers-in-the-us)
- Local Epoch context: `epoch_data_centers/compiled.json`, `epoch_data_centers/data_centers.csv`, `epoch_data_centers/data_center_timelines.csv`, and `canonical_capacity_atoms.yaml` from the repo snapshot.

