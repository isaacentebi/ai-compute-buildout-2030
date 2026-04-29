# Anthropic / Fluidstack — $50B U.S. AI Infrastructure (No Disclosed MW)

## TL;DR

Anthropic and Fluidstack announced on November 12, 2025 a **$50B "American computing infrastructure"** program covering custom-built data centers in Texas and New York, **"with more sites to come"** and capacity **"coming online throughout 2026"**. The announcement uses **"gigawatts of power"** language but discloses no megawatt figures, no term, no take-or-pay structure, no named site addresses, and no funding mechanism (whether Anthropic directly funds owned assets, leases Fluidstack-developed capacity, or underwrites Fluidstack project finance). Per Rev-4.3 policy, the canonical atom `anthropic_fluidstack_undisclosed_mw` is **intentionally excluded from all GW totals** to preserve disclosure-purity discipline; the $50B dollar magnitude is documented as a **material omission risk** because no mechanism converts dollars to MW without an analyst-inferred capex-density assumption. Site-level evidence at TeraWulf Lake Mariner (NY, 360 MW critical IT contracted to Fluidstack) and Cipher Mining Barber Lake (Colorado City, TX, 300 MW) suggests probable site mapping, but neither operator names Anthropic in primary releases.

## Counterparties

- **Operator**: Fluidstack (private; Google-backed). Cloud-capacity operator and lessee; developer of custom data-center capacity for Anthropic.
- **Anchor tenant / user**: Anthropic, PBC.
- **Financing partner(s)**: Google backstops Fluidstack lease obligations ($1.4B + $333M disclosed via TeraWulf and Cipher 8-K filings); Anthropic dollar magnitude $50B per its own announcement; physical-site landlords TeraWulf (Lake Mariner) and Cipher Mining (Barber Lake) finance shells.

## Structure

- **Type**: Unknown — public announcement does not classify as lease, take-or-pay, equity-in-Fluidstack, project-finance underwriting, or framework agreement. Likely a hybrid of cloud capacity reservation plus capex-bearing site development.
- **Term**: Not disclosed.
- **Announced contract value**: $50B "American computing infrastructure" envelope. No site-level capex break-out.
- **Equity cross-investments**: None disclosed in this transaction.
- **Take-or-pay coverage**: Not disclosed.
- **Optionality**: High. "More sites to come"; "gigawatts of power" without MW; "throughout 2026" without delivery curve.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | n/d | T5 | Anthropic and Fluidstack say "throughout 2026"; no MW disclosure |
| 2027 | n/d | T5 | "More sites to come"; site-level evidence at Lake Mariner (full buildout 2027-03-31) and Barber Lake (Sep 2026 / Jan 2027 phasing) |
| 2028 | n/d | T5 | No primary cadence |
| 2029 | n/d | T5 | No primary cadence |
| 2030 | n/d | T5 | No primary cadence |

**No MW assigned. The atom is excluded from all totals.** Site-level candidates are tracked separately (Lake Mariner under Epoch row; Barber Lake ex-Epoch as of local snapshot). This page documents the $50B dollar magnitude and the material omission risk.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| Fluidstack Lake Mariner | Barker, NY | TeraWulf (landlord) / Fluidstack (tenant) | Fluidstack → Anthropic, G42; 0.509 GW facility by 2027-03-31 | Strongest NY candidate; 360 MW critical IT contracted Fluidstack per TeraWulf 8-K | T2 |
| Cipher Mining Barber Lake | Colorado City, TX | Cipher Mining (landlord) / Fluidstack (tenant) | Not in Epoch local snapshot | Strongest TX candidate; 300 MW lease per Cipher Nov 20, 2025 release | T3 |
| Other Texas/New York sites | undisclosed | Fluidstack | Not in Epoch | "More sites to come" envelope | T5 |

## Financing Stack

