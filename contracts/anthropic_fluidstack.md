# Anthropic Fluidstack

## TL;DR

This Rev-4.2 contract drilldown is generated from the research dispatch pending final adjudication into atoms, dedupe, and row deltas.

## Research Source

- `docs/research/A4_anthropic_fluidstack.md`

## Dispatch Content

# Rev-4.2 Research Dispatch A4: Anthropic / Fluidstack

```yaml
counterparty: Anthropic / Fluidstack
contract_overview:
  type: unknown
  term_years: null
  announced_capex_usd_b: 50.0
  delivery_window: {earliest: 2026-01-01, central: 2026-12-31, latest: null}
  exclusivity_or_optionality: >
    Anthropic and Fluidstack announced a $50B American computing infrastructure
    program covering data centers in Texas and New York, with more sites to
    come. The public announcement does not disclose MW, term, take-or-pay
    language, site names, or whether Anthropic is directly funding owned assets,
    leasing Fluidstack capacity, or underwriting Fluidstack project finance.
    Treat the announced program as a dollar-only physical-site envelope, not as
    additive MW until site-level evidence resolves overlap.
atoms:
  - id: atom:a4_anthropic_fluidstack_50b_envelope
    site: "Texas and New York Fluidstack sites, exact sites undisclosed"
    operator: Fluidstack
    user_or_anchor: Anthropic
    gw_facility: null
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2026-01-01, central: 2026-12-31, latest: null}
    operational_status: T5
    exact_quote: "building data centers with Fluidstack in Texas and New York"
    source_url: https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure
    source_publisher: Anthropic
    source_publication_date: 2025-11-12
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: "Fluidstack -> Anthropic, G42"
        overlap_gw_facility: 0.509
        overlap_evidence: >
          Epoch local snapshot carries Fluidstack Lake Mariner at 68 MW current
          and 509 MW full-buildout facility power; Anthropic/Fluidstack names a
          New York site but does not name Barker/Lake Mariner.
      - epoch_site: Google sites, unspecified US
        epoch_attributed_to: "Google -> Google DeepMind"
        overlap_gw_facility: null
        overlap_evidence: >
          Anthropic's April 2026 Google/Broadcom announcement says the new TPU
          compute is a major expansion of the November 2025 $50B American
          infrastructure commitment; some capacity may sit in Google-owned shells
          rather than Fluidstack-owned/leased shells.
      - epoch_site: Microsoft Fairwater sites, unspecified
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: null
        overlap_evidence: >
          Anthropic's Azure commitment is separate and site-undisclosed; no
          evidence ties Fluidstack to Fairwater, but the same Anthropic demand
          surface may be cited across announcements.
      - epoch_site: Anthropic-Amazon New Carlisle / Amazon Madison / Amazon Ridgeland
        epoch_attributed_to: "Amazon -> Anthropic"
        overlap_gw_facility: null
        overlap_evidence: >
          AWS Project Rainier is Anthropic's primary training/cloud partnership;
          it is a separate compute surface, but should be checked before adding
          all Anthropic-announced GW claims.
    risks:
      counterparty: "Anthropic is a private lab with fast revenue growth but heavy forward compute commitments across Fluidstack, AWS, Google/Broadcom, and Azure."
      regulatory: "No site permits are named in the Anthropic/Fluidstack announcement; local approvals must be checked at candidate sites."
      power_interconnect: "The announcement says 'gigawatts of power' but gives no queue position, utility, interconnection, or grid-upgrade allocation."
      supply_chain: "The likely TPU/NVIDIA/AI-rack bill of materials is exposed to HBM, advanced packaging, optical/networking, transformer, and switchgear bottlenecks."
      technology: "Capacity may be Google TPU, NVIDIA GPU, or mixed hardware; no primary source ties a specific chip stack to the $50B envelope."
      financing: "The public announcement does not state who funds construction debt or whether Anthropic obligations are unconditional."
      structural_optionality: "Could be a branding layer over already-signed Fluidstack leases and Google-backed sites rather than net-new physical capacity."

  - id: atom:a4_fluidstack_lake_mariner_candidate
    site: "Lake Mariner, Barker, New York"
    operator: "TeraWulf physical site / Fluidstack cloud tenant"
    user_or_anchor: "Anthropic likely; G42/Core42 also likely"
    gw_facility: [0.418, 0.450, 0.509]
    gw_it: 0.360
    basis: IT_MW
    pue_assumed: 1.25
    energization_window: {earliest: 2026-05-31, central: 2026-12-31, latest: 2027-03-31}
    operational_status: T2
    exact_quote: "total contracted critical IT load for Fluidstack at the campus increases to approximately 360 MW"
    source_url: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-079463/0001104659-25-079463.pdf
    source_publisher: TeraWulf
    source_publication_date: 2025-08-18
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: "Fluidstack -> Anthropic, G42"
        overlap_gw_facility: 0.509
        overlap_evidence: >
          Direct site-name match in local Epoch snapshot. Epoch tracks 68 MW
          current facility power and 509 MW full buildout by 2027-03-31; this
          dispatch flags the full site as an overlap candidate, with the
          Anthropic-specific share unresolved because G42/Core42 also appears in
          the site user set.
    risks:
      counterparty: "Fluidstack is the lease/customer interface; TeraWulf owns/operates the physical campus and Google backstops Fluidstack obligations."
      regulatory: "Lake Mariner reuse of a former power/crypto campus reduces greenfield risk but still depends on data center expansion permits and approvals."
      power_interconnect: "TeraWulf cites dual 345 kV feeds and 500 MW available plus 250 MW pending regulatory approval; that is credible but not risk-free."
      supply_chain: "TeraWulf filings flag construction, labor, equipment, tariff, and switchgear risk for the Lake Mariner expansion."
      technology: "Epoch infers Google TPUs for Fluidstack buildings; Anthropic and TeraWulf do not directly disclose the chip mix."
      financing: "Google backstop supports project-related debt, but TeraWulf discloses the backstop becomes effective only after lease commencement and specified defaults."
      structural_optionality: "High double-count risk with the $50B Anthropic/Fluidstack announcement and with Anthropic-Google/Broadcom TPU capacity."

  - id: atom:a4_fluidstack_barber_lake_texas_candidate
    site: "Barber Lake, Colorado City, Texas"
    operator: "Cipher Mining physical site / Fluidstack cloud tenant"
    user_or_anchor: "Fluidstack; Anthropic candidate; Google financial backstop"
    gw_facility: 0.300
    gw_it: 0.207
    basis: IT_MW
    pue_assumed: 1.449
    energization_window: {earliest: 2026-09-30, central: 2026-10-31, latest: 2027-01-31}
    operational_status: T3
    exact_quote: "lease the entire 300 MW of capacity at Cipher's Barber Lake site"
    source_url: https://www.globenewswire.com/news-release/2025/11/20/3191801/0/en/Cipher-Mining-Signs-Additional-56-MW-10-Year-AI-Hosting-Agreement-with-Fluidstack.html
    source_publisher: Cipher Mining
    source_publication_date: 2025-11-20
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: none found in local Epoch snapshot
        epoch_attributed_to: null
        overlap_gw_facility: 0.0
        overlap_evidence: >
          Local Epoch data_centers.csv has no Barber Lake/Cipher Fluidstack row
          as of the available snapshot; candidate is ex-Epoch unless a newer
          Epoch update has added it.
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: "Fluidstack -> Anthropic, G42"
        overlap_gw_facility: null
        overlap_evidence: >
          Same Fluidstack/Google financing pattern and same Anthropic Texas/New
          York announcement; adjudication should decide whether Barber Lake is
          the Texas site under the $50B envelope.
    risks:
      counterparty: "Cipher is the physical developer; Fluidstack is the customer; Anthropic is not named in Cipher's releases."
      regulatory: "Texas site is a bitcoin-to-HPC pivot with local grid and site work still to be delivered."
      power_interconnect: "Initial agreement supports 244 MW gross for 168 MW IT; later expansion uses the entire 300 MW site, with delivery not yet operational."
      supply_chain: "Delivery by September 2026 and January 2027 requires data hall, cooling, substation, and AI rack procurement to stay on schedule."
      technology: "No public source identifies whether Barber Lake will host Google TPUs, NVIDIA GPUs, or another mix."
      financing: "Google backstops $1.4B plus an additional $333M of Fluidstack lease obligations; project-related debt still depends on construction and lease commencement."
      structural_optionality: "Strong candidate for the Anthropic/Fluidstack Texas site, but not named by Anthropic or Fluidstack as Anthropic-dedicated."

  - id: atom:a4_anthropic_google_broadcom_tpu_overlap_candidate
    site: "Google/Broadcom TPU capacity, sites undisclosed"
    operator: "Google / Broadcom"
    user_or_anchor: Anthropic
    gw_facility: null
    gw_it: 3.5
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2027-01-01, central: 2027-12-31, latest: null}
    operational_status: T5
    exact_quote: "approximately 3.5 gigawatts"
    source_url: https://www.sullcrom.com/About/News-and-Events/Highlights/2026/April/SC-Advises-Broadcom-3-5GW-TPU-Based-AI-Compute-Collaboration-Google-Anthropic
    source_publisher: Sullivan & Cromwell
    source_publication_date: 2026-04-08
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: Fluidstack Lake Mariner
        epoch_attributed_to: "Fluidstack -> Anthropic, G42"
        overlap_gw_facility: null
        overlap_evidence: >
          Epoch notes point to Fluidstack Lake Mariner buildings likely serving
          Google TPUs for Anthropic; Anthropic says the Google/Broadcom compute
          is an expansion of the November 2025 $50B American infrastructure
          commitment.
      - epoch_site: Google Cedar Rapids / Goodnight / New Albany / Omaha / Pryor / Council Bluffs
        epoch_attributed_to: "Google -> Google DeepMind"
        overlap_gw_facility: null
        overlap_evidence: >
          If the TPU capacity is hosted in Google-owned US sites, it could
          overlap the Google Epoch fleet. No primary source names these sites
          for Anthropic.
    risks:
      counterparty: "Anthropic, Google, and Broadcom are all named; the exact commercial obligation and site owner are not public."
      regulatory: "Sites not disclosed, so permitting and local opposition cannot be evaluated."
      power_interconnect: "3.5 GW appears to be compute/TPU capacity, not explicitly facility interconnect MW."
      supply_chain: "TPU generations, Broadcom custom silicon, TSMC, HBM/packaging, and network components must scale through 2027."
      technology: "Custom TPU roadmap risk and workload portability risk across Trainium, TPU, and NVIDIA."
      financing: "No public RPO or capex funding schedule; industry dollar estimates are secondary."
      structural_optionality: "Anthropic itself links this to the $50B Fluidstack-era US infrastructure commitment, so additive treatment is unsafe."

  - id: atom:a4_anthropic_azure_overlap_candidate
    site: "Microsoft Azure sites, undisclosed"
    operator: Microsoft Azure
    user_or_anchor: Anthropic
    gw_facility: null
    gw_it: 1.0
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: null, central: 2028-12-31, latest: null}
    operational_status: T5
    exact_quote: "additional compute capacity up to one gigawatt"
    source_url: https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/
    source_publisher: Microsoft
    source_publication_date: 2025-11-18
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: Microsoft Fairwater Wisconsin / Atlanta / Goodyear
        epoch_attributed_to: "Microsoft -> OpenAI, Microsoft"
        overlap_gw_facility: null
        overlap_evidence: >
          Azure sites for Anthropic are not disclosed. Existing Epoch Microsoft
          AI sites are possible but unproven hosting shells; no Fluidstack
          involvement found.
    risks:
      counterparty: "Microsoft/NVIDIA/Anthropic agreement is primary, but site-level delivery is opaque."
      regulatory: "No named sites."
      power_interconnect: "1 GW is compute capacity and not linked to a facility interconnect."
      supply_chain: "Depends on NVIDIA Grace Blackwell and Vera Rubin system availability."
      technology: "NVIDIA architecture optimization could be additive to TPU/Trainium rather than replacing them."
      financing: "Microsoft also invests up to $5B in Anthropic, creating circular commercial exposure."
      structural_optionality: "Same Anthropic demand may be counted across Azure, Google/Broadcom, AWS, and Fluidstack announcements."

contradictions:
  - "Anthropic/Fluidstack and Fluidstack press releases disclose $50B, Texas, New York, gigawatts of power, and 2026 starts, but disclose no MW, site names, or term."
  - "TeraWulf and Cipher disclose concrete Fluidstack MW and Google backstops before the Anthropic announcement; neither primary source names Anthropic as the lease beneficiary."
  - "Anthropic's April 2026 Google/Broadcom release says the new TPU compute expands the November 2025 $50B US infrastructure commitment, which conflicts with treating Google/Broadcom GW as wholly additive to Fluidstack GW."
  - "Epoch local data attributes Lake Mariner to Fluidstack with Anthropic and G42 users; TeraWulf filings describe Fluidstack lease MW but do not allocate user shares between Anthropic, Google, or other Fluidstack customers."
gaps:
  - "Signed Anthropic-Fluidstack contract terms: lease, take-or-pay, capex contribution, debt support, guarantees, cancellation rights, and duration."
  - "Named sites under the $50B announcement, especially whether New York equals Lake Mariner and Texas equals Barber Lake."
  - "Anthropic-specific MW at Lake Mariner and Barber Lake, separated from G42/Core42, Google backstop exposure, and general Fluidstack cloud capacity."
  - "Facility vs IT basis for all announced gigawatt figures; no primary source converts Anthropic's gigawatts of power to interconnection MW."
  - "Utility interconnection records, PPAs, and grid upgrade cost allocation for the Texas sites."
  - "Chip allocation by site: Google TPU vs NVIDIA GPU vs mixed hardware, and whether Broadcom/Google TPU capacity physically lands at Fluidstack sites or Google-operated sites."
```

## Source Notes

- Primary company sources used: Anthropic (2025-11-12, 2026-04-06, 2026-04-20), Fluidstack (2025-11-12), TeraWulf 8-Ks/press releases (2025-08-14, 2025-08-18, 2025-10-14), Cipher Mining releases (2025-09-25, 2025-11-20), Microsoft (2025-11-18), Amazon (2026-04-20), and Epoch AI Frontier Data Centers (accessed 2026-04-28).
- Secondary/legal-adviser source used only for the specific 3.5 GW Google/Broadcom figure: Sullivan & Cromwell client highlight (2026-04-08). Anthropic's own Google/Broadcom announcement supports "multiple gigawatts" starting in 2027 and explicitly links the deal to the November 2025 $50B infrastructure commitment.
- Capacity discipline: the $50B Anthropic/Fluidstack envelope receives no direct MW assignment. Lake Mariner and Barber Lake are site candidates with separate operator-filed MW. The Google/Broadcom and Azure rows are overlap surfaces, not final incremental physical-site additions.

