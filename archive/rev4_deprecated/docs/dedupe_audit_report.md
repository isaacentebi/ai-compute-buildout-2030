# Rev-4.3 Dedupe Audit Report

`dedupe_audit.csv` is the site-level control surface for the AI compute buildout. Its rule is simple: **no overlay MW is treated as incremental unless the row says why it is not already captured by Epoch or another overlay atom**.

This report narrates the dedupe matrix — what changed across Rev-4.2 and Rev-4.3, what's still flagged, and how each overlay atom is justified against Epoch and against other overlays.

## Summary of Rev-4.3 changes

Rev-4.3 closes three load-bearing reviewer concerns that survived Rev-4.2 triage:

1. **Reviewer #5 (CoreWeave double-count) — RESOLVED.** The reviewer was correct: CoreWeave's "850 MW active" is a SUBSET of "3.1 GW total contracted power", not additive. Verbatim from the FY2025 Form 10-K: *"43 data centers with over 850 MW of active power"* AND *"total contracted power capacity was approximately 3.1 GW"*. `coreweave_operational_disclosed` (T1, 850 MW) is now `included_*=false` to avoid double-counting against `coreweave_contracted_ex_epoch` (2.300 GW = 3.1 - 0.8 Helios already in Epoch). **Headline impact: -0.85 GW raw / -0.85 GW conservative / -0.85 GW weighted.**

2. **Reviewer #3 (Anthropic-Google/Broadcom 0 GW vs Anthropic-Azure counted asymmetry) — RESOLVED with empirical adjudication.** Per the user's direction ("of course Anthropic-Google deal should exist in the paper, that's why we have tiers"), `anthropic_google_broadcom_physical_tpu` is now a T5 atom in the physical overlay. Total Anthropic-Google/Broadcom TPU exposure = 1 GW IT (Anthropic Oct 23, 2025) + 3.5 GW IT (Broadcom 8-K Apr 6, 2026) = **4.5 GW IT**. Central case 2.7 GW facility (50% physical-shell overlap with existing Google Epoch sites + Fluidstack Lake Mariner); **range 0-5.4 GW** spans full overlap to no overlap. Anthropic-Azure central is now 0.59 GW (50% Fairwater overlap; Microsoft + NVIDIA both confirm Vera Rubin deploys at Fairwater Wisconsin/Atlanta). Both rows are now treated symmetrically: counterparty + magnitude + window all present, named site absent → T5 with explicit dedupe range. **Headline impact: +2.7 - 0.59 = +2.11 GW.**

3. **Reviewer #7 (Meta Hyperion local-cached transcript URL) — RESOLVED.** Source URL replaced from `file:///Users/isaacentebi/.../Q2_FY2025.toon` to publicly hosted Meta Q2 2025 transcript PDF (`https://s21.q4cdn.com/399680738/files/doc_financials/2025/q2/META-Q2-2025-Earnings-Call-Transcript.pdf`). source_support upgraded local_cached_primary → primary_company. exact_quote: *"scale up to 5GW over several years"* (Zuckerberg). Floor (Epoch Hyperion 2.262 GW) corroborated by Meta FY2025 10-K + Engineering at Meta blog + LPSC Order U-37425. **No GW change — source-quality fix only.**

Plus three additional Rev-4.3 fixes:

4. **HUMAIN cluster source date refresh.** xAI-HUMAIN source_date 2025-05-14 (stale) → 2025-11-20 (DCD reporting + xAI Nov 19, 2025 framework agreement). HUMAIN-AMD primary corrected to AMD May 13, 2025 release. Documented overlap risks: xAI 500 MW vs NVIDIA-HUMAIN 500 MW Saudi AI factories program (May 13, 2025); AMD 500 MW vs AMD/Cisco/HUMAIN 1 GW JV (Nov 19, 2025). Sovereign — no Western impact.

5. **Reliance Andhra atom added.** New `reliance_andhra_1gw_ai_dc_mou` (T5 sovereign, 1.0 GW) per D1 research adjudication. Reliance/AP government MoU Nov 14, 2025 + 6 GWp solar support. Counted once; `digital_connexion_vizag_1gw_overlap` (Nov 26-27, 2025) marked `excluded` as same-program (12 days apart, both Reliance-linked, both AP, both 1 GW). Sovereign sidebar 3.96 → 4.96 GW.

