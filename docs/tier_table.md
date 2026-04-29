# Rev-4.3 Tier Table — Flagship Reference

This table is the report's evidence grammar. **Tiers describe the physical and contractual maturity of an atom; they are not probability bands by themselves.** Realization priors are judgmental defaults applied only after the deterministic tier rollup is shown.

If you read only one document in this packet, this is the one. Every headline number ladders up from per-atom tier assignments documented here. Source quotes are verbatim from primary materials; "Why not T(N±1)" notes show the testable boundary.

## The Six Tiers at a Glance (Western denominator only)

| Tier | One-line definition | Concrete inclusion criteria | Example atoms | Count | GW facility (low / central / high) | Why not adjacent tier |
|---|---|---|---|---:|---:|---|
| **T1** | Operational today | Energized site or current facility load in Epoch / company / utility evidence; current capacity separated from remaining buildout | `epoch_microsoft_fairwater_wisconsin_operational`; `epoch_anthropic_amazon_new_carlisle_operational`; `epoch_fluidstack_lake_mariner_operational` | 22 | 6.519 / 6.519 / 6.519 | Not T2 because these are current loads, not remaining construction |
| **T2** | Site-corroborated buildout | Named site + dated construction/permit/utility/interconnect evidence OR Epoch current-planned split with dated buildout | `epoch_microsoft_fairwater_wisconsin_buildout_remaining`; `epoch_openai_stargate_abilene_buildout_remaining`; `epoch_fluidstack_lake_mariner_buildout_remaining` | 19 | 11.888 / 11.908 / 12.218 | Not T1 (not fully energized); not T3 (physical site evidence is stronger than contract-only) |
| **T3** | Firm commercial commitment | Named counterparty + committed/leased/contracted capacity with RPO/$60.7B-class backlog support; site-level overlap or physical buildout still unresolved | `coreweave_contracted_ex_epoch`; `nebius_meta_microsoft_contract_capacity`; `applied_digital_pf2_leased_capacity` | 3 | 4.500 / 4.500 / 4.500 | Not T2 (site/interconnect evidence not tied to atom); not T4 (commercial counterparty + capacity disclosed with contract economics) |
| **T4** | Announced site plan | Named site/project with capacity estimate; financing, tenant, utility, or final delivery evidence incomplete | `epoch_meta_hyperion_buildout_remaining`; `epoch_openai_stargate_new_mexico_buildout_remaining`; `anthropic_aws_incremental_new_capacity` | 13 | 13.810 / 15.789 / 18.316 | Not T3 (firm take-or-pay/site contract unresolved); not T5 (named site/project is evidenced) |
| **T5** | Stretch / option / scaling envelope | "Up to" capacity, dollar-only envelope, residual stretch, optional expansion, or no named site; low case can be 0 incremental GW when overlap unresolved | `anthropic_google_broadcom_physical_tpu` (NEW Rev-4.3); `meta_hyperion_stretch_incremental`; `anthropic_azure_incremental_capacity` | 7 | 2.553 / 8.857 / 12.147 | Not T4 (no site-level physical assignment); not T6 (source itself discloses capacity envelope claim) |
| **T6** | Inferred from GPU / $ / fleet evidence | No direct source-disclosed MW for atom; capacity inferred from GPU count, dollars, fleet claims, or analyst conversion; inference method explicit | `xai_colossus2_residual`; `together_operational_inferred`; `voltage_park_lightning_inferred` | 3 | 0.250 / 0.328 / 0.510 | Not T5 (MW inferred by analyst, not disclosed by source) |
| | | | | **67** | **39.520 / 47.901 / 54.210** | |

**Sovereign sidebar (separate, not in Western denominator):** 4.960 GW across 9 included atoms (Stargate UAE 1.40, Microsoft G42 UAE Khazna 0.26, HUMAIN xAI Saudi 0.50, HUMAIN AMD Saudi 0.50, Reliance Jamnagar near-term 0.12, Reliance Jamnagar stretch 0.88, Reliance Andhra MoU 1.00, Culham initial 0.12, Culham scale-out 0.18). One additional row, `digital_connexion_vizag_1gw_overlap` (1.00 GW), is flagged sovereign but tier `excluded` to avoid double-count with the Reliance Andhra MoU. All sovereign atoms have `included_in_western_raw_horizon=false`.

