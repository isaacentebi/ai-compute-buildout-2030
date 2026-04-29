# AI Compute Build-Out, 2026–2030

A tracker of announced and operational AI compute capacity through 2030.

**Single source of truth**: [`tracker.csv`](tracker.csv) (machine) and [`tracker.md`](tracker.md) (human).
Built from Epoch AI's Frontier Data Centers + a small hand-curated overlay for what Epoch's documented methodology doesn't cover.

## How it works

```
epoch_data_centers/  ←  refresh_epoch.sh pulls latest from epoch.ai/data/data-centers
        +
overlay.csv          ←  hand-curated rows for capacity Epoch can't see
        ↓
build_tracker.py
        ↓
tracker.csv  +  tracker.md  +  ~/Downloads/atoms_audit.xlsx
```

Two scripts. One CSV input. One CSV output. That's the system.

## Buckets (lifecycle stage, no probability priors)

| Bucket | What goes in | Source class |
|---|---|---|
| operational | Energized facility power as of today | Epoch op. + verified neocloud |
| under_construction | Named site + dated buildout / permit / utility / interconnect | Epoch buildout-remaining + recent groundbreakings |
| contracted | Counterparty + capacity disclosed via 10-K / lease / take-or-pay | Non-Epoch overlay |
| announced | "Up to N GW" headlines without contracted basis or named site | Non-Epoch overlay |
| canceled | Project paused, terminated, or descoped post-announcement | Either source |

Sovereign sidebar items (UAE / Saudi / India / UK / EU / Asia) are reported separately and not added to the Western total.

## Refresh

```bash
bash scripts/refresh_epoch.sh
```

This pulls the latest Epoch CSVs, regenerates `epoch_data_centers/compiled.json`, and rebuilds `tracker.csv` + `tracker.md`.
Epoch updates roughly weekly. The `epoch_data_centers/snapshots/` directory keeps each pull dated.

## To audit

Open `~/Downloads/atoms_audit.xlsx`. Tab 1 (README) defines the four buckets, lists totals, and explains the columns. Tab 2 (Tracker) is the full row-level table — sortable, filterable, one row per capacity item.

## Files in the repo

| File | Purpose |
|---|---|
| `tracker.csv` / `tracker.md` | Output: every row, four-bucket view |
| `overlay.csv` | Input: hand-curated rows Epoch doesn't yet cover |
| `epoch_data_centers/` | Upstream Epoch snapshot + compile.py (their script) |
| `scripts/refresh_epoch.sh` | Pull fresh Epoch + rebuild |
| `scripts/build_tracker.py` | Combine Epoch + overlay → tracker |
| `scripts/check_urls.py` | URL liveness check |
| `scripts/check_source_freshness.py` | Last-checked-date linter |
| `source_claim_map.csv` | atom_id → publisher / URL / claim text |
| `anatomy_layer_costs.yaml` | Capex unit-economics (separate analysis, not the tracker) |
| `report.tex` / `report.pdf` | Manuscript (Rev-4.4; pre-simplification — to be rewritten on top of the tracker) |
| `archive/rev4_deprecated/` | Prior atom database, tier framework, Monte Carlo, tier-table validator, etc. — moved out so they don't accrete drift |

## Scope

- **Western**: US-led hyperscaler + frontier-lab + merchant-neocloud capacity. The primary denominator.
- **Sovereign sidebar**: UAE, Saudi Arabia, India, UK, EU sovereign-AI initiatives. Reported separately because financing model, geopolitics, and disclosure norms differ.
- **Excluded**: China (Alibaba Zhangbei tracked by Epoch but kept out of Western totals; broader Chinese AI infrastructure is materially under-disclosed and out of scope qualitatively).

## License

- Paper, data, documentation: [CC BY 4.0](LICENSE).
- Scripts: MIT (in [LICENSE](LICENSE)).
- Upstream Epoch AI data: CC BY 4.0 per Epoch's license. Cite: "Epoch AI, *Frontier Data Centers*, retrieved 2026-04-29. https://epoch.ai/data/data-centers".

## What changed in Rev-5.0 (2026-04-29)

Stripped down. Removed the six-tier evidence framework, realization-probability priors, deterministic tier-weighted point, Monte Carlo apparatus, dedupe-coverage / dedupe-reflexivity / tier-table validators, prose-discipline gate, and the 4906-line atoms YAML. Replaced with one CSV overlay + one Python script that combines it with Epoch.

Audit findings consolidated from three independent deep-research passes (Anthropic / OpenAI / Gemini) are baked into the new `overlay.csv` row magnitudes and the cancellations bucket. Manuscript still reflects the old (tier-framework) framing and is queued for rewrite on top of the tracker.