6. **Cross-overlay dedupe matrix expanded.** `dedupe_audit.csv` now covers 36 rows including 7 Anthropic-Google candidate Epoch sites (Lake Mariner + 6 Google sites), 2 Anthropic-Azure Fairwater overlaps, plus documented (not summed) cross-overlay risks for HUMAIN, Reliance, Lambda, and Nscale.

## Final Dispositions (Rev-4.3 row delta summary)

| Atom | Rev-4.1 GW | Rev-4.2 GW | **Rev-4.3 GW** | Disposition |
|---|---:|---:|---:|---|
| `anthropic_aws_incremental_new_capacity` | 3.800 | 1.973 | 1.973 | Rev-4.2: Madison + Ridgeland (1.827 GW) deduped; New Carlisle (1.229) treated as pre-existing Rainier per Anthropic Apr 20 framing |
| `openai_microsoft_fairwater_international` | 0.805 | 0.300 | 0.300 | Rev-4.2: source replacement → Narvik 230 MW + Loughton 50-90 MW primary anchors |
| `nscale_microsoft_contract_capacity` | 0.900 | 0.240 | 0.240 | Rev-4.2: Ward County floor; Narvik/Loughton deduped to Fairwater Intl; Texas option in high range |
| `crusoe_cheyenne_or_other_future_capacity` | 1.980 | 1.800 | 1.800 | Rev-4.2: T3 → T4; Cheyenne is Project Jade (Tallgrass/Crusoe primary 1.8 GW) |
| `coreweave_operational_disclosed` | 0.850 | 0.850 | **0.000 (excluded)** | Rev-4.3 (#5): subset of contracted; excluded to avoid double-count |
| `anthropic_azure_incremental_capacity` | 1.180 | 1.180 | **0.590 central (range 0-1.18)** | Rev-4.3 (#3): 50% Fairwater overlap |
| `anthropic_google_broadcom_physical_tpu` | (Class B 0) | (Class B 0) | **2.700 central (range 0-5.4)** | Rev-4.3 (#3): NEW T5 atom; 50% Epoch overlap |
| `meta_hyperion_stretch_incremental` | 3.014 | 3.014 | 3.014 | Rev-4.3 (#7): source URL fix only — public Q2 2025 PDF replaces local cache |
| `xai_humain_saudi` (sovereign) | 0.500 | 0.500 | 0.500 | Rev-4.3: source date refresh + NVIDIA-HUMAIN overlap risk documented |
| `humain_amd_saudi` (sovereign) | 0.500 | 0.500 | 0.500 | Rev-4.3: primary AMD source restored + AMD/Cisco JV subsumption risk documented |
| `reliance_jio_jamnagar` (sovereign) | 1.000 | 0.880 | 0.880 | Rev-4.2 split; Rev-4.3 unchanged |
| `reliance_jio_jamnagar_near_term_120mw` (sovereign) | 0.000 | 0.120 | 0.120 | Rev-4.2 split |
| `reliance_andhra_1gw_ai_dc_mou` (sovereign) | (none) | (none) | **1.000** | Rev-4.3 NEW; Digital Connexion deduped |
| `digital_connexion_vizag_1gw_overlap` (sovereign) | (none) | (none) | **0 (excluded)** | Rev-4.3 NEW; same program as Andhra |
| `uk_culham_ai_growth_zone` (sovereign) | 0.300 | 0.180 | 0.180 | Rev-4.2 split |
| `uk_culham_ai_growth_zone_initial_100mw` (sovereign) | 0.000 | 0.120 | 0.120 | Rev-4.2 split |

**Net first-pass impact across all rounds (Rev-4.1 → Rev-4.3):**
- Western raw horizon: 49.813 → 47.901 GW (-1.912 GW)
- Range: [44.396, 53.115] → [39.520, 54.210] (wider)
- Conservative T1+T2+T3 raw: 26.262 → 22.927 GW (-3.335 GW)
- Deterministic prob-weighted: 35.143 → 32.582 GW (net -2.6 GW)
- Sovereign sidebar: 3.96 → 4.96 GW (+1.000 GW)
- Capital envelope central: $1.843T → $1.772T

## The structural spine: neocloud-vs-hyperscaler attribution

The user's primary structural concern: *"neoclouds sometimes build for and partner with hyperscalers — are we sure neocloud capacity isn't already in Epoch under hyperscaler attribution?"*

Rev-4.2 + Rev-4.3 surface this systematically. Each non-Epoch overlay atom that names a hyperscaler anchor is checked against Epoch hyperscaler sites:

| Overlay atom | Hyperscaler anchor | Epoch sites checked | Disposition |
|---|---|---|---|
| `coreweave_contracted_ex_epoch` | Microsoft 67% revenue, OpenAI ~$22.4B, Meta ~$35B (initial $14.2B + $21B exp), IBM | Helios (deduced), Fairwater Wisconsin / Atlanta, Stargate sites, Hyperion / Prometheus / Temple | Helios deducted; customer-pool overlap with Microsoft Fairwater documented as risk note (not subtracted — no site allocation in primary sources). OpenAI says CoreWeave "complements" Microsoft/Oracle/Stargate (separate). |
| `coreweave_applied_digital_pf1_overlap_adjustment` | CoreWeave end user (lessee from Applied Digital) | None in Epoch (PF1 not in Epoch snapshot) | -400 MW dedupe applied; PF1 attributed to CoreWeave end user, not Applied Digital incremental |
| `crusoe_cheyenne_or_other_future_capacity` | Undisclosed (could be Microsoft, OpenAI, or other) | Crusoe Abilene Expansion (Microsoft, 0.941 GW Epoch), OpenAI Stargate Abilene (1.18 GW Epoch), Shackelford (1.96 GW Epoch) | Cheyenne (Project Jade) is separate Wyoming site — no Epoch row. Abilene already excluded. Shackelford is separate address (175 PR-1604 vs 5502 Spinks Rd). Cheyenne kept as 1.8 GW T4. |
| `nscale_microsoft_contract_capacity` | Microsoft | Fairwater Wisconsin / Atlanta, Goodyear, Crusoe Abilene Expansion | Narvik + Loughton deduped to Fairwater International row. Ward County / Cedarvale residual ex-Epoch. |
| `lambda_microsoft_contract` | Microsoft / NVIDIA | Fairwater Wisconsin (3.328 GW), Crusoe Abilene Expansion (0.941 GW) | No primary source ties Lambda to either site. Same-anchor candidate only — kept full at 0.320 GW with documented medium overlap risk. |
| `anthropic_aws_incremental_new_capacity` | Anthropic | New Carlisle (Anthropic confident Rainier, 1.229 GW), Madison Mega Site (speculative Rainier, 0.819 GW), Ridgeland (speculative Rainier, 1.008 GW) | NC pre-existing per Anthropic Apr 20 framing; Madison + Ridgeland (1.827 GW) deduced |
| `anthropic_azure_incremental_capacity` | Microsoft Azure | Fairwater Wisconsin (3.328 GW), Atlanta (0.859 GW), Goodyear (0.263 GW), Crusoe Abilene Expansion (0.941 GW) | Rev-4.3: 50% Fairwater overlap central (0.295 W + 0.295 A); 0.59 GW residual; range 0-1.18 |
| `anthropic_google_broadcom_physical_tpu` (NEW Rev-4.3) | Anthropic / Google Cloud | Fluidstack Lake Mariner (0.509 GW Anthropic-attributed), Goodnight (1.088), New Albany (0.543), Cedar Rapids (0.627), Pryor N (0.454), Omaha (0.474), Council Bluffs E (0.284) | Central 50% Epoch overlap (0.509 + 1.939 of Google sites = ~2.4 GW) → 2.7 GW residual; range 0-5.4 |
| `xai_colossus2_residual` | xAI | Memphis Colossus 1 (0.442 GW), Colossus 2 (1.494 GW) | Residual logic: 2.0 GW Musk claim - 1.936 GW Epoch = 0.078 GW T6 inferred. Not independent site evidence. |

**Conclusion**: For every overlay atom with an Epoch overlap candidate, the dispositional reasoning is now explicit and traceable. Rows like Anthropic-Azure that previously had `overlap_gw_facility=0.0` with the note "we don't know" now have explicit central/low/high overlap assumptions tied to primary-source evidence (Vera Rubin deployment at Fairwater).

## Sovereign annex — pairwise dedupe documentation

The sovereign sidebar sums to 4.96 GW (Rev-4.3, up from 3.96). Pairwise overlap risks within the sovereign cluster are documented, not summed:

| Sovereign atom | GW | Overlap risk | Documented disposition |
|---|---:|---|---|
| `xai_humain_saudi` | 0.500 | Likely overlaps NVIDIA-HUMAIN 500 MW Saudi AI factories (xAI is Nv-powered) | Both rows would not be additive without site/tenant allocation. NVIDIA-HUMAIN row not in atom file; if added, this would need re-adjudication. |
| `humain_amd_saudi` | 0.500 | Likely subsumed within AMD/Cisco/HUMAIN Nov 2025 JV "up to 1 GW by 2030" envelope | DCD: "unclear whether today's announcement is separate from earlier 500 MW AMD deal". Carry as documented overlap risk. |
| `reliance_andhra_1gw_ai_dc_mou` | 1.000 | Same program as Digital Connexion Vizag 1 GW (Nov 26-27, 2025 — 12 days after Reliance MoU; both Reliance-linked, both AP) | Counted once via Reliance Andhra; Digital Connexion atom marked `status: excluded`. |
| `reliance_jio_jamnagar` (stretch 0.880) + `reliance_jio_jamnagar_near_term_120mw` (0.120) | 1.000 combined | None — split is a within-program disclosure split | Both atoms counted; total = 1.0 GW Jamnagar |
| `uk_culham_ai_growth_zone` (scale-out 0.180) + `uk_culham_ai_growth_zone_initial_100mw` (0.120) | 0.300 combined | None | Both atoms counted; total = 0.300 GW Culham (resolves reviewer 300 vs 500 MW concern via PUE-converted IT-MW math) |
| `microsoft_g42_uae_khazna` | 0.700 | Could overlap with `epoch_openai_stargate_uae_buildout_remaining` (1.4 GW Epoch sovereign — UAE Stargate) | Different operator (Khazna vs G42 Stargate) but same UAE sovereign cluster; documented as cluster-level risk |

## Residual risk

The remaining substantive risk is not unexamined double-counting; it is **unresolved primary-source evidence**:
- Anthropic-Google site allocation (Google-owned vs Fluidstack-built shells) — central 50% Epoch overlap is judgmental
- Anthropic-Azure site allocation (1 GW carved from Fairwater vs net-new Microsoft regions) — central 50% Fairwater overlap is judgmental
- HUMAIN xAI / NVIDIA / AMD / Cisco overlapping 500 MW + 1 GW programs — sources don't resolve same-vs-separate
- CoreWeave customer-site allocation (Microsoft 67%, OpenAI/Meta/IBM redacted) — kept as customer-pool risk note
- Lambda Microsoft 320 MW site allocation — not publicly disclosed

Rows with unresolved overlap risk now carry `double_count_risk` and `epoch_overlap_candidates` in `canonical_capacity_atoms.yaml`, with matching rows in `dedupe_audit.csv`. Each judgment carries a documented assumption with low/high range.

## Cross-references

- `dedupe_audit.csv` — 36 rows, full overlay × Epoch matrix
- `row_delta_ledger.csv` — every Rev-4.2 + Rev-4.3 atom delta with finding ID
- `RESPONSE_TO_AUDIT.md` — finding-by-finding map
- `canonical_capacity_atoms.yaml` — `epoch_overlap_candidates[]` per atom
- `docs/research/` — primary-source evidence registers (A1-D3)
- `contracts/` — per-contract drilldown pages with dedupe sections
