# Rev-4.2 Dedupe Audit Report

`dedupe_audit.csv` is the site-level control surface for Rev-4.2. Its rule is simple: no overlay MW is treated as incremental unless the row says why it is not already captured by Epoch or another overlay atom.

## Final Dispositions

The first adjudication pass removed **3.172 GW** from the Western raw facility denominator, moving the headline from **49.813 GW** to **46.641 GW**.

| Atom | Prior GW | Rev-4.2 GW | Disposition |
|---|---:|---:|---|
| `anthropic_aws_incremental_new_capacity` | 3.800 | 1.973 | Partial dedupe for Madison and Ridgeland Epoch Rainier candidates. |
| `openai_microsoft_fairwater_international` | 0.805 | 0.300 | Source replacement to named Narvik/Loughton MW anchors. |
| `nscale_microsoft_contract_capacity` | 0.900 | 0.240 | Keep Ward County/Cedarvale floor; dedupe Narvik/Loughton to Fairwater; carry Texas option only in high range. |
| `crusoe_cheyenne_or_other_future_capacity` | 1.980 | 1.800 | Keep Cheyenne as T4 site-plan capacity; Abilene remains excluded as Epoch overlap. |

## Rows Kept With Explicit Non-Overlap Evidence

CoreWeave operational capacity remains included because the local Epoch Helios row has no current operational MW. CoreWeave contracted ex-Epoch capacity remains included because Helios is already deducted and no public site allocation proves further overlap.

Lambda/Microsoft remains included at 0.320 GW with a medium double-count risk flag: research found no evidence Lambda operates Fairwater Wisconsin or Crusoe Abilene, but the Microsoft/NVIDIA anchor makes it a continuing watch item.

xAI Colossus residual remains T6 and explicitly depends on subtracting Epoch Colossus 1 and 2. It is not treated as independent site evidence.

## Sovereign Annex Splits

Reliance/Jio Jamnagar is split into a 0.120 GW near-term row and a 0.880 GW stretch residual. Culham is split into a 0.120 GW initial opportunity and a 0.180 GW central stretch residual. These rows stay outside the Western denominator.

## Residual Risk

The remaining high-risk issue is not an unexamined double count; it is unresolved public evidence. Rows with unresolved overlap risk now carry `double_count_risk` and `epoch_overlap_candidates` in `canonical_capacity_atoms.yaml`, with matching rows in `dedupe_audit.csv`.