**Capital envelope**: $1.772T central ($1.437–2.251T range) at $37B/facility-GW × 47.901 GW. Treated as **capex envelope**, not announced-capex-as-bound (per Rev-4.2 prose discipline).

---

## T1: Operational today

### Inclusion Criteria (testable)

- Named site has current facility MW, IT MW, or operational status in Epoch / company / utility / permit evidence
- Current capacity is separated from remaining buildout (T1 row vs T2 row)
- Atom is counted once at the physical-site layer

### Worked Examples

#### `epoch_microsoft_fairwater_wisconsin_operational` — 0.555 GW facility

- Operator/anchor: Microsoft / OpenAI, Microsoft
- Source quote: *"Mount Pleasant, WI"* operational facility per Epoch AI Frontier Data Centers (2026-04-20 snapshot)
- Why T1 not T2: current operational slice; remaining buildout (2.773 GW) is a separate T2 atom

#### `epoch_anthropic_amazon_new_carlisle_operational` — 1.092 GW facility

- Operator/anchor: Amazon / Anthropic
- Source quote: *"St. Joseph County, IN"* — Project Rainier #confident per Epoch
- Why T1 not T2: already-operational Rainier capacity; New Carlisle is the strongest Anthropic-AWS Epoch context site, treated as pre-existing per Anthropic Apr 20, 2026 "new capacity" framing

#### `epoch_fluidstack_lake_mariner_operational` — 0.068 GW facility

- Operator/anchor: Fluidstack / Anthropic, G42
- Source quote: *"Lake Mariner, NY"* — Anthropic-attributed per Epoch (TPU for Anthropic per Epoch notes)
- Why T1 not T2: current energized slice; remaining buildout (0.441 GW) is a separate T2 atom

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 22
- **Total GW facility**: 6.519
- **Realization confidence prior**: 1.00 (T1 atoms are observed operational)

Note: `coreweave_operational_disclosed` (0.850 GW T1) is retained at tier-table level for visibility but `included_raw_horizon: false` at the totals level — it is a subset of the 3.1 GW total contracted (CoreWeave 10-K) and would double-count against `coreweave_contracted_ex_epoch` (T3, 2.300 GW). Reviewer #5 fix Rev-4.3.

---

## T2: Site-corroborated buildout

### Inclusion Criteria (testable)

- Named site or campus
- Dated construction / buildout / permit / utility / interconnection or dataset evidence
- Physical evidence is stronger than contract-only evidence even if the full site is not energized

### Worked Examples

#### `epoch_microsoft_fairwater_wisconsin_buildout_remaining` — 2.773 GW facility

- Operator/anchor: Microsoft / OpenAI, Microsoft
- Source quote: *"3328.0 MW facility by 2027-10-03"* (Epoch buildout schedule)
- Why T2 not T1: remaining buildout, not current load
- Why T2 not T3: site (Mount Pleasant) and buildout schedule are physically identified

#### `epoch_openai_stargate_abilene_buildout_remaining` — 0.980 GW facility

- Operator/anchor: Oracle / OpenAI
- Source quote: *"5502 Spinks Road, Abilene, TX"* — first phase live on OCI per Crusoe (2025-09-30)
- Why T2 not T1: current and remaining capacity split
- Why T2 not T3: Abilene site-corroborated (permit + utility + Crusoe construction record)

#### `epoch_fluidstack_lake_mariner_buildout_remaining` — 0.441 GW facility

- Operator/anchor: Fluidstack / Anthropic, G42
- Source quote: *"509.0 MW facility by 2027-03-31"* (Epoch buildout schedule)
- Why T2 not T1: not all capacity online today
- Why T2 not T3: site-level buildout evidence exists at Lake Mariner

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 19
- **Total GW facility**: 11.908 (low 11.888, high 12.218)
- **Realization confidence prior**: 0.88

