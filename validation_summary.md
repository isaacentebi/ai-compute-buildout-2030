# Validation Summary

| Check | Status | Detail |
|---|---|---|
| stale current-facing values | PASS | python3 scripts/check_stale_numbers.py passed. `grep_stale_values_output.txt` contains only explicitly labeled historical comparison values. |
| stale archived values | allowed | `archive/pre_rev4_1/` is excluded from current-facing validation. |
| source URL verified | PASS | verified_ok=93; redirected_verified=5; blocked_manual_review=33; failed=0; replaced=2. |
| blocked URLs | WARN | 33 blocked/manual-review URLs listed in `url_check_report.json`. |
| redirects | WARN | 5 redirects listed with `final_url` and content-validation status. |
| row_level_audit dimensions | PASS | 81 capacity atoms x 40 columns. |
| compute_commitments_totals.csv freshness | PASS | Regenerated from canonical totals. |
| direct script invocation from package root | PASS | Required python3 scripts/... commands and bash scripts/run_validation.sh completed. |
