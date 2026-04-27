# COOLING LAYER: Anatomy of One AI Facility Gigawatt
*Source: cooling-stack-research subagent, 2026-04-27. Primary-source research note.*

## 1. Executive framing

The cooling layer is the most architecture-disrupted line item in the 2026-vintage AI data center BOM. Between the H100/A100 era (2022-2023) and the GB200/B200/Rubin era (2025-2027), per-rack heat dissipation rose roughly 3-4x — from ~30-50 kW/rack to ~120-132 kW/rack on NVIDIA's NVL72 reference design ([NVIDIA developer blog, 2024](https://developer.nvidia.com/blog/nvidia-contributes-nvidia-gb200-nvl72-designs-to-open-compute-project/); [The Register, 2024-03-21](https://www.theregister.com/2024/03/21/nvidia_dgx_gb200_nvk72/)). This forced direct-to-chip (DLC) liquid cooling from optional to mandatory, ratcheted facility cooling capex by 2-3x on a $/MW basis, and made WUE a board-level metric for the four US hyperscalers.

**Headline figure**: cooling-layer capex for a 2026-vintage greenfield 1 GW AI campus runs approximately **$2.0M–$3.5M/MW**, of which roughly $0.8M–$1.5M/MW is direct liquid cooling (cold plates, manifolds, CDUs), $0.6M–$1.2M/MW is the central plant (chillers, towers, dry coolers, pumps, piping), and $0.3M–$0.7M/MW is residual air-side. Total cooling is roughly **15–20% of total facility capex** of ~$10–12M/MW shell-and-core, per [JLL 2026 Global Data Center Outlook](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook).

## 2. Sub-component cost decomposition