---

## T3: Firm commercial commitment

### Inclusion Criteria (testable)

- Counterparty AND capacity disclosed
- Commitment is contract / lease / customer-backed (RPO, take-or-pay, MSA + order forms)
- Site-level mapping, physical energization, or Epoch overlap remains unresolved

### Worked Examples

#### `coreweave_contracted_ex_epoch` — 2.300 GW facility

- Operator/anchor: CoreWeave / Microsoft 67% revenue, OpenAI, Meta, IBM
- Source quote: *"total contracted power capacity was approximately 3.1 GW"* — CoreWeave FY2025 Form 10-K (filed 2026-03-02)
- Math: 3.100 GW total contracted - 0.800 GW Helios already in Epoch = 2.300 GW ex-Epoch
- Why T3 not T2: per-customer site allocation redacted in 10-K
- Why T3 not T4: $60.7B RPO + $66.8B revenue backlog + 5-year weighted-average contract duration with named investment-grade counterparties

#### `nebius_meta_microsoft_contract_capacity` — 2.000 GW facility

- Operator/anchor: Nebius / Meta + Microsoft
- Source quote: *"new AI infrastructure agreement with Meta"* — Nebius press release (2026-03-16)
- Why T3 not T2: physical site-level overlap unresolved
- Why T3 not T4: counterparty-backed commercial capacity disclosed

#### `applied_digital_pf2_leased_capacity` — 0.200 GW facility

- Operator/anchor: Applied Digital / undisclosed investment-grade hyperscaler
- Source quote: *"200 megawatts"* critical IT lease — Applied Digital press release (2025-10-22)
- Why T3 not T2: site (Polaris Forge 2) is named but tenant identity redacted
- Why T3 not T4: investment-grade hyperscaler commitment with executed lease

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 3
- **Total GW facility**: 4.500
- **Realization confidence prior**: 0.78

---

## T4: Announced site plan

### Inclusion Criteria (testable)

- Named site or project exists
- Public evidence supports a capacity estimate or buildout plan
- Firm customer / contract / utility details are incomplete OR site is not yet sufficiently evidenced for T2

### Worked Examples

#### `anthropic_aws_incremental_new_capacity` — 1.973 GW facility (Rev-4.2: 3.800 → 1.973 after dedupe)

- Operator/anchor: Amazon Web Services / Anthropic
- Source quote: *"up to 5GW of new capacity"* — Anthropic Apr 20, 2026 announcement
- Math: 5.0 GW announced - 1.827 GW dedupe (Madison 0.819 + Ridgeland 1.008 Epoch Rainier candidates) - 1.200 GW assumed inside other AWS expansion = 1.973 GW residual ex-Epoch
- Why T4 not T3: final take-or-pay terms and full site allocation not disclosed
- Why T4 not T5: commitment tied to AWS / Project Rainier with concrete candidate sites in Mississippi (MDEQ permits 1720-00098 Madison + 1720-00099 Ridgeland)

#### `epoch_meta_hyperion_buildout_remaining` — 2.262 GW facility

- Operator/anchor: Meta / Meta
- Source quote: *"delivering over two gigawatts of compute capacity"* — Meta Richland Parish data center page
- Why T4 not T3: row is site plan / buildout, not customer resale contract
- Why T4 not T5: Richland Parish / Hyperion is named project with $27B Blue Owl JV financing + LPSC Order U-37425 supporting ~2 GW initial generation

#### `crusoe_cheyenne_or_other_future_capacity` — 1.800 GW facility (Rev-4.2: T3 → T4 demote, 1.980 → 1.800 GW)

- Operator/anchor: Crusoe / Tallgrass JV, anchor tenant undisclosed
- Source quote: *"develop a 1.8 gigawatt (GW) AI data center campus"* — Tallgrass press release (2025-07-24)
- Why T4 not T3: no firm hyperscaler tenant or take-or-pay commitment disclosed; reviewer #6 demote
- Why T4 not T5: Laramie County File 26-023 site-plan approval (2026-01-06) for Project Jade + BFC Power; Tallgrass $7B energy infrastructure investment

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 13
- **Total GW facility**: 15.789 (low 13.810, high 18.316)
- **Realization confidence prior**: 0.58

