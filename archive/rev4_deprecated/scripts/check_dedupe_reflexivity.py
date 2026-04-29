#!/usr/bin/env python3
"""Check cross-atom dedupe candidate reflexivity.

If atom A declares a cross-overlay candidate atom B, B must declare A. Epoch
site candidates are covered by check_dedupe_coverage.py and are not reflexive.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
ATOMS = ROOT / "canonical_capacity_atoms.yaml"


def load_atoms() -> dict[str, dict[str, Any]]:
    with ATOMS.open() as f:
        rows = (yaml.safe_load(f) or {}).get("atoms") or []
    return {str(row.get("atom_id")): row for row in rows if row.get("atom_id")}


def declared_cross_candidates(atom: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    for candidate in atom.get("cross_overlay_overlap_candidates") or []:
        if isinstance(candidate, dict):
            value = candidate.get("atom_id") or candidate.get("overlay_atom_id")
        else:
            value = candidate
        if value:
            out.add(str(value))
    return out


def main() -> int:
    atoms = load_atoms()
    edges: set[tuple[str, str]] = set()
    for atom_id, atom in atoms.items():
        for other in declared_cross_candidates(atom):
            edges.add((atom_id, other))

    errors: list[str] = []
    for left, right in sorted(edges):
        if right not in atoms:
            errors.append(f"{left}: cross-overlay candidate {right} is not a known atom_id")
            continue
        if (right, left) not in edges:
            errors.append(f"{left} lists {right}, but {right} does not list {left}")

    if errors:
        print("DEDUPE REFLEXIVITY FAILED")
        for error in errors:
            print(f"  {error}")
        return 1

    print(f"dedupe reflexivity gate passed: {len(edges)} directed cross-atom links checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
