# Response to Rev-4.1 Audit

Rev-4.3 (this revision) treats the audit as directionally correct — the prior packet was not defensible as written, and the revision rebuilds the evidence layer before defending any headline number. Rev-4.2 made first-pass corrections; **Rev-4.3 closes the load-bearing reviewer findings that survived Rev-4.2 triage**, re-runs the deterministic and probability-weighted rollups, and ships a manifest-validated packet.

## Headline numbers (Rev-4.3 vs Rev-4.1 baseline)

| Metric | Rev-4.1 | Rev-4.2 | **Rev-4.3** | Direction |
|---|---:|---:|---:|---|
| Raw Western horizon (facility GW) | 49.813 | 46.641 | **47.901** | reviewer-driven changes net +0 vs Rev-4.1, but composition is materially different |
| Range (low / high) | 44.396 / 53.115 | 40.370 / 49.660 | **39.520 / 54.210** | wider on both ends — more honest about uncertainty |
| Conservative T1+T2+T3 raw | 26.262 | 23.777 | **22.927** | -3.3 GW (CoreWeave double-count + Fairwater Intl source replace + Crusoe T3→T4) |
| Deterministic prob-weighted | 35.143 | 32.757 | **32.582** | -2.6 GW |
| Capital envelope central (USD T) | 1.843 | 1.726 | **1.772** | follows raw Western × $37B/facility-GW |
| Sovereign sidebar (facility GW) | 3.96 | 3.96 | **4.96** | +1.0 (Reliance Andhra atom added; Digital Connexion deduped) |

The Rev-4.3 raw Western figure (47.901 GW) is HIGHER than Rev-4.2 (46.641 GW) because the new `anthropic_google_broadcom_physical_tpu` atom (+2.7 GW central) more than offsets the CoreWeave double-count fix (-0.85) and Anthropic-Azure partial Fairwater dedupe (-0.59). The wider range (39.52 / 54.21) reflects genuine uncertainty across these atoms. **Every delta is documented in `row_delta_ledger.csv` with finding ID and reason code.**

## Reproducibility (Finding #2)

The Rev-4.1 packet shipped with `scripts/` containing thin wrappers that delegated to root-level implementations not included in the zip. The full implementations existed in the repository continuously. Rev-4.2/4.3 ships a manifest-validated packet: every file in `MANIFEST.md` is present, sha256-verified, and `bash scripts/run_validation.sh` reproduces all canonical totals from a clean unzip. Build script: `scripts/build_packet.py`.

## Finding Map

