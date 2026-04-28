# OpenAI Stargate UAE — Sovereign Sidebar (1 GW Cluster, 1.4 GW Epoch Facility)

## TL;DR

Stargate UAE is OpenAI's first international Stargate deployment, announced May 22, 2025 as a **"1-gigawatt compute cluster"** in Abu Dhabi within a broader 5 GW UAE-US AI Campus, built by G42 / Khazna Data Centers and operated by OpenAI and Oracle under the U.S.-UAE AI Acceleration Partnership. The named near-term tranche is **"first 200MW"** with G42 confirming on October 16, 2025 that civil/structural/architectural construction is well advanced and long-lead equipment procurement is complete. The U.S. Department of Commerce November 19, 2025 statement approved up to **"35,000 Nvidia Blackwell"** GB300-equivalent chips for G42 and Humain combined, conditional on KYC, security, and reporting requirements. Per Rev-4.3 policy, this entry is treated as a **sovereign sidebar** entry (`scope: sovereign`, `included_raw_horizon: false`, `included_probability_weighted: false`) and is **NOT in the Western denominator**. The canonical Epoch row carries 1.400 GW facility (1.207 GW IT bridge), T4, with 200 MW first tranche by 2026-12-01 and full buildout by 2028-01-01.

## Counterparties

- **Operator**: G42 / Khazna Data Centers (UAE state-linked infrastructure) for build; OpenAI and Oracle for cluster operations.
- **Anchor tenant / user**: OpenAI (named cluster); Oracle (cloud co-operator); UAE sovereign / regional users; approved U.S. cloud service providers under Commerce KYC framework.
- **Financing partner(s)**: G42/Khazna (UAE/PIF-adjacent capital); MGX (initial Stargate equity funder per Jan 2025 launch); SoftBank (consortium participant); NVIDIA (GB300 supplier); Cisco (networking/security/observability). UAE entities also commit reciprocal U.S. digital infrastructure investment per Commerce framing.

## Structure

- **Type**: JV (sovereign-AI government-to-government framework) plus chip procurement (NVIDIA GB300) plus cloud capacity (OpenAI/Oracle operation).
- **Term**: Not disclosed at project level.
- **Announced contract value**: Not disclosed at the Stargate UAE project level.
- **Equity cross-investments**: Multi-party consortium (G42, OpenAI, Oracle, NVIDIA, Cisco, SoftBank, MGX); UAE-specific funding shares undisclosed.
- **Take-or-pay coverage**: Not disclosed.
- **Optionality**: High. 200 MW is the only construction-progress tranche; remaining 800 MW remains a named plan; export-license cadence beyond Nov 2025 35,000-chip approval is sequential and conditional.

## GW Shape Over Time

| Year | Facility GW (low / central / high) | Operational status | Notes |
|------|-----------------------------------|---------------------|-------|
| 2026 | 0.20 / 0.28 / 0.28 | T4 | Building 1+2 first tranche by 2026-12-01 per Epoch local snapshot |
| 2027 | 0.28 / 0.50 / 1.0 | T4 | Mid-cluster ramp; remaining 800 MW pending |
| 2028 | 0.5 / 1.0 / 1.40 | T4 | Full buildout by 2028-01-01 per Epoch |
| 2029 | 1.0 / 1.40 / 1.40 | T4 | Stable cluster envelope |
| 2030+ | 1.40 / 1.40 / 1.40 | T4 | Sovereign sidebar; not in Western denominator |

**Sovereign sidebar — NOT in Western denominator.** `scope: sovereign`, `included_raw_horizon: false`, `included_probability_weighted: false`.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|------|----------|----------|-------------------|----------------------------|------|
| OpenAI Stargate UAE | Abu Dhabi, UAE (within 5 GW UAE-US AI Campus, ~10 sq mi) | G42/Khazna build; OpenAI+Oracle operate | G42 → OpenAI; 0.0 GW current, 0.28 GW first tranche by 2026-12-01, 1.40 GW full by 2028-01-01 | Direct match to canonical Epoch row | T4 (sovereign) |
| Microsoft / G42 Khazna expansion | Abu Dhabi, UAE | G42/Khazna build; Microsoft Azure sovereign cloud | Khazna/G42 → Microsoft Azure sovereign cloud; 0.20 GW IT / 0.26 GW facility | Separate sovereign overlap candidate; not part of Stargate UAE cluster | T4 (sovereign) |

## Financing Stack

