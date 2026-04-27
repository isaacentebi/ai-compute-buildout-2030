# GRID INTERCONNECTION + LONG-LEAD-TIME EQUIPMENT — Anatomy of One AI Facility Gigawatt
*Source: grid-interconnect-research subagent, 2026-04-27. Primary-source research note.*

## Headline

The 2026 AI campus does not face a "buy more land and build" problem — it faces a **substation-and-iron** problem. Three constraints bind: (1) LPTs/HV switchgear sold out 2-4 years; (2) frame-class gas turbines sold out 2028-2031; (3) ISO/RTO interconnection queues clear in 4+ years for generation, 5+ years for very-large loads in PJM/MISO.

**Defensible 2026 grid-interface envelope ($/MW)**:

| Posture | Substation-to-fence | Network upgrades | BTM gen | **Total grid-side $/MW** |
|---|---|---|---|---|
| Best (ERCOT fast-track) | $0.3-0.5M | $0.0-0.2M | $0 | **$0.3-0.7M/MW** |
| Median (PJM/MISO + assigned upgrades) | $0.4-0.7M | $0.3-0.8M | $0 | **$0.7-1.5M/MW** |
| Constrained (full BTM gas + grid backstop) | $0.4-0.7M | $0.2-0.5M | $1.0-1.5M | **$1.6-2.7M/MW** |
| Worst (heavy bespoke transmission + BTM gen) | $0.6-1.0M | $1.5-2.5M | $1.0-1.5M | **$3.1-5.0M/MW** |

This sits *on top of* ~$8-10M/MW data-hall capex.

## Long-lead-time equipment (the binding constraint)

| Equipment | Size | 2025-26 lead time | Indicative price |
|---|---|---|---|
| **Large power transformer (LPT, ≥100 MVA)** | 100-500+ MVA | **80-128 weeks; up to 210 weeks for HV specialised** | $2-5M for 100 MVA; $5-10M+ for 500 MVA GSU |
| **GSU transformer** | 200-900 MVA | **144 weeks avg** | $5-15M |
| Step-down (DC use, ≥2.5 MVA) | — | 12+ months on premium | $0.3-2M for 10-100 MVA |
| **HV circuit breaker** (230-500 kV) | — | **~151 weeks (~3 yrs)** | n.d. |
| MV/HV switchgear | — | **~44 weeks** (improved from 60+ in 2023) | n.d. |
| **GE Vernova HA-class gas turbine** | 350-570 MW | **Sold out through 2028; reservations to 2029-2031** | List ~$700-1,000/kW |
| **Siemens Energy SGT-9000HL** | 593 SC / 880 CC MW | Backlog to 2030; 3-5 yrs | n.d. |
| Mitsubishi M501JAC | 448 SC MW | 5 yrs typical, up to 7 | n.d. |

Sources: [Wood Mackenzie 30% LPT supply deficit 2025](https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/); [PowerMag transformer outlook 2026](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/); [GE Vernova 80 GW backlog (Utility Dive Sep 2025)](https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/).

**Strazik (GE Vernova CEO) at Q3 2025 earnings**: ~80 GW backlog stretching into 2029, customers reserving slots out to 2031. By Dec 2025 investor update, backlog grew to ~100 GW. *"No reason to risk increasing capacity today because gas turbines are not the only component with a long lead time."*

**Bruch (Siemens Energy CEO) FY2025 annual report**: €138B order backlog substantially from "electricity needs for data centers… especially in the U.S., this has driven unprecedented demand for gas turbines and grid infrastructure." Heavy-duty gas turbine production expanding from ~48/yr to 70-80/yr by 2026.

**Hitachi Energy**: $4.5B incremental capex through 2027, including $457M South Boston VA LPT plant (largest US plant by 2028) + $106M Alamo TN. CEO Schierenbeck warns multi-year supply gap remains.

For a 1 GW campus, on-site high-side transformers + switchyard now represent **$50-150M of long-lead iron** that must be ordered 2-4 years ahead.

## ISO/RTO interconnection economics

