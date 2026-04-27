# FORECASTER $/GW RECONCILIATION — Anatomy of One AI Facility Gigawatt
*Source: forecaster-comparison subagent, 2026-04-27. Primary-source research note.*

## THE BASIS-CONFUSION CHEAT SHEET (the most important table in this brief)

| Convention | Typical $/GW | Sources using it |
|---|---|---|
| Per **server-power GW** (IT-load), full all-in (IT+infra+power) | **$40-55B** | Epoch headline ($44B); Nvidia/Jensen ($50-60B); Stargate ($50B); Bernstein ($35B closer to facility-GW) |
| Per **facility-power GW**, all-in | **$25-35B** | Epoch facility figure ($29-30B); McKinsey ~$33B; **the paper's $23-30B sits here** |
| Per IT-load GW, **shell+M&E only, no IT** | **$10-15B** | Cushman ($11.7M/MW avg); JLL ($11.3M/MW); Hyperion JV ($13.5B/GW) |
| Per IT-load GW, **AI fit-out only** (incremental over standard hyperscale) | **+$20-30B** | JLL (+$25M/MW); ConstructElements (+$20M/MW) |

**Apparent disagreements between forecasters of 3-5× in $/GW almost always disappear once you align on which row above each is using.**

## Headline Comparison Table

| Source | $/GW total | Hardware/accel | Shell+civil | Power | Cooling | Networking | Vintage | Notes |
|---|---|---|---|---|---|---|---|---|
| **Epoch AI** | **$44B (server-GW) / $29-30B (facility-GW)** | $30B IT | in $14B "other" | in $14B | in $14B | in $30B | Nov 2025 [1] | **Two bases**. Primary. Closest direct analog to paper. |
| **Bernstein (Stacy Rasgon)** | **~$35B/GW** | GPUs 39%, CPU 3% | in M&E ~33% | Generators 6%, Tx 5%, UPS 4% | ~4% | ~13% | Nov 2025 [3] | Likely IT-load GW basis. Secondary citation. |
| **McKinsey** | **~$33B/GW** (derived $5.2T/156 GW) | $3.3T IT (~$21B/GW) | $1.6T infra (~$10B/GW) | $0.3T (~$2B/GW) | in infra | in IT | Apr 2025 [4] | "Cost of Compute" |
| **Bain** | **~$25B/GW** (derived $500B/yr ÷ 20 GW/yr) | not decomposed | n/a | n/a | n/a | n/a | Sep 2025 [6] | Bain gives total/year only |
| **JLL** | **$11.3M/MW shell+core (2026); +$25M/MW AI fit-out; $45-55B/GW "fully built"** | separate | $11.3M/MW | in shell | in shell | in IT | Jan 2026 [7] | Most explicit basis-segregated |
| **Cushman & Wakefield** | **$9.3-15M/MW (avg $11.7M/MW) "critical load"** | excluded (OFCI/tenant) | included | included | included | limited | 2025 [8] | Shell+core+M&E only, IT-load denom |
| **Goldman Sachs** | not per-GW; $1.15T total hyperscaler 2025-2027 | n/a | n/a | n/a | n/a | n/a | Sep/Oct 2025 [9] | No per-GW headline |
| **Morgan Stanley (Stephen Byrd)** | not per-GW; ~$3T 2025-2028; 74 GW US by 2028 | n/a | n/a | n/a | n/a | n/a | 2025-26 [11] | Implied $50-60B/GW gross — but global vs US scope muddy |
| **JP Morgan** | $5T total global DC+AI; $1.4T/yr by 2030 | n/a | n/a | n/a | n/a | n/a | 2025-26 [12] | No per-GW |
| **BloombergNEF** | not per-GW; $750B 2026 capex (top-14); 23.1 GW UC | n/a | n/a | n/a | n/a | n/a | Mar 2026 [13] | |
| **Synergy Research** | $142B Q3 2025 hyperscaler ($568B annualized); IT capacity 170% YoY | n/a | n/a | n/a | n/a | n/a | Q3 2025 [14] | Aggregate only |
| **Dell'Oro** | DC capex >$1T cumulative by 2029; 21% CAGR | tracks IT vs facility | yes | yes | yes | yes | Aug 2025 [15] | $/MW in subscription only |
| **IEA "Energy and AI"** | $580B DC investment 2025; >$400B big-tech 2025 (+75% in 2026) | n/a | n/a | n/a | n/a | n/a | Apr 2025 [16] | Aggregate only |
| **Aschenbrenner** | "tens of $B" 1 GW (2026); "$100s of B" 10 GW (2028); $1T+ 100 GW (2030) | "~half" GPUs (40% NVDA + 13% IB) | "rest" power+building+cooling | $1B/GW gas gen alone | in "rest" | 13% IB | Jun 2024 [18] | $20-50B/GW depending on year |
| **Nvidia / Jensen** | **$50-60B per GW total ("AI factory")** | $35B Nvidia chips+systems | — | — | — | — | Q2 FY26 Aug 2025 [19] | Self-interested. NVDA ~$35B/$50-60B |
| **Barclays counter** | $50-60B/GW total; **$32.5-42B compute+networking** | midpoint $39B/GW | — | — | — | 65-70% w/compute | Sep 2025 [19] | Implies $11-21B/GW non-compute |
| **Stargate (OpenAI/Oracle/SoftBank)** | **$500B / 10 GW = $50B/GW**; Oracle deal $300B / 4.5 GW = ~$67B/GW | not disclosed | — | — | — | — | Jan/Sep-Oct 2025 [20] | May include OPEX. Outlier high. |
| **Meta Hyperion / Blue Owl JV** | **$27B for 2 GW = ~$13.5B/GW**; campus to 5 GW | excluded | included | partial (Entergy gas separate) | included | excluded | Oct 2025 [21] | Shell+initial M&E ONLY |
| **CoreWeave 10-K (FY25)** | **$14.9B FY25 capex / 850 MW = ~$17.5M/MW**; FY26 guide $30-35B / +850 MW = ~$19M/MW marginal | majority GPUs | partial (much leased) | minimal (leased) | partial | majority of remainder | Feb 2026 [22] | NeoCloud, asset-light |
| **Nebius (Q4 FY25)** | FY26 capex $16-20B; YE26 800-1000 MW = **~$18-22M/MW marginal** | **~79% GPUs** | ~20% DC build | <1% power | in DC build | in GPUs | Feb 2026 [23] | Cleanest disclosed primary split |

