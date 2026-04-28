# Rev-4.2 Tier Table

This table is the report's evidence grammar. Tiers describe the physical and contractual maturity of an atom; they are not probability bands by themselves. Realization priors are judgmental defaults used only after the deterministic tier rollup is shown.

| Tier | One-line definition | Concrete inclusion criteria | Example atoms | Count | GW facility | Why not adjacent tier |
|---|---|---|---|---:|---:|---|
| T1 | Operational today. | Energized site or current facility load in Epoch/company/utility evidence. | atom:epoch_microsoft_fairwater_wisconsin_operational; atom:epoch_anthropic_amazon_new_carlisle_operational; atom:epoch_fluidstack_lake_mariner_operational | 24 | 7.572 | Not T2 because these are current loads, not remaining construction. |
| T2 | Site-corroborated buildout with near-term physical evidence. | Named site plus construction/permit/utility/interconnect evidence or Epoch current-planned split with dated buildout. | atom:epoch_microsoft_fairwater_wisconsin_buildout_remaining; atom:epoch_openai_stargate_abilene_buildout_remaining; atom:epoch_fluidstack_lake_mariner_buildout_remaining | 19 | 12.413 | Not T1 because not fully energized; not T3 because physical site evidence is stronger than contract-only. |
| T3 | Firm commercial commitment without enough site evidence to be T2. | Named counterparty and committed/leased/contracted capacity, but site-level overlap or physical buildout remains unresolved. | atom:coreweave_contracted_ex_epoch; atom:nebius_meta_microsoft_contract_capacity; atom:crusoe_cheyenne_or_other_future_capacity | 4 | 6.480 | Not T2 until site/interconnect evidence is tied to the atom; not T4 because commercial counterparty/capacity is disclosed. |
| T4 | Announced site plan or named project lacking full firm-contract evidence. | Named site/project and capacity estimate, but financing, tenant, utility, or final delivery evidence remains incomplete. | atom:epoch_meta_hyperion_buildout_remaining; atom:epoch_openai_stargate_new_mexico_buildout_remaining; atom:anthropic_aws_incremental_new_capacity | 16 | 19.136 | Not T3 when firm take-or-pay/site contract is unresolved; not T5 when a named site/project is evidenced. |
| T5 | Stretch, option, or scaling envelope. | "Up to" capacity, dollar-only envelope, residual stretch, optional expansion, or no named site. | atom:anthropic_azure_incremental_capacity; atom:meta_hyperion_stretch_incremental; atom:anthropic_fluidstack_undisclosed_mw | 11 | 8.047 | Not T4 without a site-level physical assignment; not T6 when the source itself discloses a capacity/envelope claim. |
| T6 | Analyst-inferred capacity. | GPU/$/fleet inference where no source directly discloses MW for the atom. | atom:xai_colossus2_residual; atom:together_operational_inferred; atom:voltage_park_lightning_inferred | 3 | 0.328 | Not T5 because the MW is inferred by the analyst, not disclosed by the source. |

## T1: Operational today

### Inclusion Criteria (testable)

- A named site has current facility MW, IT MW, or an operational status in Epoch, company, utility, or permit evidence.
- The current capacity is separated from remaining buildout.
- The row is counted once at the physical-site layer.

### Worked Examples

#### Example 1: atom:epoch_microsoft_fairwater_wisconsin_operational

- Operator/anchor: Microsoft / OpenAI, Microsoft
- GW facility: 0.555
- Source quote: "Epoch current facility power for Microsoft Fairwater Wisconsin"
- Why T1 not T2: the row is the current operational slice.

#### Example 2: atom:epoch_anthropic_amazon_new_carlisle_operational

- Operator/anchor: Amazon / Anthropic
- GW facility: 1.092
- Source quote: "Epoch current facility power for Anthropic-Amazon New Carlisle"
- Why T1 not T2: the row is already-operational Rainier capacity.

