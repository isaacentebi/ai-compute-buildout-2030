# Meta Hyperion / Blue Owl JV — Richland Parish, Louisiana

## TL;DR

Meta Hyperion is Meta's largest data-center campus, located in Richland Parish (Holly Ridge), Louisiana, with a primary-source floor of **"over two gigawatts of compute capacity"** per Meta's Richland Parish data-center page and a separate Q2 2025 earnings call statement from Mark Zuckerberg that Hyperion **"can scale up to 5GW over several years"**. The October 21, 2025 Blue Owl JV restructured ownership: Blue Owl-managed funds hold 80% and Meta holds 20% of the JV, with $27B development cost shared pro rata; Meta enters four-year initial operating leases with extension options up to 20 years and a 16-year residual value guarantee threshold of approximately $28B (per Meta FY2025 10-K). The Rev-4.2 canonical structure carries `epoch_meta_hyperion_buildout_remaining` (2.262 GW facility floor by 2028-01-01, T4) and a separate `meta_hyperion_stretch_incremental` atom (2.738 GW IT / 3.014 GW facility, T5) representing the 5 GW stretch above the Epoch floor, with Rev-4.3 source URL refresh from a local cached transcript to the publicly hosted Meta Q2 2025 transcript PDF.

## Counterparties

- **Operator**: Meta Platforms, Inc. (NASDAQ: META) — anchor user and operating-services provider; JV owns campus assets, Meta provides construction and property management.
- **Anchor tenant / user**: Meta (sole anchor; campus dedicated to Meta open-source LLM training and AI workloads).
- **Financing partner(s)**: Blue Owl Capital-managed funds (80% JV equity); PIMCO (bond investor); Meta (20% equity + lease commitments).

## Structure

- **Type**: JV (campus financing/ownership) plus operating leases plus residual value guarantee. Not a take-or-pay cloud capacity contract.
- **Term**: Four-year initial operating-lease term, extension options up to 20 years total; 16-year residual value guarantee period.
- **Announced contract value**: ~$27B estimated total development cost (building + long-lived power/cooling/connectivity); $12.31B initial lease commitment commencing 2029 (Meta FY2025 10-K); $45.95B Meta maximum exposure to loss; ~$28B RVG threshold.
- **Equity cross-investments**: Blue Owl-managed funds 80% / Meta 20% JV. Meta contributed land/CIP assets ($4.30B per FY2025 10-K); Blue Owl contributed $7.0B investor cash; Meta received $2.55B distribution.
- **Take-or-pay coverage**: N/A (operating-lease structure with RVG, not take-or-pay).
- **Optionality**: High. Four-year initial leases with extension options; non-renewal/RVG mechanics explicitly optional. Stretch beyond 2.262 GW Epoch floor depends on additional generation/transmission approvals.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.0 / 0.0 / 0.0 | T4 | Construction phase; no operational MW |
| 2027 | 0.0 / 0.5 / 1.0 | T4 | First-phase commissioning candidate |
| 2028 | 1.0 / 1.5 / 2.262 | T4 | Epoch floor full buildout date 2028-01-01; LPSC U-37425 approved CCCTs late 2028 |
| 2029 | 2.0 / 2.262 / 3.5 | T4/T5 | Lease commencement 2029 per FY2025 10-K; third CCCT online by year-end |
| 2030 | 2.262 / 3.0 / 5.0 | T4/T5 | Stretch capacity ramp; depends on additional generation/transmission |
| 2031+ | 2.262 / 3.5 / 5.0 | T5 | Full Zuckerberg "scale up to 5 GW over several years" envelope |

