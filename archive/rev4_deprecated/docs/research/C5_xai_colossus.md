# Rev-4.2 Research Dispatch C5: xAI Colossus 1 + 2

accessed_date: 2026-04-28

## TL;DR

xAI's Memphis Colossus footprint is real, large, and unusually fast-moving, and any ex-Epoch physical capacity row should be checked against the local Epoch Memphis rows first. xAI's own sources support Colossus as a 200k-GPU supercomputer with a stated path to 1M GPUs in Memphis and "over one million H100 GPU equivalents" across Colossus I and II by year-end 2025. Local Epoch context already carries Colossus 1 at 425 MW facility operational plus 17 MW remaining, and Colossus 2 at 1,494 MW facility full buildout by 2026-05-13; the overlay's separate 60 MW IT / 78 MW facility `xai_colossus2_residual` row is an analyst residual after subtracting the local Epoch Colossus 1 + 2 buildout from Musk's "almost 2GW" claim.

The residual is plausible only as a small unresolved candidate, not as a primary-disclosed site capacity. It also has a basis-risk: the local overlay subtracts 1.94 GW of Epoch facility MW from an ambiguous "training compute" / "almost 2GW" statement, then treats the 0.06 GW remainder as IT MW and multiplies by PUE 1.30 to get 0.078 GW facility. That should stay flagged for adjudication.

Operational status is mixed. Local Epoch compiled context says Colossus 1 is operational at 425 MW facility, and Colossus 2 is operational_today with a 302 MW timeline_now estimate as of 2026-01-13, but the canonical atom table carries Colossus 2 only as a 1,494 MW T2 buildout_remaining atom. MLGW statements materially constrain the power story: Paul Lowery / Colossus 1 had 150 MW grid service in May 2025 and a possible second 150 MW by late 2025, while Tulane / Colossus 2 had no final studied MLGW power request in May and only about 0.5 MW general service in July 2025. Mississippi records and litigation allege a Southaven gas plant supplies Colossus 2, and MDEQ permit materials cover a separate 1,200 MW / 41-turbine permitted gas plant at 2875 Stanton Road.

## Evidence Notes

- xAI primary pages support the GPU scale but do not disclose facility MW, IT MW, PUE, or a clean Colossus 1 / Colossus 2 MW split.
- Local Epoch is the load-bearing MW source. It carries Colossus 1 at 425 MW current / 442 MW full buildout and Colossus 2 at 1,494 MW full buildout. Local compiled Epoch context also estimates Colossus 2 at 302 MW operational as of 2026-01-13.
- The current `xai_colossus2_residual` atom is not site evidence. It is the arithmetic residual from Musk's "almost 2GW" statement less local Epoch Colossus 1 + 2 full buildout of about 1.94 GW.
- MLGW confirms grid-service limits and process constraints. Paul Lowery / Colossus 1 had 150 MW grid power in May 2025 and a pending second 150 MW request; Tulane / Colossus 2 had no final request or system-impact study then, and MLGW later said it was not supplying power to the Colossus 2 supercomputer.
- Power/gas/environmental risk is high: Shelby County turbine permitting, an April 2026 Shelby notice to convert the Colossus 1 construction permit to an operating permit with 12 turbines, MDEQ Southaven gas-plant permitting, and April 2026 NAACP litigation all remain active risk indicators.

