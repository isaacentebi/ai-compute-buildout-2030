# Overlay Reconciliation Report

Generated: 2026-04-27

## Executive Decision

The overlay is structurally wrong under the strict row-atom scope rule, not merely suffering from neocloud tier drift. The current 51.427 GW Western facility raw horizon is reproducible only if all Epoch sites are retained in the Western denominator. Once `OpenAI Stargate UAE` is moved to the sovereign sidebar and `Alibaba Zhangbei` is excluded, the rebuilt Western facility raw horizon is **47.901 GW**.

Classification versus 51.427 GW: **RED** (-3.526 GW).

The neocloud T3/T4 split in latest `main` is already corrected to the expected split. The earlier all-contracted-into-T3 failure is tier drift that has been repaired, but the atom rebuild exposes a separate scope problem in the Epoch floor.

## Required Answers

1. **Is the current 51.427 GW Western facility raw horizon still supported?**
   Not under strict atom scope. The all-Epoch convention rebuilds to 49.504 GW, effectively matching 51.427 after rounding. The strict Western denominator rebuilds to **47.901 GW**.

2. **If not, what is the rebuilt number?**
   **47.901 GW facility**, range **[39.520, 54.210] GW**, IT bridge **40.878 GW**.

3. **Which rows caused the delta?**
   The scope delta is driven by `epoch_openai_stargate_uae_buildout_remaining` (-1.400 GW to Western, moved to sovereign), `epoch_alibaba_zhangbei_operational` (-0.203 GW to Western, excluded), and -0.011 GW of rounding versus the legacy hand total.

4. **Is the neocloud T3/T4 split wrong?**
   In the latest checked-out `main`, no. The atom rollup regenerates T3 = **4.500 GW** and T4 = **2.610 GW**. That matches the corrected `neocloud_overlay.yaml` split.

5. **What is the corrected T3/T4 split?**
   Overall Western facility: T3 = **4.500 GW**, T4 = **15.789 GW**. Neocloud-only: T3 = **4.500 GW**, T4 = **2.610 GW**.

6. **What are the corrected conservative and probability-weighted totals?**
   Conservative T1+T2+T3 raw facility = **22.927 GW**. Deterministic tier-default probability-weighted facility = **32.582 GW**. Probability-weighted delta versus the pre-atom, neocloud-corrected overlay baseline (36.162 GW) = **-3.580 GW**.

7. **Which rows have stale or missing sources?**
- None.

8. **Which rows are source-supported only by secondary media?**
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `nscale_operational_seed_capacity` (0.020 GW): First US site online; retained but secondary-source flagged.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `fermi_speculative_excluded_or_T5_only` (unknown MW): 11-17 GW permit aspiration has no customer contract and no operational MW; excluded from Western denominator.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.
- `reliance_andhra_1gw_ai_dc_mou` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): November 14, 2025 Reliance / AP government MoU for 1 GW AI data center backed by 6 GWp solar; described as twin to Jamnagar. Likely SAME PROGRAM as the Nov 26-27, 2025 Digital Connexion (Reliance/Brookfield/Digital Realty JV) Visakhapatnam 1 GW campus announcement (12 days apart, both Reliance-linked, both AP, both 1 GW). Counted once via this atom; digital_connexion_vizag_1gw_overlap is excluded.
- `digital_connexion_vizag_1gw_overlap` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): excluded as overlap with reliance_andhra_1gw_ai_dc_mou. Both are 1 GW AP AI data-center programs disclosed within 12 days, both Reliance-linked. Atom retained for transparency / cross-reference but deducted via dedupe_adjustment_mw.

9. **Which rows rely on analyst MW inference?**
- `openai_microsoft_fairwater_international` (0.300 GW): Rev-4.2 source replacement: current primary sources support 230 MW Narvik plus 50-90 MW Loughton; central carried at 300 MW facility instead of the prior 805 MW midpoint.
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `together_operational_inferred` (0.081 GW): Operational MW inferred from GPU/site footprint; T6 in tier rollup.
- `voltage_park_lightning_inferred` (0.169 GW): MW inferred from roughly 35k GPU footprint across six sites; no direct MW disclosure.

