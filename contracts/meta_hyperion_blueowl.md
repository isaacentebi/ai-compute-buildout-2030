# Meta Hyperion Blueowl

## TL;DR

This Rev-4.2 contract drilldown is generated from the research dispatch pending final adjudication into atoms, dedupe, and row deltas.

## Research Source

- `docs/research/B1_meta_hyperion_blueowl.md`

## Dispatch Content

# Rev-4.2 Research Dispatch B1: Meta Hyperion / Blue Owl

accessed_date: 2026-04-28

## TL;DR

Meta Hyperion is a real Richland Parish, Louisiana AI data center campus with a firm primary-source floor of "over two gigawatts" of compute capacity and a separate Meta CEO / engineering stretch claim that Hyperion can scale to 5 GW over several years. The Blue Owl transaction is best read as a campus-financing / ownership JV plus operating leases, not a cloud capacity contract: Meta retains use and operational control services, Blue Owl-managed funds hold 80% of the JV, and Meta holds 20%.

For Rev-4.2 purposes, the 2.0-2.26 GW Hyperion floor is already an Epoch overlap candidate (`epoch_meta_hyperion_buildout_remaining`, 2.262 GW facility by 2028-01-01). The incremental candidate is only the stretch above that floor: about 2.74 GW if Meta's 5 GW claim is treated as full Hyperion site capacity. Do not final-adjudicate here; carry it as a candidate because the firm JV/development-cost evidence is 2 GW-scale, while the 5 GW statement is later and less mechanically tied to permitted grid/generation assets.

## Evidence Notes

- Meta's own Richland Parish page says the site is its largest data center to date, 4 million square feet, $10B+ investment, and "delivering over two gigawatts of compute capacity" for future open-source LLM training.
- Meta's October 21, 2025 JV release says Blue Owl-managed funds own 80%, Meta owns 20%, the parties fund pro rata shares of about $27B of building plus long-lived power/cooling/connectivity development costs, Meta contributed land/CIP assets, Blue Owl contributed about $7B cash, Meta received about $3B, and Meta entered four-year initial operating leases with extension options plus a 16-year residual value guarantee.
- Meta's FY2025 10-K replaces the cached transcript / press-only financing evidence with filed figures: $4.30B contributed assets, $2.55B distribution, $27B estimated development costs, $12.31B initial lease commitment commencing in 2029, RVG threshold about $28B, and $45.95B maximum exposure to loss.
- LPSC Order U-37425 supports the utility critical path: Entergy sought approval for generation and transmission resources to serve Meta/Laidley in Richland Parish; the approved package includes three new 1x1 combined-cycle combustion turbine generators, two near the customer site and one at Waterford/Killona, plus transmission and customer-protection/CIAC mechanics. Entergy's release says two Richland Parish facilities are expected online in late 2028 and the third by end-2029.
- A newer 2026 expansion to seven additional gas plants / more than 7 GW total supply was reported by news and advocacy sources before this dispatch date; primary LPSC docket extraction should be refreshed before using it as counted capacity.