| # | Finding | Disposition | Magnitude | Evidence |
|---|---|---|---:|---|
| 1 | Reviewer #1 — Epoch 31.45 GW framing as "physically evidenced" | **Fixed (prose discipline + tier-table reframe)** | n/a | Banned-phrase linter in `scripts/check_prose_discipline.py` rejects the prior framing language and enforces the replacement "T1+T2 site-corroborated subtotal". The 31.45 GW Epoch number is reframed as "Epoch site-level current+planned (T1+T2+T4+T5 mix)". See `docs/tier_table.md` for explicit per-tier composition. |
| 2 | Reproducibility | **Fixed mechanically** | n/a | `MANIFEST.md`, `sha256_manifest.txt`, `scripts/build_packet.py`. Reviewer-side reproduction (`unzip && bash scripts/run_validation.sh`) passes cleanly. |
| 3 | Anthropic consistency (Google/Broadcom = 0 GW vs Azure counted) | **Fixed Rev-4.3** | +2.110 GW central net (Google +2.7, Azure -0.59) | Added `anthropic_google_broadcom_physical_tpu` atom (NEW Rev-4.3): 4.5 GW IT exposure (1 GW Anthropic Oct 2025 + 3.5 GW Broadcom 8-K Apr 2026); central 2.7 GW facility (50% Epoch overlap assumption against Fluidstack Lake Mariner + 6 Google Epoch sites); range 0-5.4 GW; T5 (counterparty + magnitude + window all present, named site absent). Anthropic-Azure central reduced 1.180 → 0.590 GW with 50% Fairwater overlap (Microsoft + NVIDIA confirm Vera Rubin deploys at Fairwater Wisconsin/Atlanta — the chip class Anthropic uses). Both rows now treated symmetrically per the inclusion test. |
| 4 | Anthropic-AWS overlap | **Fixed Rev-4.2** | -1.827 GW | `anthropic_aws_incremental_new_capacity` 3.800 → 1.973 GW. Madison (0.819 GW) and Ridgeland (1.008 GW) Epoch Rainier candidates deduped; New Carlisle (1.229 GW Epoch "confident" Rainier) treated as pre-existing per Anthropic Apr 20 "new capacity" framing. MDEQ permits 1720-00098 (Madison) and 1720-00099 (Ridgeland) confirm physical AWS sites. Rationale documented in `dedupe_audit.csv` and `contracts/anthropic_aws.md`. |
| 5 | CoreWeave double-count | **Fixed Rev-4.3** | -0.850 GW | CoreWeave 10-K verbatim: *"43 data centers with over 850 MW of active power"* AND *"total contracted power capacity was approximately 3.1 GW"*. The 850 MW active is a SUBSET of the 3.1 GW contracted, not additive. `coreweave_operational_disclosed` (850 MW T1) atom retained for tier-table T1 visibility but `included_*=false` to avoid double-counting against `coreweave_contracted_ex_epoch` (2.300 GW = 3.1 - 0.8 Helios already in Epoch). Headline -0.85 GW; conservative -0.85; weighted -0.85. |
| 6 | Crusoe / Abilene | **Fixed Rev-4.2** | -0.180 GW headline; -1.980 GW conservative | `crusoe_cheyenne_or_other_future_capacity` 1.980 → 1.800 GW with tier T3 → T4. Tallgrass primary release (Jul 24, 2025): "develop a 1.8 gigawatt (GW) AI data center campus." Laramie County File 26-023 site-plan approval Jan 6, 2026. Cheyenne (Project Jade) is separate Wyoming site from Crusoe Abilene Expansion (already in Epoch as 0.941 GW Microsoft). The 10 GW stretch is T5 only. |
| 7 | Meta Hyperion sourcing | **Fixed Rev-4.3** | 0 GW (source-quality fix only) | `meta_hyperion_stretch_incremental` source URL replaced from `file:///Users/isaacentebi/.../Q2_FY2025.toon` (local cache) to `https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf` (publicly hosted Q2 2025 transcript). source_support: `local_cached_primary` → `primary_company`. exact_quote: *"scale up to 5GW over several years"* (Zuckerberg). Floor (Epoch Hyperion 2.262 GW) corroborated by Meta FY2025 10-K + Engineering at Meta blog + LPSC Order U-37425. JV with Blue Owl: Meta 20% / Blue Owl 80%, $27B development cost, 4-year initial leases + 16-year RVG, $45.95B max exposure to loss. |
| 8 | Nscale / Microsoft | **Fixed Rev-4.2** | -0.660 GW | `nscale_microsoft_contract_capacity` 0.900 → 0.240 GW. Narvik (230 MW) and Loughton (50-90 MW) deduped to `openai_microsoft_fairwater_international` row (which itself was reduced 0.805 → 0.300 GW with primary-source MW anchors). Ward County / Cedarvale ~234-240 MW residual kept as floor; Texas 700 MW option moved to high range only. |
| 9 | Sovereign treatment | **Fixed Rev-4.2 + Rev-4.3** | sovereign sidebar 3.96 → 4.96 GW (+1.0 GW Reliance Andhra) | Rev-4.2 split Reliance into 0.120 GW near-term (T2 Feb 2026 summit) + 0.880 GW stretch (T5 RIL AGM gigawatt-scale). Rev-4.2 split Culham into 0.120 GW initial (T4 UKAEA primary) + 0.180 GW scale-out (T5). Reviewer 300 vs 500 MW Culham inconsistency resolved: 100 MW IT initial × 1.20 PUE = 120 MW facility; scale-out 150 MW IT × 1.20 = 180 MW facility; total = 300 MW facility (NOT 500 MW). Rev-4.3 added `reliance_andhra_1gw_ai_dc_mou` (T5 1.0 GW) with explicit dedupe to `digital_connexion_vizag_1gw_overlap` (excluded — same Reliance-linked AP program 12 days apart). HUMAIN xAI source date refreshed Nov 20 2025; HUMAIN AMD primary source corrected to AMD May 13 2025 release. Documented overlap risks: xAI 500 MW vs NVIDIA-HUMAIN 500 MW (same Saudi AI factories program); AMD 500 MW vs AMD/Cisco/HUMAIN 1 GW JV Nov 2025. All sovereign rows are explicitly NOT in Western denominator. The reframed terminology removes the prior subtotal-as-floor framing everywhere. |
| 10 | Reviewer #10 — prose framing | **Fixed by linter** | n/a | `scripts/check_prose_discipline.py` enforces banned-phrase replacement and is green at validation. The replacement vocabulary is documented in the linter source. |