```yaml
counterparty: xAI
contract_overview:
  type: unknown
  term_years: null
  announced_capex_usd_b: null
  delivery_window: {earliest: 2024-08-11, central: 2026-05-13, latest: 2026-12-31}
  exclusivity_or_optionality: >
    Self-build / affiliate-owned AI training campuses in the Memphis-Southaven
    area, not a third-party take-or-pay contract. Public xAI sources disclose GPU
    scale and financing, not MW contract terms. Musk's "almost 2GW" statement is
    a scale claim for xAI training compute across Colossus buildings and should
    not be treated as a separate ex-Epoch commitment without dedupe.
atoms:
  - id: atom:epoch_xai_colossus_1_operational
    site: "xAI Colossus 1, 3231 Riverport Rd / Paul R. Lowry Road, Memphis, TN"
    operator: xAI
    user_or_anchor: xAI
    gw_facility: 0.425
    gw_it: 0.366
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2024-08-11, central: 2026-02-11, latest: null}
    operational_status: T1
    exact_quote: "Epoch current facility power for xAI Colossus 1"
    source_url: https://epoch.ai/data/data-centers
    source_publisher: "Epoch AI Frontier Data Centers local snapshot"
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "Local compiled Epoch context: current_power_mw 425.0, operational_today true, timeline_now last_update 2026-02-11."
      - "MLGW's May 5, 2025 update said the Paul Lowery site was receiving 150 MW from the TVA/MLGW grid and could reach 300 MW after a second request, upgrades, and TVA approval."
    epoch_site_overlap_candidates:
      - epoch_site: "xAI Colossus 1"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.425
        overlap_evidence: "Direct local Epoch site row; count once as Epoch site."
      - epoch_site: "xAI Colossus 1 buildout remaining"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.017
        overlap_evidence: "Same site; local canonical table carries an additional 17 MW to 442 MW full buildout."
    risks:
      counterparty: "Medium: xAI has substantial capital access but is private, fast-changing, and has limited site-level financial disclosure."
      regulatory: "High: Colossus 1 turbine permit appeal history and April 2026 operating-permit conversion notice remain relevant."
      power_interconnect: "High: grid service lags the full Epoch facility-power estimate; behind-the-meter turbines and curtailment agreements are central to operations."
      supply_chain: "Medium-high: H100/H200/B200/GB200 availability and high-density integration drive the schedule."
      technology: "Medium-high: fast GPU, cooling, battery, and turbine integration creates reliability risk."
      financing: "Medium: xAI announced a $20B Series E, but no site-level project-finance terms were found."
      structural_optionality: "Medium: official xAI GPU claims do not map cleanly to MW, and local Epoch inferred MW depends on GPU/PUE assumptions."

  - id: atom:epoch_xai_colossus_1_buildout_remaining
    site: "xAI Colossus 1, Memphis, TN"
    operator: xAI
    user_or_anchor: xAI
    gw_facility: 0.017
    gw_it: 0.0147
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: null, central: 2026-02-11, latest: null}
    operational_status: T2
    exact_quote: "Epoch remaining buildout to 442.0 MW facility by 2026-02-11"
    source_url: https://epoch.ai/data/data-centers
    source_publisher: "Epoch AI Frontier Data Centers local snapshot"
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "Central date is before the accessed date; leave to adjudication whether this should remain a remaining-buildout atom or fold into operational capacity."
    epoch_site_overlap_candidates:
      - epoch_site: "xAI Colossus 1"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.017
        overlap_evidence: "Same physical campus as Colossus 1 operational atom."
    risks:
      counterparty: "Same as Colossus 1 operational."
      regulatory: "Same as Colossus 1 operational."
      power_interconnect: "Same as Colossus 1 operational."
      supply_chain: "Small residual but tied to the same GPU/cooling stack."
      technology: "Small residual; status may already be superseded by local compiled timeline."
      financing: "No site-level financing terms found."
      structural_optionality: "Potentially stale remaining-buildout split because central date predates accessed_date."

  - id: atom:epoch_xai_colossus_2_buildout_remaining
    site: "xAI Colossus 2, 5420 Tulane Rd, Memphis, TN"
    operator: xAI
    user_or_anchor: xAI
    gw_facility: 1.494
    gw_it: 1.288
    basis: facility_MW
    pue_assumed: 1.16
    energization_window: {earliest: 2025-10-19, central: 2026-05-13, latest: null}
    operational_status: T2
    exact_quote: "Epoch remaining buildout to 1494.0 MW facility by 2026-05-13"
    source_url: https://epoch.ai/data/data-centers
    source_publisher: "Epoch AI Frontier Data Centers local snapshot"
    source_publication_date: 2026-04-20
    accessed_date: 2026-04-28
    source_notes:
      - "Local compiled Epoch context says operational_today true with timeline_now power_mw 302.0 as of 2026-01-13; canonical atom table still carries the full 1,494 MW as buildout_remaining."
      - "MLGW July 22, 2025 statement says MLGW was not supplying power to the Colossus 2 supercomputer at 5420 Tulane Road."
      - "NAACP April 14, 2026 complaint alleges the Southaven Colossus Gas Plant supplies Colossus 2; allegations are not adjudicated here."
    epoch_site_overlap_candidates:
      - epoch_site: "xAI Colossus 2"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 1.494
        overlap_evidence: "Direct local Epoch site row; any Colossus 2 / MACROHARDRR / almost-2GW capacity should be checked against this before adding residual."
      - epoch_site: "Memphis Colossus 2 residual"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.078
        overlap_evidence: "Overlay residual is mechanically derived after subtracting Colossus 1 + 2 Epoch buildout; possible same-campus overlap, not independent site evidence."
    risks:
      counterparty: "Medium: xAI official financing is large, but private-company disclosure is limited."
      regulatory: "High: Colossus 2 power path involves Mississippi gas-plant permit/litigation and Memphis/Southaven cross-border impacts."
      power_interconnect: "High: MLGW had no final studied Tulane request in May 2025 and said in July 2025 it was not powering Colossus 2; Southaven gas generation appears critical."
      supply_chain: "High: local Epoch full-buildout estimate implies roughly 550k GPUs / 1.39M H100e; delivery depends on advanced NVIDIA systems."
      technology: "High: gas turbines, batteries, dry coolers/condensers, dense GPUs, and cross-site power integration are all moving in parallel."
      financing: "Medium: xAI's $20B Series E supports infrastructure buildout generally; no Colossus 2 project-finance package found."
      structural_optionality: "High: xAI's GPU/H100e claims, Musk's 2 GW claim, and local Epoch MW estimates do not share a single disclosed power basis."

  - id: atom:xai_colossus2_residual_candidate
    site: "Memphis Colossus 2 / MACROHARDRR residual candidate"
    operator: xAI
    user_or_anchor: xAI
    gw_facility: 0.078
    gw_it: 0.060
    basis: IT_MW
    pue_assumed: 1.30
    energization_window: {earliest: 2025-12-30, central: 2026-12-31, latest: null}
    operational_status: T6
    exact_quote: "Will take @xAI training compute to almost 2GW"
    source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/musk-purchases-third-building-at-memphis-site-to-expand-xais-training-capacity-to-a-monstrous-2-gigawatts-announcement-comes-days-after-musk-vows-to-have-more-ai-compute-than-everyone-else
    source_publisher: "Tom's Hardware, quoting Elon Musk on X"
    source_publication_date: 2025-12-30
    accessed_date: 2026-04-28
    source_notes:
      - "Local overlay logic: 2.0 GW claim less 0.442 GW Colossus 1 full buildout and 1.494 GW Colossus 2 full buildout leaves about 0.064 GW, rounded to 0.060 GW IT; facility point is 0.060 * PUE 1.30 = 0.078 GW."
      - "Basis warning: the 2 GW public statement says training compute and may not be IT MW; local Epoch overlap is facility MW. Treat as analyst residual only."
      - "Reuters/Investing and DCD also report the same Musk statement, but no primary xAI release or filing with MW detail was found."
    epoch_site_overlap_candidates:
      - epoch_site: "xAI Colossus 1"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.442
        overlap_evidence: "Local overlay subtracts Colossus 1 full buildout from the 2 GW claim."
      - epoch_site: "xAI Colossus 2"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 1.494
        overlap_evidence: "Local overlay subtracts Colossus 2 full buildout from the 2 GW claim; MACROHARDRR may be within the Colossus 2/third-building envelope."
      - epoch_site: "xAI Colossus 2 operational context"
        epoch_attributed_to: "xAI"
        overlap_gw_facility: 0.302
        overlap_evidence: "Local compiled Epoch timeline estimates 302 MW operational as of 2026-01-13; candidate split issue against canonical buildout_remaining atom."
    risks:
      counterparty: "Medium: scale depends on xAI execution and financing despite strong 2026 funding announcement."
      regulatory: "High: incremental residual, if real, likely requires the same Southaven/Memphis power and air-permit path."
      power_interconnect: "High: no direct utility or interconnection source supports an incremental 78 MW facility slice outside Epoch."
      supply_chain: "Medium-high: residual likely maps to additional GB200/B-series systems or H100e-equivalent growth."
      technology: "Medium-high: residual capacity could be absorbed by cooling/power tuning at existing Colossus buildings rather than a new physical block."
      financing: "Medium: no financing allocated specifically to the residual."
      structural_optionality: "Very high: row is an analyst inference, not a disclosed MW commitment."
contradictions:
  - "xAI official pages emphasize 200k GPUs, 1M-GPU plans, and Colossus I/II over one million H100 GPU equivalents, but do not disclose MW; local Epoch supplies the MW conversion."
  - "Local Epoch compiled context says Colossus 2 is operational_today with timeline_now 302 MW as of 2026-01-13, while the canonical atom table carries Colossus 2 as 1,494 MW buildout_remaining and no separate operational atom."
  - "MLGW May 2025 said Tulane / Colossus 2 had no final studied power request; MLGW July 2025 said it was not supplying the Colossus 2 supercomputer; local Epoch nevertheless estimates Colossus 2 operational at 302 MW by January 2026, apparently relying on behind-the-meter / Southaven power evidence."
  - "xAI says it is investing in water recycling to avoid Memphis Aquifer industrial draw, but April 2026 reporting says Musk sequenced the water plant after finishing/stabilizing Colossus 2."
  - "Residual logic treats Musk's ambiguous 'almost 2GW' training-compute claim as an IT MW residual after subtracting Epoch facility MW; this basis mismatch should be resolved before final totals."
gaps:
  - "Primary xAI, utility, or permit document disclosing Colossus 1 and Colossus 2 IT MW, facility MW, PUE, and current metered load."
  - "TVA board approval / service-agreement records for the second 150 MW Paul Lowery increment and any Tulane Road system-impact study."
  - "Final operating status and emissions-control compliance for Shelby County permit 01156-01PC after the April 2026 conversion request from 15 to 12 turbines."
  - "Final MDEQ permit-board appeal outcome and federal litigation outcome for the Southaven Colossus Gas Plant."
  - "Whether MACROHARDRR / Colossus 3 is physically inside the Epoch Colossus 2 envelope, a separate Epoch candidate, or the source of the small residual."
  - "Whether the 13 MGD water-recycling facility is on schedule, delayed, or no longer load-bearing for cooling/water-risk mitigation."
```