10. **Which rows are sovereign and must not enter the Western denominator?**
- `epoch_openai_stargate_uae_buildout_remaining` (1.400 GW): Epoch remaining buildout to 1400.0 MW facility by 2028-01-01; project=Stargate #confident; country=United Arab Emirates.
- `microsoft_g42_uae_khazna` (0.260 GW): Sovereign UAE capacity; sidebar only, not Western denominator.
- `xai_humain_saudi` (0.500 GW): Rev-4.3 source date refresh (D2 research): updated source_date from May 2025 (stale) to Nov 20, 2025 — DCD reporting on US-Saudi Investment Forum + xAI Nov 19, 2025 framework agreement (https://x.ai/news/grok-goes-global). xAI 500 MW is Nvidia-powered per media context; potential overlap with NVIDIA-HUMAIN 500 MW Saudi AI factories program (May 13, 2025) — sources do not resolve whether same physical capacity. Sovereign sidebar only (not Western).
- `humain_amd_saudi` (0.500 GW): Rev-4.3 source corrected (D2 research): primary AMD May 13, 2025 release ("AMD AND HUMAIN FORM STRATEGIC, $10B COLLABORATION") states 500 MW over five years across a network from Saudi Arabia to the United States. AMD/Cisco/HUMAIN November 19, 2025 JV is later/deepened collaboration for up to 1 GW by 2030 with 100 MW Saudi phase 1; DCD explicitly flags uncertainty on whether November 1 GW is separate from or part of May 500 MW. Treat May 500 MW as base candidate; do NOT sum with AMD/Cisco 1 GW until adjudication.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.
- `reliance_andhra_1gw_ai_dc_mou` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): November 14, 2025 Reliance / AP government MoU for 1 GW AI data center backed by 6 GWp solar; described as twin to Jamnagar. Likely SAME PROGRAM as the Nov 26-27, 2025 Digital Connexion (Reliance/Brookfield/Digital Realty JV) Visakhapatnam 1 GW campus announcement (12 days apart, both Reliance-linked, both AP, both 1 GW). Counted once via this atom; digital_connexion_vizag_1gw_overlap is excluded.
- `digital_connexion_vizag_1gw_overlap` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): excluded as overlap with reliance_andhra_1gw_ai_dc_mou. Both are 1 GW AP AI data-center programs disclosed within 12 days, both Reliance-linked. Atom retained for transparency / cross-reference but deducted via dedupe_adjustment_mw.
- `uk_culham_ai_growth_zone` (0.180 GW): Rev-4.2 split: this row carries the Culham scale-out/stretch residual beyond the source-stated initial 100 MW opportunity; central preserves the prior 300 MW facility midpoint when combined with the initial row.
- `uk_culham_ai_growth_zone_initial_100mw` (0.120 GW): Rev-4.2 split: initial 100 MW Culham opportunity converted to 120 MW facility at PUE 1.2 and separated from the scale-out stretch row.

