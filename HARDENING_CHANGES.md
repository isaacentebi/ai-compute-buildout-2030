# Rev-4.1 Hardening Changes

- Preserved the canonical Rev-4.1 overlay constants; no atom-ledger validation required changing them.
- Replaced current-facing neocloud financing residual-probability text with the corrected 3.3% / 60% conditional logic and 25% total target.
- Regenerated `compute_commitments_totals.csv` from canonical atom-derived totals.
- Updated current-facing row-level audit references to 81 capacity atoms x 40 columns.
- Updated README, manifest, confidence decomposition, BibTeX metadata, and H100e convention wording.
- Replaced AMD/OpenAI source references with official AMD Newsroom and OpenAI pages for the 6 GW AMD GPU / initial 1 GW MI450 H2 2026 claim.
- Hardened URL validation to record `final_url`, distinguish verified redirects, blocked/manual-review URLs, failed URLs, and replaced sources.
- URL validation now fails only on `failed_urls` (dead links or content mismatches). `blocked_manual_review` means the site blocked deterministic automation with 401/403/429 and requires browser/manual review; those URLs are reported as WARN, not silently treated as verified.
- Added root-runnable `scripts/` entrypoints and a package-root validation script.
- Expanded stale-number validation across current-facing `.tex`, `.md`, `.yaml`, `.json`, and `.csv` files, excluding archived historical files.
- Moved stale side artifacts to `archive/pre_rev4_1/`.
- Regenerated report, audit, source freshness, URL, rendered-text, PDF info, validation, citation inventory, source map, and checksum artifacts.