## Where Forecasters Agree

1. **Total cluster cost = $30-60B/GW** for AI-dense facilities incl. IT. Convergent center: **$35-50B/GW**. Epoch's $29-30B for facility-GW sits at bottom; Aschenbrenner's "tens of $B for 1 GW" consistent.
2. **IT hardware (GPUs + networking) dominates ~60-70% of total**. Bernstein 39%+13%=52%; Epoch 30/44≈68%; Nebius ~79%; McKinsey $3.3T/$4.9T≈67%.
3. **M&E (power + cooling) is ~25-35% of total** facility-inclusive. Bernstein ~one-third; Epoch 14/44≈32%.
4. **Shell + civil alone = ~$10-12M/MW IT-load** (JLL $10.7M→$11.3M; Cushman avg $11.7M; ConstructElements $10-12M). **Most-anchored single number in the literature.**
5. **AI-specific fit-out adds $20-30M/MW** above standard hyperscale (JLL +$25M; ConstructElements +$20M).
6. **Power generation, when separately costed, is small per GW** — McKinsey $2.2-3.2B/GW; Aschenbrenner ~$1B/GW gas. Sits **outside** DC capex if grid-supplied, **inside** if BTM.

## Where Forecasters Diverge

1. **Basis (IT-load vs facility-power GW)** — biggest source of confusion.
   - Server-power: $44B Epoch
   - Facility-power: $29-30B Epoch / $33B McKinsey / **paper's $23-30B**
   - At PUE 1.2-1.3, the two bases differ ~20-30%
2. **Whether power gen is included**. Meta-Hyperion JV $27B/2 GW EXCLUDES Entergy gas. McKinsey ADDS $2.2-3.2B/GW. Stargate $50B/GW likely INCLUDES BTM. Swings comparable numbers 5-10%.
3. **Whether IT hardware is included**. C&W $11.7M/MW EXCLUDES OFCI; CoreWeave $17.5M/MW INCLUDES GPUs but EXCLUDES leased shell; Epoch $44B/GW is everything. Naive comparison spans 4× range while measuring different things.
4. **Networking inside hardware vs separate**. Bernstein splits ~13% line; Epoch lumps inside $30B IT; Aschenbrenner credits IB separately ~13%. Implied total similar; decomposition not portable.
5. **Outliers**:
   - **High**: Oracle $300B/4.5 GW Stargate ≈ $67B/GW (multi-year service component, not pure capex)
   - **Low**: Meta Hyperion ~$13.5B/GW = shell+M&E only without IT
   - **Self-interested mid-high**: Nvidia $50-60B/GW