---

## T5: Stretch / option / scaling envelope

### Inclusion Criteria (testable)

- "Up to" capacity, stretch language, option, dollar-only infrastructure envelope, OR undisclosed sites
- Source is real, but physical-site assignment not strong enough for T4
- Low case can be **zero incremental GW** when overlap is unresolved

### Worked Examples

#### `anthropic_google_broadcom_physical_tpu` — 2.700 GW central / range 0–5.4 (NEW Rev-4.3)

- Operator/anchor: Google Cloud + Broadcom / Anthropic
- Source quote: *"approximately 3.5 gigawatts"* — Broadcom Form 8-K (2026-04-06); plus *"vast majority will be sited in the United States"* — Anthropic Apr 6, 2026
- Math: 1 GW IT (Anthropic Oct 23, 2025 "well over a gigawatt") + 3.5 GW IT (Broadcom 8-K Apr 6, 2026) = 4.5 GW IT total exposure. Central case 50% Epoch overlap (Fluidstack Lake Mariner 0.509 + 6 Google Epoch sites Goodnight/New Albany/Cedar Rapids/Pryor N/Omaha/Council Bluffs E summing ~3.5 GW, halved) → 2.7 GW residual facility. Range 0 (full overlap absorbed) to 5.4 GW (no overlap).
- Why T5 not T4: no specific Azure region, site, utility, PPA, or contract tenor disclosed for Anthropic-Google capacity allocation
- Why T5 not T6: GW figure source-disclosed, not analyst-inferred
- Per user direction: replaces prior 0 GW Class B chip-procurement treatment that violated 3-of-3 source-content inclusion test (counterparty + magnitude + window all present)

#### `meta_hyperion_stretch_incremental` — 3.014 GW facility (range 0–3.014)

- Operator/anchor: Meta / Meta
- Source quote: *"scale up to 5GW over several years"* — Mark Zuckerberg, Meta Q2 2025 earnings call (2025-07-30); **Rev-4.3 source URL replaced from local cache to public Q2 2025 transcript PDF** addressing reviewer #7
- Math: 5.0 GW Zuckerberg stretch - 2.262 GW Epoch Hyperion floor = 2.738 GW IT × 1.10 PUE = 3.014 GW facility incremental above floor
- Why T5 not T4: stretch above the 2 GW-scale floor lacks the same utility/JV support; LPSC U-37425 supports ~2 GW initial only
- Why T5 not T6: Meta CEO disclosed the stretch directly

#### `anthropic_azure_incremental_capacity` — 0.590 GW central / range 0–1.18 (Rev-4.3: 1.180 → 0.590 partial Fairwater dedupe)

- Operator/anchor: Microsoft Azure / Anthropic
- Source quote: *"up to one gigawatt of compute capacity"* — Microsoft Official Blog (2025-11-18)
- Math: Central case applies 50% Fairwater overlap assumption (Microsoft Azure Blog 2026-01-05 + NVIDIA IR 2026-01-05 confirm Vera Rubin deploys at Fairwater Wisconsin/Atlanta — the chip class Anthropic uses on Azure). 0.295 GW Wisconsin + 0.295 GW Atlanta = 0.590 GW dedupe; residual 0.590 GW central. Range 0 (full Fairwater carve-out) to 1.18 GW (full net-new Microsoft sites).
- Why T5 not T4: no Azure region/site disclosed
- Why T5 not T6: capacity source-disclosed by Microsoft, not analyst-inferred

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 7
- **Total GW facility**: 8.857 (low 2.553, high 12.147 — Anthropic-Azure low 0, Anthropic-Google low 0, Meta-Hyperion stretch low 0 each contribute to the wide low-side band; Anthropic-Google high case 5.4 widens the upside)
- **Realization confidence prior**: 0.32

---

