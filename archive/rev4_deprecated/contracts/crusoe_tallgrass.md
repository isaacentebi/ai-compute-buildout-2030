# Crusoe / Tallgrass — Cheyenne Project Jade and Abilene

## TL;DR

The Crusoe/Tallgrass contract bundle splits into two physically distinct development envelopes. **Cheyenne (Project Jade)** is a 1.8 GW AI data center campus in southeast Wyoming announced jointly by Tallgrass and Crusoe on July 24, 2025, with Laramie County File 26-023 site plans for both Project Jade (600 acres / five DC buildings / 40 BESS units / six continuous phases) and the BFC Power / Cheyenne Power Hub (659 acres / two combined-cycle turbines plus aero turbines and a fuel-cell yard) "approved with conditions" January 6, 2026. Tallgrass's release also says the campus is "designed to scale up to 10 gigawatts," but the on-site generation cap is 2.7 GW per DCD reporting — so the 8.2 GW stretch beyond 1.8 GW would require additional generation. **No public hyperscaler tenant or take-or-pay obligation has been disclosed for Cheyenne.** This warrants a T4 tier for the 1.8 GW base atom and T5 for the 8.2 GW stretch increment. **Abilene** is different: Crusoe's existing 1.18 GW Stargate/Oracle/OpenAI campus (5502 Spinks Rd) and the adjacent 0.941 GW Crusoe Abilene Microsoft Expansion (announced March 27, 2026) are both already in the Epoch row set and are excluded from this overlay's incremental count via `crusoe_abilene_epoch_overlap`. Shackelford County (175 Private Road 1604) is a separate Epoch row at 1.96 GW.

## Counterparties

- **Operator:**
  - **Cheyenne:** WY DC 1, LLC (indirect Crusoe subsidiary; Project Jade applicant/owner per Laramie County site-plan package). Tallgrass Integrated Logistics Solutions (BFC Power and Cheyenne Power Hub applicant/owner).
  - **Abilene:** Crusoe (developer); Oracle Cloud Infrastructure (operator at Stargate Phase 1).
- **Anchor tenant:**
  - **Cheyenne:** Undisclosed. Public sources do not name a hyperscaler tenant, lease term, take-or-pay, or RPO for Project Jade.
  - **Abilene Stargate (5502 Spinks Rd):** OpenAI via Oracle, original Stargate site (in Epoch).
  - **Abilene Microsoft (adjacent):** Microsoft, named explicitly in Crusoe's March 27, 2026 release (in Epoch as `Crusoe Abilene Expansion`).
- **Financing partners:**
  - Tallgrass (energy-infrastructure investment of approximately $7B per DCD); Crusoe announced $50B total project ambition for Cheyenne.
  - Blue Owl / Crusoe $15B Abilene JV financing (Kirkland & Ellis press release, May 2025).
  - GE Vernova 29-unit gas turbine deal for Crusoe (separate announcement).

## Structure

- **Type:** Cheyenne — JV / co-located energy + data-center development; tenant unknown. Abilene — colocation/build-to-suit cloud capacity (Stargate/Microsoft).
- **Term:** Not disclosed for Cheyenne. Stargate/Abilene Phase 1 buildout running 2024–2026; Abilene Microsoft expansion energization mid-2027.
- **Announced contract value:** Cheyenne — DCD reports up to $50B total project cost and $7B Tallgrass infrastructure investment; **no public anchor lease or project-finance close.** Abilene Stargate — $15B Blue Owl JV financing (development-side).
- **RPO/backlog:** None disclosed for Cheyenne. Abilene Stargate sits within OpenAI's broader Stargate commitments via Oracle.
- **Take-or-pay coverage:** Not disclosed for Cheyenne. Abilene Microsoft Expansion structure not publicly specified beyond Microsoft's named support.
- **Exclusivity:** None disclosed for Cheyenne.
- **Optionality:** "Designed to scale up to 10 gigawatts" (Tallgrass press release 2025-07-24) is explicit scale-up optionality, not firm capacity. The 600 MW Abilene expansion that OpenAI evaluated in September 2025 was reportedly shifted away by Crusoe to the Microsoft adjacent campus per AP March 2026.

## GW Shape Over Time

| Year | Facility GW low | Facility GW central | Facility GW high | Operational status | Notes |
|---|---:|---:|---:|---|---|
| 2026 | 0.0 | 0.0 | 0.0 | T4 | Project Jade site plan approved January 6, 2026; construction commencement; no buildings energized |
| 2027 | 0.20 | 0.30 | 0.50 | T4 | DCD: "first data center buildings hoped to be electrified in 2027"; Abilene Microsoft Expansion first building mid-2027 (in Epoch) |
| 2028 | 0.60 | 0.90 | 1.20 | T4 | Multi-phase Cheyenne build per six-phase site plan |
| 2029 | 1.20 | 1.50 | 1.80 | T4 | Approaching site-plan capacity per Laramie County package |
| 2030 | 1.50 | 1.80 | 1.80 | T4 | Project Jade site-plan capacity envelope |
| Stretch | — | — | 10.0 | T5 | "Designed to scale up to 10 gigawatts" (Tallgrass); requires power beyond 2.7 GW on-site cap |