- **Capex envelope**: Not disclosed at project level.
- **Equity / debt / RPO**: G42 leads build/investment with UAE/PIF capital; multi-party consortium funding; UAE entities commit reciprocal U.S. digital infrastructure investment.
- **Public disclosures**: OpenAI Stargate UAE introduction May 22, 2025; G42 release May 22, 2025; Cisco consortium release May 22, 2025; U.S. Commerce 5 GW campus unveiling May 15, 2025; G42 PRNewswire construction update Oct 16, 2025; U.S. Commerce UAE/Saudi chip exports statement Nov 19, 2025; G42 chip approval release Nov 20, 2025.

## Atoms Sourced (in canonical_capacity_atoms.yaml)

- `epoch_openai_stargate_uae_buildout_remaining` — 1.400 GW facility (1.207 GW IT bridge at PUE 1.16), T4, scope sovereign, **excluded from Western raw and probability-weighted totals** (`scope: sovereign`, `included_raw_horizon: false`, `included_probability_weighted: false`).

## Dedupe Notes

This Stargate UAE atom is intentionally segregated from the Western denominator. The dedupe direction is `full_remove_from_western_keep_sovereign`. The named 1 GW OpenAI Stargate cluster sits inside a broader 5 GW UAE-US AI Campus per Commerce; the remaining ~4 GW is broader campus capacity (U.S. hyperscaler + approved CSP), not OpenAI-specific, and is **not** carried as a separate sovereign atom in canonical to avoid silent expansion of sovereign sidebar. The Microsoft/G42 Khazna 200 MW expansion (Microsoft Nov 5, 2025) is a separate sovereign overlap candidate tracked under `microsoft_g42_uae_khazna`. Local Epoch facility-MW conversion (1 GW cluster → 1.4 GW facility at PUE 1.16) remains a candidate convention rather than a primary-source basis disclosure.

## Risk Axes

1. **Counterparty risk** — Medium. G42/Khazna is UAE state-linked infrastructure; OpenAI and Oracle are operators, but project-level binding economics are not disclosed. G42 has historic CCP-affiliation allegations that the company denies and that drove its 2022-onward pivot toward U.S. partners.
2. **Regulatory risk** — High. U.S. advanced-chip exports are licensed and conditioned on security/reporting controls; future U.S. policy or compliance findings can slow deployment. Commerce November 19, 2025 approved up to 35,000 GB300-equivalents for G42/Humain combined — materially below several-hundred-thousand-GPU long-run ambition. Further allocations require ongoing BIS review.
3. **Power / interconnect risk** — Medium-high. Commerce says full campus uses nuclear, solar, and gas; no primary utility interconnect schedule or plant-by-plant COD found. UAE grid integration at 1 GW cluster scale typically requires multi-year substation/generation alignment.
4. **Supply chain risk** — Medium. G42 says long-lead equipment procured and first mechanical deliveries arrived; GB300 export availability remains gating. NVIDIA Grace Blackwell systems and Cisco networking/security gear are named.
5. **Technology obsolescence risk** — Medium. Source language is "AI cluster / infrastructure capacity," not a clean facility-vs-IT power basis. Multi-year construction window may see GB300 → Rubin transition; UAE reliance on continued export licensing of frontier chips.
6. **Financing risk** — Medium. Capex and debt/equity stack undisclosed; likely backed by G42/Khazna/UAE capital plus partner vendor contributions. Broader Stargate names MGX/SoftBank/OpenAI/Oracle, but UAE-specific funding shares not public.
7. **Structural optionality** — High. 200 MW is the only construction-progress tranche; remaining 800 MW remains a named plan. Sovereign-AI policy framing means deployment cadence depends on bilateral U.S.-UAE Acceleration Partnership health and continued export licensing.

## Temporal Logic

- **Earliest**: 2026-01-01 — OpenAI/G42 May 2025 announcements: "200MW expected to go live in 2026"; G42 October 16, 2025 update: civil/structural/architectural construction well advanced, long-lead equipment procured.
- **Central**: 2026-12-01 — Epoch local timeline carries Building 1 and 2 first tranche operational by this date.
- **Latest**: 2028-01-01 — Epoch local snapshot full buildout date.
- **Critical-path dependency**: Continued BIS/Commerce export licensing beyond Nov 2025 35,000-chip approval; UAE substation/generation phasing for 1 GW cluster; G42-Khazna construction execution; OpenAI/Oracle cloud-platform commissioning.

## Reviewer Findings Addressed