## Evidence Register

| Source | Date | Type | Load-bearing evidence | Short quote | Accessed |
| --- | --- | --- | --- | --- | --- |
| [xAI Colossus page](https://x.ai/colossus) | null | Primary company page | Colossus GPU scale and February 2025 150k+ jobs; no MW. | "200 K GPUs" | 2026-04-28 |
| [xAI Memphis page](https://x.ai/memphis) | null | Primary company page | Memphis is home to Colossus; 1M GPU plan; MLGW/TVA relationship. | "plans to equip this facility with 1 million GPUs" | 2026-04-28 |
| [xAI Series E announcement](https://x.ai/news/series-e?_bhlid=10271a39b16b0316ace641881ed1c10a82479785) | 2026-01-06 | Primary company announcement | $20B financing and Colossus I/II H100e scale. | "over one million H100 GPU equivalents" | 2026-04-28 |
| [xAI Our Commitment to Memphis](https://x.ai/memphis/our-commitment) | null | Primary company page | Substation spending, batteries, water recycling claims, Shelby permit timeline. | "35 million to build a 150MW substation" | 2026-04-28 |
| [MLGW May 5, 2025 xAI update](https://www.mlgw.com/images/content/files/pdf/new/5-5-25%20xAI%20Update.pdf) | 2025-05-05 | Primary utility update | Paul Lowery 150 MW grid service, second 150 MW pending, Tulane 260 MW-1.1 GW discussed but not studied. | "xAI is receiving 150MW of power" | 2026-04-28 |
| [MLGW July 22, 2025 Tulane statement](https://www.mlgw.com/images/content/files/pdf/XAIJuly2025Statement.pdf) | 2025-07-22 | Primary utility statement | Tulane general service around 0.5 MW; MLGW not supplying Colossus 2 supercomputer. | "not supplying power to their supercomputer" | 2026-04-28 |
| [Shelby County / CTC permit 01156-01PC via Scribd mirror](https://www.scribd.com/document/883601734/01156-01PC-070225-Permit) | 2025-07-02 | Local permit document mirror | 15 Solar SMT-130 turbines, 16.48 MW each, permit number and emissions limits. | "Fifteen (15) Solar SMT-130" | 2026-04-28 |
| [Shelby County April 2026 public notice](https://www.shelbytnhealth.com/DocumentCenter/View/7726/PUBLIC-NOTICE-472026?bidId=) | 2026-04-07 | Primary local public notice | CTC request to convert construction permit to operating permit and reduce turbines from 15 to 12. | "from 15 to 12 units" | 2026-04-28 |
| [NAACP / Young, Gifted & Green appeal of CTC air permit](https://cdn.arstechnica.net/wp-content/uploads/2025/07/NAACP-and-YGGs-xAI-Air-Permit-Appeal-7-15-2025.pdf) | 2025-07-16 | Legal appeal / advocacy filing | Alleges 35 turbines and more than 420 MW generating capacity at peak; challenges permit logic. | "35 turbines with a total generating capacity" | 2026-04-28 |
| [MDEQ Southaven PSD air construction permit](https://opcgis.deq.state.ms.us/ensearchonline/get_doc.aspx?dt=dpermit&id=1825411) | 2026-01-15 | Primary state permit document | MZX Tech 2875 Stanton Road PSD construction permit for Southaven gas plant; monitoring/emissions conditions. | "MZX Tech LLC 2875 Stanton Road" | 2026-04-28 |
| [NAACP v. xAI / MZX Tech complaint](https://cdn.mississippitoday.org/wp-content/uploads/2026/04/15090443/xAI-Southaven-Complaint.pdf) | 2026-04-14 | Federal complaint / legal filing | Alleges 27 unpermitted turbines, Colossus Gas Plant supplies Colossus 2, and separate permitted 1,200 MW / 41-turbine plant. | "supplies power to xAI's Colossus 2" | 2026-04-28 |
| [Tom's Hardware, Musk MACROHARDRR / 2 GW report](https://www.tomshardware.com/tech-industry/artificial-intelligence/musk-purchases-third-building-at-memphis-site-to-expand-xais-training-capacity-to-a-monstrous-2-gigawatts-announcement-comes-days-after-musk-vows-to-have-more-ai-compute-than-everyone-else) | 2025-12-30 | Secondary media quoting X post | Source for local residual row; no primary MW filing found. | "almost 2GW" | 2026-04-28 |
| [Reuters via Investing.com, third building report](https://www.investing.com/news/stock-market-news/musks-xai-buys-third-building-to-expand-ai-compute-power-4426034) | 2025-12-30 | Secondary wire report quoting X post | Confirms same Musk MACROHARDRR statement; no location disclosed by Musk. | "third building called MACROHARDRR" | 2026-04-28 |
| [AOL / Commercial Appeal, water plant on hold](https://www.aol.com/news/elon-musk-confirms-xai-wastewater-213551302.html) | 2026-04-09 | Secondary local reporting | Reports Musk said xAI will finish/stabilize Colossus 2 before building the water recycling plant; includes TDEC/permit context. | "focus on finishing Colossus 2" | 2026-04-28 |
| [Epoch AI Frontier Data Centers local snapshot](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset context | Colossus 1 and 2 MW, dates, operational status, and overlap basis from `epoch_data_centers` and canonical atoms. | "xAI Colossus 2" | 2026-04-28 |

## Research Notes

- Residual arithmetic: local overlay carries Colossus 1 full buildout 442 MW facility plus Colossus 2 full buildout 1,494 MW facility = 1,936 MW. Subtracting from a 2.0 GW headline leaves 64 MW, rounded to 60 MW. The row then treats that 60 MW as IT and applies PUE 1.30, producing 78 MW facility. This is not a primary-source MW disclosure.
- Candidate dedupe posture: flag `xai_colossus2_residual` against both Epoch Colossus 1 and Epoch Colossus 2. MACROHARDRR / Colossus 3 may be a separate building, but the current MW support is analyst residual logic rather than primary site evidence.
- Operational/buildout posture: Colossus 1 is strongly operational in local Epoch and xAI sources. Colossus 2 has local Epoch operational context at 302 MW but canonical buildout treatment at 1,494 MW; final split should be handled in adjudication.
- Power posture: grid power alone does not explain the local Epoch MW estimates. Colossus 1 uses MLGW/TVA grid plus turbines/batteries and curtailment; Colossus 2 appears to rely on Southaven gas-generation infrastructure, at least during buildout, based on MLGW statements and legal filings.
- Environmental posture: air permitting and emissions are not peripheral; they are the binding risk to schedule and realizability. Water-recycling mitigation is also uncertain because current local reporting says xAI is prioritizing Colossus 2 completion before the plant.