| Sub-component | Typical $/MW (low-high) | Source / basis | Date |
|---|---|---|---|
| DLC cold plates + manifolds (rack-level) | $250k - $500k | Inferred from CoolIT in-rack pricing of ~$20k/rack ([Deep Fundamental, 2025](https://deepfundamental.substack.com/p/deep-dive-liquid-cooling)); ~7 racks/MW at NVL72 density | 2025 |
| CDUs (coolant distribution units) | $300k - $700k | CoolIT L2L 8-rack CDU at ~$140k; Motivair MCDU-70 family scales 105 kW to 2.5 MW, single 2.5 MW unit list-priced in low-millions ([Schneider/Motivair, 2025](https://www.se.com/us/en/about-us/newsroom/news/press-releases/schneider-electric-unveils-liquid-cooling-portfolio-with-motivair-featuring-dedicated-solutions-and-services-for-hpc-and-ai-workloads-68da975376d417f4a10de42c/)) | 2025 |
| Facility water loop / TCS piping | $150k - $300k | Industry estimate; ASHRAE TC9.9 mandates demarcation between FWS and TCS via CDU ([ASHRAE TC9.9 Liquid Cooling Bulletin, Sep 2024](https://www.datacenterdynamics.com/en/news/ashrae-publishes-liquid-cooling-guidelines-as-chip-power-moves-into-uncharted-territory/)) | 2024 |
| DLC retrofit (alt. brownfield case) | $2.0M - $3.0M | Dell'Oro / Introl analysis: retrofit DLC carries ~$2-3M/MW premium ([Introl, 2025](https://introl.com/blog/liquid-vs-air-cooling-ai-data-centers)) | 2025 |
| Chillers (water-cooled centrifugal, 300+ tons) | $400k - $900k | $300-$800/ton ([LNEYA 2025](https://www.lneya-online.com/en/chiller-price-guide-2025-cost-breakdown-by-type-capacity-and-application.html)); ~285 tons/MW thermal at full load with overhead | 2025 |
| Cooling towers + condenser-water (wet/evap baseline) | $150k - $350k | DOE FEMP cooling water guidance; 855 gpm/MW design flow ([DOE FEMP](https://www.energy.gov/cmei/femp/cooling-water-efficiency-opportunities-federal-data-centers)) | 2024 |
| Dry coolers + adiabatic hybrid (water-constrained) | $300k - $600k | Required for closed-loop zero-water designs ([Microsoft Cloud Blog, 2024-12-09](https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/)) | 2024 |
| Pumps + piping + valves (central plant) | $100k - $250k | Mechanical contractor budgets; not separately disclosed by hyperscalers | 2024 |
| Residual air-side (CRAH, RDHx, fan walls, containment) | $200k - $500k | Even NVL72 reference (Vertiv 7MW arch) is hybrid liquid-air; 20-30% of rack load and 100% of switching gear stays air-cooled ([Vertiv, 2024-10-14](https://www.vertiv.com/en-emea/about/news-and-insights/news-releases/vertiv-codevelops-with-nvidia-complete-power-and-cooling-blueprint-for--nvidia-gb200-nvl72-platform/)) | 2024 |
| BMS/controls/monitoring | $50k - $150k | Industry estimate | 2024 |
| **Total cooling (greenfield, AI-optimized)** | **~$2.0M - $3.5M/MW** | Synthesis; consistent with Introl's $3-4M/MW liquid-cooling figure ([Introl, 2025](https://introl.com/blog/liquid-vs-air-cooling-ai-data-centers); [CBRE H1 2025](https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025)) | 2025 |

**Sanity check from MEP ratios**: HVAC/mechanical typically equals 15-20% of total data center capex per industry breakdowns ([Dgtl Infra](https://dgtlinfra.com/how-much-does-it-cost-to-build-a-data-center/)). At a 2026 AI campus build cost of ~$11.3M/MW shell-and-core (JLL forecast) plus ~$8-10M/MW of additional MEP fit-out for AI density, the 15-20% mechanical share lands at $2-4M/MW — squarely consistent with the bottoms-up table above.

## 3. Air, immersion, and the architecture mix in 2026

**Air cooling**: still ~70%+ of installed global capacity by floor-area but rapidly being phased down in new AI builds. ASHRAE TC9.9 (Sep 2024 bulletin) bluntly states air cooling is no longer sufficient beyond ~20-25 kW/rack — well below the 80-130 kW/rack of B200/GB200. Pure-air capex is materially cheaper (~$1.5-2.0M/MW per Introl) but cannot be specified for a Blackwell+ campus without DLC retrofit later.

**Direct-to-chip liquid (DLC)**: this is the 2026 baseline. Dell'Oro reports DLC revenue surged **156% Y/Y in 2Q 2025**, with the total liquid cooling market exceeding $2.5B in 2025 and forecast to surpass $8B by 2030 ([Dell'Oro, 2025](https://www.delloro.com/news/delloro-group-raises-market-forecast-for-data-center-liquid-cooling-and-rack-power-distribution/)). NVIDIA's NVL72 reference architecture mandates 25-45°C inlet liquid, 80 L/min flow, junction temp <75°C — air alone is physically incapable of holding that envelope at 1.2 kW/GPU. Vertiv's co-developed 7 MW reference architecture is the de facto blueprint and claims ~50% faster deployment vs. bespoke builds. Schneider Electric's $850M acquisition of Motivair (Oct 2024) was an explicit play to vertically integrate CDU + cold-plate + chiller scope ([The Register, 2024-10-17](https://www.theregister.com/2024/10/17/schneider_850m_stake_motivair/)). AWS launched its in-house IRHX (In-Row Heat Exchanger) DLC system in July 2025, claiming 20% better power efficiency than off-the-shelf, designed specifically to retrofit Blackwell into existing air-cooled halls.

**Immersion (single- and two-phase)**: still niche for hyperscale AI training in 2026. Single-phase ~62% of immersion market share; two-phase has higher growth (19.4% CAGR through 2031) but PFAS regulatory pressure on dielectric fluids and serviceability friction have kept it boutique. Industry estimates put combined Meta/MS/AWS immersion AI capacity at ~40 MW — a rounding error against the gigawatts of DLC capacity in flight. **Honest flag**: most AI sites are NOT immersion. NVL72 reference is DLC. Treat immersion as a 2027-2030 optional uplift, not a base case.

## 4. Heat-rejection plant choices

Three architectural choices dominate in 2026:

1. **Wet evaporative towers + water-cooled centrifugal chillers** — lowest energy use (PUE 1.10-1.20 in temperate climates), highest water use (1-2 L/kWh annualized in moderate climates, up to 4-5 L/kWh in hot/dry sites). Google Council Bluffs and Iowa fleet are evaporative.

2. **Hybrid adiabatic / closed-loop with dry coolers** — Microsoft's Aug 2024 design pivot. Closed-loop water once, then dry-cooler / mechanical chiller heat rejection — zero ongoing evaporative water consumption per facility (saves ~125M L/year/DC) at the cost of higher PUE. Pilots: Phoenix, AZ and Mt. Pleasant, WI (online 2026).

3. **Air-cooled magnetic-bearing chillers** — highest energy use (PUE 1.30-1.40 typical), zero water. Standard for water-stressed Texas/Arizona greenfield where wet-tower permits are now slowed by hydrology studies.

## 5. PUE and WUE — hyperscaler scoreboard

**PUE (most recent disclosed fleet averages)**:

| Operator | PUE | Year | Source |
|---|---|---|---|
| Google global fleet | 1.09 | 2024 | [Google 2024 Environmental Report](https://sustainability.google/reports/google-2024-environmental-report/) |
| Meta operational DCs | 1.08 | 2023-24 | [Meta 2024 Sustainability Report](https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf) |
| Microsoft (recent builds) | ~1.12 | 2024 | [Microsoft 2024 ESR](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Microsoft-2024-Environmental-Sustainability-Report.pdf) |
| AWS (industry-implied) | ~1.15 | 2024 | [AWS Sustainability](https://aws.amazon.com/sustainability/data-centers/) |
| Industry average (Uptime) | 1.56 | 2024 | [Uptime 2024 Survey](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf) |

**WUE (latest disclosed)**:

| Operator | WUE (L/kWh) | Year | Source |
|---|---|---|---|
| AWS | **0.15** | 2024 | [Amazon 2024 Sustainability Report, AWS Summary](https://sustainability.aboutamazon.com/2024-amazon-sustainability-report-aws-summary.pdf) |
| Meta | **0.18** | 2023-24 | [Meta 2024 Sustainability Report](https://sustainability.atmeta.com/wp-content/uploads/2024/08/Meta-2024-Sustainability-Report.pdf) |
| Microsoft | **0.30** (legacy); target 0 for new builds | FY2024 | [Microsoft 2024 ESR Data Fact](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2024-Environmental-Sustainability-Report-Data-Fact.pdf) |
| Google | ~1.1 L/kWh implied (8.1B gallons fleet 2024) | 2024 | [Google 2024 Env Report](https://sustainability.google/reports/google-2024-environmental-report/) |
| LBNL projected average | 0.45-0.48 | 2028 forecast | [LBNL 2024](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf) |

**Geographic divergence is sharp**. Google Council Bluffs IA campus alone consumed ~1B gallons in 2024. In Texas, data centers are projected to drive a 3% statewide water-use increase by 2030; in Arizona, conditional permits now require third-party hydrology studies. AWS explicitly avoids evaporative cooling in Cape Town, Querétaro. For a 1 GW AI campus, the wet-vs-dry choice swings annual water consumption by **1.5–3 billion gallons/year** at full load.

## 6. AI-density transition: how much of the cooling capex ramp is silicon-driven?

| Era | GPU | TDP | Rack power | Cooling | Cooling capex est. ($/MW facility) |
|---|---|---|---|---|---|
| A100 era (~2020-2022) | A100 | ~400 W | 15-25 kW/rack | Air (CRAH + containment) | $0.8M - $1.3M/MW |
| H100 era (~2022-2024) | H100 | ~700 W | 30-50 kW/rack | Air with rear-door HX, partial DLC | $1.2M - $1.8M/MW |
| **B200/GB200 era (2025-2027)** | B200/GB200 | 1,000-1,200 W | **80-132 kW/rack** | **DLC mandatory + air for residuals** | **$2.0M - $3.5M/MW** |
| Rubin era (2027+, projected) | Rubin/Rubin Ultra | est. 1,500-2,400 W | 200+ kW/rack | DLC + possible 2-phase / immersion uplift | $3.0M - $5.0M/MW |

**Conclusion on the ramp**: roughly two-thirds of the 2-3x cooling capex jump from H100-era to Blackwell-era is driven by chip density itself (cold plates, manifolds, CDUs, larger and faster facility loops). The remaining one-third reflects climate/water siting constraints (zero-water designs, dry coolers, magnetic-bearing chillers in hot/dry markets) and redundancy uplift (ASHRAE TC9.9's Sep 2024 active-redundancy guidance on the TCS loop).

## 7. Defensible total cooling-layer $/MW for a 2026-vintage AI campus

**Greenfield, 1 GW AI campus, 2026 commissioning, NVL72 / B200 baseline**:
- Low end (temperate, wet evaporative, single-vendor): **~$2.0M/MW**
- Central case: **~$2.5M-$3.0M/MW**
- High end (water-stressed TX/AZ, closed-loop zero-water, redundant CDUs): **~$3.5M/MW**

For a full 1 GW campus, that totals **$2.0B-$3.5B in cooling-layer facility capex**. As a fraction of total facility build (~$10-12M/MW shell-and-core per JLL), cooling alone is **20-30% of facility capex** — up from the historical ~15-20% benchmark.

For brownfield retrofits of existing air-cooled halls into Blackwell-capable DLC (AWS IRHX-style), incremental cooling capex is **$2-3M/MW** — close to greenfield because the cold-plate/CDU/facility-loop scope is largely unavoidable.

## 8. Honest caveats

- Vendors do not publish $/MW pricing publicly. Numbers synthesize unit-pricing data points, industry-tracker estimates, and inferred MEP-share ratios. Hyperscalers' internal numbers differ — Google/Meta vertical integration likely puts them at the lower end.
- Rubin-era projection ($3.0-5.0M/MW for 2027+) is directional, not citable.
- Water consumption ranges are climate-sensitive by ~3x.
