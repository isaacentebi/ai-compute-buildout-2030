# Overlay Reconciliation Report

Generated: 2026-04-27

## Executive Decision

The overlay is structurally wrong under the strict row-atom scope rule, not merely suffering from neocloud tier drift. The current 51.427 GW Western facility raw horizon is reproducible only if all Epoch sites are retained in the Western denominator. Once `OpenAI Stargate UAE` is moved to the sovereign sidebar and `Alibaba Zhangbei` is excluded, the rebuilt Western facility raw horizon is **46.641 GW**.

Classification versus 51.427 GW: **RED** (-4.786 GW).

The neocloud T3/T4 split in latest `main` is already corrected to the expected split. The earlier all-contracted-into-T3 failure is tier drift that has been repaired, but the atom rebuild exposes a separate scope problem in the Epoch floor.

## Required Answers

1. **Is the current 51.427 GW Western facility raw horizon still supported?**
   Not under strict atom scope. The all-Epoch convention rebuilds to 48.244 GW, effectively matching 51.427 after rounding. The strict Western denominator rebuilds to **46.641 GW**.

2. **If not, what is the rebuilt number?**
   **46.641 GW facility**, range **[40.370, 49.660] GW**, IT bridge **39.808 GW**.

3. **Which rows caused the delta?**
   The scope delta is driven by `epoch_openai_stargate_uae_buildout_remaining` (-1.400 GW to Western, moved to sovereign), `epoch_alibaba_zhangbei_operational` (-0.203 GW to Western, excluded), and -0.011 GW of rounding versus the legacy hand total.

4. **Is the neocloud T3/T4 split wrong?**
   In the latest checked-out `main`, no. The atom rollup regenerates T3 = **4.500 GW** and T4 = **2.610 GW**. That matches the corrected `neocloud_overlay.yaml` split.

5. **What is the corrected T3/T4 split?**
   Overall Western facility: T3 = **4.500 GW**, T4 = **15.789 GW**. Neocloud-only: T3 = **4.500 GW**, T4 = **2.610 GW**.

6. **What are the corrected conservative and probability-weighted totals?**
   Conservative T1+T2+T3 raw facility = **23.777 GW**. Deterministic tier-default probability-weighted facility = **32.757 GW**. Probability-weighted delta versus the pre-atom, neocloud-corrected overlay baseline (36.162 GW) = **-3.405 GW**.

7. **Which rows have stale or missing sources?**
- None.

8. **Which rows are source-supported only by secondary media?**
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `nscale_operational_seed_capacity` (0.020 GW): First US site online; retained but secondary-source flagged.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `fermi_speculative_excluded_or_T5_only` (unknown MW): 11-17 GW permit aspiration has no customer contract and no operational MW; excluded from Western denominator.
- `xai_humain_saudi` (0.500 GW): Saudi sovereign JV; sidebar only, not Western denominator.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.

9. **Which rows rely on analyst MW inference?**
- `openai_microsoft_fairwater_international` (0.300 GW): Rev-4.2 source replacement: current primary sources support 230 MW Narvik plus 50-90 MW Loughton; central carried at 300 MW facility instead of the prior 805 MW midpoint.
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `together_operational_inferred` (0.081 GW): Operational MW inferred from GPU/site footprint; T6 in tier rollup.
- `voltage_park_lightning_inferred` (0.169 GW): MW inferred from roughly 35k GPU footprint across six sites; no direct MW disclosure.

10. **Which rows are sovereign and must not enter the Western denominator?**
- `epoch_openai_stargate_uae_buildout_remaining` (1.400 GW): Epoch remaining buildout to 1400.0 MW facility by 2028-01-01; project=Stargate #confident; country=United Arab Emirates.
- `microsoft_g42_uae_khazna` (0.260 GW): Sovereign UAE capacity; sidebar only, not Western denominator.
- `xai_humain_saudi` (0.500 GW): Saudi sovereign JV; sidebar only, not Western denominator.
- `humain_amd_saudi` (0.500 GW): Saudi AMD-HUMAIN sovereign JV; sidebar only, not Western denominator.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.
- `uk_culham_ai_growth_zone` (0.180 GW): Rev-4.2 split: this row carries the Culham scale-out/stretch residual beyond the source-stated initial 100 MW opportunity; central preserves the prior 300 MW facility midpoint when combined with the initial row.
- `uk_culham_ai_growth_zone_initial_100mw` (0.120 GW): Rev-4.2 split: initial 100 MW Culham opportunity converted to 120 MW facility at PUE 1.2 and separated from the scale-out stretch row.