## T6: Inferred from GPU / $ / fleet evidence

### Inclusion Criteria (testable)

- No direct source-disclosed MW for the atom
- Capacity inferred from GPU count, dollars, fleet claims, or analyst conversion
- Inference method is explicit and does not masquerade as physical evidence

### Worked Examples

#### `xai_colossus2_residual` — 0.078 GW facility

- Operator/anchor: xAI / xAI
- Source quote: *"Memphis Colossus 2 residual"* — Tom's Hardware (2025-12-30)
- Math: 2.0 GW Musk "almost-2-GW" claim - 0.442 GW Epoch Colossus 1 - 1.494 GW Epoch Colossus 2 = 0.064 GW remaining → carried at 0.078 GW with secondary-source uncertainty
- Why T6 not T5: residual MW is analyst logic after Epoch overlap, not direct MW disclosure; Tom's Hardware secondary

#### `together_operational_inferred` — 0.081 GW facility

- Operator/anchor: Together AI / Together AI
- Source quote: *"Maryland, Memphis, Sweden operational footprint"* (Together press)
- Math: MW inferred from GPU footprint and operational sites
- Why T6 not T5: MW is inferred from operational footprint, not directly disclosed

#### `voltage_park_lightning_inferred` — 0.169 GW facility

- Operator/anchor: Voltage Park / Lightning AI
- Source quote: *"six-site US GPU cloud footprint"* (Voltage Park merger context)
- Math: ~35,000 GPU footprint → MW inferred at GPU TDP × utilization
- Why T6 not T5: capacity analyst-inferred from GPU-cloud footprint, not directly disclosed

### Aggregate Stats (Rev-4.3 adjudicated atom database)

- **Atom count**: 3
- **Total GW facility**: 0.328 (low 0.250, high 0.510)
- **Realization confidence prior**: 0.25

---

## Realization Confidence Priors (judgmental)

| Tier | Realization prior | Interpretation |
|---|---:|---|
| T1 | 1.00 | Operational; observed |
| T2 | 0.88 | Site evidence + buildout schedule; small slip risk |
| T3 | 0.78 | Firm commercial commitment; some delivery risk |
| T4 | 0.58 | Announced site, financing/anchor incomplete |
| T5 | 0.32 | Stretch / scaling option; high cancellation risk |
| T6 | 0.25 | Inferred capacity; high uncertainty in basis itself |

These are judgmental priors, not empirical frequencies. The Monte Carlo simulation applies them as default tier-realization rates and adds named systemic stress shocks; reviewer flagged double-discounting risk between tier priors and stress shocks (deferred to Rev-4.4).

## Cross-Tier Validation

- Σ T1+T2+T3 raw = 22.927 GW (matches `canonical_totals.json` `conservative_T1_T2_T3_raw_gw_facility`)
- Σ T1+T2+T3+T4 raw = 38.716 + 0.328 carry = 39.044 GW (matches `canonical_totals.json` `raw_non_stretch_gw_facility`)
- Σ all tiers raw central = 47.901 GW (matches `canonical_totals.json` `raw_western_horizon_gw_facility`)
- Σ all tiers raw high = 54.210 GW (matches `canonical_totals.json` `full_realization_ceiling_gw_facility`)
- Σ all tiers raw low = 39.520 GW (matches `canonical_totals.json` `raw_western_horizon_range_gw_facility[0]`; reflects atoms with low=0 cases like Anthropic-Azure, Anthropic-Google/Broadcom, and Meta-Hyperion stretch whose atom-level low subtotals to 0)

## Cross-References

- Atom data: `canonical_capacity_atoms.yaml`
- Per-row delta history: `row_delta_ledger.csv`
- Site-level dedupe matrix: `dedupe_audit.csv` + narrative in `docs/dedupe_audit_report.md`
- Per-contract drilldowns: `contracts/` directory (17 pages, schema in `contracts/_schema.md`)
- Audit response: `RESPONSE_TO_AUDIT.md`
- Research dispatches (primary-source evidence): `docs/research/A1` through `D3`