11. **Which rows are double-count risks?**
- `anthropic_aws_incremental_new_capacity` (1.973 GW): Rev-4.2 partial dedupe: prior 3.800 GW residual is reduced by 0.819 GW Madison and 1.008 GW Ridgeland Epoch Rainier candidates; remaining 1.973 GW is site-unallocated Anthropic/AWS capacity.
- `anthropic_azure_incremental_capacity` (0.590 GW): Rev-4.3 dedupe adjudication: Microsoft and NVIDIA both confirm Vera Rubin (the chip class Anthropic uses on Azure) deploys at Fairwater Wisconsin and Atlanta. Central case applies a 50% Fairwater overlap assumption (590 MW facility net-new), with low=0 (full overlap, all Anthropic Azure capacity carved from Fairwater Epoch rows) and high=1180 (no overlap, Anthropic gets net-new Microsoft sites). Documented as judgmental; sources do not disclose Anthropic site list.
- `anthropic_google_broadcom_physical_tpu` (2.700 GW): Rev-4.3 NEW ATOM (per user direction: "Anthropic-Google deal should exist in the paper at appropriate tier"). Total Anthropic-Google/Broadcom TPU exposure = 1 GW IT (Anthropic Oct 23, 2025) + 3.5 GW IT (Broadcom 8-K Apr 6, 2026) = 4.5 GW IT. Central case assumes 50% physical-shell overlap with existing Google Epoch sites (Goodnight 1.09 GW + New Albany 0.54 + Cedar Rapids 0.63 + Council Bluffs E 0.28 + Pryor N 0.45 + Omaha 0.47 = 3.46 GW Google candidates) plus Fluidstack Lake Mariner (0.51 GW). Net-new central = 5.4 GW facility / 2 = 2.7 GW. Low = 0 (full overlap absorbed by Epoch + Fluidstack); high = 5.4 GW (no overlap, full net-new physical capacity).
- `openai_microsoft_fairwater_international` (0.300 GW): Rev-4.2 source replacement: current primary sources support 230 MW Narvik plus 50-90 MW Loughton; central carried at 300 MW facility instead of the prior 805 MW midpoint.
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `coreweave_operational_disclosed` (0.850 GW): Reviewer #5 fix (Rev-4.3): CoreWeave 10-K reports 43 DC with over 850 MW active power AND total contracted power capacity approximately 3.1 GW; the 850 MW active is a subset of the 3.1 GW contracted, not additive. Atom retained for tier-table T1 visibility but excluded from all totals to avoid double-counting against coreweave_contracted_ex_epoch (2.300 GW = 3.1 contracted - 0.8 Helios already in Epoch).
- `coreweave_contracted_ex_epoch` (2.300 GW): Rev-4.3: 3.1 GW total contracted (CoreWeave 10-K) includes 850 MW active fleet AND 800 MW Helios buildout (already in Epoch). Net incremental ex-Epoch = 3.1 - 0.8 = 2.3 GW. This atom captures the full CoreWeave non-Epoch contracted footprint (active + future); coreweave_operational_disclosed is excluded as a subset to avoid double-counting (reviewer #5 fix).
- `coreweave_epoch_overlap_helios` (0.800 GW): Overlap atom: Helios is already counted as an Epoch site and removed from CoreWeave contracted ex-Epoch capacity.
- `coreweave_applied_digital_pf1_overlap_adjustment` (0.400 GW): PF1 is Applied Digital real estate leased to CoreWeave; counted under CoreWeave fleet and excluded from Applied Digital incremental capacity.
- `nscale_microsoft_contract_capacity` (0.240 GW): Rev-4.2 partial dedupe/source replacement: keep Ward County/Cedarvale at the primary-supported ~240 MW floor; remove Narvik/Loughton to Fairwater and carry the 700 MW Texas second phase only as high/option.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `crusoe_abilene_epoch_overlap` (2.120 GW): Abilene Phase 1+2 and Microsoft Abilene expansion are already counted in Epoch; excluded from Crusoe incremental neocloud capacity.
- `crusoe_cheyenne_or_other_future_capacity` (1.800 GW): Rev-4.2 split: Cheyenne/Project Jade retained at 1.8 GW site-plan capacity; extra 0.18 GW residual removed and Abilene remains excluded as Epoch overlap.
- `lambda_microsoft_contract` (0.320 GW): Private pre-IPO capacity with Microsoft/NVIDIA anchors; T4 because no public RPO/take-or-pay capacity disclosure.
- `xai_humain_saudi` (0.500 GW): Rev-4.3 source date refresh (D2 research): updated source_date from May 2025 (stale) to Nov 20, 2025 — DCD reporting on US-Saudi Investment Forum + xAI Nov 19, 2025 framework agreement (https://x.ai/news/grok-goes-global). xAI 500 MW is Nvidia-powered per media context; potential overlap with NVIDIA-HUMAIN 500 MW Saudi AI factories program (May 13, 2025) — sources do not resolve whether same physical capacity. Sovereign sidebar only (not Western).
- `humain_amd_saudi` (0.500 GW): Rev-4.3 source corrected (D2 research): primary AMD May 13, 2025 release ("AMD AND HUMAIN FORM STRATEGIC, $10B COLLABORATION") states 500 MW over five years across a network from Saudi Arabia to the United States. AMD/Cisco/HUMAIN November 19, 2025 JV is later/deepened collaboration for up to 1 GW by 2030 with 100 MW Saudi phase 1; DCD explicitly flags uncertainty on whether November 1 GW is separate from or part of May 500 MW. Treat May 500 MW as base candidate; do NOT sum with AMD/Cisco 1 GW until adjudication.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.
- `reliance_andhra_1gw_ai_dc_mou` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): November 14, 2025 Reliance / AP government MoU for 1 GW AI data center backed by 6 GWp solar; described as twin to Jamnagar. Likely SAME PROGRAM as the Nov 26-27, 2025 Digital Connexion (Reliance/Brookfield/Digital Realty JV) Visakhapatnam 1 GW campus announcement (12 days apart, both Reliance-linked, both AP, both 1 GW). Counted once via this atom; digital_connexion_vizag_1gw_overlap is excluded.
- `digital_connexion_vizag_1gw_overlap` (1.000 GW): Rev-4.3 NEW ATOM (D1 research adjudication): excluded as overlap with reliance_andhra_1gw_ai_dc_mou. Both are 1 GW AP AI data-center programs disclosed within 12 days, both Reliance-linked. Atom retained for transparency / cross-reference but deducted via dedupe_adjustment_mw.
- `uk_culham_ai_growth_zone` (0.180 GW): Rev-4.2 split: this row carries the Culham scale-out/stretch residual beyond the source-stated initial 100 MW opportunity; central preserves the prior 300 MW facility midpoint when combined with the initial row.
- `uk_culham_ai_growth_zone_initial_100mw` (0.120 GW): Rev-4.2 split: initial 100 MW Culham opportunity converted to 120 MW facility at PUE 1.2 and separated from the scale-out stretch row.

12. **Which values should be considered canonical for the manuscript?**
   Use `canonical_totals.json`:
   - Raw Western facility horizon: **47.901 GW**
   - Raw Western facility range: **[39.520, 54.210] GW**
   - Raw non-stretch facility: **39.044 GW**
   - Conservative T1+T2+T3 raw: **22.927 GW**
   - Probability-weighted facility: **32.582 GW**
   - Row-uncertainty high envelope facility: **54.210 GW**
   - Sovereign sidebar facility: **4.960 GW**
   - Capital envelope central: **$1.772T** (**$1.437T-$2.251T**)

## Generated Six-Tier Western Facility Rollup

```yaml
T1_operational: 6.519
T2_physically_evidenced: 11.908
T3_firm_commercial: 4.500
T4_announced_site_plan: 15.789
T5_loi_or_stretch: 8.857
T6_analyst_inference: 0.328
total_gw_announced_facility: 47.901
total_gw_non_stretch_facility: 39.044
total_gw_conservative_facility_raw: 22.927
total_gw_probability_weighted_facility: 32.582
```

## Decision Rules

- Raw horizon delta is 3.526 GW, so this is **YELLOW** and can proceed only with documented deltas.
- Probability-weighted delta versus the pre-atom, neocloud-corrected baseline is 3.580 GW, above 0.5 GW, so Monte Carlo must be rerun before manuscript repair. Monte Carlo rerun artifact is present at `monte_carlo_output_facility_seed20260424.json`.
- Conservative delta versus the pre-atom, neocloud-corrected baseline is 3.538 GW, below 0.5 GW, so floor-like claims do not require wholesale rewrite on that basis alone.