#### Example 3: atom:epoch_fluidstack_lake_mariner_operational

- Operator/anchor: Fluidstack / Anthropic, G42
- GW facility: 0.068
- Source quote: "Epoch current facility power for Fluidstack Lake Mariner"
- Why T1 not T2: the atom captures the current energized slice, while the separate buildout atom captures remaining capacity.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 24
- Total GW facility: 7.572
- Realization confidence prior: 1.00

## T2: Site-corroborated buildout

### Inclusion Criteria (testable)

- Named site or campus.
- Dated construction/buildout, permit, utility, interconnection, or dataset evidence.
- Physical evidence is stronger than contract-only evidence, even if the full site is not energized.

### Worked Examples

#### Example 1: atom:epoch_microsoft_fairwater_wisconsin_buildout_remaining

- Operator/anchor: Microsoft / OpenAI, Microsoft
- GW facility: 2.773
- Source quote: "remaining buildout to 3328.0 MW facility by 2027-10-03"
- Why T2 not T1: this is remaining buildout, not current load.
- Why T2 not T3: the site and buildout are physically identified.

#### Example 2: atom:epoch_openai_stargate_abilene_buildout_remaining

- Operator/anchor: Oracle / OpenAI
- GW facility: 0.980
- Source quote: "remaining buildout to 1180.0 MW facility"
- Why T2 not T1: current and remaining capacity are split.
- Why T2 not T3: the Abilene site is site-corroborated.

#### Example 3: atom:epoch_fluidstack_lake_mariner_buildout_remaining

- Operator/anchor: Fluidstack / Anthropic, G42
- GW facility: 0.441
- Source quote: "remaining buildout to 509.0 MW facility by 2027-03-31"
- Why T2 not T1: not all capacity is online today.
- Why T2 not T3: site-level buildout evidence exists.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 20
- Total GW facility: 12.028
- Realization confidence prior: 0.88

## T3: Firm commercial commitment

### Inclusion Criteria (testable)

- Counterparty and capacity are disclosed.
- The commitment is contract/lease/customer-backed.
- Site-level mapping, physical energization, or Epoch overlap remains unresolved.

### Worked Examples

#### Example 1: atom:coreweave_contracted_ex_epoch

- Operator/anchor: CoreWeave / Microsoft, OpenAI, Meta, IBM
- GW facility: 2.300
- Source quote: "CoreWeave contracted fleet ex Epoch Helios"
- Why T3 not T2: Rev-4.2 must still map CoreWeave capacity against Epoch hyperscaler sites.
- Why T3 not T4: disclosed contracted fleet evidence is stronger than announced-site-only evidence.

#### Example 2: atom:nebius_meta_microsoft_contract_capacity

- Operator/anchor: Nebius / Meta, Microsoft
- GW facility: 2.000
- Source quote: "Nebius contracted fleet"
- Why T3 not T2: physical site-level overlap is unresolved.
- Why T3 not T4: the commercial capacity is counterparty-backed.

#### Example 3: atom:crusoe_cheyenne_or_other_future_capacity

- Operator/anchor: Crusoe / OpenAI or other anchors
- GW facility: 1.980
- Source quote: "Cheyenne and residual ex-Epoch contracted capacity"
- Why T3 not T2: Cheyenne/Abilene residual treatment still needs site-level dedupe.
- Why T3 not T4: capacity is tied to a commercial/operator claim, not just a speculative site plan.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 3
- Total GW facility: 4.500
- Realization confidence prior: 0.78

## T4: Announced site plan

### Inclusion Criteria (testable)

- Named site or project exists.
- Public evidence supports a capacity estimate or buildout plan.
- Firm customer/contract/utility details are incomplete or the site is not yet sufficiently evidenced for T2.

### Worked Examples

#### Example 1: atom:epoch_meta_hyperion_buildout_remaining