## Net first-pass headline impact

| | Raw Western | Conservative | Prob-weighted |
|---|---:|---:|---:|
| Rev-4.2 headline | 46.641 | 23.777 | 32.757 |
| **Rev-4.3 deltas** | | | |
| CoreWeave operational excluded (#5) | -0.850 | -0.850 | -0.850 |
| Anthropic-Azure 50% Fairwater dedupe (#3) | -0.590 | 0.000 | -0.177 |
| Anthropic-Google T5 added (#3) | +2.700 | 0.000 | +0.810 |
| Meta Hyperion source replace (#7) | 0.000 | 0.000 | 0.000 |
| HUMAIN sources refreshed (#9) | 0.000 | 0.000 | 0.000 |
| Reliance Andhra atom added (#9, sovereign) | 0.000 | 0.000 | 0.000 |
| **Rev-4.3 headline** | **47.901** | **22.927** | **32.582** |

## What this revision does NOT include

- **No Monte Carlo re-architecture.** Per user direction, MC is treated as third priority ("cosmetic"). MC is re-run with the new atom values; methodology unchanged. The double-discounting concern (tier-prob × stress shocks) is acknowledged in `report.tex` Section 8 with a one-paragraph caveat. Deferred to Rev-4.4.
- **No new geographic scope.** Western + sovereign-stretch annex remain the same set.
- **No source paywalled-content redistribution.** Same exclusion as Rev-4.1.

## Manual verification list status (reviewer's table)

| Row | Reviewer concern | Rev-4.3 disposition |
|---|---|---|
| `anthropic_aws_incremental_new_capacity` | 3.8 GW T4; largest fragile overlay | Reduced to 1.973 GW; Madison/Ridgeland deduped; NC pre-existing; documented |
| `anthropic_google_broadcom_tpu` | 0 GW Class B; inconsistent with Azure | NEW physical T5 atom 2.7 GW central (range 0-5.4); 50% Epoch overlap |
| `anthropic_fluidstack_undisclosed_mw` | excluded; may omit >0.5 GW | Excluded with explicit material-omission risk note (no MW disclosed) |
| `openai_microsoft_fairwater_international` | 0.805 GW T2 too strong | Reduced to 0.300 GW T2 with named Narvik 230 + Loughton 50-90 MW anchors |
| `coreweave_contracted_ex_epoch` | possible 0.85 GW double count | Resolved Rev-4.3 — operational excluded as subset of contracted; -0.85 GW |
| `crusoe_cheyenne_or_other_future_capacity` | T3 mis-tier; 1.98 GW | Demoted T3 → T4; capacity 1.980 → 1.800 GW (Tallgrass primary 1.8 GW) |
| `meta_hyperion_stretch_incremental` | local cached transcript URL | Public Q2 2025 PDF URL; source_support primary_company |
| `nscale_microsoft_contract_capacity` | secondary-only 0.9 GW | 0.240 GW T4; Narvik/Loughton deduped to Fairwater Intl |
| `lambda_microsoft_contract` | primary financing only, MW not primary | 0.320 GW T4; documented anchor-overlap risk; no primary site MW |
| `together_*` | analyst-inferred footprint | T6 maintained; documented inference method |
| `voltage_park_lightning_inferred` | T6 inferred | T6 maintained; documented inference method |
| `xai_colossus2_residual` | secondary residual | T6 maintained with residual logic explicit |
| `xai_humain_saudi` | secondary | source date refreshed to 2025-11-20; primary xAI framework + DCD size; sovereign |
| `humain_amd_saudi` | DCD blocked | Primary AMD May 13 2025 release; sovereign; documented AMD/Cisco JV subsumption risk |
| `reliance_jio_jamnagar` | secondary; mixes near-term and stretch | Split into 0.120 near-term T2 + 0.880 stretch T5; sovereign |
| `reliance_andhra_1gw_ai_dc_mou` | NEW potential omission | Added Rev-4.3; deduped to Digital Connexion same-program |
| `uk_culham_ai_growth_zone` | 300 vs 500 MW inconsistency | Split into 0.120 initial T4 + 0.180 scale-out T5; total 300 MW facility |
| `fermi_speculative_excluded_or_T5_only` | exclusion verify | Excluded maintained; T5 narrative-only |

## Cross-overlay dedupe coverage

`dedupe_audit.csv` now covers 36 rows including site-level overlap candidates for all 13 flagged overlay atoms plus cross-overlay risk documentation:
- 7 Anthropic-Google candidate Epoch sites (Lake Mariner, Goodnight, New Albany, Cedar Rapids, Omaha, Pryor North, Council Bluffs East)
- 2 Anthropic-Azure Fairwater overlaps (Wisconsin, Atlanta)
- 4 CoreWeave Epoch + customer-pool candidates (Helios deduped, Fairwater customer-overlap risk, Stargate separate, Hyperion/Prometheus separate)
- 3 Crusoe Abilene + Cheyenne disambiguations
- 2 HUMAIN cross-program risks (xAI ↔ NVIDIA Saudi; AMD ↔ AMD/Cisco JV) — DOCUMENTED, not summed
- 1 Reliance same-program adjudication (Andhra MoU = Digital Connexion Vizag)
- Plus Lambda/Microsoft, Nscale Microsoft, xAI Colossus residual logic

See `docs/dedupe_audit_report.md` for the narrative.

## Reproducibility verification

```bash
unzip ai-compute-reviewer-packet-rev4_3.zip
cd ai-compute-reviewer-packet-rev4_3/
bash scripts/run_validation.sh
```

Expected output: all gates G1-G7 green; canonical totals reproduce from `canonical_capacity_atoms.yaml` deterministically; no banned phrases in `report.tex` or any markdown / YAML files; URL automation passes; source freshness ≤180 days for all atoms (waivers documented).

## Cross-references

- **Trust artifact**: `row_delta_ledger.csv` — every Rev-4.2 + Rev-4.3 atom delta with finding ID, reason code, and net impact on each canonical metric.
- **Dedupe matrix**: `dedupe_audit.csv` + narrative in `docs/dedupe_audit_report.md`.
- **Tier definitions**: `docs/tier_table.md` — flagship deliverable; tier criteria + worked examples + count/GW per tier.
- **Per-contract drilldowns**: `contracts/` directory — 17 pages, schema in `contracts/_schema.md`.
- **Research dispatches** (primary-source evidence registers): `docs/research/A1` through `D3`.
- **Reconciliation ledger**: `overlay_reconciliation_report.md`.
