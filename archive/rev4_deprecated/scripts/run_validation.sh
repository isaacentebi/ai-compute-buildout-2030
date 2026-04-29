#!/usr/bin/env bash
# Wrapper that runs offline validation first (fast, deterministic) and then
# the URL-side validation (slow, network-dependent). Called by reviewers
# who want the full sweep; CI can call run_offline_validation.sh alone.
set -euo pipefail

bash "$(dirname "$0")/run_offline_validation.sh"
bash "$(dirname "$0")/run_url_validation.sh"
