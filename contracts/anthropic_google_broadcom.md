# Anthropic / Google Cloud / Broadcom — TPU Capacity (4.5 GW exposure)

## TL;DR

Anthropic's Google Cloud / Broadcom TPU capacity stack totals approximately 4.5 GW IT cumulative exposure: 1 GW IT from the October 23, 2025 Anthropic / Google Cloud announcement (**"well over a gigawatt"**, up to one million TPUs in 2026) plus 3.5 GW IT from the April 6, 2026 Broadcom Form 8-K (Anthropic accesses **"approximately 3.5 gigawatts"** beginning 2027 through Broadcom-supplied Google-built TPUs). Per user direction, Rev-4.3 introduces a NEW canonical atom `anthropic_google_broadcom_physical_tpu` carrying 2.700 GW facility central (range 0–5.400 GW) — a 50% partial overlap dedupe applied against six Google Epoch sites (Goodnight, New Albany, Cedar Rapids, Council Bluffs East, Pryor North, Omaha) plus Fluidstack Lake Mariner, reflecting Anthropic's framing that the April 2026 Google/Broadcom expansion is an enlargement of the November 2025 $50B U.S. infrastructure commitment. T5 evidence tier — counterparty named, GW magnitude disclosed, broad delivery window stated; sites unallocated.

## Counterparties

- **Operator**: Google Cloud (Alphabet, NASDAQ: GOOGL) as cloud service operator; Broadcom (NASDAQ: AVGO) as TPU/rack-component supply channel; "operational and financial partners" referenced in Broadcom 8-K but not named.
- **Anchor tenant / user**: Anthropic, PBC.
- **Financing partner(s)**: Broadcom and Google Cloud bilaterally referenced but no joint capex disclosure; Anthropic dollar magnitude **"tens of billions"** per Anthropic October 23, 2025 release. Broadcom 8-K explicitly conditions consumption on Anthropic's continued commercial success.

## Structure

- **Type**: Cloud capacity (Google Cloud TPU services) plus chip/silicon procurement (Broadcom-supplied Google TPUs).
- **Term**: Broadcom 8-K references long-term TPU and supply-assurance agreement with Google **"through up to 2031"**; Anthropic-specific tenor undisclosed.
- **Announced contract value**: "Tens of billions" (Anthropic Oct 23, 2025); precise dollar figure not disclosed.
- **Equity cross-investments**: None disclosed for this transaction (separate from Microsoft/NVIDIA Anthropic equity stack).
- **Take-or-pay coverage**: Not disclosed in any primary source. Broadcom 8-K characterizes consumption as conditional on Anthropic commercial trajectory.
- **Optionality**: High. "Up to one million TPUs"; "approximately 3.5 GW"; "vast majority will be sited in the United States"; physical shells described as Google-owned, Fluidstack, or "operational and financial partners" — multi-party structure permits staging.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.0 / 0.20 / 1.20 | T5 | "Well over a gigawatt" coming online in 2026 (Anthropic Oct 23, 2025); first 1 GW IT tranche |
| 2027 | 0.0 / 0.50 / 2.00 | T5 | Broadcom 8-K "beginning in 2027"; 3.5 GW IT tranche commences |
| 2028 | 0.0 / 1.50 / 3.50 | T5 | Mid-window ramp |
| 2029 | 0.0 / 2.20 / 4.50 | T5 | Closer to full envelope |
| 2030 | 0.0 / 2.70 / 5.40 | T5 | Central case full 4.5 GW IT / 5.4 GW facility envelope with 50% overlap |
| 2031 | 0.0 / 2.70 / 5.40 | T5 | Broadcom 8-K supply-assurance term through 2031 |

The canonical residual is 2.700 GW facility central (= 5.400 GW × 50% overlap), with low=0 (full overlap absorbed by Epoch + Fluidstack) and high=5.400 GW (no overlap, full net-new physical capacity).

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Fluidstack Lake Mariner | Barker, NY | TeraWulf / Fluidstack | Fluidstack → Anthropic, G42; 0.509 GW facility by 2027-03-31 | 0.509 GW (strongest single-site overlap; only Epoch site with Anthropic-Fluidstack attribution) | T2 |
| Goodnight (Claude TX) | Claude, Texas | Google | Google → Google DeepMind; 1.088 GW by 2027-10-01 | 0.544 GW (50% allocation) | T2 |
| Google New Albany | New Albany, OH | Google | Google → Google DeepMind; 0.543 GW by 2026-12-18 | 0.272 GW (50% allocation) | T1/T2 |
| Google Cedar Rapids | Cedar Rapids, IA | Google | Google → Google DeepMind; 0.627 GW by 2028-11-18 | 0.314 GW (50% allocation) | T2 |
| Google Omaha | Omaha, NE | Google | Google → Google DeepMind; 0.474 GW by 2027-07-26 | 0.237 GW (50% allocation) | T1/T2 |
| Google Pryor (North) | Pryor, OK | Google | Google → Google DeepMind; 0.454 GW by 2026-05-17 | 0.227 GW (50% allocation) | T1/T2 |
| Google Council Bluffs (East) | Council Bluffs, IA | Google | Google → Google DeepMind; 0.284 GW by 2026-06-10 | 0.142 GW (50% allocation) | T1/T2 |
| Net-new sites | undisclosed | Google / Broadcom partners | Not in Epoch | Balance of 2.7 GW central; high case 5.4 GW | T5 |

