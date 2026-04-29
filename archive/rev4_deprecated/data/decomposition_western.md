# Per-tier site decomposition — Western raw horizon (47.901 GW facility)

Built from `row_level_audit.csv` rows where `included_in_western_raw_horizon=true`. All GW are facility power. Online column shows central energization year ("op." = operational today; for Epoch rows the year is the buildout completion date in the source notes).
**Online column**: best-available central energization year. Operational rows show `op.` Future-buildout rows show the buildout completion year from the source notes when available, or a defensible central year for non-Epoch atoms. Many Epoch buildouts have a `latest` year in the source data; the Epoch census is dominated by 2026–2028 commissioning.

| Tier | Atoms | GW | Default prob |
|---|---:|---:|---:|
| T1 operational | 22 | 6.519 | 1.00 |
| T2 physically evidenced | 19 | 11.908 | 0.88 |
| T3 firm commercial | 3 | 4.500 | 0.78 |
| T4 announced site plan | 13 | 15.789 | 0.58 |
| T5 LOI / stretch | 7 | 8.857 | 0.32 |
| T6 analyst inference | 3 | 0.328 | 0.25 |
| **Total** | **67** | **47.901** |  |

---

## T1 Operational today (6.519 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| Anthropic-Amazon New Carlisle | Amazon | Anthropic | 1.092 | — | op. |
| QTS Richmond | QTS | (undisclosed AI tenant) | 0.854 | — | op. |
| Microsoft Fairwater Wisconsin | Microsoft | OpenAI, Microsoft | 0.555 | — | op. |
| Meta Prometheus | Meta | Meta | 0.531 | — | op. |
| Microsoft Fairwater Atlanta | Microsoft | OpenAI | 0.433 | — | op. |
| xAI Colossus 1 | xAI | xAI | 0.425 | — | op. |
| Google New Albany | Google | Google DeepMind | 0.407 | — | op. |
| Amazon Madison Mega Site | Amazon | Anthropic | 0.341 | — | op. |
| Microsoft Goodyear | Microsoft | OpenAI | 0.263 | — | op. |
| OpenAI Stargate Abilene | Oracle | OpenAI | 0.200 | — | op. |
| Crusoe Norway + Iceland | Crusoe | merchant | 0.200 | — | op. |
| Meta Temple | Meta | Meta | 0.198 | — | op. |
| Google Council Bluffs (East) | Google | Google DeepMind | 0.190 | — | op. |
| Google Omaha | Google | Google DeepMind | 0.189 | — | op. |
| Nebius operational fleet | Nebius | multiple | 0.170 | — | op. |
| STACK Infrastructure NVA02 | STACK Infrastructure | (undisclosed AI tenant) | 0.118 | — | op. |
| Google Cedar Rapids | Google | Google DeepMind | 0.105 | — | op. |
| Fluidstack Lake Mariner | Fluidstack | Anthropic, G42 | 0.068 | — | op. |
| Google Pryor (North) | Google | Google DeepMind | 0.065 | — | op. |
| Lambda operational fleet (US) | Lambda | merchant | 0.050 | — | op. |
| Vantage TX1 | Vantage Data Centers | (undisclosed AI tenant) | 0.045 | — | op. |
| Nscale North Carolina seed site | Nscale | merchant | 0.020 | — | op. |

**T1 total: 6.519 GW across 22 atoms**

## T2 Under construction / physically evidenced (11.908 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| Microsoft Fairwater Wisconsin | Microsoft | OpenAI, Microsoft | 2.773 | — | 2027 |
| QTS Cedar Rapids | QTS | (undisclosed AI tenant) | 1.587 | — | 2027 |
| xAI Colossus 2 | xAI | xAI | 1.494 | — | 2026 |
| Google Goodnight (TX) | Google | Google DeepMind | 1.088 | — | 2027 |
| OpenAI Stargate Abilene | Oracle | OpenAI | 0.980 | — | 2026 |
| Crusoe Abilene Expansion | Microsoft | Microsoft | 0.941 | — | 2027 |
| Meta Prometheus | Meta | Meta | 0.579 | — | 2026 |
| Fluidstack Lake Mariner | Fluidstack | Anthropic, G42 | 0.441 | — | 2027 |
| Microsoft Fairwater Atlanta | Microsoft | OpenAI | 0.426 | — | 2026 |
| Google Pryor (North) | Google | Google DeepMind | 0.389 | — | 2026 |
| Fairwater Narvik and Loughton | Microsoft | OpenAI / Microsoft | 0.300 | [0.28, 0.61] | ? |
| Google Omaha | Google | Google DeepMind | 0.285 | — | 2027 |
| Anthropic-Amazon New Carlisle | Amazon | Anthropic | 0.137 | — | 2026 |
| Google New Albany | Google | Google DeepMind | 0.136 | — | 2026 |
| Vantage TX1 | Vantage Data Centers | (undisclosed AI tenant) | 0.134 | — | 2027 |
| Google Council Bluffs (East) | Google | Google DeepMind | 0.094 | — | 2026 |
| QTS Richmond | QTS | (undisclosed AI tenant) | 0.067 | — | 2026 |
| Meta Temple | Meta | Meta | 0.040 | — | 2026 |
| xAI Colossus 1 | xAI | xAI | 0.017 | — | 2026 |

**T2 total: 11.908 GW across 19 atoms**

## T3 Firm commercial commitment (4.500 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| CoreWeave contracted fleet ex Epoch Helios | CoreWeave | Microsoft / OpenAI / Meta / IBM | 2.300 | — | 2027–28 |
| Nebius contracted fleet | Nebius | Microsoft / Meta | 2.000 | — | 2027 |
| Polaris Forge 2 | Applied Digital | undisclosed hyperscaler | 0.200 | — | 2026 |

