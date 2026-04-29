#!/usr/bin/env python3
"""Ensure every atom-declared Epoch overlap candidate is represented in dedupe_audit.csv."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
ATOMS = ROOT / "canonical_capacity_atoms.yaml"
DEDUPE = ROOT / "dedupe_audit.csv"


def load_atoms() -> list[dict[str, Any]]:
    with ATOMS.open() as f:
        return list((yaml.safe_load(f) or {}).get("atoms") or [])


def candidate_site(candidate: Any) -> str:
    if isinstance(candidate, dict):
        return str(candidate.get("epoch_site") or candidate.get("epoch_site_id") or "").strip()
    return str(candidate).strip()


def main() -> int:
    atoms = load_atoms()
    flagged: set[tuple[str, str]] = set()
    for atom in atoms:
        atom_id = str(atom.get("atom_id") or "")
        for candidate in atom.get("epoch_overlap_candidates") or []:
            site = candidate_site(candidate)
            if atom_id and site:
                flagged.add((atom_id, site))

    if not flagged:
        print("dedupe coverage gate passed: no atom-level overlap candidates declared yet")
        return 0

    if not DEDUPE.exists():
        print(f"DEDUPE COVERAGE FAILED: {DEDUPE.relative_to(ROOT)} is missing")
        return 1

    covered: set[tuple[str, str]] = set()
    with DEDUPE.open(newline="") as f:
        for row in csv.DictReader(f):
            atom_id = (row.get("overlay_atom_id") or "").strip()
            site = (row.get("epoch_site_id") or row.get("epoch_site") or "").strip()
            if atom_id and site:
                covered.add((atom_id, site))

    missing = sorted(flagged - covered)
    if missing:
        print("DEDUPE COVERAGE FAILED")
        for atom_id, site in missing:
            print(f"  {atom_id}: missing dedupe_audit.csv row for {site}")
        return 1

    print(f"dedupe coverage gate passed: {len(flagged)} candidate rows covered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