## Financing Stack

- **Capex envelope**: Not disclosed at the Anthropic-Google-Broadcom level. Anthropic frames as "tens of billions"; Broadcom 8-K references undisclosed operational/financial partners.
- **Equity / debt / RPO**: No equity cross-investment in this transaction. Anthropic side dollar exposure absorbed in broader $50B U.S. infrastructure commitment per Anthropic Apr 6, 2026 release.
- **Public disclosures**: Anthropic Oct 23, 2025; Google Cloud Oct 23, 2025; Anthropic Apr 6, 2026; Google Cloud Apr 6, 2026; Broadcom Form 8-K filed 2026-04-06; Sullivan & Cromwell client highlight 2026-04-08.

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `anthropic_google_broadcom_physical_tpu` — 2.700 GW facility central (range 0–5.400), T5, NEW Rev-4.3 atom; partial 50% overlap dedupe against six Google Epoch sites plus Fluidstack Lake Mariner; included in raw-horizon and probability-weighted totals.

## Dedupe Notes

Rev-4.3 NEW ATOM per user direction: **"Anthropic-Google deal should exist in the paper at appropriate tier"**, replacing the prior 0 GW Class B treatment. Total Anthropic-Google/Broadcom TPU exposure = 1 GW IT (Anthropic Oct 23, 2025) + 3.5 GW IT (Broadcom 8-K Apr 6, 2026) = 4.5 GW IT, converted to 5.4 GW facility at PUE 1.20. Central case applies 50% physical-shell overlap with existing Google Epoch sites plus Fluidstack Lake Mariner: Goodnight 0.544 + New Albany 0.272 + Cedar Rapids 0.314 + Omaha 0.237 + Pryor North 0.227 + Council Bluffs East 0.142 + Lake Mariner 0.509 ≈ 2.245 GW deduped, with central residual 2.700 GW representing net-new physical capacity beyond those overlaps. Low=0 (full overlap absorbed); high=5.4 GW (no overlap, full net-new). Anthropic explicitly links the April 6, 2026 Google/Broadcom expansion to the November 12, 2025 $50B Fluidstack U.S. infrastructure commitment, supporting same-program treatment. Dedupe direction: `partial_overlap_50pct_central_against_google_epoch_plus_fluidstack`.

## Risk Axes

1. **Counterparty risk** — Broadcom 8-K explicitly conditions consumption on Anthropic's continued commercial success (demand and credit risk). Anthropic also stacking AWS 5 GW + Azure 1 GW + Fluidstack $50B simultaneously; demand absorption requires sustained enterprise/consumer revenue trajectory. Multi-party structure (Google + Broadcom + unnamed operational/financial partners) creates allocation ambiguity.
2. **Regulatory risk** — No named site allocation, so local land-use, air-permit, and water constraints cannot be checked at the contract level. If allocated to Goodnight (Claude, TX), Texas H&L permitting and ERCOT load-study cadence apply; if Iowa/Nebraska sites, state Public Utility Commission review and water-use disclosures.
3. **Power / interconnect risk** — 4.5 GW IT / 5.4 GW facility implies multi-GW utility commitments; no public utility queue, substation, or PPA evidence at the Anthropic-specific level. If absorbed into Google's existing Epoch fleet, grid risk is partially priced; if net-new, unbooked.
4. **Supply chain risk** — Depends on Google TPU generation roadmap (TPU v6 / TPU v7), Broadcom custom ASIC / rack-component supply, TSMC fabrication capacity, HBM/advanced packaging, and networking optics. Broadcom 8-K supply-assurance through 2031 implies long-tail capacity reservation.
5. **Technology obsolescence risk** — TPU vs. NVIDIA GPU portability risk; Anthropic must maintain workload portability across Trainium, TPU, and NVIDIA platforms. Custom Broadcom silicon roadmap risk if architecture transitions over 2027–2031 window.
6. **Financing risk** — No public RPO or capex funding schedule; Broadcom says parties are discussing operational and financial partners, indicating financing stack not finalized. Industry dollar estimates remain secondary. Alphabet/Google Cloud RPO disclosure does not isolate Anthropic-specific.
7. **Structural optionality** — Multi-party structure may allow staging across Google-owned regions, Fluidstack shells, or other operational partners; physical capacity not assignable from public sources alone. "Up to one million TPUs" and "approximately 3.5 GW" both imply ranges. Anthropic links April 2026 deal to November 2025 $50B Fluidstack commitment, raising same-customer-demand-double-count risk against the Fluidstack overlay.

