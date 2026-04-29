#!/usr/bin/env python3
"""Rev-4.2 prose discipline gate.

Scans current-facing Markdown, TeX, and YAML files for phrases that make
stronger methodological claims than the evidence layer supports.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {".md", ".tex", ".yaml", ".yml"}
IGNORE_DIRS = {".git", ".claude", "__pycache__", "archive"}
IGNORE_FILES = {"docs/research/_template.md"}

BANNED: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"physically[\s-]evidenced floor", re.IGNORECASE), "T1+T2 site-corroborated subtotal"),
    (re.compile(r"31\.45\s+GW\s+physically\s+evidenced", re.IGNORECASE), "31.45 GW Epoch site-level current+planned (T1+T2+T4+T5 mix)"),
    (re.compile(r"disclosed floor", re.IGNORECASE), "sovereign stretch annex"),
    (re.compile(r"\bcapex commitment\b", re.IGNORECASE), "capex envelope"),
    (re.compile(r"\bcommitted capex\b", re.IGNORECASE), "announced capex"),
    (re.compile(r"full-realization ceiling", re.IGNORECASE), "row-uncertainty high envelope"),
    (re.compile(r"end of Q2 2026", re.IGNORECASE), "as of 2026-04-28"),
]


def current_facing_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        rel = path.relative_to(ROOT)
        if str(rel) in IGNORE_FILES:
            continue
        if any(part in IGNORE_DIRS for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    errors: list[str] = []
    for path in current_facing_files():
        rel = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
            for pattern, replacement in BANNED:
                match = pattern.search(line)
                if match:
                    errors.append(f"{rel}:{lineno}: banned phrase `{match.group(0)}`; use `{replacement}`")

    if errors:
        print("PROSE DISCIPLINE GATE FAILED")
        for error in errors:
            print(error)
        return 1

    print("prose discipline gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