| ISO/RTO | Active gen queue | Median IR→COD | 2025/26 capacity | 2026/27 capacity | Reform |
|---|---|---|---|---|---|
| **PJM** | ~280 GW; transition cycle backlog ~46 GW | 4+ yrs | **$269.92/MW-day record** | **$329.17/MW-day price cap** | TC1 done Sept 2024 (40 GW studied, 17 GW IAs); FERC ordered colocation rules Dec 2025 |
| **MISO** | **215 GW** (Sep 2025) | 4+ yr | PRA spiked Zone 7/MISO-South 2024-25 | n.d. | ERAS expedited; Q2 cycle 6.1 GW (Dec 2025) mostly storage |
| **ERCOT** | **~226 GW large-load IRs (Nov 2025)**, up from 63 GW prior year; **73% data centers** | <2 yrs historic, now overloaded | No central capacity market | — | "Batch Zero" large-load review late 2025 |
| **SPP** | >150 GW gen queue | n.d. | n.d. | n.d. | FERC accepted Provisional Load Process Aug 2025 |
| **CAISO** | 350 GW Cluster 15 → 126 GW active (2025) | 4+ yrs | RA $6-8/kW-mo N; >$15/kW-mo S | n.d. | 2025 IPP effective Jun 25, 2025 |

**Primary**: [LBNL Queued Up 2025](https://emp.lbl.gov/publications/queued-2025-edition-characteristics): ~10,300 active projects, **1,400 GW gen + 890 GW storage = ~2,300 GW total**; median IR→COD doubled from <2 yrs (2000-07) to **>4 yrs** (2018-24). Only 13% of 2000-2019 IRs reached COD by end-2024 (77% withdrawn).

[LBNL PJM Interconnection Cost Analysis 2023](https://emp.lbl.gov/publications/interconnection-cost-analysis-pjm): generator interconnection costs **8× pre-2018** at $240/kW (2020-22 cohort). Network upgrades dominate: $71/kW completed, $227/kW active, $563/kW withdrawn.

**DOE Oct 2025 ANOPR (Docket RM26-4)** explicitly proposes large loads pay full cost-causation; FERC must act by Apr/Jun 2026.

## Customer-funded transmission upgrades — named cases

| Project | Region/Utility | Disclosed grid cost | Capacity | $/MW grid-side |
|---|---|---|---|---|
| **AEP Ohio / SB Energy Piketon** | PJM/AEP Ohio | **$4.2B** new 765 kV | 10 GW DC campus (9.2 GW colocated gas) | **~$420k/MW** |
| **Entergy Hyperion (Meta Richland Parish)** | MISO-South | **$1.2B** for 100-mi 500 kV (separate from gen) + $3.2B for 3 CCGTs (2.26 GW) → expansion to 10 plants/5.2 GW | Up to 5 GW Meta load | **$240k/MW** transmission only |
| **AEP Ohio Delaware/Licking 345 kV** | PJM/AEP | n.d.; serves 1.5 GW incremental | 1.5 GW | n.d. |
| **Talen/AWS Susquehanna** | PJM/Talen-PPL | Existing nuclear; FERC rejected expanded ISA Nov 2024; rehearing denied Apr 2025 | 960 MW (option to 480 MW cap) | n/a (BTM colo) |
| **CAISO 2.5 GW South Bay upgrade** | CAISO | >$2B / 2.5 GW | 2.5 GW | **~$0.8M/MW** |

**Cost-allocation reform**: per UCS Sep 2025, **>$4.3B of DC-driven transmission upgrades in 2024** alone were socialised across PJM ratepayers. This is the loophole DOE/FERC are closing in RM26-4.

## Behind-the-meter generation — the workaround

**Stargate Abilene (Crusoe/Oracle/OpenAI/SoftBank, ERCOT)**:
- 1.2 GW IT load on 875 acres, 8 buildings, end-2026
- TCEQ permit: ~360 MW BTM gas (10 simple-cycle turbines)
- Parker Hannifin contracted: **29 GE Vernova LM2500XPRESS dual-fuel ~35 MW each = ~1.015 GW**
- Crusoe announced **4.5 GW additional BTM gas** late 2025

**Meta Hyperion / Entergy (MISO-South)**:
- $27B Meta capex; up to 5 GW
- LA PSC approved 3 CCGTs = 2.26 GW; expanded to **10 gas plants totalling 5.2 GW**; first units 2028
- Plus Entergy $1.2B / 100-mi 500 kV line complete Dec 2026

**Amazon-Talen Susquehanna (PJM colocated nuclear)**:
- $650M asset purchase Mar 2024; 300 MW BTM
- 480 MW expansion **rejected by FERC 2-1 Nov 2024**; rehearing denied Apr 2025; appeal at 5th Circuit
- New June 2025 deal restructured as **front-of-meter 17-yr 1.92 GW PPA = ~$18B**
- All-in plant cost <$24/MWh per Talen 2025

**Microsoft/Constellation Crane Clean Energy Center (TMI Unit 1 restart)**:
- Sept 2024 PPA, 20-yr, 835 MW, target 2028
- Constellation $1B DOE loan guarantee Nov 2025
- **Morgan Stanley estimated PPA price ~$98/MWh** vs ~$50/MWh PJM market + ~$30/MWh PTC (analyst hearsay)

**SMR queue (long-dated, all 2030+)**:
- Amazon-X-Energy: $500M Series C-1, plan >5 GW by 2039
- Google-Kairos: MPDA Oct 2024 for up to 7 SMRs/500 MW; first unit 2030
- Oracle: 3 SMRs / ~1 GW (2025 Q1 earnings)
- Oklo: Aurora upsized 50→75 MW; 1,350 MW LOIs; first INL deployment late 2027

**BTM gas economics**:
- EIA AEO2025/Lazard LCOE+ June 2025: CCGT capex **$2,000-2,157/kW** (up from <$1,500/kW in 2023, +66%); OCGT/peaker ~$1,300/kW
- Lazard 2025: CCGT $48-109/MWh; gas peaker $149-251/MWh unsubsidised LCOE
- A 1 GW BTM gas peaker fleet = **$1.0-1.5B capex + ~$60-100/MWh dispatch**

## PPA structures

[LevelTen Q4 2025 / Q1 2026]:
- N. America wind PPA: **$79.40/MWh** (+24% YoY)
- N. America solar PPA: **$64.49/MWh** (+13% YoY)
- ISO-NE solar P25: **$115/MWh**; PJM solar P25 $81/MWh; ERCOT cheapest at $49/MWh
- Q1 2026: solar +4.7%, wind +7.9% QoQ — "highest rates on record"

Direct nuclear PPAs (Talen/AWS, Constellation/Microsoft): above-market $90-100/MWh range for 17-20 year tenor.

## Risk flags

**NERC 2025 LTRA (July 2025) — the structural binder**:
> Summer peak demand forecast +224 GW over 10 years (+24% on 2025 peak, +69% over 2024 LTRA baseline). 13 of 23 assessment areas at elevated/high resource adequacy risk. MISO, PJM, ERCOT, WECC-NW, WECC-Basin, SERC-Central all flagged red.

**Even if every queue reform succeeds and every gas turbine slot delivers on time, NERC's own bulk-system planners now expect the resource gap to widen, not close, through the decade.**

## Hearsay flagged

- Constellation-Microsoft TMI ~$98/MWh: Morgan Stanley estimate; not Constellation-confirmed
- Talen-AWS PPA implied $/MWh: only $18B/1.92 GW/17-yr aggregate disclosed
- "Microsoft AEP Ohio $2.7B" framing: could not verify against primary AEP/PUCO/FERC. Verifiable $4.2B project is **SB Energy/SoftBank**-Piketon, not Microsoft. Recommend paper drop or recharacterise this.
- BTM gas turbine spot pricing: OEMs don't disclose unit pricing; $700-1,000/kW is industry consensus per Bernstein/JPM utility notes