- **Capex envelope**: $50B Anthropic dollar magnitude (not site capex). Site capex absorbed by landlords (TeraWulf at Lake Mariner; Cipher Mining at Barber Lake) and Fluidstack debt with Google backstop.
- **Equity / debt / RPO**: Google backstops $1.4B + $333M Fluidstack lease obligations per TeraWulf and Cipher SEC filings; Anthropic underwrites Fluidstack via $50B program but mechanism not disclosed.
- **Public disclosures**: Anthropic Nov 12, 2025; Fluidstack Nov 12, 2025; TeraWulf 8-K Aug 18, 2025 (Fluidstack 360 MW critical IT contract); Cipher Mining Nov 20, 2025 (Barber Lake full 300 MW lease).

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `anthropic_fluidstack_undisclosed_mw` — null MW, T5, status `contracted`, **excluded from all totals** (`included_raw_horizon: false`, `included_non_stretch: false`, `included_conservative_T1_T2_T3: false`, `included_probability_weighted: false`). Documented `unknown_mw_reason: "No direct MW disclosure; dollar-only conversion intentionally not used."`
- `fluidstack_anthropic_undisclosed_mw` — paired exclusion atom (overlay-side).
- Cross-references: `epoch_fluidstack_lake_mariner_operational` (0.068 GW), `epoch_fluidstack_lake_mariner_buildout_remaining` (full buildout to 0.509 GW).

## Dedupe Notes

The Anthropic-Fluidstack $50B envelope is **deliberately not converted to MW** to avoid counting the same Anthropic demand multiple times across overlapping announcements. Anthropic's April 6, 2026 Google/Broadcom 3.5 GW release explicitly frames that deal as **"a major expansion of our November 2025 $50 billion American infrastructure commitment"**, raising same-program overlap risk against `anthropic_google_broadcom_physical_tpu` (which carries 2.700 GW central / 5.400 GW facility high). Lake Mariner is the only Epoch site explicitly carrying Anthropic-Fluidstack attribution and is treated as a candidate overlap with `anthropic_google_broadcom_physical_tpu` (0.509 GW credited to that atom's overlap dedupe). Barber Lake (Cipher) is ex-Epoch in the local snapshot and remains a candidate for adjudication. The $50B dollar magnitude is preserved on this page as a **material omission risk** so reviewers see the disclosure gap rather than a silent zero.

## Risk Axes

1. **Counterparty risk** — Anthropic is a private lab with fast revenue growth but heavy forward compute commitments stacked across Fluidstack ($50B), AWS (5 GW / $100B+), Google/Broadcom (4.5 GW IT), and Azure (1 GW / $30B). Fluidstack is private and Google-backed; no SEC RPO disclosure.
2. **Regulatory risk** — No site permits named in the Anthropic/Fluidstack announcement. Lake Mariner relies on TeraWulf's existing crypto-to-AI conversion permits; Barber Lake similarly is a bitcoin-to-HPC pivot requiring local approvals; "more sites to come" exposes Anthropic to undisclosed local opposition and grid-study cadence at unannounced campuses.
3. **Power / interconnect risk** — "Gigawatts of power" language with no queue position, utility, interconnection, or grid-upgrade allocation. TeraWulf cites dual 345 kV feeds and 500 MW available plus 250 MW pending regulatory approval at Lake Mariner; Cipher cites 300 MW Barber Lake delivery.
4. **Supply chain risk** — TPU/NVIDIA/AI-rack bill of materials exposed to HBM, advanced packaging, optical/networking, transformer, and switchgear bottlenecks. Fluidstack chip mix not publicly tied to specific Anthropic workloads.
5. **Technology obsolescence risk** — Capacity may be Google TPU, NVIDIA GPU, or mixed hardware; no primary source ties a specific chip stack to the $50B envelope. If TPU/Google-Broadcom architecture shifts (Broadcom 8-K supply through 2031), Fluidstack-built shells must remain chip-flexible.
6. **Financing risk** — Public announcement does not state who funds construction debt or whether Anthropic obligations are unconditional. TeraWulf and Cipher both flag construction, financing, and principal-customer risks. Google backstop becomes effective only after lease commencement and specified defaults per TeraWulf disclosure.
7. **Structural optionality** — Could be a branding layer over already-signed Fluidstack leases (Lake Mariner, Barber Lake) and Google-backed sites rather than net-new physical capacity. Anthropic's April 6, 2026 framing of Google/Broadcom as a $50B-program expansion supports same-program overlap interpretation; reviewer caution warranted before treating $50B as fully incremental.

## Temporal Logic

- **Earliest**: 2026-01-01 — Anthropic and Fluidstack say capacity comes online **"throughout 2026"**.
- **Central**: 2026-12-31 — mid-year ramp aligned with Lake Mariner full buildout (2027-03-31) and Barber Lake delivery (Sep 2026 / Jan 2027 phasing).
- **Latest**: Not disclosed; "more sites to come" implies post-2026 delivery.
- **Critical-path dependency**: Site identification beyond Lake Mariner and Barber Lake; chip allocation (TPU vs GPU); Fluidstack project-finance closes; Anthropic enterprise revenue trajectory to support $50B obligation.