**T3 total: 4.500 GW across 3 atoms**

## T4 Announced site plan (15.789 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| Meta Hyperion | Meta | Meta | 2.262 | — | 2028 |
| OpenAI Stargate New Mexico | Oracle | OpenAI | 2.210 | — | 2028 |
| Anthropic–AWS Project Rainier residual (ex-Madison/Ridgeland Epoch) | Amazon | Anthropic | 1.973 | [0.00, 3.80] | 2028 |
| OpenAI Stargate Shackelford | Oracle | OpenAI | 1.960 | — | 2028 |
| Crusoe Cheyenne (Project Jade, Tallgrass JV) | Crusoe | Tallgrass / merchant | 1.800 | — | 2027 |
| OpenAI Stargate Michigan | Oracle | OpenAI | 1.383 | — | 2028 |
| OpenAI Stargate Wisconsin | Oracle | OpenAI | 1.300 | — | 2028 |
| OpenAI Stargate Milam | Softbank | OpenAI | 1.200 | — | 2028 |
| Google Cedar Rapids | Google | Google DeepMind | 0.522 | — | 2028 |
| STACK Infrastructure NVA02 | STACK Infrastructure | (undisclosed AI tenant) | 0.369 | — | 2028 |
| Lambda Marathon NY + leased capacity | Lambda | Microsoft / NVIDIA | 0.320 | — | 2027 |
| Together AI NA secured capacity | Together AI | merchant + inference customers | 0.250 | — | 2027 |
| Nscale Ward County / Cedarvale TX (Microsoft floor) | Nscale | Microsoft / Google | 0.240 | [0.23, 0.94] | 2027 |

**T4 total: 15.789 GW across 13 atoms**

## T5 LOI / stretch / option (8.857 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| Meta Hyperion stretch (Richland LA, beyond 2.26 GW Epoch floor) | Meta | Meta | 3.014 | [0.00, 3.01] | 2029 |
| Anthropic–Google/Broadcom physical TPU (US, sites unspecified) | Google Cloud / Broadcom | Anthropic | 2.700 | [0.00, 5.40] | 2027 |
| Amazon Ridgeland | Amazon | Anthropic | 1.008 | — | 2027 |
| Coreweave Helios | Coreweave | Microsoft | 0.800 | — | 2029 |
| Anthropic–Azure incremental (Fairwater carve-out applied) | Microsoft Azure | Anthropic | 0.590 | [0.00, 1.18] | 2027 |
| Amazon Madison Mega Site | Amazon | Anthropic | 0.478 | — | 2026 |
| Stream Phoenix | Stream Data Centers | (undisclosed AI tenant) | 0.267 | — | 2030 |

**T5 total: 8.857 GW across 7 atoms**

## T6 Analyst inference (0.328 GW)

| Site / commitment | Operator | Anchor tenant | GW central | GW range | Online |
|---|---|---|---:|---|:---:|
| Voltage Park / Lightning six-site US fleet | Voltage Park / Lightning | merchant | 0.169 | — | 2026 |
| Together AI fleet (MD, TN, Sweden) | Together AI | merchant | 0.081 | — | op. |
| xAI Colossus 2 residual (Memphis) | xAI | xAI | 0.078 | [0.00, 0.26] | 2027 |

**T6 total: 0.328 GW across 3 atoms**

---

## Sovereign sidebar (separate, NOT in Western denominator) — 4.960 GW

Nine included atoms. One additional row, `digital_connexion_vizag_1gw_overlap` (1.000 GW), is flagged sovereign but tier `excluded` to avoid double-count with the Reliance Andhra MoU.

| Site | Operator | Anchor / context | GW | Tier | Online |
|---|---|---|---:|:---:|:---:|
| OpenAI Stargate UAE | G42 | OpenAI | 1.400 | T4 | 2028 |
| Reliance Andhra Pradesh AI cluster (MoU) | Reliance Industries / Jio | India sovereign / Reliance users | 1.000 | T5 | 2030 |
| Reliance Jamnagar stretch (Gujarat) | Reliance Industries / Jio | Reliance-owned + Indian enterprise | 0.880 | T5 | 2028 |
| HUMAIN xAI Saudi (Phase 1) | HUMAIN | xAI | 0.500 | T4 | 2028 |
| HUMAIN AMD Saudi (5-year, $10B JV) | HUMAIN / AMD / Cisco | Saudi sovereign + Luma AI Phase 1 | 0.500 | T4 | 2028 |
| UAE Khazna Microsoft-G42 expansion | Khazna Data Centers / G42 | Microsoft Azure sovereign cloud | 0.260 | T4 | 2027 |
| Culham AI Growth Zone scale-out beyond initial … | UK Government / UKAEA | UK sovereign + TBD tenant | 0.180 | T5 | 2030 |
| Jamnagar Gujarat near-term AI data center tranche | Reliance Industries / Jio | Reliance-owned + Indian enterprise | 0.120 | T2 | 2026 |
| Culham AI Growth Zone initial 100 MW opportunity | UK Government / UKAEA | UK sovereign + TBD tenant | 0.120 | T4 | 2027 |
| **Total** |  |  | **4.960** |  |  |

### Excluded as dedupe overlap (reported but not in any total)

- **digital_connexion_vizag_1gw_overlap** — Digital Connexion / Reliance-Brookfield Vizag JV (1.000 GW). Excluded to avoid double-count with `reliance_andhra_1gw_ai_dc_mou`; flagged sovereign for provenance only.