## VERDICT ON THE PAPER'S $23-30B/GW

**Sits at the LOW end of the credible facility-GW basis range, but defensible if and only if the basis is explicitly facility-power GW with IT included and BTM gen excluded.**

- **Epoch's facility-GW figure: $29B**. Paper's range overlaps directly.
- **McKinsey's derived: $33B/GW**; backing out McKinsey's $300B power line gets **$31B/GW** (IT+infra, facility-GW). Within rounding distance of paper's high end.
- **Bernstein ~$35B/GW (IT-load basis)** translates to **~$28B/GW on facility-GW basis** (PUE 1.25). Inside paper's $23-30B band.
- **JLL's $45-55B/GW for fully-built ecosystems** is materially higher — but includes IT fit-out at 100% saturation + BTM power; this is "OpenAI Stargate"-grade, not typical 2026 hyperscale.
- **Stargate ($50B/GW) and Nvidia ($50-60B/GW)** are 2× paper's number — server-GW or AI-factory bases for most aggressive deployments, may embed multi-year service economics or self-interest.

**Recommendations for the paper**:
1. **State explicitly** the $23-30B is per **facility-power GW** (not server-power GW); this lowers $/GW vs Epoch's $44B headline by ~30-35%.
2. **Disclose** what is included (IT hardware? networking? grid interconnect? BTM generation?).
3. **Note** Epoch's facility-GW figure of $29-30B is the closest direct analog. **If paper's number is below $29B, it is at the optimistic edge.**

## Coverage Gaps

- Could not retrieve full Goldman "Generational Growth" PDF, full Morgan Stanley Byrd notes, full JPM Kolanovic notes (paywalls). Cited via secondary outlets quoting them.
- Bernstein Rasgon Nov-2025 cited via Investing.com (verbatim quote); original is institutional.
- IEA "Energy and AI" PDF returned binary; aggregates from exec summary page.
- SemiAnalysis cluster BOM model is institutional-only; public newsletter pieces confirm categories but not totals.
- CoreWeave $17-19M/MW is asset-light (leased shell); should not be read as "facility-inclusive $/GW".

## Sources

1. [Epoch AI – Frontier Data Centers Hub (Nov 2025)](https://epoch.ai/blog/introducing-the-frontier-data-centers-hub/)
2. [Epoch AI – Frontier Data Centers Documentation](https://epoch.ai/data/data-centers-documentation)
3. [Investing.com — Bernstein/Rasgon $35B/GW (Nov 2025)](https://www.investing.com/news/stock-market-news/how-much-does-a-gw-of-data-center-capacity-actually-cost-4314046)
4. [McKinsey — The Cost of Compute (Apr 2025)](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers)
6. [Bain — Compute Power Report 2025](https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/)
7. [JLL 2026 Global Data Center Outlook](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook)
8. [Cushman & Wakefield US DC Cost Guide 2025](https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide)
9. [Goldman — $500B+ AI capex 2026](https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026)
13. [BNEF — AI DC build at full speed (Mar 2026)](https://about.bnef.com/insights/commodities/ai-data-center-build-advances-at-full-speed-five-things-to-know/)
14. [Synergy — hyperscale capex Q3 2025](https://www.srgresearch.com/articles/hyperscale-spending-spree-is-driving-dramatic-growth-in-data-center-capacity)
15. [Dell'Oro — DC capex >$1T by 2029](https://www.delloro.com/news/data-center-capex-to-surpass-1-trillion-by-2029/)
16. [IEA — Energy and AI exec summary](https://www.iea.org/reports/energy-and-ai/executive-summary)
18. [Aschenbrenner — Trillion-Dollar Cluster](https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/)
19. [Yahoo/Barclays — Jensen $50B/GW vs Barclays counter](https://finance.yahoo.com/news/nvidias-jensen-math-50-billion-033104538.html)
21. [Meta+Blue Owl $27B Hyperion JV](https://www.globaldatacenterhub.com/p/meta-blue-owls-27b-bet-is-this-the)
22. [DCD — CoreWeave 5GW + capex doubles 2026](https://www.datacenterdynamics.com/en/news/coreweave-aims-to-add-5gw-more-data-center-capacity-by-2030-anticipates-capex-in-2026-to-double/)
23. [DCD — Nebius capex update 2025](https://www.datacenterdynamics.com/en/news/nebius-increases-projected-capex-for-2025-to-2bn/)