## Reviewer Findings Addressed

- **Material omission risk documented**: $50B "gigawatts of power" with no MW is preserved as a disclosure gap rather than silently zeroed. Atom carries `unknown_mw_reason` field; both `anthropic_fluidstack_undisclosed_mw` and `fluidstack_anthropic_undisclosed_mw` are excluded from totals.
- **Same-program overlap with Anthropic-Google/Broadcom**: Anthropic Apr 6, 2026 release explicitly frames Google/Broadcom 3.5 GW as expansion of the Nov 2025 $50B commitment. Documented in `dedupe_audit.csv` and reflected in `anthropic_google_broadcom_physical_tpu` overlap dedupe (0.509 GW Lake Mariner credit).
- **Site-level candidates flagged**: Lake Mariner (Epoch) and Barber Lake (ex-Epoch) carried as adjudication candidates with operator-side primary MW evidence.

## Open Questions / Gaps

- Signed Anthropic-Fluidstack contract terms: lease, take-or-pay, capex contribution, debt support, guarantees, cancellation rights, duration.
- Named sites under the $50B announcement, especially whether New York equals Lake Mariner and Texas equals Barber Lake, plus the "more sites to come" envelope.
- Anthropic-specific MW at Lake Mariner and Barber Lake, separated from G42/Core42, Google backstop exposure, and general Fluidstack cloud capacity.
- Facility vs IT basis for all announced "gigawatt" figures; no primary source converts Anthropic's "gigawatts of power" to interconnection MW.
- Utility interconnection records, PPAs, and grid upgrade cost allocation for the Texas sites.
- Chip allocation by site: Google TPU vs NVIDIA GPU vs mixed hardware, and whether Broadcom/Google TPU capacity physically lands at Fluidstack sites or Google-operated sites.
- Whether the $50B figure should be partially absorbed into `anthropic_google_broadcom_physical_tpu` overlap dedupe at higher fraction than the current Lake Mariner credit.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [Anthropic, "$50 billion in American AI infrastructure"](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure) | 2025-11-12 | Primary company announcement | $50B; Texas and New York; throughout 2026 | "building data centers with Fluidstack in Texas and New York"; "$50 billion" |
| [Fluidstack, "Selected by Anthropic to deliver custom data centers in the US"](https://www.fluidstack.io/about-us/blog/fluidstack-selected-by-anthropic-to-deliver-custom-data-centers-in-the-us) | 2025-11-12 | Primary company announcement | "Custom" Anthropic data centers; "gigawatts of power" framing | "gigawatts of power" |
| [TeraWulf 8-K](https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-079463/0001104659-25-079463.pdf) | 2025-08-18 | SEC filing | Lake Mariner Fluidstack 360 MW critical IT contract; Google backstop | "total contracted critical IT load for Fluidstack at the campus increases to approximately 360 MW" |
| [Cipher Mining, Barber Lake 300 MW lease](https://www.globenewswire.com/news-release/2025/11/20/3191801/0/en/Cipher-Mining-Signs-Additional-56-MW-10-Year-AI-Hosting-Agreement-with-Fluidstack.html) | 2025-11-20 | Primary company announcement | Fluidstack leases full 300 MW at Cipher Barber Lake site | "lease the entire 300 MW of capacity at Cipher's Barber Lake site" |
| [Anthropic, "Google/Broadcom partnership"](https://www.anthropic.com/news/google-broadcom-partnership-compute) | 2026-04-06 | Primary company announcement | Frames Google/Broadcom as expansion of $50B Nov 2025 commitment | "major expansion of our November 2025 $50 billion American infrastructure commitment" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Lake Mariner facility MW; Anthropic/G42 user attribution | "Fluidstack Lake Mariner" |

## Cross-Links

- Research dispatch: `docs/research/A4_anthropic_fluidstack.md`
- Atoms: `canonical_capacity_atoms.yaml` (`anthropic_fluidstack_undisclosed_mw`, `fluidstack_anthropic_undisclosed_mw`)
- Dedupe entries: `dedupe_audit.csv` (rows for `fluidstack_anthropic_undisclosed_mw`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
- Related: `contracts/anthropic_google_broadcom.md` (same-program overlap), `contracts/anthropic_aws.md`, `contracts/anthropic_azure.md`
