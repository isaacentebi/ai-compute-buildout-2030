# rev-3 Numerical Snapshot — Phase B gate

Data cutoff: 2026-04-24. Seed for MC: 20260424. Draws: 10,000.

## Primary (facility basis)

| # | Label | Value |
|---|-------|-------|
| 1 | Operational today (tier-clean, IT) | 7.56 GW (7.81 GW facility including T6-inferred 0.25 GW facility) |
| 1a | Operational today (facility equivalent at blended PUE 1.16) | ~8.7–9.0 GW |
| 2 | Raw announced 2030 (facility) | 51.43 GW |
| 3 | Raw non-stretch (announced − T5 facility) | 45.17 GW |
| 4 | Deterministic tier-weighted (facility) | 36.75 GW |
| 5 | MC median p50 (facility) | 31.76 GW |
| 6 | MC p10 / p90 (facility) | 24.60 GW / 37.37 GW |
| 6a | MC p05 / p95 (facility) | 23.10 GW / 38.40 GW |
| 7 | Full realization ceiling (facility) | 54.72 GW |

Conservative T1+T2+T3 raw facility: 27.93 GW.
Sovereign sidebar facility: 2.56 GW.

## Secondary (IT-load bridge)

| # | Label | Value |
|---|-------|-------|
| 1 | Operational today (IT) | 7.81 GW facility |
| 2 | Raw announced 2030 (IT) | 43.93 GW |
| 3 | Raw non-stretch (announced − T5 IT) | 44.32 GW |
| 4 | Deterministic tier-weighted (IT) | 36.08 GW |
| 5 | MC median p50 (IT) | 31.12 GW |
| 6 | MC p10 / p90 (IT) | 23.96 GW / 36.66 GW |
| 7 | Full realization ceiling (IT) | 53.48 GW |

Conservative T1+T2+T3 IT: 27.78 GW.
Sovereign sidebar IT: 1.91 GW.

## Per-tier (facility / IT)

| Tier | GW facility | GW IT | Default prob |
|------|-------------|-------|--------------|
| T1 | 7.560 | 7.56 | 1.00 |
| T2 | 12.425 | 12.32 | 0.88 |
| T3 | 7.950 | 7.90 | 0.78 |
| T4 | 16.910 | 16.28 | 0.58 |
| T5 | 6.754 | 6.30 | 0.32 |
| T6 | 0.328 | 0.26 | 0.25 |
| Σ  | 51.427 | 43.93 | |

## MC tail probabilities (facility basis)

- P(realized < conservative 27.93) = 27.9%
- P(realized < prob-weighted 36.75) = 86.1%
- P(realized < raw_non_stretch 45.17) = 100.0%
- P(realized < announced 51.43) = 100.0%

## H100e reconciliation (unchanged under basis flip — chip counts are invariant)

- Epoch Layer 1: 46.15M H100e / 33.05 GW facility (1,388 H100e per IT-MW; ~1,157 per facility-MW at PUE 1.20 blended)
- Class A overlay: 14.22M H100e / 8.17 GW IT / 8.88 GW facility
- Neocloud ex-Epoch: 17.84M H100e / 9.39 GW IT / 9.49 GW facility
- WESTERN TOTAL: 78.21M H100e / 43.93 GW IT / 51.43 GW facility
- Sovereign: 3.30M H100e / 1.91 GW IT / 2.56 GW facility

## Capital envelope (rev-2 footprint, unchanged)

- Capex aggregate: ~$847B from per-row audit rollup; ~$1.2–1.5T when RPO overlap and stretch rows included (narrative envelope)
- RPO aggregate: ~$550B across hyperscaler-neocloud and lab-hyperscaler contracts (not a funding channel — revenue underwriting)

## Grid-region corrections for Phase C.8

- Meta Hyperion (Richland Parish, LA): MISO-South (Entergy Louisiana), NOT ERCOT
- xAI Colossus 2 (Memphis, TN): MISO (MLGW), NOT ERCOT

## Key rev-3 label retirements

- "Universal IT-equivalent denominator" language: REMOVED
- "44.7 GW bear" / "bear arithmetic" / "bear reading": RETIRED → "raw non-stretch"
- "[43, 58] GW facility" (incorrect ±15% framing): DELETED
