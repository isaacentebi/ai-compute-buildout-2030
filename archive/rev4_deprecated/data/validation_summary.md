# Validation (Rev-5.0)

The tracker pipeline is too small to need a validation harness. Verify by running it.

```bash
bash scripts/refresh_epoch.sh   # pulls latest Epoch + rebuilds tracker
python3 scripts/build_tracker.py  # rebuild without refresh
```

Outputs you should see:

- `tracker.csv` — N rows, where N = (Epoch sites with op. or buildout > 5 MW) + overlay rows
- `tracker.md` — same data in four-bucket markdown view
- Console totals per bucket per scope

## Sanity checks

- Sum of `gw_facility` across `status=operational` Western rows should match Epoch's reported `OP_MW` total minus `(unspecified)` excluded sites.
- Each overlay row carries a `source_url`. Run `python3 scripts/check_urls.py` to verify URL liveness.
- Each overlay row carries `source_date` and `last_checked`. Run `python3 scripts/check_source_freshness.py` for staleness.

## What was retired

The Rev-4.x validation suite (`audit_totals.py`, `check_dedupe_coverage.py`, `check_dedupe_reflexivity.py`, `check_prose_discipline.py`, `check_stale_numbers.py`, `check_tier_table.py`, `monte_carlo_horizon.py`, `build_overlay_totals.py`, `run_offline_validation.sh`, `run_url_validation.sh`) is in `archive/rev4_deprecated/scripts/`. It was guarding an over-engineered atom database and tier framework that we replaced with a four-bucket tracker.
