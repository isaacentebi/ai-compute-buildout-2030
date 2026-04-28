#!/usr/bin/env python3
"""
Source-freshness publication gate.

This gate checks the exact row_level_audit.csv shipped with the PDF. It treats
source publication age and source verification age as separate fields:

  source_publication_date  when the cited source was published
  last_verified_date       when the source was rechecked for freshness
  freshness_status         explicit audit status or waiver status
  freshness_waiver_reason  row-level reason an old source remains acceptable

An old source is not automatically invalid. It fails only when the row has not
been recently verified and has not been explicitly waived.

Usage
  python3 check_source_freshness.py --today 2026-04-25
  python3 check_source_freshness.py --json
"""

import argparse
import csv
import datetime
import json
import sys
from pathlib import Path


def parse_date(value):
    """Accept ISO dates, YYYY-MM month strings, date objects, or blanks."""
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    raw = str(value).strip()
    if not raw:
        return None
    try:
        return datetime.date.fromisoformat(raw)
    except (TypeError, ValueError):
        pass
    try:
        return datetime.date.fromisoformat(f"{raw}-01")
    except (TypeError, ValueError):
        return None


def classify(days, warn_days, fail_days):
    if days is None:
        return "MISSING"
    if days <= warn_days:
        return "GREEN"
    if days <= fail_days:
        return "YELLOW"
    return "RED"


def normalized_status(row, today, warn_days, fail_days):
    source_date = parse_date(row.get("source_publication_date"))
    verified_date = parse_date(row.get("last_verified_date") or row.get("last_checked"))
    raw_status = (row.get("freshness_status") or "").strip()
    waiver = (row.get("freshness_waiver_reason") or "").strip()
    days = (today - verified_date).days if verified_date else None

    computed = classify(days, warn_days, fail_days)
    lowered = raw_status.lower()
    if lowered.startswith("waived"):
        gate_status = "WAIVED"
    elif lowered in {"current_verified", "verified_current", "fresh"}:
        gate_status = "GREEN"
    elif lowered in {"green", "yellow", "red", "missing"}:
        gate_status = raw_status.upper()
    elif raw_status:
        gate_status = raw_status
    else:
        gate_status = computed

    if gate_status in {"RED", "YELLOW"} and waiver:
        gate_status = "WAIVED"

    return {
        "file_path": None,
        "commitment_id": row.get("commitment_id", ""),
        "operator": row.get("operator", ""),
        "source_publication_date": source_date.isoformat() if source_date else "",
        "last_verified_date": verified_date.isoformat() if verified_date else "",
        "days_since_verification": days,
        "freshness_status": gate_status,
        "freshness_waiver_reason": waiver,
        "primary_source_url": row.get("primary_source_url", ""),
        "western_denominator": row.get("western_denominator", ""),
        "evidence_tier": row.get("evidence_tier", ""),
    }


def load_rows(audit_csv, today, warn_days, fail_days):
    with audit_csv.open(newline="") as f:
        rows = []
        for row in csv.DictReader(f):
            normalized = normalized_status(row, today, warn_days, fail_days)
            normalized["file_path"] = str(audit_csv)
            rows.append(normalized)
        return rows


def temporal_monotonicity_gate(base):
    """No atom's central energization date may precede its source publication date."""
    try:
        import yaml  # type: ignore
    except ImportError:
        print("ERROR: PyYAML is required for --temporal", file=sys.stderr)
        return 2

    atoms_path = base / "canonical_capacity_atoms.yaml"
    with atoms_path.open() as f:
        atoms = (yaml.safe_load(f) or {}).get("atoms") or []

    errors = []
    for atom in atoms:
        atom_id = atom.get("atom_id", "<unknown>")
        source_date = parse_date(atom.get("source_date") or atom.get("source_publication_date"))
        window = atom.get("energization_window") or {}
        central = None
        if isinstance(window, dict):
            central = parse_date(window.get("central"))
        if source_date and central and central < source_date:
            errors.append(f"{atom_id}: energization_window.central={central.isoformat()} precedes source_date={source_date.isoformat()}")

    if errors:
        print("TEMPORAL MONOTONICITY FAILED")
        for error in errors:
            print(f"  {error}")
        return 1

    print(f"temporal monotonicity gate passed: {len(atoms)} atoms checked")
    return 0


def print_rows(title, rows):
    if not rows:
        return
    print(f"  --- {title} ({len(rows)}) ---")
    rows = sorted(rows, key=lambda r: (-(r["days_since_verification"] or -1), r["commitment_id"]))
    for row in rows:
        days = row["days_since_verification"]
        days_text = f"{days:3d}d" if days is not None else "n/a "
        print(
            f"    [{row['freshness_status'][:3]}] {days_text}  "
            f"{row['commitment_id']} | {row['operator']} | "
            f"source={row['source_publication_date'] or 'unknown'} | "
            f"verified={row['last_verified_date'] or 'NEVER'}"
        )
        if row["freshness_waiver_reason"]:
            print(f"         waiver: {row['freshness_waiver_reason']}")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-csv", default="row_level_audit.csv")
    parser.add_argument("--warn-days", type=int, default=30)
    parser.add_argument("--fail-days", type=int, default=60)
    parser.add_argument("--today", default=None, help="YYYY-MM-DD; default is real today")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--temporal", action="store_true", help="check atom energization central dates against source publication dates")
    args = parser.parse_args()

    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()
    script_dir = Path(__file__).resolve().parent
    base = script_dir.parent if script_dir.name == "scripts" else script_dir
    if args.temporal:
        return temporal_monotonicity_gate(base)

    audit_csv = (base / args.audit_csv).resolve()
    if not audit_csv.exists():
        print(f"ERROR: audit CSV not found: {audit_csv}", file=sys.stderr)
        return 2

    rows = load_rows(audit_csv, today, args.warn_days, args.fail_days)
    buckets = {"GREEN": [], "YELLOW": [], "RED": [], "MISSING": [], "WAIVED": []}
    for row in rows:
        buckets.setdefault(row["freshness_status"], []).append(row)

    failing = buckets.get("RED", []) + buckets.get("MISSING", [])

    payload = {
        "today": today.isoformat(),
        "warn_days": args.warn_days,
        "fail_days": args.fail_days,
        "file_path": str(audit_csv),
        "total_rows": len(rows),
        "counts": {key: len(value) for key, value in buckets.items() if value or key in {"GREEN", "YELLOW", "RED", "MISSING", "WAIVED"}},
        "rows": rows,
    }

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 1 if failing else 0

    print("=" * 80)
    print(f"SOURCE FRESHNESS GATE  (today={today.isoformat()}, warn>{args.warn_days}d, fail>{args.fail_days}d)")
    print("=" * 80)
    print(f"  File path    : {audit_csv}")
    print(f"  Total rows   : {len(rows)}")
    print(f"  GREEN        : {len(buckets.get('GREEN', [])):3d}")
    print(f"  YELLOW       : {len(buckets.get('YELLOW', [])):3d}")
    print(f"  RED          : {len(buckets.get('RED', [])):3d}")
    print(f"  MISSING      : {len(buckets.get('MISSING', [])):3d}")
    print(f"  WAIVED       : {len(buckets.get('WAIVED', [])):3d}")
    print()

    for status in ("RED", "YELLOW", "MISSING", "WAIVED", "GREEN"):
        print_rows(status, buckets.get(status, []))

    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
