# CRUSOE / STARGATE ABILENE — Anatomy of an AI Facility Gigawatt
*Source: crusoe-research subagent, 2026-04-27. Primary-source research note.*

## Headline

Crusoe has not published a line-item BOM. What is publicly extractable: **all-in committed capital for the 1.2 GW Abilene campus = ~$15B = ~$12.5M/MW for the facility shell, power, and cooling envelope, EXPLICITLY EXCLUDING the IT (GPUs/networking) which sits on Oracle's balance sheet.**

This is the cleanest landlord/tenant capex split disclosure in the industry. **For paper purposes: $12.5M/MW shell+power+cooling, separate from accelerator+server BOM ($19-23M/MW per accelerator agent).**

## Capital stack and per-MW economics

- **Total committed capital**: ~$15B (Crusoe newsroom press release, May 2025)
- **JPMorgan-led senior debt**: $9.6B total — $2.3B initial (late 2024) + **$7.1B construction loan** (May 22, 2025) (Bloomberg, Newmark, DCD)
- **Equity**: ~$5B from Crusoe + Blue Owl Real Assets + Primary Digital Infrastructure
- **Phase 1 JV (Oct 15, 2024)**: $3.4B for 206 MW / 998k sq ft = ~**$16.5M/MW Phase 1 alone** (loaded with site-wide power infra)
- **Phase 2 marginal**: implied ~$11.5M/MW (scale economics)
- **Crusoe Series E (Oct 2025)**: $1.375B at >$10B valuation; cumulative raised ~$3.9B
- **Loan terms** (interest rate, tenor, covenants): not publicly disclosed

## Stargate Abilene — site, power, water, cooling

**Site & MW**:
- 1,100-acre campus, 90 acres leased from 800-acre Lancium Clean Campus
- 8 buildings, ~4M sq ft at completion
- Phase 1: 2 buildings, 200+ MW, 980k sq ft, energized H1 2025
- Phase 2: 6 additional buildings; full **1.2 GW target by mid-2026**
- **Microsoft expansion** (announced March 2026, replacing scrapped 600 MW OpenAI expansion): 900 MW across 2 buildings, **336 MW critical IT load per building**, total Abilene footprint = **2.1 GW**, energization mid-2027

**Power source split**:
- "Grid-connected but not grid-dependent" — connected to ERCOT, drawing from regional wind/solar, with on-site BTM natural gas turbines
- **BTM gas: 29 × LM2500XPRESS (35 MW each) = ~1 GW combined** (10 ordered Dec 2024, 19 ordered June 2025) — GE Vernova case study
- TCEQ permit 177263 lists Abilene plant as 5 × Solar Titan 350 (38 MW) + 5 × GE LM2500 (34.1 MW) ≈ 360 MW
- Project Jade (Tallgrass partnership): announced 2.7 GW initial / scalable to 10 GW; CCGT + simple-cycle gas + Bloom fuel cells. Crusoe public commitment >$40B; Tallgrass $7B; combined ≥$50B

**Water/cooling — the defining architectural choice**:
- **Closed-loop, zero-water-evaporation, direct-to-chip liquid cooling**
- Water inventory: ~1M gallons per building initial fill (8M gal total)
- ~50,000 gal/building/year for water-quality maintenance only
- Heat rejection via air-cooled chillers on building perimeter
- Lochmiller (McKinsey, Nov 2025): "We have installed a closed-loop, non-evaporative liquid cooling system…the facility does not consume any water as part of the heat-rejection process."

**PUE / WUE**:
- Target PUE: 1.2-1.3 (Crusoe 2024 Impact Report)
- WUE not disclosed as L/kWh; effectively zero-evaporative by design
- 50,000 gal/building/year maintenance implies WUE ≈ 0

**Density**:
- **50,000 GB200 NVL72-class GPUs per building** on a single integrated network fabric
- Lochmiller standard rack = 50 kW (Acquired 2023, pre-GB200)
- Per-building IT load: 336 MW critical (Microsoft phase 2026 disclosure)
- Implied site density at maturity: ~300 W/sq ft

## Lochmiller / Cavness direct quotes with numbers

**Chase Lochmiller (CEO)**:
- *Madrona "Founded & Funded"*: "Quarter of Northern Virginia's 4.5 GW total capacity… about the power of Denver to power this data center." On schedule: **"Original timeline bid: 2.5 years; we delivered in 12 months."** On manufacturing: power-distribution centers normally 100 weeks; Crusoe production is 20 weeks. On staffing: "7,000 people on site working daily." On building footprint: "Each building approximately 500,000 square feet… traditional web data center equivalent: 1.5 to 2 million square feet."
- *Acquired (Aug 2023)*: "A traditional data center, oftentimes, the standard rack power density is seven kilowatts. A single H100 server, you really need a budget of 12 kilowatts for that single server… For our cloud computing platform, we typically standardize around a **50-kilowatt rack**."
- *McKinsey "At the Edge" (Nov 2025)*: "Energy is at the core of computing. Our 'energy-first' model is designed to solve the massive scaling challenges AI faces at its most foundational layer." Also: **"It's easier to move data than it is to move energy."**

