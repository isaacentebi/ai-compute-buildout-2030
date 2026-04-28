#!/usr/bin/env python3
"""Rev-4.1 regression checks for stale numbers and missing bundle files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = [
    "README.md",
    "PROMPT.md",
    "MANIFEST.md",
    "report.tex",
    "CHANGELOG.md",
    "CONFIDENCE_DECOMPOSITION.md",
]
STALE = [r"51\.9", r"51\.93", r"50\.62", r"31\.8", r"31\.5", r"36\.8", r"55\.3", r"53\.48", r"37-page"]
LOCAL_REF = re.compile(r"`([^`]+?\.(?:py|yaml|csv|json|md|pdf|tex|txt))`|\[.*?\]\(([^)]+)\)")


def is_historical(line: str) -> bool:
    lowered = line.lower()
    return any(token in lowered for token in ["old", "rev-3", "rev-2", "was", "historical", "pre-revision"])


def stale_number_check() -> list[str]:
    errors = []
    patterns = [re.compile(p) for p in STALE]
    for doc in DOCS:
        if doc == "CHANGELOG.md":
            continue
        path = ROOT / doc
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
            if doc == "CHANGELOG.md" and is_historical(line):
                continue
            for pattern in patterns:
                if pattern.search(line):
                    errors.append(f"{doc}:{lineno}: stale current-facing value `{pattern.pattern}`")
    return errors


def missing_file_check() -> list[str]:
    errors = []
    for doc in DOCS:
        if doc == "CHANGELOG.md":
            continue
        path = ROOT / doc
        if not path.exists():
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


def main() -> int:
    errors = stale_number_check() + missing_file_check()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("regression checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
