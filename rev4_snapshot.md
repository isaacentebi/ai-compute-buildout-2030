# rev-4 Numerical Snapshot — Bottoms-up unit economics + capital envelope reset

Data cutoff: 2026-04-27. Seed for MC: 20260424. Draws: 10,000.

## Primary (facility basis) — physical capacity

These figures are unchanged from rev-3 (the rev-4 update is on capital, not capacity).

| # | Label | Value |
|---|-------|-------|
| 1 | Operational today (tier-clean, IT) | 7.56 GW (7.76 GW including T6-inferred 0.20 GW) |
| 1a | Operational today (facility equivalent at blended PUE 1.16) | ~8.7–9.0 GW |
| 2 | Raw announced 2030 (facility) | 51.93 GW |
| 3 | Raw non-stretch (announced − T5 facility) | 45.17 GW |
| 4 | Deterministic tier-weighted (facility) | 36.75 GW |
| 5 | MC median p50 (facility) | 31.76 GW |
| 6 | MC p10 / p90 (facility) | 24.60 GW / 37.37 GW |
| 6a | MC p05 / p95 (facility) | 23.10 GW / 38.40 GW |
| 7 | Full realization ceiling (facility) | 55.32 GW |

Conservative T1+T2+T3 raw facility: 27.93 GW.
Sovereign sidebar facility: 2.06 GW.

## Per-tier (facility / IT)

| Tier | GW facility | GW IT | Default prob |
|------|-------------|-------|--------------|
| T1 | 7.560 | 7.56 | 1.00 |
| T2 | 12.425 | 12.32 | 0.88 |
| T3 | 7.950 | 7.90 | 0.78 |
| T4 | 16.910 | 16.28 | 0.58 |
| T5 | 6.754 | 6.30 | 0.32 |
| T6 | 0.328 | 0.26 | 0.25 |
| Σ  | 51.927 | 50.62 | |

## H100e reconciliation (basis-invariant)

- Epoch Layer 1: 46.15M H100e / 33.05 GW facility
- Class A overlay: 14.22M H100e / 9.38 GW facility
- Neocloud ex-Epoch: 17.84M H100e / 9.49 GW facility
- WESTERN TOTAL: 78.21M H100e / 51.93 GW facility
- Sovereign: 3.30M H100e / 2.06 GW facility

## Capital envelope (REV-4 RESET — bottoms-up unit economics)

### Per facility-GW

| Quantity | Value |
|---|---|
| Range across operator mix and BTM share | **$30–47B / facility-GW** |
| Central (grid-tied, blended Western mix) | **~$37B / facility-GW** |
| Central (with BTM gas) | ~$39B / facility-GW |
| Crusoe Abilene disclosed (shell+power+cooling, no IT) | $12.5M/MW |
| Bottoms-up facility-only-no-IT central | $13.2M/MW (reconciles to Crusoe within 5%) |
| Bottoms-up IT BOM at customer (rack + out-of-rack net + storage) | $19–28M/MW (central $23.5M) |

### Per layer (central case, $/MW)

| Layer | $M/MW central |
|---|---|
| Shell + civil + land + base/AI fit-out | 6.5 |
| Cooling stack | 2.75 |
| Power infrastructure (grid-tied) | 2.8 |
| (BTM gas adder, when applicable) | (+1.0–2.5) |
| Out-of-rack networking | 3.5 |
| Accelerator + server BOM (rack-complete) | 19.5 |
| Storage | 0.55 |
| Grid interface (median) | 1.1 |
| **Total facility-GW (grid-tied central)** | **~37** |

### Capital envelope at horizon points

| Horizon point | Facility GW | × $30–47B/GW | Central |
|---|---:|---|---|
| Monte Carlo p10 | 24.6 | $0.74–1.16T | ~$0.91T |
| Scenario-adjusted median (MC p50) | 31.8 | $0.95–1.49T | ~$1.18T |
| Tier-weighted point | 36.8 | $1.10–1.73T | ~$1.36T |
| Monte Carlo p90 | 37.4 | $1.12–1.76T | ~$1.38T |
| Raw non-stretch | 45.2 | $1.36–2.12T | ~$1.67T |
| **Raw announced (paper headline)** | **51.9** | **$1.56–2.44T** | **~$1.92T** |
| Full ceiling | 55.3 | $1.66–2.60T | ~$2.05T |

### Capex bridge (raw 51.9 GW central $1.9T)

| Category | $B central | Share of central |
|---|---:|---:|
| Accelerator + server BOM (rack-complete) | 1,010 | 53% |
| Shell + civil + land + AI fit-out | 340 | 18% |
| Cooling + power infrastructure | 290 | 15% |
| Out-of-rack networking + storage | 210 | 11% |
| Grid interface + LPT | 60 | 3% |
| **Total** | **~1,910** | **100%** |

### Financing bridge (proportional, $1.9T central)

| Source | $B central | Share |
|---|---:|---:|
| Hyperscaler operating cash flow | 900 | 47% |
| Corporate debt (hyperscaler + neocloud) | 300 | 16% |
| SPV / project-finance debt (RPO-wrapped) | 300 | 16% |
| Sovereign wealth (MGX, HUMAIN, UK DSIT, RIL) | 250 | 13% |
| Equity (public + private) | 150 | 8% |
| **Total** | **~1,900** | **100%** |

### RPO (revenue underwriting, NOT capex — unchanged)

$550B aggregate: Oracle–OpenAI $300B, Anthropic–Amazon $100B+, Anthropic–Google $52–60B, Nebius–Meta $27B, Nebius–Microsoft $19.4B, CoreWeave–MS/OpenAI $50B.

## Compute payload — chips per facility-MW (counterintuitive finding)

| Vintage / Platform | Chips/MW | H100e/chip | H100e/MW |
|---|---:|---:|---:|
| 2024 — H100 (HGX 8-GPU) | ~570 | 1.0 | ~0.57M |
| 2025–26 — GB200 NVL72 | ~440 | 2.5 | ~1.10M |
| 2026 — GB300 NVL72 | ~415 | 3.75 | ~1.55M |
| 2H'2026–27 — Vera Rubin NVL144 (theoretical pure) | ~850 | 7.5 | 6.4M |
| 2028 — realistic deployed mix | 700–800 | 8–10 | 1.5–2.5M |

Chips per facility-MW *decreases* with each generation; H100e per chip *rises* faster. The compute story is "more H100e per chip", not "more chips per watt".

## Monte Carlo tail probabilities (facility basis, unchanged from rev-3)

- P(realized < conservative 27.93) = 27.9%
- P(realized < prob-weighted 36.75) = 86.1%
- P(realized < raw_non_stretch 45.17) = 100.0%
- P(realized < announced 51.93) = 100.0%

## Stress scenario deltas (rev-4 update at $37B/GW central)

- Correlated 10–12 GW removal: ~$370–440B from capex envelope (was rev-3 $300–350B at $30B/GW implicit)
- Neocloud spread-widening 2 GW removal: ~$75B (was rev-3 $60B)

## Grid-region corrections (unchanged from rev-3)

- Meta Hyperion (Richland Parish, LA): MISO-South (Entergy Louisiana), NOT ERCOT
- xAI Colossus 2 (Memphis, TN): MISO (MLGW), NOT ERCOT

## Key rev-4 label retirements

- "$1.2–1.5 trillion capital envelope": SUPERSEDED → $1.9T (range $1.6–2.4T)
- "$1.5 trillion question" (§5 title): SUPERSEDED → "$2 trillion question"
- Implicit accelerator $17–20M per facility-MW: SUPERSEDED → $19.5M/MW central rack-complete