## Temporal Logic

- **Earliest**: 2026-01-01 — Google Cloud Oct 23, 2025 release: Anthropic will have access to capacity **"coming online in 2026"**.
- **Central**: 2028-07-01 — mid-window ramp blending the 2026 1 GW tranche and the 2027+ 3.5 GW tranche.
- **Latest**: 2031-12-31 — Broadcom 8-K supply-assurance horizon **"through up to 2031"**.
- **Critical-path dependency**: Google TPU generation cadence (v6/v7 ramp); Broadcom custom-ASIC / rack-component supply; identification of "operational and financial partners" referenced in Broadcom 8-K; site allocation decisions (Google-owned vs. Fluidstack vs. other).

## Reviewer Findings Addressed

- **Rev-4.3 user direction**: "Anthropic-Google deal should exist in the paper at appropriate tier" — addressed by NEW atom `anthropic_google_broadcom_physical_tpu` at T5, central 2.700 GW facility, 4.5 GW IT total exposure (1 GW + 3.5 GW). Replaces prior 0 GW Class B treatment.
- **Dedupe explicit**: 50% overlap against six Google Epoch sites + Fluidstack Lake Mariner documented in `dedupe_audit.csv` rows.
- **Source upgrade**: Broadcom Form 8-K (SEC filing) is primary-tier evidence for the 3.5 GW tranche; replaces secondary-only Sullivan & Cromwell highlight.

## Open Questions / Gaps

- Site list for the 2026 one-million-TPU tranche and the 2027+ 3.5 GW tranche.
- Whether the 3.5 GW is IT load, facility load, contractual compute nameplate, or another capacity convention.
- Whether Anthropic's November 2025 $50B Fluidstack commitment includes physical shells for Google/Broadcom TPUs.
- Identity of Broadcom's "operational and financial partners" — whether they include Fluidstack, Google-owned campuses, utilities, SPVs, or colocation lessors.
- Alphabet/Google Cloud or Anthropic contract accounting: RPO, minimum take-or-pay, prepayment, cancellation, and term.
- Utility interconnection evidence for any candidate site that would support multi-GW incremental TPU load.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Broadcom Form 8-K](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/0001193125-26-144028-index.htm) | 2026-04-06 | SEC filing | 3.5 GW Anthropic access via Broadcom; long-term TPU/supply-assurance through 2031 | "approximately 3.5 gigawatts" |
| [Anthropic, "Expanding our use of Google Cloud TPUs and services"](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) | 2025-10-23 | Primary company announcement | Up to one million TPUs; well over 1 GW in 2026; "tens of billions" | "well over a gigawatt" |
| [Anthropic, "Google/Broadcom partnership"](https://www.anthropic.com/news/google-broadcom-partnership-compute) | 2026-04-06 | Primary company announcement | Multiple GW TPU capacity from 2027; "vast majority" U.S.-sited; expansion of $50B U.S. infra commitment | "vast majority will be sited in the United States" |
| [Google Cloud, "Anthropic Expands Use of Google Cloud and TPUs"](https://www.googlecloudpresscorner.com/2026-04-06-Anthropic-Expands-Use-of-Google-Cloud-and-TPUs) | 2026-04-06 | Primary company announcement | Delivery via Google Cloud services and Google-built TPUs through Broadcom | "Google-built TPUs supplied through Broadcom" |
| [Google Cloud, "Anthropic to Expand Use of Google Cloud TPUs and Services"](https://www.googlecloudpresscorner.com/2025-10-23-Anthropic-to-Expand-Use-of-Google-Cloud-TPUs-and-Services) | 2025-10-23 | Primary company announcement | 2026 capacity availability | "coming online in 2026" |
| [Anthropic, "$50B in American AI infrastructure"](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure) | 2025-11-12 | Primary company announcement | $50B Fluidstack U.S. infra commitment; framing for April 2026 expansion | "$50 billion" |
| [Sullivan & Cromwell client highlight](https://www.sullcrom.com/About/News-and-Events/Highlights/2026/April/SC-Advises-Broadcom-3-5GW-TPU-Based-AI-Compute-Collaboration-Google-Anthropic) | 2026-04-08 | Secondary legal-adviser | Confirms 3.5 GW transaction architecture | "3.5GW TPU-based AI compute" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Site-level facility MW for Goodnight/New Albany/Cedar Rapids/Omaha/Pryor/Council Bluffs/Lake Mariner | "Google" / "Fluidstack" |

## Cross-Links

- Research dispatch: `docs/research/A3_anthropic_google_broadcom.md`
- Atoms: `canonical_capacity_atoms.yaml` (`anthropic_google_broadcom_physical_tpu`)
- Dedupe entries: `dedupe_audit.csv` (rows for `anthropic_google_broadcom_physical_tpu`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
- Related: `contracts/anthropic_fluidstack.md` (same-program overlap), `contracts/anthropic_aws.md`, `contracts/anthropic_azure.md`
