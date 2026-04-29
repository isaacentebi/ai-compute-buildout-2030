# Rev-4.1 Reproduction Prompt

Use the files in this bundle to reproduce the Rev-4.1 audit outputs and manuscript.

Run:

```bash
python3 audit_totals.py --basis all
python3 check_source_freshness.py --today 2026-04-27
python3 monte_carlo_horizon.py --basis facility --draws 10000 --seed 20260424
python3 monte_carlo_horizon.py --basis it --draws 10000 --seed 20260424
python3 check_urls.py
pdflatex -interaction=nonstopmode report.tex
pdflatex -interaction=nonstopmode report.tex
pdftotext report.pdf - > report_rendered.txt
```

The canonical current values are in `CANONICAL_CONSTANTS.md`. Current-facing prose should not override those values.
