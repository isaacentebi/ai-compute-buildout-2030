#!/usr/bin/env bash
# Offline deterministic validation. Runs in seconds without network access.
# Use scripts/run_url_validation.sh for the URL/freshness side, which is slow
# and depends on external availability.
set -euo pipefail

python3 scripts/build_overlay_totals.py --check --check-overlay
python3 scripts/check_dedupe_coverage.py
python3 scripts/check_dedupe_reflexivity.py
python3 scripts/audit_totals.py --provenance
python3 scripts/check_tier_table.py
python3 scripts/check_prose_discipline.py
python3 scripts/audit_totals.py --basis all
python3 scripts/check_stale_numbers.py
