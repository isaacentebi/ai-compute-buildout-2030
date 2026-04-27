# BUILDING SHELL + CIVIL + LAND — Anatomy of One AI Facility Gigawatt
*Source: shell-land-research subagent, 2026-04-27. Primary-source research note.*

## Headline

For a 2026-vintage AI greenfield in Tier-2/3 markets (TX, OH, MS, IA, WI):
- Land: $0.05-0.4M/MW
- Civil + utilities + permitting: $0.4-1.3M/MW
- Shell (concrete/steel): $1.4-2.5M/MW
- Base fit-out: $1.5-2.5M/MW
- AI fit-out delta: $1.0-3.0M/MW
- **Total: $4.4-9.7M/MW, central tendency ~$6-7M/MW**

NoVA Tier-1: add $1-1.5M/MW for land → $5.5-11M/MW. Tier-4 rural (Hyperion-style): $4-6M/MW (land effectively free, longer civil).

A 1 GW campus = **$4-10B in shell+civil+land alone before a single transformer or GPU arrives.**

## Land — the regional cost waterfall (30× spread)

[Cushman & Wakefield 2025](https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide): 2024 weighted-average sale price $5.59/sq ft = $244,000/acre; avg parcel 224 acres; parcels ≥50 acres up 23% YoY.

**Tier 1 — Northern Virginia (Loudoun + PWC)**:
- SDC Capital Leesburg Q4'25: 97 acres for **$615M = $6.3M/acre** (record, 5 DCs approved)
- Amazon NoVA Nov 2025: $700M / ~189 acres = **$3.7M/acre**
- Loudoun avg DC-zoned land 2025: **$3.76M/acre** (+$1.4M from 2024)
- PWC Vint Hill: $2M/acre for 4-building campus
- Ashburn residential conversion offers: up to **$4.4M/acre**

**Tier 2/3 markets**:
- Atlanta: Microsoft Douglas County $148k/acre (2021); QTS Fayetteville $257k/acre; Amazon Douglasville $501k/acre
- Phoenix: NTT Mesa **$1.7M/acre** ($300M / 174 ac, record); QTS reportedly $637k/acre
- Texas Abilene: Crusoe/Stargate on Lancium Clean Campus (lease, not purchase)
- Wisconsin Mt Pleasant: Microsoft $225.8M / 1,363 ac = **$165,700/acre**
- Ohio New Albany: Google **$750k/acre** (~80+ ac for $63M)
- Iowa Cedar Rapids: Google 414 ac for $576M project
- Mississippi Madison: AWS 1,750 ac total (750 + 1,000) for $10B initial / $25B total
- Louisiana Richland Parish (Meta Hyperion): 2,250 ac initial + ~1,400 ac expansion = ~3,650 ac total; rural farmland implies <$30M land cost vs $27B JV

**Per-MW translation**:
- Tier-1 NoVA: 5-8 ac/100 MW × $3-6M/ac = **$150-480/kW**
- Tier-2/3: 5-10 ac/100 MW × $0.2-1.7M/ac = **$10-170/kW**
- Tier-4 rural: $150-750k/ac × 7-10 ac/100 MW = **$10-75/kW**

Land typically <2% of total capex; Loudoun can reach 5%+ on fully-loaded basis.

## Site civil + utilities

$300-700k/MW typical; $700k-$1.2M/MW for sites needing heavy fill/rock excavation/extended utility tie-ins. [Cushman 2025](https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide): civil + shell together = 15-20% of total construction. On $11.3M/MW base (JLL 2026): $1.7-2.3M/MW combined.

Specialist contractors: Turner, AECOM, Skanska, DPR, Holder, Mortenson, Whiting-Turner, Clayco, Rosendin Electric. **Rosendin and DPR led Crusoe Abilene job — 474k sq ft single-story buildings in <1 year.**

## Building shell construction

**Tilt-up concrete dominates greenfield hyperscale shells** for speed. DPR/Digital Realty case study: 2-story tilt panels installed at **8-10 panels/day, ~45 min/panel**. Structural steel preferred for multi-story; AI sites consume **~20,000 tonnes steel per facility (30-40 lb/sq ft)**.

**Square-footage-per-MW has fallen sharply with liquid cooling**:
- Air-cooled at 40 kW/rack: ~25 racks/MW × ~100 sq ft/rack = ~2,500 sq ft/MW white space
- DLC at 100-130 kW/rack: ~1,000 sq ft/MW = **60% white-space compaction**
- Total gross sq ft/MW: ~10,000-12,000 (2019) → **~6,000-8,000 (2025 AI)**

Shell-only construction: $200-350/sq ft Tier-2 markets. Per MW: 7,000 sq ft × $275/sq ft ≈ **$1.9M/MW shell-only**.

## Fit-out (raised floor, fire suppression, BMS/DCIM, security)

