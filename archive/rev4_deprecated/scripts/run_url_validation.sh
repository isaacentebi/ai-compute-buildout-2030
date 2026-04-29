#!/usr/bin/env bash
# URL-side validation. Slow and network-dependent; can stall on blocked
# hosts. Run separately from the offline validation gate.
set -euo pipefail

python3 scripts/check_source_freshness.py --temporal
python3 scripts/check_urls.py
python3 scripts/check_source_freshness.py