Abilene capacity (1.18 GW Stargate Phase 1 + 0.941 GW Microsoft Expansion = 2.121 GW total) is fully in the Epoch row set; not duplicated above.

## Sites

| Site | Location | Operator | Epoch attribution | Overlap with this contract | Tier |
|---|---|---|---|---:|---|
| Project Jade / Switchgrass Industrial Park | ~8 mi south of Cheyenne, west of US-85, ~1 mi south of Terry Ranch Rd, Laramie County, WY | WY DC 1, LLC (Crusoe sub) | None in local Epoch snapshot | 1.8 GW facility (site-plan capacity); 8.2 GW stretch ex-Epoch | T4 / T5 stretch |
| BFC Power / Cheyenne Power Hub | 659 acres adjacent to Project Jade | Tallgrass Integrated Logistics Solutions | None in local Epoch | Co-located power; 2.7 GW on-site cap | T4 |
| Crusoe Stargate Abilene | 5502 Spinks Rd, Abilene, TX | Crusoe; Oracle Cloud Infrastructure operator | Epoch row "OpenAI Stargate Abilene" 1.18 GW full buildout 2026-07-01 | 1.18 GW (excluded; already Epoch-attributed) | T2 |
| Crusoe Abilene Microsoft Expansion | Adjacent to 5502 Spinks Rd | Crusoe | Epoch row "Crusoe Abilene Expansion" 0.941 GW buildout 2027-11-11 | 0.941 GW (excluded; already Epoch-attributed) | T2 |
| OpenAI Stargate Shackelford | 175 Private Road 1604, Abilene, Shackelford County, TX | Oracle | Separate Epoch row "OpenAI Stargate Shackelford" 1.96 GW full buildout 2028-12-31 | Separate site (different address); not Crusoe Abilene | T2 |
| Crusoe Norway / Iceland operational | Various | Crusoe | Not in this overlay's Epoch slice | Operational seed capacity | T1 |

## Financing Stack

- **Capex envelope (Cheyenne):** DCD reports up to $50B total project cost; Tallgrass energy-infrastructure investment approximately $7B.
- **Equity:** Crusoe (private; recent Series E and venture financing). Tallgrass (privately held energy infrastructure operator).
- **Project finance / debt:** No Cheyenne project-finance close has been publicly announced. Abilene Stargate has $15B Blue Owl/Crusoe JV financing (Kirkland & Ellis announcement, May 2025).
- **RPO / prepaid:** None disclosed for Cheyenne. Abilene Stargate falls under OpenAI/Oracle commitments documented separately.
- **Public disclosures:** Tallgrass Crusoe press release (2025-07-24); Laramie County File 26-023 site-plan approval (2026-01-06); Crusoe Abilene Stargate live announcement (2025-09-30); Crusoe 900 MW Microsoft Abilene release (2026-03-27); GE Vernova 29-turbine deal release; Kirkland Blue Owl JV release.

## Atoms Sourced

- `atom:crusoe_cheyenne_or_other_future_capacity` (1.8 GW T4) — Cheyenne Project Jade site-plan capacity per Tallgrass primary release "develop a 1.8 gigawatt (GW) AI data center campus." Local canonical atom carries a 1.98 GW point reflecting residual ex-Epoch accounting.
- `atom:crusoe_abilene_epoch_overlap` (excluded) — 1.18 GW Stargate + 0.941 GW Microsoft Expansion already in Epoch; subtracted to avoid double-counting.
- `atom:crusoe_norway_iceland_operational` — Crusoe's existing Norway/Iceland operational footprint.
- `atom:epoch_crusoe_abilene_expansion_buildout_remaining` (0.941 GW; Epoch row, Microsoft-attributed).
- Cheyenne stretch increment (8.2 GW T5) — implicit "designed to scale up to 10 gigawatts" minus 1.8 GW site-plan base; not separately atomized in canonical (treated as T5 optionality).

## Dedupe Notes

