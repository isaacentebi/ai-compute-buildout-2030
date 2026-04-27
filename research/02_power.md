# POWER INFRASTRUCTURE LAYER — Anatomy of One AI Facility Gigawatt
*Source: power-stack-research subagent, 2026-04-27. Primary-source research note.*

## Headline

**Power-infrastructure layer for a 1 GW AI campus, 2025-2026 vintage**:
- **Grid-tied with diesel backup**: **$1.9-3.7M/MW** ($1.9-3.7B per GW)
- **Behind-the-meter gas (Stargate/Hyperion model)**: **$2.5-5.7M/MW** ($2.5-5.7B per GW)
- BTM gas alone is $1.0-2.5M/MW — when present, rivals the rest of the layer combined
- Roughly **5-12% of total AI campus capex** but most exposed to supply-chain risk

Turner & Townsend 2025 cost index: Electrical = **48-54% of total DC build cost** (54% air-cooled, 48% liquid-cooled). Against $10.7M/MW shell-and-core (rising to $11.3M/MW in 2026), this implies ~$5.0-5.7M/MW for electrical scope inside the building footprint, *excluding* utility-side substation, BTM gen, HV interconnection.

## Sub-component cost decomposition ($/MW for a 1 GW AI campus)

| Sub-component | Low | High | Source / basis | Date |
|---|---|---|---|---|
| Utility substation + customer switchyard (138/230/345/500 kV) | $150k | $400k | Dominion 900 MW Chesterfield filing via DCD; SemiAnalysis | 2025 |
| **Main power transformers (HV + MV step-down + GSU)** | **$300k** | **$600k** | [Wood Mackenzie via PowerMag, Aug 2025](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/); ElecBase pricing guide | 2025 |
| MV + LV switchgear and bus | $250k | $400k | [Dell'Oro Q4'25](https://www.delloro.com/news/data-center-physical-infrastructure-market-reaches-10-9-billion-in-4q-2025-up-20-percent-y-y/); Eaton/Powell vendor disclosures | 2025-26 |
| UPS + batteries (Li-ion mix) | $300k | $600k | Vertiv Q3'25 SEC; Schneider Galaxy VXL launch; MarketsandMarkets | 2025 |
| Diesel backup gensets (if used) | $700k | $1,200k | Cummins/CSDG; SemiAnalysis | 2025 |
| **Behind-the-meter gas generation (aero/frame/CCGT)** | **$1,000k** | **$2,500k** | Gas Turbine World 2024; GridLab Sept 2025; Crusoe + GE Vernova; Entergy/Meta filings | 2024-26 |
| In-building distribution (busway, PDU, RPP) | $150k | $300k | Dell'Oro; Starline/Anixter | 2025 |
| Onsite BESS (4-hr, ride-through + arbitrage) | $30k | $160k | NREL ATB 2024; Ember Oct 2025 | 2024-25 |
| Onsite solar (token / sustainability) | $0 | $25k | Hyperscaler PPA disclosures | 2025 |

## The transformer crisis — the layer's binding constraint

[Wood Mackenzie via PowerMag, Aug 2025](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/):
- **Power transformer lead time: 128 weeks (~29 months)**
- **GSU transformer lead time: 144 weeks (~33 months)**
- **HV switchgear lead time: 44 weeks**
- **Power transformer prices: +77% since 2019**; GSU +45%; distribution up to +95%
- **2025 supply deficit: 30% on power transformers**

NERC's 2025 Summer Reliability Assessment confirms 2024 average lead times of ~120 weeks with large-class units at 80-210 weeks.

**OEM capacity response** (2024-25 announcements, ~$1.8B aggregate):
- Hitachi Energy: $457M South Boston, VA (largest US LPT plant by 2028) + $106M Alamo, TN
- Siemens Energy: $150M Charlotte, NC (2027 production)
- GE Vernova / Prolec GE: >$300M
- Eaton: $340M S. Carolina (2027)
- HD Hyundai Electric: Alabama expansion +30% by 2026

Per-unit pricing: large 3-phase GSU **>$5M/unit**; 50-100 MVA HV step-down **$3-5M+/unit**. A 1 GW campus needs 12-20 main HV→MV transformers + at least 2 GSUs if BTM present + hundreds of MV→LV unit substation transformers.

## Backup generation — the BTM gas pivot

Traditional diesel: Cummins guidance ~$350/kW pre-installation; installed $700-1,200/kW. Cummins DQKAN 2.5 MW @ $1.30M list ($519/kW). For 1 GW with 2N redundancy: $1.4-2.4B installed — but many AI builds are abandoning full 2N diesel for BTM gas.

**GE Vernova ended 2025 with 80 GW gas-turbine backlog stretching into 2029**, with Q4'25 alone booking 18 GW of new orders. CEO Strazik told investors reservations will be "sold out through 2030 by end of 2026" — primary, GE Vernova Q4'25 earnings via [Utility Dive](https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/).

**Three benchmark BTM deals**:
1. **Stargate / Crusoe Abilene (Project Ludicrous)**: 29 × GE Vernova LM2500XPRESS @ 35 MW = ~1 GW combined; $12-15B for 1.2 GW campus. Crusoe + Engine No. 1 JV: 4.5 GW behind-the-meter gas.
2. **Meta Hyperion (Entergy Louisiana)**: 10 gas plants delivering >7 GW; **$11B for the 10 plants** (~$1.57M/MW for gas hardware, embedded in regulated rate base). Total Meta-Blue Owl JV: $27B.
3. Aeroderivative installed cost benchmark (Gas Turbine World 2024):
   - 105 MW twin-aero simple-cycle: $123.5M = **$1,175/kW installed**
   - 237 MW F-class simple cycle: **$713/kW**
   - 418 MW H-class single-shaft CCGT: **$1,084/kW**
   - 1,083 MW H-class multi-shaft CCGT: **$950/kW**
   - 2025 escalation: ~10% above these levels

EIA AEO 2025 reference: simple-cycle aeroderivative $1,294/kW; industrial-frame simple cycle $785/kW; combined cycle $824-921/kW. **Real-world 2025 hyperscale CCGT runs $2.2-2.5M/MW — 2-3× EIA reference** ([GridLab Sept 2025](https://gridlab.org/wp-content/uploads/2025/09/GridLab_Gas-Turbine-Costs-Report-1.pdf); PowerMag).

## Layer-dominating items (in order)

1. **Behind-the-meter gas generation** ($1.0-2.5M/MW). When present, rivals the entire rest of the layer combined.
2. **Main power transformers** ($300-600k/MW). Highest-inflation, longest-lead.
3. **UPS + batteries** ($300-600k/MW). Rising with Li-ion shift and 800V DC transition.

## Inflation flags 2024 → 2026

- Power transformers: +77% since 2019; marginal 2024-2026 +15-25%
- Distribution transformers: up to +95% since 2019
- MV switchgear: +50% since 2021
- Gas turbines: ~10% above Gas Turbine World reference; new GE Vernova reservation pricing materially above current orders
- CCGT installed: $2.2-2.5M/MW in 2025 vs EIA reference $0.82-0.92M/MW (2-3× the reference)

## Defensible total

- **Grid-tied with diesel backup**: **$2.0-3.7M/MW**
- **BTM gas (Stargate/Hyperion model)**: **$2.5-5.5M/MW**
- Roughly 5-12% of total AI campus capex