The Epoch floor is 2.262 GW facility by 2028-01-01. The stretch atom carries 2.738 GW IT (3.014 GW facility at PUE 1.10), range 0–3.014, status `speculative`, T5.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Meta Hyperion / Richland Parish Data Center | Holly Ridge, Richland Parish, LA | Meta (operations); JV (asset ownership) | Meta → Meta; 2.262 GW facility by 2028-01-01 (project=Hyperion #confident) | 2.262 GW Epoch floor + 2.738 GW IT stretch | T4 |

## Financing Stack

- **Capex envelope**: ~$27B total development cost (building + power/cooling/connectivity), shared pro rata 80/20 between Blue Owl funds and Meta.
- **Equity / debt / RPO**: Blue Owl-managed funds $7.0B investor cash contributed; Meta $4.30B contributed assets, $2.55B distribution received; $12.31B initial lease commitment commencing 2029 (Meta FY2025 10-K); $45.95B Meta maximum exposure to loss; ~$28B RVG threshold over 16-year period.
- **Public disclosures**: Meta Richland Parish data-center page; Meta Blue Owl JV release Oct 21, 2025; Meta FY2025 10-K (replaces prior press-only financing evidence with filed figures); LPSC Order U-37425 (Entergy 3 CCCT generation + transmission approval); Entergy LPSC approval release.

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `epoch_meta_hyperion_buildout_remaining` — 2.262 GW facility floor by 2028-01-01, T4, project=Hyperion #confident.
- `meta_hyperion_stretch_incremental` — 2.738 GW IT / 3.014 GW facility (range 0–3.014), T5, status `speculative`, included in raw-horizon and probability-weighted totals; **excluded from non-stretch and conservative T1/T2/T3 totals**. Rev-4.3 source URL replaced from local cached transcript (`file:///...`) to publicly hosted Meta Q2 2025 transcript PDF (`https://s21.q4cdn.com/.../META-Q2-2025-Earnings-Call-Transcript.pdf`).

## Dedupe Notes

The 5 GW Zuckerberg stretch is defined as a residual: 5.000 GW Q2 2025 earnings call statement minus 2.262 GW Epoch Hyperion floor = 2.738 GW IT (3.014 GW facility at PUE 1.10). The Epoch floor is already counted in `epoch_meta_hyperion_buildout_remaining`; the stretch is incremental to Epoch only above the floor and is tagged T5 because it lacks (a) named permits beyond LPSC U-37425 (which approves three CCCTs for ~2 GW initial Hyperion service), (b) firm site-plan beyond initial Hyperion campus, and (c) hardware/financing JV expansion past the current $27B Blue Owl envelope. Meta engineering blog (2025-09-29) corroborates "scale up to 5GW once finished". 2026 reporting that Entergy is seeking seven additional gas plants and >7 GW total supply has not been verified against primary LPSC docket extraction; this remains an open follow-up. Dedupe direction: `none` (stretch already split from Epoch floor).

## Risk Axes

1. **Counterparty risk** — Low for Meta credit (investment-grade); high for whether the 5 GW stretch is a committed contract — Q2 2025 earnings-call language is forward-looking, not contractual. Blue Owl 80% JV ownership shifts asset-level credit to fund LPs (PIMCO, bond investors).
2. **Regulatory risk** — LPSC U-37425 approved three CCCTs for ~2 GW initial Hyperion service; the 5 GW stretch likely requires additional LPSC orders. Intervenors and customer-protection conditions show nontrivial ratepayer/regulatory scrutiny. 2026 reporting cites Entergy seeking seven additional gas plants and >7 GW total supply — primary docket extraction pending.
3. **Power / interconnect risk** — High. Initial three CCCTs and transmission are late-2028/end-2029 critical path. Two CCCTs near customer site; one at Waterford/Killona; transmission and customer-protection/CIAC mechanics in U-37425. The 5 GW stretch exceeds initial two-gigawatt power/generation package; requires generation, transmission, and substation expansion not yet in approved dockets.
4. **Supply chain risk** — Medium-high. 4M square-foot campus plus grid/generation/transmission equipment creates transformer/switchgear/turbine risk. Multi-GW accelerator (Vera Rubin and successors), liquid-cooling, electrical gear, and gas-turbine delivery risk over 5-year stretch window.
5. **Technology obsolescence risk** — Medium. AI cluster architecture may shift before 2029; "over several years" timing makes future chip/rack power density and architecture uncertain. Lease optionality (4-year initial + 16-year RVG) creates technology refresh path; Meta has structural protection.
6. **Financing risk** — Medium. Off-balance-sheet VIE depends on leases, RVG, and Blue Owl/PIMCO/bond investor funding. $27B Blue Owl JV covers ~2 GW campus development; additional stretch funding (~$28B+) is not cleanly separated and depends on continued Blue Owl/PIMCO/bond investor appetite.
7. **Structural optionality** — High. CEO/engineering "stretch" language plus 4-year initial lease + RVG mechanics floor confidence at zero incremental firm capacity above the Epoch 2.262 GW Hyperion atom. Meta's optionality is a feature, not a bug, of the JV structure.

## Temporal Logic

- **Earliest**: 2028-01-01 — Epoch full buildout date for the 2.262 GW floor; LPSC release says two Richland Parish facilities expected online in late 2028.
- **Central**: 2029-01-01 — Lease commencement per Meta FY2025 10-K; third CCCT online by end-2029 per Entergy.
- **Latest**: 2030-2032 — full 5 GW stretch envelope plausible only with additional generation/transmission approvals beyond U-37425.
- **Critical-path dependency**: Entergy CCCT commissioning (three plants, late 2028/end-2029); MISO transmission queue / MTEP references for Holly Ridge 1.8 GW load; Blue Owl/PIMCO bond offering execution; whether 2026 Entergy seven-additional-plants application advances through LPSC.

## Reviewer Findings Addressed

- **Rev-4.3 reviewer #7 fix**: Source URL replaced from local cached transcript file (`file:///...`) to publicly hosted Meta Q2 2025 earnings call transcript PDF at `https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf`. Engineering at Meta blog (2025-09-29) corroborates "scale up to 5 GW once finished".
- **JV structure verified**: Meta FY2025 10-K supersedes press-release rounded figures with filed amounts ($4.30B contributed assets, $2.55B distribution, $7.0B investor cash, $12.31B initial lease commitment commencing 2029, $45.95B maximum exposure to loss).
- **Stretch split documented**: 2.738 GW IT stretch separated from 2.262 GW Epoch floor; tagged T5 to reflect speculative status; included in raw-horizon and probability-weighted totals only.

## Open Questions / Gaps

- 2026 LPSC application/order for the seven additional gas plants — primary docket extraction pending.
- MISO transmission queue / MTEP references for the Holly Ridge 1.8 GW load and 500 kV transmission projects.
- Whether Blue Owl / "Beignet" debt offering documents are public enough to cite directly for bond size, maturity ladder, amortization, and PIMCO participation.
- Basis adjudication: Meta says "compute capacity"; Epoch stores facility MW with PUE 1.16. 5 GW stretch convention not fully resolved.
- Whether Meta's 2026 expansion / Meta Compute statements broaden Hyperion beyond the Richland Parish site or include other Louisiana/U.S. clusters.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Meta Richland Parish Data Center page](https://datacenters.atmeta.com/richland-parish-data-center/) | n.d. | Primary company page | Largest Meta DC; 4M sq ft; $10B+; "over two gigawatts" floor | "delivering over two gigawatts of compute capacity" |
| [Meta Q2 2025 earnings call transcript](https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf) | 2025-07-30 | Primary investor disclosure | 5 GW stretch | "scale up to 5GW over several years" |
| [Meta / Blue Owl JV release](https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Announces-Joint-Venture-with-Funds-Managed-by-Blue-Owl-Capital-to-Develop-Hyperion-Data-Center/) | 2025-10-21 | Primary company announcement | 80/20 JV; $27B development cost; 4-year initial lease + 16-year RVG | "joint venture" |
| [Meta FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) | 2026-02 | SEC filing | $4.30B contributed assets; $2.55B distribution; $12.31B lease commitment from 2029; $45.95B max loss; $28B RVG threshold | "Hyperion" |
| [Meta Engineering blog](https://engineering.fb.com/2025/09/29/data-infrastructure/metas-infrastructure-evolution-and-the-advent-of-ai/) | 2025-09-29 | Primary company feature | Engineering corroboration of 5 GW scale | "scale up to 5 GW" |
| [LPSC Order U-37425](https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/ViewFile?fileId=nDWn%2Fjuc2%2BA%3D) | 2025 | Government order | Three CCCT approval; Waterford/Killona placement; CIAC mechanics | "Meta/Laidley" |
| [Entergy LPSC approval release](https://www.entergy.com/news/entergy-louisiana-receives-lpsc-approval-for-major-infrastructure-investments-to-support-metas-data-center-and-improve-reliability) | 2025 | Primary utility announcement | Two Richland Parish facilities online late 2028; third end-2029 | "to support Meta's data center" |
| [Louisiana Governor / LED announcement](https://gov.louisiana.gov/news/4697) | 2024 | Government announcement | Site-selection context | "Hyperion" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | 2.262 GW facility floor by 2028-01-01 | "Meta Hyperion" |

## Cross-Links

- Research dispatch: `docs/research/B1_meta_hyperion_blueowl.md`
- Atoms: `canonical_capacity_atoms.yaml` (`epoch_meta_hyperion_buildout_remaining`, `meta_hyperion_stretch_incremental`)
- Dedupe entries: `dedupe_audit.csv` (rows for `meta_hyperion_stretch_incremental`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
