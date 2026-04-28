# Overlay Reconciliation Report

Generated: 2026-04-27

## Executive Decision

The overlay is structurally wrong under the strict row-atom scope rule, not merely suffering from neocloud tier drift. The current 51.427 GW Western facility raw horizon is reproducible only if all Epoch sites are retained in the Western denominator. Once `OpenAI Stargate UAE` is moved to the sovereign sidebar and `Alibaba Zhangbei` is excluded, the rebuilt Western facility raw horizon is **49.813 GW**.

Classification versus 51.427 GW: **YELLOW** (-1.614 GW).

The neocloud T3/T4 split in latest `main` is already corrected to the expected split. The earlier all-contracted-into-T3 failure is tier drift that has been repaired, but the atom rebuild exposes a separate scope problem in the Epoch floor.

## Required Answers

1. **Is the current 51.427 GW Western facility raw horizon still supported?**
   Not under strict atom scope. The all-Epoch convention rebuilds to 51.416 GW, effectively matching 51.427 after rounding. The strict Western denominator rebuilds to **49.813 GW**.

2. **If not, what is the rebuilt number?**
   **49.813 GW facility**, range **[44.396, 53.115] GW**, IT bridge **42.467 GW**.

3. **Which rows caused the delta?**
   The scope delta is driven by `epoch_openai_stargate_uae_buildout_remaining` (-1.400 GW to Western, moved to sovereign), `epoch_alibaba_zhangbei_operational` (-0.203 GW to Western, excluded), and -0.011 GW of rounding versus the legacy hand total.

4. **Is the neocloud T3/T4 split wrong?**
   In the latest checked-out `main`, no. The atom rollup regenerates T3 = **6.480 GW** and T4 = **1.470 GW**. That matches the corrected `neocloud_overlay.yaml` split.

5. **What is the corrected T3/T4 split?**
   Overall Western facility: T3 = **6.480 GW**, T4 = **16.476 GW**. Neocloud-only: T3 = **6.480 GW**, T4 = **1.470 GW**.

6. **What are the corrected conservative and probability-weighted totals?**
   Conservative T1+T2+T3 raw facility = **26.262 GW**. Deterministic tier-default probability-weighted facility = **35.143 GW**. Probability-weighted delta versus the pre-atom, neocloud-corrected overlay baseline (36.162 GW) = **-1.019 GW**.

7. **Which rows have stale or missing sources?**
- None.

8. **Which rows are source-supported only by secondary media?**
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `nscale_operational_seed_capacity` (0.020 GW): First US site online; retained but secondary-source flagged.
- `nscale_microsoft_contract_capacity` (0.900 GW): Private-company contracted capacity after subtracting Fairwater Narvik/Loughton overlap; T4 because no public RPO/take-or-pay disclosure and source is secondary.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `fermi_speculative_excluded_or_T5_only` (unknown MW): 11-17 GW permit aspiration has no customer contract and no operational MW; excluded from Western denominator.
- `xai_humain_saudi` (0.500 GW): Saudi sovereign JV; sidebar only, not Western denominator.
- `reliance_jio_jamnagar` (1.000 GW): India sovereign/strategic capacity; sidebar only, not Western denominator.

9. **Which rows rely on analyst MW inference?**
- `openai_microsoft_fairwater_international` (0.805 GW): International Fairwater sites named; MW estimated from disclosed site-scale range and nScale/Microsoft partnership.
- `xai_colossus2_residual` (0.078 GW): Residual between Musk 2 GW claim and Epoch Colossus buildout; nearly all capacity already in Epoch.
- `together_operational_inferred` (0.081 GW): Operational MW inferred from GPU/site footprint; T6 in tier rollup.
- `voltage_park_lightning_inferred` (0.169 GW): MW inferred from roughly 35k GPU footprint across six sites; no direct MW disclosure.

10. **Which rows are sovereign and must not enter the Western denominator?**
- `epoch_openai_stargate_uae_buildout_remaining` (1.400 GW): Epoch remaining buildout to 1400.0 MW facility by 2028-01-01; project=Stargate #confident; country=United Arab Emirates.
- `microsoft_g42_uae_khazna` (0.260 GW): Sovereign UAE capacity; sidebar only, not Western denominator.
- `xai_humain_saudi` (0.500 GW): Saudi sovereign JV; sidebar only, not Western denominator.
- `humain_amd_saudi` (0.500 GW): Saudi AMD-HUMAIN sovereign JV; sidebar only, not Western denominator.
- `reliance_jio_jamnagar` (1.000 GW): India sovereign/strategic capacity; sidebar only, not Western denominator.
- `uk_culham_ai_growth_zone` (0.300 GW): UK sovereign AI Growth Zone; sidebar only, not Western denominator.

11. **Which rows are double-count risks?**
- `coreweave_epoch_overlap_helios` (0.800 GW): Overlap atom: Helios is already counted as an Epoch site and removed from CoreWeave contracted ex-Epoch capacity.
- `coreweave_applied_digital_pf1_overlap_adjustment` (0.400 GW): PF1 is Applied Digital real estate leased to CoreWeave; counted under CoreWeave fleet and excluded from Applied Digital incremental capacity.
- `nscale_fairwater_overlap_adjustment` (0.600 GW): Nscale Narvik/Loughton capacity is attributed to the Fairwater atom; excluded here to avoid double-count.
- `crusoe_abilene_epoch_overlap` (2.120 GW): Abilene Phase 1+2 and Microsoft Abilene expansion are already counted in Epoch; excluded from Crusoe incremental neocloud capacity.

12. **Which values should be considered canonical for the manuscript?**
   Use `canonical_totals.json`:
   - Raw Western facility horizon: **49.813 GW**
   - Raw Western facility range: **[44.396, 53.115] GW**
   - Raw non-stretch facility: **43.066 GW**
   - Conservative T1+T2+T3 raw: **26.262 GW**
   - Probability-weighted facility: **35.143 GW**
   - Full-realization ceiling facility: **53.115 GW**
   - Sovereign sidebar facility: **3.960 GW**
   - Capital envelope central: **$1.843T** (**$1.494T-$2.341T**)

## Generated Six-Tier Western Facility Rollup

```yaml
T1_operational: 7.369
T2_physically_evidenced: 12.413
T3_firm_commercial: 6.480
T4_announced_site_plan: 16.476
T5_loi_or_stretch: 6.747
T6_analyst_inference: 0.328
total_gw_announced_facility: 49.813
total_gw_non_stretch_facility: 43.066
total_gw_conservative_facility_raw: 26.262
total_gw_probability_weighted_facility: 35.143
```

## Decision Rules

- Raw horizon delta is 1.614 GW, so this is **YELLOW** and can proceed only with documented deltas.
- Probability-weighted delta versus the pre-atom, neocloud-corrected baseline is 1.019 GW, above 0.5 GW, so Monte Carlo must be rerun before manuscript repair. Monte Carlo rerun artifact is present at `monte_carlo_output_facility_seed20260424.json`.
- Conservative delta versus the pre-atom, neocloud-corrected baseline is 0.203 GW, below 0.5 GW, so floor-like claims do not require wholesale rewrite on that basis alone.