- **Epoch overlap:** Crusoe Abilene Stargate (5502 Spinks Rd) is already an Epoch row at 1.18 GW; Crusoe Abilene Microsoft Expansion is already an Epoch row at 0.941 GW. Both excluded from this overlay's incremental count.
- **Cross-overlay overlap:** Cheyenne is not in Epoch; primary candidate ex-Epoch incremental site at 1.8 GW. The 0.18 GW gap between local canonical 1.98 GW and Tallgrass's 1.8 GW disclosure is residual ex-Epoch accounting from earlier Crusoe-future-capacity inputs and is documented in the C2 dispatch as not Cheyenne-specific.
- **Shackelford separation:** OpenAI Stargate Shackelford is a separate Epoch row at a different address (175 Private Road 1604, Shackelford County) versus Crusoe Abilene's 5502 Spinks Rd; do not merge.
- **Residual incremental GW:** 1.8 GW Cheyenne base + 8.2 GW stretch optionality (T5; not counted in central case).

## Risk Axes

1. **Counterparty:** Crusoe and Tallgrass are credible named developers, but **no public hyperscaler tenant, lease term, or take-or-pay contract is disclosed for Cheyenne.** Cheyenne is the principal counterparty risk: a 1.8 GW campus without an anchor tenant is structurally weaker than Abilene Stargate (Oracle/OpenAI) or Abilene Microsoft.
2. **Regulatory:** Laramie County File 26-023 site plans were approved with conditions on January 6, 2026 — further air, water, generation, pipeline, and construction permits remain execution gates. Tallgrass's BFC Power site requires fuel-cell yard, two combined-cycle turbines, temporary aeroderivative/light-duty turbines, and permanent aeroderivative/light-duty simple-cycle turbines, each of which carries separate state/federal permitting tracks. Wyoming PSC and FERC pipeline interconnection filings have not been publicly identified.
3. **Power / interconnect:** **The 2.7 GW on-site generation cap is the binding ceiling on the 10 GW stretch** — DCD reports the BFC/Cheyenne Power Hub will only generate 2.7 GW, so a 10 GW campus would need additional power sources beyond the planned plant. Cheyenne also depends on behind-the-meter gas/cogeneration, BESS (40 units in site plan), Tallgrass gas/CO2/water assets, and county/federal/state approvals. Abilene depends on ERCOT primary connection plus GE Vernova gas turbines for backup/grid stability; AP cites a 350 MW existing gas plant.
4. **Supply chain:** Multi-GW gas turbines, fuel cells, transformers, switchgear, liquid-cooling equipment, and AI racks face constrained delivery windows. The 29-unit GE Vernova gas turbine package for Crusoe addresses some equipment supply but does not cover the full Cheyenne BFC scope.
5. **Technology obsolescence:** Public sources do not identify chip stack, rack density, or critical IT load for Cheyenne; the 1.8 GW figure is facility/site-plan capacity, not IT MW. Future rack density and architecture could materially alter GW-to-compute translation.
6. **Financing:** **DCD reports $7B Tallgrass energy infrastructure and up to $50B total project cost; no public project-finance close or anchor lease has been found for Cheyenne.** Abilene has $15B Blue Owl JV financing for Stargate.
7. **Structural optionality:** **1.8 GW is a site-plan/development target; 10 GW is explicitly scale-up optionality** with no committed power, tenant, or financing path. Abilene Microsoft Expansion is structurally firmer (Microsoft named, on-site power plant under construction, mid-2027 first-energization target).

## Temporal Logic

- **Earliest plausible energization (Cheyenne):** 2027 — DCD says "first data center buildings hoped to be electrified in 2027."
- **Central case (Cheyenne):** 1.8 GW site-plan capacity by 2029–2030 across six continuous phases per the Laramie County package.
- **Latest plausible (Cheyenne):** Stretch optionality to 10 GW would require additional generation beyond the 2.7 GW on-site cap; no firm 10 GW timeline is publicly committed.
- **Critical-path dependency:** BFC Power / Cheyenne Power Hub permits and turbine deliveries; behind-the-meter gas pipeline interconnect; transmission upgrades for any ex-2.7-GW expansion.

## Reviewer Findings Addressed

- **Reviewer #6 (Rev-4.2):** "Cheyenne should be demoted to T4 because no public hyperscaler tenant or take-or-pay disclosed." Resolved. Cheyenne base 1.8 GW is T4; stretch beyond 1.8 GW to 10 GW is T5.
- **Abilene split:** Confirmed both 1.18 GW Stargate Phase 1 and 0.941 GW Microsoft Expansion are already Epoch rows; excluded from this overlay's incremental count.
- **Shackelford separation:** Verified Shackelford (175 Private Road 1604) is a different physical site from Crusoe Abilene (5502 Spinks Rd); kept as separate Epoch row.
- **2.7 GW on-site cap:** Documented explicitly as binding constraint on the 10 GW stretch language.

## Open Questions / Gaps

