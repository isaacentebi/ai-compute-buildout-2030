#!/usr/bin/env python3
"""Rev-4.1 regression checks for stale numbers and missing bundle files."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
EXTENSIONS = {".tex", ".md", ".yaml", ".json", ".csv"}
IGNORE_DIR_PARTS = {"archive", ".git", ".claude", "__pycache__", "epoch_data_centers"}
STALE = [
    r"51\.9", r"51\.93", r"51\.43", r"43\.93", r"36\.46", r"36\.8",
    r"27\.93", r"54\.72", r"55\.3", r"2\.56", r"32\.52", r"31\.8",
    r"31\.5", r"33 rows", r"33-row", r"44 columns", r"11\.8%",
]
LOCAL_REF = re.compile(r"`([^`]+?\.(?:py|yaml|csv|json|md|pdf|tex|txt))`|\[.*?\]\(([^)]+)\)")


def is_historical(line: str) -> bool:
    lowered = line.lower()
    return any(token in lowered for token in [
        "old", "wrong", "rev-3", "rev-2", "was", "historical",
        "pre-revision", "pre_rev4_1", "comparison_baseline",
        "prior_current_values", "generated comparison",
    ])


def current_facing_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in IGNORE_DIR_PARTS for part in rel_parts):
            continue
        if rel_parts[-1] in {"source_freshness_report.json", "url_check_report.json"}:
            continue
        if rel_parts[:2] == ("archive", "pre_rev4_1"):
            continue
        files.append(path)
    return sorted(files)


def stale_number_check() -> list[str]:
    errors = []
    patterns = [re.compile(p) for p in STALE]
    for path in current_facing_files():
        doc = str(path.relative_to(ROOT))
        in_changelog_history = doc == "CHANGELOG.md"
        in_historical_block = False
        for lineno, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
            if doc == "CANONICAL_CONSTANTS.md" and line.startswith("## Historical Comparison"):
                in_historical_block = True
            if doc == "generated_overlay_totals.yaml" and line.startswith("  prior_current_values_from_addendum:"):
                in_historical_block = True
            if doc == "generated_overlay_totals.yaml" and line.startswith("  expected_post_neocloud_split_only:"):
                in_historical_block = True
            if in_changelog_history or in_historical_block or is_historical(line):
                continue
            for pattern in patterns:
                if pattern.search(line):
                    errors.append(f"{doc}:{lineno}: stale current-facing value `{pattern.pattern}`")
    return errors


def missing_file_check() -> list[str]:
    errors = []
    for path in current_facing_files():
        doc = str(path.relative_to(ROOT))
        if doc == "CHANGELOG.md":
            continue
        in_not_included = False
        for lineno, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
            if "Deliberately not included" in line:
                in_not_included = True
            for match in LOCAL_REF.finditer(line):
                ref = match.group(1) or match.group(2) or ""
                ref = ref.split("#", 1)[0]
                if not ref or ref.startswith(("http", "mailto")) or in_not_included:
                    continue
                if not re.search(r"\.(py|yaml|csv|json|md|pdf|tex|txt)$", ref):
                    continue
                if not (ROOT / ref).exists():
                    errors.append(f"{doc}:{lineno}: missing referenced file `{ref}`")
    return errors


def canonical_overlay_totals_check() -> list[str]:
    result = subprocess.run(
        [sys.executable, "scripts/build_overlay_totals.py", "--check-only", "--check-overlay"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode == 0:
        return []
    output = (result.stdout + result.stderr).strip()
    return [f"canonical overlay totals drift from canonical_capacity_atoms.yaml:\n{output}"]


def main() -> int:
    errors = stale_number_check() + missing_file_check() + canonical_overlay_totals_check()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("regression checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
