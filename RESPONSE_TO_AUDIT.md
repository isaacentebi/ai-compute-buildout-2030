# Response to Rev-4.1 Audit

Rev-4.2 treats the audit as directionally correct: the prior packet was not defensible as written, and the revision rebuilds the evidence layer before defending any headline number.

## Reproducibility (Finding #2)

The Rev-4.1 packet shipped with `scripts/` containing thin wrappers that delegated to root-level implementations not included in the zip. The full implementations existed in the repository continuously. Rev-4.2 ships a manifest-validated packet: every file in `MANIFEST.md` is present, sha256-verified, and `bash scripts/run_validation.sh` reproduces all canonical totals from a clean unzip. Build script: `scripts/build_packet.py`.

## Finding Map

| Finding | Disposition | Evidence |
|---|---|---|
| #1 Epoch floor / scope | Fixed in atom database | Western raw facility total is now 46.641 GW from `canonical_capacity_atoms.yaml`; `generated_overlay_totals.yaml` and `canonical_totals.json` are regenerated from atoms. |
| #2 Reproducibility | Fixed mechanically | `MANIFEST.md`, `sha256_manifest.txt`, `scripts/build_packet.py` |
| #3 Anthropic consistency | Partially fixed; residual risk flagged | Anthropic-AWS reduced by 1.827 GW; Azure kept as T5 with site-overlap candidates; Google/Broadcom and Fluidstack remain non-additive physical rows pending site MW. |
| #4 Anthropic-AWS overlap | Fixed with partial dedupe | `anthropic_aws_incremental_new_capacity` moves 3.800 -> 1.973 GW; Madison and Ridgeland overlap candidates are recorded in `dedupe_audit.csv`. |
| #5 CoreWeave double count | Audited; Helios already deducted | CoreWeave contracted ex-Epoch remains 2.300 GW because Helios is already removed and no further site-level overlap was proven; risk remains explicit in atom candidates. |
| #6 Crusoe / Abilene | Fixed | `crusoe_cheyenne_or_other_future_capacity` moves 1.980 -> 1.800 GW and T3 -> T4; Abilene stays excluded as Epoch overlap. |
| #7 Meta Hyperion sourcing | Fixed in sourcing layer | Research dispatch replaces cached-transcript-only dependence; Epoch floor remains counted and stretch remains T5. |
| #8 Nscale / Microsoft | Fixed with source replacement and dedupe | Fairwater International moves 0.805 -> 0.300 GW; Nscale Microsoft moves 0.900 -> 0.240 GW with Narvik/Loughton deduped to Fairwater. |
| #9 Sovereign treatment | Fixed in annex structure | Reliance and Culham are split into near-term and stretch rows; all sovereign rows remain outside the Western denominator with explicit tiers. |
| #10 Prose framing | Fixed by linter | `scripts/check_prose_discipline.py` passes after replacing floor/ceiling/commitment language. |

The net first-pass headline impact is -3.172 GW on the Western raw facility total, -2.485 GW on the conservative T1+T2+T3 subset, and -2.386 GW on the deterministic tier-weighted facility view. See `row_delta_ledger.csv`.
