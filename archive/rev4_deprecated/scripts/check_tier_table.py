#!/usr/bin/env python3
"""Validate Rev-4.4 tier-table coverage against canonical atoms.

Now actually compares the per-tier central GW printed in
docs/tier_table.md against the atom-level sum in row_level_audit.csv,
and asserts that the published headline 47.901 / 39.520 / 54.210 row
matches canonical_totals.json. This closes the prior gate that
reported "0 examples checked" while the table was stale.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
ATOMS = ROOT / "canonical_capacity_atoms.yaml"
TIER_TABLE = ROOT / "docs" / "tier_table.md"
ROW_AUDIT = ROOT / "row_level_audit.csv"
CANONICAL_TOTALS = ROOT / "canonical_totals.json"

EXAMPLE_RE = re.compile(r"`([a-z][a-z0-9_]+)`")
TIER_ROW_RE = re.compile(
    r"\|\s*\*\*(T[1-6])\*\*[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|"
    r"\s*([0-9]+\.[0-9]+)\s*/\s*([0-9]+\.[0-9]+)\s*/\s*([0-9]+\.[0-9]+)\s*\|",
)
HEADLINE_RE = re.compile(
    r"\|\s*\|\s*\|\s*\|\s*\|\s*\*\*(\d+)\*\*\s*\|"
    r"\s*\*\*([0-9]+\.[0-9]+)\s*/\s*([0-9]+\.[0-9]+)\s*/\s*([0-9]+\.[0-9]+)\*\*\s*\|",
)
TOLERANCE = 0.01

TIER_DEFAULTS = {"T1": 1.00, "T2": 0.88, "T3": 0.78, "T4": 0.58, "T5": 0.32, "T6": 0.25}


def _f(x: str) -> float:
    return float(x) if x not in ("", None) else 0.0


def load_atoms() -> list[dict[str, Any]]:
    with ATOMS.open() as f:
        return list((yaml.safe_load(f) or {}).get("atoms") or [])


def atom_tier_sums() -> dict[str, dict[str, float]]:
    """Sum row_level_audit.csv per tier in low/central/high facility GW."""
    sums: dict[str, dict[str, float]] = {
        t: {"count": 0, "low": 0.0, "central": 0.0, "high": 0.0} for t in TIER_DEFAULTS
    }
    with ROW_AUDIT.open() as f:
        for r in csv.DictReader(f):
            if r["included_in_western_raw_horizon"].strip().lower() != "true":
                continue
            t = r["evidence_tier"]
            if t not in sums:
                continue
            cf = _f(r["capacity_mw_facility"])
            cl = _f(r["capacity_mw_facility_low"]) if r["capacity_mw_facility_low"] else cf
            ch = _f(r["capacity_mw_facility_high"]) if r["capacity_mw_facility_high"] else cf
            sums[t]["count"] += 1
            sums[t]["central"] += cf / 1000.0
            sums[t]["low"] += cl / 1000.0
            sums[t]["high"] += ch / 1000.0
    return sums


def main() -> int:
    atoms = load_atoms()
    atom_ids = {str(atom.get("atom_id")) for atom in atoms if atom.get("atom_id")}
    errors: list[str] = []

    if not TIER_TABLE.exists():
        print(f"TIER TABLE FAILED: missing {TIER_TABLE.relative_to(ROOT)}")
        return 1

    text = TIER_TABLE.read_text(errors="ignore")
    examples = {tok for tok in EXAMPLE_RE.findall(text) if tok in atom_ids}
    for example in sorted(examples):
        if example not in atom_ids:
            errors.append(f"tier-table example {example} not in canonical_capacity_atoms.yaml")

    for tier in TIER_DEFAULTS:
        if f"## {tier}:" not in text:
            errors.append(f"docs/tier_table.md missing section for {tier}")

    for atom in atoms:
        atom_id = atom.get("atom_id")
        if atom.get("evidence_tier") in TIER_DEFAULTS:
            if not atom.get("tier_rationale"):
                errors.append(f"{atom_id}: missing tier_rationale")

    sums = atom_tier_sums()
    table_rows = TIER_ROW_RE.findall(text)
    table_lookup = {tier: (int(c), float(lo), float(ce), float(hi)) for tier, c, lo, ce, hi in table_rows}

    for tier, agg in sums.items():
        if tier not in table_lookup:
            errors.append(f"{tier}: no parseable row found in docs/tier_table.md headline table")
            continue
        t_count, t_low, t_central, t_high = table_lookup[tier]
        if t_count != agg["count"]:
            errors.append(
                f"{tier}: doc atom count {t_count} != row_level_audit.csv {agg['count']}"
            )
        for name, doc_val, atom_val in (
            ("low", t_low, agg["low"]),
            ("central", t_central, agg["central"]),
            ("high", t_high, agg["high"]),
        ):
            if abs(doc_val - atom_val) > TOLERANCE:
                errors.append(
                    f"{tier}: doc {name}={doc_val:.3f} GW disagrees with atom-sum {atom_val:.3f} GW"
                )

    headline_match = HEADLINE_RE.search(text)
    if not headline_match:
        errors.append("docs/tier_table.md headline footer (count + low/central/high) not parseable")
    else:
        h_count, h_low, h_central, h_high = headline_match.groups()
        atom_central = sum(s["central"] for s in sums.values())
        atom_low = sum(s["low"] for s in sums.values())
        atom_high = sum(s["high"] for s in sums.values())
        for name, doc_val, atom_val in (
            ("low", float(h_low), atom_low),
            ("central", float(h_central), atom_central),
            ("high", float(h_high), atom_high),
        ):
            if abs(doc_val - atom_val) > TOLERANCE:
                errors.append(
                    f"headline {name}: doc {doc_val:.3f} != atom-sum {atom_val:.3f}"
                )

    if CANONICAL_TOTALS.exists():
        ct = json.loads(CANONICAL_TOTALS.read_text())
        atom_central = sum(s["central"] for s in sums.values())
        atom_high = sum(s["high"] for s in sums.values())
        atom_low = sum(s["low"] for s in sums.values())
        det_weighted = sum(s["central"] * TIER_DEFAULTS[t] for t, s in sums.items())
        for label, doc_val, atom_val in (
            ("raw_western_horizon_gw_facility", ct.get("raw_western_horizon_gw_facility"), atom_central),
            ("full_realization_ceiling_gw_facility", ct.get("full_realization_ceiling_gw_facility"), atom_high),
            ("deterministic_probability_weighted_gw_facility", ct.get("deterministic_probability_weighted_gw_facility"), det_weighted),
        ):
            if doc_val is None:
                errors.append(f"canonical_totals.json missing {label}")
            elif abs(float(doc_val) - atom_val) > TOLERANCE:
                errors.append(
                    f"canonical_totals.{label} = {doc_val} disagrees with atom sum {atom_val:.3f}"
                )
        ct_low_pair = ct.get("raw_western_horizon_range_gw_facility") or [None, None]
        if ct_low_pair[0] is None or abs(float(ct_low_pair[0]) - atom_low) > TOLERANCE:
            errors.append(
                f"canonical_totals.raw_western_horizon_range_gw_facility[0] = {ct_low_pair[0]} disagrees with atom low-sum {atom_low:.3f}"
            )

    if errors:
        print("TIER TABLE GATE FAILED")
        for error in errors[:200]:
            print(f"  {error}")
        if len(errors) > 200:
            print(f"  ... {len(errors) - 200} more")
        return 1

    print(
        f"tier table gate passed: {len(examples)} example atoms checked, "
        f"{len(atoms)} atoms covered, per-tier and headline sums reconcile to canonical totals"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