**Cully Cavness (President, co-founder)**:
- *CERAWeek 2026*: on natural gas — "It's the power source that is most scalable and available today."

## Lease/landlord economics — the cleanest disclosure in the industry

- **Crusoe = campus owner-operator (landlord); Oracle = offtake tenant on 15-year lease; OpenAI = Oracle's customer**
- Lochmiller: "Our customer is Oracle. OpenAI is Oracle's customer."
- **Lease term: 15 years**, signed mid-2024 for ~220 MW IT, expanded ~660 MW early 2025
- Aggregate lease value: "$15-20B" with annual rent **">$1B/year for 15 years"** (SemiAnalysis — secondary, but most explicit reconstruction available; not Crusoe-confirmed)
- **Capex split**:
  - Crusoe / Blue Owl / Primary Digital fund **shell + power + cooling + site infrastructure** (~$15B)
  - **Oracle funds the IT** — reportedly ~400,000 NVIDIA GB200 chips at ~$40B (spyglass.org / WSJ, secondary)
  - Oracle then sub-rents chips to OpenAI (and reportedly Microsoft for displaced capacity)
- **Triple-net or take-or-pay**: not publicly disclosed; structure implies one (only way the leverage credibly works)

## Press coverage with hard numbers

- Bloomberg (May 22, 2025): $7.1B JPMorgan-led construction loan
- DCD (May 2025): "Crusoe secures $11.6bn in debt and equity for OpenAI's Stargate"
- Reuters/Bloomberg (March 6, 2026): planned 600 MW OpenAI/Oracle expansion **scrapped**; financing stalled, OpenAI demand forecasts shifted
- DCD/Yahoo (March 2026): Microsoft picked up the unwanted capacity, leasing what Oracle/OpenAI walked away from
- CNBC (Dec 11, 2025): Oracle's lease commitments increased ~150% to accommodate AI demand

## Grid-flex thesis evolution

1. **2018-2022 (founding)**: colocate modular DCs at oil/gas wellheads to monetize flared methane ("Digital Flare Mitigation"). 2024 Impact Report: 10.4 Bcf waste gas → 1.3 TWh electricity.
2. **2023-2024 pivot**: sold Bitcoin/flare-gas business to NYDIG (425+ modular DCs / 250+ MW). Consolidated around AI cloud + AI factory development.
3. **2024-present**: AI data centers as **dispatchable, location-flexible loads** monetizing stranded/curtailed energy — wind in West Texas, gas in Permian, fuel cells (Bloom), iron-air storage (Form Energy 12 GWh deal, deliveries from 2027).
4. **BTM as core**: 29× LM2500XPRESS (~1 GW) + Engine No. 1 partnership for **4.5 GW natural gas**.
5. **Strategic point**: binding constraint on AI scale-up is **energy-interconnect timeline**. Crusoe's edge: bring own power on-site, faster than utility queues clear. 12-month Phase 1 vs 2.5-year industry standard.

## Numbers most confident in

- 1.2 GW Phase 1+2; 2.1 GW with Microsoft Phase 3
- 8 buildings, ~4M sq ft, ~500k sq ft per building
- **~$15B all-in for 1.2 GW = ~$12.5M/MW shell+power+cooling**
- $9.6B JPMorgan debt + ~$5B equity
- 15-year Oracle lease, OpenAI as Oracle's tenant
- Closed-loop zero-water DLC; ~1M gal initial fill, ~50k gal/yr maintenance
- Target PUE 1.2-1.3
- 50 kW rack standard pre-GB200; 336 MW critical IT/building, 50k GB200 GPUs/building (Microsoft phase)
- 29× LM2500XPRESS ≈ 1 GW BTM gas
- Phase 1 energized within ~12 months of June 2024 groundbreaking

## Numbers NOT disclosed

- Line-item BOM (shell vs cooling vs power vs networking vs land within the $12.5M/MW)
- Measured (vs target) PUE for Abilene
- Quantified WUE in L/kWh
- GB200 NVL72 per-rack kW
- JPMorgan loan terms (rate, tenor, covenants)
- Whether Oracle lease is take-or-pay/triple-net (strongly inferred from leverage)
- Annual rent Oracle pays Crusoe (SemiAnalysis $1B+/yr is secondary)
- Brookfield-specific dollar commitment to Abilene JV
- BTM vs grid hour-by-hour split
- Per-MW capex for Microsoft 900 MW phase in isolation