- Pull full Laramie County Project Jade and BFC Power/Cheyenne Power Hub site-plan sheets into a structured table: building count, square footage, generation units, phasing, conditions of approval, water/emissions assumptions.
- Find primary air permit, water permit, and any Wyoming PSC/FERC interconnect or pipeline filings for BFC Power and Cheyenne Power Hub.
- Confirm whether any hyperscaler tenant, lease term, take-or-pay, or project-finance close has been publicly filed for Cheyenne.
- Resolve Cheyenne capacity basis: 1.8 GW appears to be data-center campus/facility capacity; county materials disclose no critical IT MW.
- Reconcile Crusoe's 2.1 GW public Abilene total, Epoch's 1.180 + 0.941 = 2.121 GW facility buildout, and the Microsoft 672 MW critical-IT disclosure (two 336 MW critical-IT buildings).
- Check whether OpenAI relocated its previously evaluated 600 MW Abilene expansion to a specific other site after the March 2026 reshuffle.

## Source Citations

| Source | Date | Type | Load-bearing claim | Quote (verbatim) |
|---|---|---|---|---|
| [Tallgrass / Crusoe Cheyenne announcement](https://tallgrass.com/newsroom/press-releases/Crusoe) | 2025-07-24 | Primary release | 1.8 GW campus, 10 GW scale; Tallgrass partnership | "develop a 1.8 gigawatt (GW) AI data center campus"; "designed to scale up to 10 gigawatts" |
| [Laramie County File 26-023 approval](https://laramiecounty.legistar.com/LegislationDetail.aspx?GUID=1623FD5B-974F-4551-9E2F-53A415151CCE&ID=7792288) | 2026-01-06 | Primary county legistar | Project Jade and BFC Power site plans approved with conditions | "approved with conditions" |
| [Laramie County planning memo attachment](https://laramiecounty.legistar.com/View.ashx?GUID=0946D063-8DEE-42DD-B75C-867B3A63027D&ID=15061112&M=F) | 2026-01-06 | Primary county document | 600 acres, 5 DC buildings, 40 BESS units | "five data center buildings" |
| [Laramie County press release](https://www.laramiecountywy.gov/files/sharedassets/public/v/1/county/press-release/tall-grasscrusoe-energy-and-data-center-project-in-southern-laramie-county.pdf) | 2026-01-06 | Primary county release | Co-located scope; Tallgrass and Crusoe naming | "Tall Grass/Crusoe energy and data center project" |
| [DCD Cheyenne approval report](https://www.datacenterdynamics.com/en/news/crusoe-gets-go-ahead-for-18gw-data-center-campus-and-power-plant-in-cheyenne-wyoming/) | 2026-01-08 | Secondary trade press | $7B Tallgrass infrastructure; 2.7 GW on-site generation; 2027 first-energization aspiration | "$7 billion"; "first data center buildings hoped to be electrified in 2027" |
| [Crusoe Abilene Microsoft 900 MW announcement](https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure) | 2026-03-27 | Primary release | 900 MW site, two 336 MW critical-IT buildings, mid-2027 energization | "900 MW site includes two new buildings"; "336 MW of critical IT" |
| [Crusoe Abilene Stargate live announcement](https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live) | 2025-09-30 | Primary release | Stargate Phase 1 live on OCI; eight-building campus | "first phase of Stargate's flagship data center campus" |
| [OpenAI Stargate five-site announcement](https://openai.com/index/five-new-stargate-sites/) | 2025-09-23 | Primary release | Shackelford County named as Stargate site | "located in Shackelford County, Texas" |
| [AP on Microsoft Abilene reshuffle](https://apnews.com/article/ai-stargate-microsoft-openai-crusoe-oracle-f4f74c3a4617d8cfab5b933fc31ccc6e) | 2026-03-27 | Secondary wire | Microsoft taking over Abilene expansion after OpenAI shifted | "Microsoft" |
| [Kirkland Blue Owl Crusoe JV](https://www.kirkland.com/news/press-release/2025/05/kirkland-advises-blue-owl-on-data-center-development) | 2025-05 | Primary law-firm release | $15B Abilene JV development financing | "$15 billion" |
| [Epoch AI Frontier Data Centers](https://epoch.ai/data/data-centers) | 2026-04-20 | Local dataset | Stargate Abilene 1.18 GW; Crusoe Abilene Expansion 0.941 GW; Stargate Shackelford 1.96 GW | "OpenAI Stargate Abilene"; "Crusoe Abilene Expansion"; "OpenAI Stargate Shackelford" |

## Cross-Links

- Research dispatch: `docs/research/C2_crusoe_tallgrass.md`
- Canonical atoms: `canonical_capacity_atoms.yaml` rows for `crusoe_cheyenne_or_other_future_capacity`, `crusoe_abilene_epoch_overlap`, `crusoe_norway_iceland_operational`, `epoch_crusoe_abilene_expansion_buildout_remaining`.
- Dedupe ledger: `dedupe_audit.csv` rows for the above atom IDs.
- Schema: `contracts/_schema.md`.
