# Decomposition by ISO / grid region — Western 47.901 GW

Atoms grouped by inferred grid balancing authority. ISO is taken from `compute_commitments_overlay.yaml` `row_audit.iso_rto` where available; otherwise inferred from the site name + state. "—" means the atom has no site disclosed (e.g. Anthropic–Google/Broadcom physical TPU, Anthropic–Azure incremental, Anthropic–AWS Rainier residual unnamed shells). All GW are facility power.

| ISO / grid | Atoms | GW central | Share of 47.9 |
|---|---:|---:|---:|
| ERCOT | 14 | 11.926 | 24.9% |
| MISO | 12 | 9.938 | 20.7% |
| — | 8 | 6.249 | 13.0% |
| MISO-South / Entergy | 2 | 5.276 | 11.0% |
| MISO-South | 4 | 3.800 | 7.9% |
| WECC / non-ISO NM | 1 | 2.210 | 4.6% |
| TVA / MLGW | 5 | 2.095 | 4.4% |
| PJM (Dominion) | 4 | 1.408 | 2.9% |
| PJM (Ohio) | 2 | 1.110 | 2.3% |
| SPP | 4 | 0.928 | 1.9% |
| SERC / Southern Co | 2 | 0.859 | 1.8% |
| PJM (AEP Ohio) | 2 | 0.543 | 1.1% |
| NYISO | 2 | 0.509 | 1.1% |
| MISO, SERC non-ISO, WECC non-ISO, Nord Pool, GB ESO | 1 | 0.300 | 0.6% |
| WECC / SRP/APS | 1 | 0.267 | 0.6% |
| WECC / SRP | 1 | 0.263 | 0.5% |
| Statnett | 1 | 0.200 | 0.4% |
| SERC / Duke | 1 | 0.020 | 0.0% |
| **Total** | **67** | **47.901** | **100.0%** |

---

## ERCOT — 14 atoms — 11.926 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| CoreWeave contracted fleet ex Epoch Helios | CoreWeave | Microsoft / OpenAI / Meta / IBM | T3 | 2.300 | 2027–28 |
| OpenAI Stargate Shackelford | Oracle | OpenAI | T4 | 1.960 | 2028 |
| Project Jade / Cheyenne site-plan capacity ex-Abilene | Crusoe | Tallgrass / merchant | T4 | 1.800 | 2027 |
| OpenAI Stargate Milam | Softbank | OpenAI | T4 | 1.200 | 2028 |
| Goodnight | Google | Google / DeepMind | T2 | 1.088 | 2027 |
| OpenAI Stargate Abilene | Oracle | OpenAI | T2 | 0.980 | 2026 |
| Crusoe Abilene Expansion | Microsoft | Microsoft | T2 | 0.941 | 2027 |
| Coreweave Helios | Coreweave | Microsoft | T5 | 0.800 | 2029 |
| Ward County/Cedarvale Texas Microsoft floor | Nscale | Microsoft / Google / DeepMind | T4 | 0.240 | 2027 |
| OpenAI Stargate Abilene | Oracle | OpenAI | T1 | 0.200 | op. |
| Meta Temple | Meta | Meta | T1 | 0.198 | op. |
| Vantage TX1 | Vantage Data Centers | undisclosed AI tenant | T2 | 0.134 | 2027 |
| Vantage TX1 | Vantage Data Centers | undisclosed AI tenant | T1 | 0.045 | op. |
| Meta Temple | Meta | Meta | T2 | 0.040 | 2026 |

## MISO — 12 atoms — 9.938 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Microsoft Fairwater Wisconsin | Microsoft | OpenAI / Microsoft | T2 | 2.773 | 2027 |
| QTS Cedar Rapids | QTS | undisclosed AI tenant | T2 | 1.587 | 2027 |
| OpenAI Stargate Michigan | Oracle | OpenAI | T4 | 1.383 | 2028 |
| OpenAI Stargate Wisconsin | Oracle | OpenAI | T4 | 1.300 | 2028 |
| Anthropic-Amazon New Carlisle | Amazon | Anthropic | T1 | 1.092 | op. |
| Microsoft Fairwater Wisconsin | Microsoft | OpenAI / Microsoft | T1 | 0.555 | op. |
| Google Cedar Rapids | Google | Google / DeepMind | T4 | 0.522 | 2028 |
| Polaris Forge 2 | Applied Digital | merchant / undisclosed hyperscaler | T3 | 0.200 | 2026 |
| Google Council Bluffs (East) | Google | Google / DeepMind | T1 | 0.190 | op. |
| Anthropic-Amazon New Carlisle | Amazon | Anthropic | T2 | 0.137 | 2026 |
| Google Cedar Rapids | Google | Google / DeepMind | T1 | 0.105 | op. |
| Google Council Bluffs (East) | Google | Google / DeepMind | T2 | 0.094 | 2026 |