- Operator/anchor: Meta / Meta
- GW facility: 2.262
- Source quote: "delivering over two gigawatts of compute capacity"
- Why T4 not T3: the row is a site plan/buildout rather than a customer resale contract.
- Why T4 not T5: Richland Parish/Hyperion is a named project with financing and utility evidence.

#### Example 2: atom:epoch_openai_stargate_new_mexico_buildout_remaining

- Operator/anchor: Oracle / OpenAI
- GW facility: 2.210
- Source quote: "remaining buildout to 2210.0 MW facility"
- Why T4 not T3: the evidence is a site/project plan, not a standalone commercial lease row.
- Why T4 not T5: the site is named in the Epoch layer.

#### Example 3: atom:anthropic_aws_incremental_new_capacity

- Operator/anchor: Amazon / Anthropic
- GW facility: 3.800
- Source quote: "up to 5GW of new capacity"
- Why T4 not T3: final take-or-pay and site allocation are not disclosed.
- Why T4 not T5: the commitment is tied to AWS/Rainier with concrete candidate sites, pending Rev-4.2 dedupe.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 18
- Total GW facility: 18.569
- Realization confidence prior: 0.58

## T5: Stretch / option / scaling envelope

### Inclusion Criteria (testable)

- "Up to" capacity, stretch language, option, dollar-only infrastructure envelope, or undisclosed sites.
- The source is real, but physical-site assignment is not strong enough for T4.
- The low case can be zero incremental GW when overlap is unresolved.

### Worked Examples

#### Example 1: atom:anthropic_azure_incremental_capacity

- Operator/anchor: Microsoft Azure / Anthropic
- GW facility: 1.180 high case
- Source quote: "up to one gigawatt of compute capacity"
- Why T5 not T4: no Azure site is named.
- Why T5 not T6: the capacity claim is source-disclosed, not analyst-inferred.

#### Example 2: atom:meta_hyperion_stretch_incremental

- Operator/anchor: Meta / Meta
- GW facility: 3.014
- Source quote: "scale up to 5GW over several years"
- Why T5 not T4: the stretch above the 2 GW-scale floor lacks the same utility/JV support.
- Why T5 not T6: Meta disclosed the stretch claim directly.

#### Example 3: atom:anthropic_fluidstack_undisclosed_mw

- Operator/anchor: Fluidstack / Anthropic
- GW facility: none assigned
- Source quote: "building data centers with Fluidstack in Texas and New York"
- Why T5 not T4: no MW or site list is disclosed.
- Why T5 not T6: no analyst dollar-to-MW conversion is used.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 11
- Total GW facility: 7.807
- Realization confidence prior: 0.32

## T6: Inferred from GPU/$/fleet evidence

### Inclusion Criteria (testable)

- No direct source-disclosed MW for the atom.
- Capacity is inferred from GPU count, dollars, fleet claims, or analyst conversion.
- The inference method is explicit and does not masquerade as physical evidence.

### Worked Examples

#### Example 1: atom:xai_colossus2_residual

- Operator/anchor: xAI / xAI
- GW facility: 0.078
- Source quote: "Memphis Colossus 2 residual"
- Why T6 not T5: residual MW is analyst logic after Epoch overlap, not a direct MW disclosure.

#### Example 2: atom:together_operational_inferred

- Operator/anchor: Together AI / Together AI
- GW facility: 0.081
- Source quote: "Maryland, Memphis, Sweden operational footprint"
- Why T6 not T5: the MW is inferred from operational footprint evidence.

#### Example 3: atom:voltage_park_lightning_inferred

- Operator/anchor: Voltage Park / Lightning AI
- GW facility: 0.169
- Source quote: "Six-site US GPU cloud footprint"
- Why T6 not T5: the capacity is analyst-inferred from GPU-cloud footprint, not directly disclosed MW.

### Aggregate Stats (Rev-4.2 adjudicated atom database)

- Atom count: 3
- Total GW facility: 0.328
- Realization confidence prior: 0.25