20-25% of total construction capex = $100-200/sq ft = **$1.5-2.5M/MW base fit-out**. AI-specific delta (high-density busway, in-row CDUs, leak detection, advanced BMS): **+$1-3M/MW**.

## Permitting & local opposition

Typical US DC permitting: 6-18 months; Tier-1 markets stretched to 24-36 months. **Data Center Watch (Oct 2025): $64B of US DC projects blocked or delayed by local opposition** in past 2 years.

Named cases:
- **Memphis xAI Colossus**: SELC appealed 15-turbine air permit on behalf of NAACP; xAI ran dozens of unpermitted methane turbines for ~12 months; >2,000 public comments against draft permit
- **Hampden Township PA**: rejected
- **Meade County KY**: 135-acre rezoning blocked
- **Mt Pleasant WI**: Microsoft proposal in neighboring village rejected Nov 2025; same village board approved 15 add'l buildings Jan 2026

Trump WH **EO 14318** (July 2025): NEPA categorical exclusions, FAST-41, federal-land siting — accelerant for federal land but not for local opposition.

Soft-cost legal/environmental: $5-25M for 1 GW campus (well under $50/kW).

## Construction labor inflation

- **Turner Building Cost Index +5-6%/yr through 2025**
- **ENR BCI +4.2%, CCI +3.6%** full-year 2025
- **Turner & Townsend DC Cost Index +5.5%/yr 2025** (down from +9.0% 2024); 60% expect +5-15% in 2026, 21% expect >15%
- **AGC 2025**: ~439k worker shortage, 80%+ firms can't fill craft/salaried roles
- DC trades (electricians, mechanical pipefitters, controls): **25-30% wage premium**
- NoVA electrician unions: $27/hr start → **$60/hr post-training**; experienced DC journeymen clearing **$200k/yr with overtime**
- All-trades hourly: **$40.55/hr (Jan 2026)** per BLS/AGC
- **AI-DC cost premium: 7-10% above air-cooled cloud builds** (Turner & Townsend)

## Total construction-cycle time

2019 vintage: 24-30 months shovel-to-COD. 2024-2026 has bifurcated:

- **Crusoe Abilene Phase 1**: vertical June 2024 → operational Sept 2025 = ~15 months from vertical, ~21 months including civil
- **xAI Colossus Memphis**: 19 days concept→site mobilization, **122 days groundbreaking→operational** (100k H100 live July 2024) — but reused Electrolux factory shell
- **Meta Gallatin TN**: 2020 announce → late 2024 COD = ~4 years
- **Microsoft Mt Pleasant WI**: rolling delivery, multi-year

Typical 2026 utility-power-constrained sites: **30-48 months**. Long pole shifted from civil/structural to **transformer + switchgear lead times (up to 4 years for large MV transformers vs ~40 weeks pre-2020)** + grid interconnection studies. PJM/ERCOT now demand **20% non-refundable interconnection deposits = $50-200M for a GW campus** before studies commence. Energy procurement adds 6-12 months.

## Named recent (2023-2026) AI campus projects

| Project | Location | MW/GW | Acres | Land cost | Total capex | Implied $/MW |
|---|---|---|---|---|---|---|
| Meta Hyperion + expansion | Richland Parish LA | ~2,230 MW | 2,250 + ~1,400 | Not disclosed (rural) | $10B → $27B JV → $50B cited | ~$12-22M/MW |
| Crusoe/OpenAI Stargate Abilene | Abilene TX | 1.2 GW | ~1,000-1,100 | On Lancium (lease) | $3-4B at full 1 GW (shell only) | ~$3-4M/MW shell-only |
| Microsoft Mt Pleasant | WI | Multi-GW | ~1,363+ | $225.8M ($165k/ac) | $3.3B Phase 1 + $13.3B Phase 2 = $16.6B | ~$10-15M/MW |
| AWS Madison County | MS | Multi-GW | 1,750 | Not disclosed | $10B → $25B total | ~$10-15M/MW |
| SDC Capital Leesburg | VA | 5 DCs approved | 97 | $615M ($6.3M/ac) | Land only | n/a |
| Amazon NoVA | VA | — | ~189 | $700M ($3.7M/ac) | Land only | n/a |
| NTT Mesa | AZ | Multi-DC | 174 | $300M ($1.7M/ac) | Land only | n/a |
| Meta Gallatin | TN | 500 MW | ~900 | Not disclosed | $1.5B+ | ~$3M/MW |
| xAI Colossus Phase 1 | Memphis TN | ~200 MW | factory reuse | Existing shell | ~$3B | ~$15M/MW |

## Defensible total

For typical 1 GW 2026 AI greenfield in Tier-2/3 markets: **$4.4-9.7M/MW, central ~$6-7M/MW**. For Tier-1 NoVA: $5.5-11M/MW. For Tier-4 rural: $4-6M/MW. **A 1 GW campus = $4-10B in shell+civil+land alone.**