11. **Which rows are double-count risks?**
- `anthropic_aws_incremental_new_capacity` (1.973 GW): Rev-4.2 partial dedupe: prior 3.800 GW residual is reduced by 0.819 GW Madison and 1.008 GW Ridgeland Epoch Rainier candidates; remaining 1.973 GW is site-unallocated Anthropic/AWS capacity.
- `anthropic_azure_incremental_capacity` (1.180 GW): 1 GW Azure compute commitment; no sites named, so range floors at zero.
- `openai_microsoft_fairwater_international` (0.300 GW): Rev-4.2 source replacement: current primary sources support 230 MW Narvik plus 50-90 MW Loughton; central carried at 300 MW facility instead of the prior 805 MW midpoint.
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `coreweave_operational_disclosed` (0.850 GW): Operational fleet capacity disclosed by public company; counted once under CoreWeave, not Applied Digital.
- `coreweave_contracted_ex_epoch` (2.300 GW): 3.1 GW contracted less 0.8 GW Helios already counted in Epoch; T3 due RPO/backlog and named IG customers.
- `coreweave_epoch_overlap_helios` (0.800 GW): Overlap atom: Helios is already counted as an Epoch site and removed from CoreWeave contracted ex-Epoch capacity.
- `coreweave_applied_digital_pf1_overlap_adjustment` (0.400 GW): PF1 is Applied Digital real estate leased to CoreWeave; counted under CoreWeave fleet and excluded from Applied Digital incremental capacity.
- `nscale_microsoft_contract_capacity` (0.240 GW): Rev-4.2 partial dedupe/source replacement: keep Ward County/Cedarvale at the primary-supported ~240 MW floor; remove Narvik/Loughton to Fairwater and carry the 700 MW Texas second phase only as high/option.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `crusoe_abilene_epoch_overlap` (2.120 GW): Abilene Phase 1+2 and Microsoft Abilene expansion are already counted in Epoch; excluded from Crusoe incremental neocloud capacity.
- `crusoe_cheyenne_or_other_future_capacity` (1.800 GW): Rev-4.2 split: Cheyenne/Project Jade retained at 1.8 GW site-plan capacity; extra 0.18 GW residual removed and Abilene remains excluded as Epoch overlap.
- `lambda_microsoft_contract` (0.320 GW): Private pre-IPO capacity with Microsoft/NVIDIA anchors; T4 because no public RPO/take-or-pay capacity disclosure.
- `reliance_jio_jamnagar` (0.880 GW): Rev-4.2 split: this row carries the Jamnagar sovereign stretch residual beyond the separately disclosed >120 MW near-term tranche.
- `reliance_jio_jamnagar_near_term_120mw` (0.120 GW): Rev-4.2 split: near-term Jamnagar tranche carried separately from the 1 GW sovereign stretch row.
- `uk_culham_ai_growth_zone` (0.180 GW): Rev-4.2 split: this row carries the Culham scale-out/stretch residual beyond the source-stated initial 100 MW opportunity; central preserves the prior 300 MW facility midpoint when combined with the initial row.
- `uk_culham_ai_growth_zone_initial_100mw` (0.120 GW): Rev-4.2 split: initial 100 MW Culham opportunity converted to 120 MW facility at PUE 1.2 and separated from the scale-out stretch row.

12. **Which values should be considered canonical for the manuscript?**
   Use `canonical_totals.json`:
   - Raw Western facility horizon: **46.641 GW**
   - Raw Western facility range: **[40.370, 49.660] GW**
   - Raw non-stretch facility: **39.894 GW**
   - Conservative T1+T2+T3 raw: **23.777 GW**
   - Probability-weighted facility: **32.757 GW**
   - Row-uncertainty high envelope facility: **49.660 GW**
   - Sovereign sidebar facility: **3.960 GW**
   - Capital envelope central: **$1.726T** (**$1.399T-$2.192T**)

## Generated Six-Tier Western Facility Rollup

```yaml
T1_operational: 7.369
T2_physically_evidenced: 11.908
T3_firm_commercial: 4.500
T4_announced_site_plan: 15.789
T5_loi_or_stretch: 6.747
T6_analyst_inference: 0.328
total_gw_announced_facility: 46.641
total_gw_non_stretch_facility: 39.894
total_gw_conservative_facility_raw: 23.777
total_gw_probability_weighted_facility: 32.757
```

## Decision Rules

- Raw horizon delta is 4.786 GW, so this is **YELLOW** and can proceed only with documented deltas.
- Probability-weighted delta versus the pre-atom, neocloud-corrected baseline is 3.405 GW, above 0.5 GW, so Monte Carlo must be rerun before manuscript repair. Monte Carlo rerun artifact is present at `monte_carlo_output_facility_seed20260424.json`.
- Conservative delta versus the pre-atom, neocloud-corrected baseline is 2.688 GW, below 0.5 GW, so floor-like claims do not require wholesale rewrite on that basis alone.