- **Sovereign sidebar treatment confirmed**: `scope: sovereign`, `included_raw_horizon: false`, `included_probability_weighted: false`. Stargate UAE is **NOT in Western denominator**. Local canonical correctly tags this row.
- **5 GW campus separation**: Broader 5 GW UAE-US AI Campus is documented as bilateral sovereign program with hyperscaler allocation not disclosed; OpenAI-specific cluster is 1 GW only. The remaining ~4 GW is **not** carried as a separate atom.
- **G42-Microsoft Khazna 200 MW**: Tracked separately under `microsoft_g42_uae_khazna` as additional sovereign overlap candidate.

## Open Questions / Gaps

- Project-level capex, ownership, debt/equity split, and take-or-pay obligations for Stargate UAE.
- Whether OpenAI has exclusive, priority, or partial rights to the 1 GW cluster, and whether Oracle is cloud operator, capacity reseller, or co-operator.
- Facility-vs-IT basis for the 200 MW and 1 GW figures; local Epoch facility conversion remains candidate, not primary-source fact.
- Primary power/interconnection schedule for the Abu Dhabi site, including substations, gas/nuclear/solar supply contracts, and COD milestones.
- Export-license cadence beyond the November 2025 35,000 GB300-equivalent approval, and whether approvals are allocated to Stargate UAE versus other G42/UAE facilities.
- Physical verification refresh after the local Epoch 2025-11-16 imagery note and G42's October 2025 construction update.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote |
|--------|------|------|---------------------|-------|
| [OpenAI, "Introducing Stargate UAE"](https://openai.com/index/introducing-stargate-uae/) | 2025-05-22 | Primary company announcement | First international Stargate; 1 GW; 200 MW in 2026 | "1-gigawatt compute cluster" |
| [U.S. Commerce, "UAE and US Presidents attend the unveiling of Phase 1 of new 5GW AI campus in Abu Dhabi"](https://www.commerce.gov/news/press-releases/2025/05/uae-and-us-presidents-attend-unveiling-phase-1-new-5gw-ai-campus-abu) | 2025-05-15 | Primary government announcement | 5 GW campus; G42 build; KYC/security; nuclear/solar/gas | "5GW of capacity" |
| [G42, "Global Tech Alliance Launches Stargate UAE"](https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae) | 2025-05-22 | Primary company announcement | G42 build; OpenAI/Oracle operate; consortium | "1-gigawatt compute cluster" |
| [Cisco, "Cisco Joins Stargate UAE Initiative"](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2025/m05/cisco-joins-stargate-uae-initiative.html) | 2025-05-22 | Primary company announcement | Consortium confirmation; 1 GW target; 200 MW initial | "200MW expected to go live in 2026" |
| [G42 PRNewswire construction update](https://www.prnewswire.com/news-releases/g42-provides-update-on-construction-of-stargate-uae-ai-infrastructure-cluster-302586401.html) | 2025-10-16 | Primary company wire | Khazna developer role; long-lead procurement complete; first mechanical deliveries | "first 200MW" |
| [U.S. Commerce, "Statement on UAE and Saudi Chip Exports"](https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports) | 2025-11-19 | Primary government announcement | 35,000 GB300-equivalent approval; security/reporting | "up to 35,000 Nvidia Blackwell chips" |
| [G42, "G42 Receives U.S. Approval for Advanced AI Chip Exports"](https://www.g42.ai/resources/news/g42-receives-us-approval-advanced-ai-chip-exports-enabling-full-scale-deployment-trusted-ai-infrastructure) | 2025-11-20 | Primary company announcement | Approval moves project from planning to deployment | "RTE/BIS guidelines" |
| [Microsoft, "Microsoft and G42 Accelerate UAE's Digital Future"](https://news.microsoft.com/source/emea/2025/11/microsoft-and-g42-accelerate-uaes-digital-future-with-major-data-centre-expansion/) | 2025-11-05 | Primary company announcement | Separate Microsoft 200 MW Khazna sovereign cloud expansion | "200 megawatts" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | 1.400 GW facility full buildout 2028-01-01; 0.28 GW first tranche 2026-12-01; sovereign scope | "OpenAI Stargate UAE" |

## Cross-Links

- Research dispatch: `docs/research/B3_openai_stargate_uae.md`
- Atoms: `canonical_capacity_atoms.yaml` (`epoch_openai_stargate_uae_buildout_remaining`)
- Dedupe entries: `dedupe_audit.csv` (row for `epoch_openai_stargate_uae_buildout_remaining`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Schema: `contracts/_schema.md`
- Related: `contracts/openai_stargate_us.md` (Western denominator stack), `contracts/humain.md` (Saudi sovereign sidebar parallel)
