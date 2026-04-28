#!/usr/bin/env python3
"""Validate Rev-4.2 tier-table coverage against canonical atoms."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
ATOMS = ROOT / "canonical_capacity_atoms.yaml"
TIER_TABLE = ROOT / "docs" / "tier_table.md"
EXAMPLE_RE = re.compile(r"atom:([A-Za-z0-9_.-]+)")


def load_atoms() -> list[dict[str, Any]]:
    with ATOMS.open() as f:
        return list((yaml.safe_load(f) or {}).get("atoms") or [])


def main() -> int:
    atoms = load_atoms()
    atom_ids = {str(atom.get("atom_id")) for atom in atoms if atom.get("atom_id")}
    errors: list[str] = []

    if not TIER_TABLE.exists():
        print(f"TIER TABLE FAILED: missing {TIER_TABLE.relative_to(ROOT)}")
        return 1

    text = TIER_TABLE.read_text(errors="ignore")
    examples = set(EXAMPLE_RE.findall(text))
    for example in sorted(examples):
        if example not in atom_ids:
            errors.append(f"tier-table example atom:{example} is not in canonical_capacity_atoms.yaml")

    for tier in ("T1", "T2", "T3", "T4", "T5", "T6"):
        if f"## {tier}:" not in text:
            errors.append(f"docs/tier_table.md missing section for {tier}")

    for atom in atoms:
        atom_id = atom.get("atom_id")
        if atom.get("evidence_tier") in {"T1", "T2", "T3", "T4", "T5", "T6"}:
            if not atom.get("tier_rationale"):
                errors.append(f"{atom_id}: missing tier_rationale")

    if errors:
        print("TIER TABLE GATE FAILED")
        for error in errors[:200]:
            print(f"  {error}")
        if len(errors) > 200:
            print(f"  ... {len(errors) - 200} more")
        return 1

    print(f"tier table gate passed: {len(examples)} examples checked, {len(atoms)} atoms covered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