## — — 8 atoms — 6.249 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| "vast majority" US-sited per Anthropic | Google Cloud / Broadcom | Anthropic | T5 | 2.700 | 2027 |
| Nebius contracted fleet | Nebius | Microsoft / Meta | T3 | 2.000 | 2027 |
| Azure sites not disclosed | Microsoft Azure | Anthropic | T5 | 0.590 | 2027 |
| Lambda leased, signed, committed capacity | Lambda | Microsoft / NVIDIA | T4 | 0.320 | 2027 |
| North America secured capacity | Together AI | merchant / inference customers | T4 | 0.250 | 2027 |
| Nebius operational fleet | Nebius | undisclosed AI tenant | T1 | 0.170 | op. |
| Six-site US GPU cloud footprint | Voltage Park / Lightning | merchant neocloud | T6 | 0.169 | 2026 |
| Lambda operational fleet | Lambda | merchant neocloud | T1 | 0.050 | op. |

## MISO-South / Entergy — 2 atoms — 5.276 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Hyperion stretch beyond Epoch evidenced 2.262 GW | Meta | Meta | T5 | 3.014 | 2029 |
| Meta Hyperion | Meta | Meta | T4 | 2.262 | 2028 |

## MISO-South — 4 atoms — 3.800 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Project Rainier residual after Madison/Ridgeland Epo… | Amazon | Anthropic | T4 | 1.973 | 2028 |
| Amazon Ridgeland | Amazon | Anthropic | T5 | 1.008 | 2027 |
| Amazon Madison Mega Site | Amazon | Anthropic | T5 | 0.478 | 2026 |
| Amazon Madison Mega Site | Amazon | Anthropic | T1 | 0.341 | op. |

## WECC / non-ISO NM — 1 atoms — 2.210 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| OpenAI Stargate New Mexico | Oracle | OpenAI | T4 | 2.210 | 2028 |

## TVA / MLGW — 5 atoms — 2.095 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| xAI Colossus 2 | xAI | xAI | T2 | 1.494 | 2026 |
| xAI Colossus 1 | xAI | xAI | T1 | 0.425 | op. |
| Maryland, Memphis, Sweden operational footprint | Together AI | merchant neocloud | T6 | 0.081 | op. |
| Memphis Colossus 2 residual | xAI | xAI | T6 | 0.078 | 2027 |
| xAI Colossus 1 | xAI | xAI | T2 | 0.017 | 2026 |

## PJM (Dominion) — 4 atoms — 1.408 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| QTS Richmond | QTS | undisclosed AI tenant | T1 | 0.854 | op. |
| STACK Infrastructure NVA02 | STACK Infrastructure | undisclosed AI tenant | T4 | 0.369 | 2028 |
| STACK Infrastructure NVA02 | STACK Infrastructure | undisclosed AI tenant | T1 | 0.118 | op. |
| QTS Richmond | QTS | undisclosed AI tenant | T2 | 0.067 | 2026 |

## PJM (Ohio) — 2 atoms — 1.110 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Meta Prometheus | Meta | Meta | T2 | 0.579 | 2026 |
| Meta Prometheus | Meta | Meta | T1 | 0.531 | op. |

## SPP — 4 atoms — 0.928 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Google Pryor (North) | Google | Google / DeepMind | T2 | 0.389 | 2026 |
| Google Omaha | Google | Google / DeepMind | T2 | 0.285 | 2027 |
| Google Omaha | Google | Google / DeepMind | T1 | 0.189 | op. |
| Google Pryor (North) | Google | Google / DeepMind | T1 | 0.065 | op. |

## SERC / Southern Co — 2 atoms — 0.859 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Microsoft Fairwater Atlanta | Microsoft | OpenAI | T1 | 0.433 | op. |
| Microsoft Fairwater Atlanta | Microsoft | OpenAI | T2 | 0.426 | 2026 |

## PJM (AEP Ohio) — 2 atoms — 0.543 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Google New Albany | Google | Google / DeepMind | T1 | 0.407 | op. |
| Google New Albany | Google | Google / DeepMind | T2 | 0.136 | 2026 |

## NYISO — 2 atoms — 0.509 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Fluidstack Lake Mariner | Fluidstack | Anthropic / G42 / Anthropic | T2 | 0.441 | 2027 |
| Fluidstack Lake Mariner | Fluidstack | Anthropic / G42 / Anthropic | T1 | 0.068 | op. |

## MISO, SERC non-ISO, WECC non-ISO, Nord Pool, GB ESO — 1 atoms — 0.300 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Fairwater Narvik and Loughton | Microsoft | OpenAI / Microsoft | T2 | 0.300 | ? |

## WECC / SRP/APS — 1 atoms — 0.267 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Stream Phoenix | Stream Data Centers | undisclosed AI tenant | T5 | 0.267 | 2030 |

## WECC / SRP — 1 atoms — 0.263 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Microsoft Goodyear | Microsoft | OpenAI | T1 | 0.263 | op. |

## Statnett — 1 atoms — 0.200 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| Norway and Iceland operational sites | Crusoe | merchant neocloud | T1 | 0.200 | op. |

## SERC / Duke — 1 atoms — 0.020 GW

| Site | Operator | Anchor | Tier | GW | Online |
|---|---|---|:--:|---:|:--:|
| North Carolina seed site | Nscale | merchant neocloud | T1 | 0.020 | op. |