```yaml
counterparty: "Meta Platforms / Blue Owl Capital-managed funds"
contract_overview:
  type: JV
  term_years: 4
  announced_capex_usd_b: 27
  delivery_window: {earliest: 2028-01-01, central: 2029-01-01, latest: 2030-12-31}
  exclusivity_or_optionality: "Meta leases all campus facilities from the JV after completion; four-year initial lease terms, extension options up to 20 years, and residual value guarantees for the first 16 years. This creates strategic optionality rather than a take-or-pay cloud resale contract."
atoms:
  - id: atom:meta_hyperion_blueowl_floor
    site: "Hyperion / Richland Parish Data Center, Holly Ridge/Richland Parish, LA"
    operator: "Meta; JV owns campus assets; Meta provides construction/property management"
    user_or_anchor: Meta
    gw_facility: 2.262
    gw_it: 1.95
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2028-01-01, central: 2029-01-01, latest: 2030-12-31}
    operational_status: T4
    exact_quote: "delivering over two gigawatts of compute capacity"
    source_url: "https://datacenters.atmeta.com/richland-parish-data-center/"
    source_publisher: "Meta Data Centers"
    source_publication_date: null
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Meta Hyperion"
        epoch_attributed_to: Meta
        overlap_gw_facility: 2.262
        overlap_evidence: "Local Epoch atom says remaining buildout to 2262.0 MW facility by 2028-01-01; project=Hyperion #confident."
    risks:
      counterparty: "Low: Meta is the anchor and operating user; Blue Owl is financing/asset partner."
      regulatory: "Medium: LPSC U-37425 intervenors and customer-protection conditions show nontrivial ratepayer/regulatory scrutiny."
      power_interconnect: "High: initial three CCCTs and transmission are late-2028/end-2029 critical path; later 2026 seven-plant expansion needs primary docket refresh."
      supply_chain: "Medium: 4M square-foot campus plus grid/generation/transmission equipment creates transformer/switchgear/turbine risk."
      technology: "Medium: AI cluster architecture may shift before 2029; Meta has optional lease structure and RVG."
      financing: "Medium: off-balance-sheet VIE depends on leases, RVG, and Blue Owl/PIMCO/bond investor funding."
      structural_optionality: "High: initial four-year lease terms and non-renewal/RVG mechanics are explicitly optional."
  - id: atom:meta_hyperion_stretch_above_epoch_candidate
    site: "Hyperion stretch beyond current Epoch 2.262 GW facility floor"
    operator: Meta
    user_or_anchor: Meta
    gw_facility: 2.738
    gw_it: null
    basis: ambiguous_compute
    pue_assumed: null
    energization_window: {earliest: 2029-01-01, central: 2030-12-31, latest: null}
    operational_status: T5
    exact_quote: "scale up to 5GW over several years"
    source_url: "https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf"
    source_publisher: "Meta Platforms Q2 2025 earnings transcript"
    source_publication_date: 2025-07-30
    accessed_date: 2026-04-28
    epoch_site_overlap_candidates:
      - epoch_site: "Meta Hyperion"
        epoch_attributed_to: Meta
        overlap_gw_facility: 2.262
        overlap_evidence: "Candidate residual only: 5.000 GW stretch less Epoch's 2.262 GW facility floor equals 2.738 GW before basis conversion."
    risks:
      counterparty: "Low for sponsor credit; high for whether this stretch is a committed contract."
      regulatory: "Medium-high: 5 GW stretch may depend on additional generation/transmission approvals beyond U-37425."
      power_interconnect: "High: the 5 GW claim exceeds the initial two-gigawatt power/generation package."
      supply_chain: "High: multi-GW accelerator, liquid-cooling, electrical gear and turbine delivery risk."
      technology: "High: over-several-years language makes future chip/rack power density and architecture uncertain."
      financing: "Medium: current $27B JV covers the 2 GW-scale campus development; additional stretch funding is not cleanly separated."
      structural_optionality: "High: CEO/engineering stretch language plus lease optionality floor the confidence at zero incremental firm capacity."
contradictions:
  - "Meta data-center page and JV release support an over-2-GW campus; Meta Q2 transcript and engineering blog state Hyperion can scale to 5 GW. Treat 5 GW as stretch unless a primary permit/utility/JV amendment ties it to specific additional power and buildings."
  - "Meta press release rounded Blue Owl cash contribution and Meta distribution to about $7B/about $3B; FY2025 10-K gives filed amounts of $4.30B contributed assets and $2.55B distribution, with $7.0B investor cash."
  - "Local project context cites three gas plants / roughly 2.26 GW for initial Hyperion service, while 2026 reporting says Entergy sought seven additional plants and more than 7 GW total. Use the latter only as a follow-up candidate until primary docket lines are extracted."
gaps:
  - "Pull the 2026 LPSC application/order for the seven additional gas plants and map each unit, MW, COD, and customer-cost protections to Hyperion."
  - "Extract MISO transmission queue / MTEP references for the Holly Ridge 1.8 GW load and 500 kV transmission projects from primary planning documents."
  - "Confirm whether Blue Owl / Beignet debt offering documents are public enough to cite directly for bond size, maturity ladder, amortization, and PIMCO participation."
  - "Resolve basis: Meta says compute capacity; Epoch stores facility MW with PUE 1.16. Do not convert the 5 GW stretch without an adjudication rule."
  - "Check whether Meta's 2026 expansion/Meta Compute statements broaden Hyperion beyond the Richland Parish site or include other Louisiana/US clusters."
```

## Source Pointers

- Meta Richland Parish profile: https://datacenters.atmeta.com/richland-parish-data-center/
- Meta / Blue Owl JV release: https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Announces-Joint-Venture-with-Funds-Managed-by-Blue-Owl-Capital-to-Develop-Hyperion-Data-Center/
- Meta FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Meta Q2 2025 transcript: https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf
- Meta engineering blog: https://engineering.fb.com/2025/09/29/data-infrastructure/metas-infrastructure-evolution-and-the-advent-of-ai/
- LPSC Order U-37425: https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/ViewFile?fileId=nDWn%2Fjuc2%2BA%3D
- Entergy LPSC approval release: https://www.entergy.com/news/entergy-louisiana-receives-lpsc-approval-for-major-infrastructure-investments-to-support-metas-data-center-and-improve-reliability
- Louisiana Governor / LED announcement: https://gov.louisiana.gov/news/4697

