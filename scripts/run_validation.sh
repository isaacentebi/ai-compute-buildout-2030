#!/usr/bin/env bash
set -euo pipefail

python3 scripts/build_overlay_totals.py --check --check-overlay
python3 scripts/check_dedupe_coverage.py
python3 scripts/check_dedupe_reflexivity.py
python3 scripts/audit_totals.py --provenance
python3 scripts/check_tier_table.py
python3 scripts/check_prose_discipline.py
python3 scripts/check_source_freshness.py --temporal
python3 scripts/audit_totals.py --basis all
python3 scripts/check_stale_numbers.py
python3 scripts/check_urls.py
python3 scripts/check_source_freshness.py
python3 scripts/monte_carlo_horizon.py --basis facility --draws 10000 --seed 20260424 >/tmp/ai_compute_mc_validation.txt
