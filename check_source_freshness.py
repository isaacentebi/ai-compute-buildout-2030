#!/usr/bin/env python3
"""
Source-freshness linter.

Walks compute_commitments_overlay.yaml (row_audit block) and neocloud_overlay.yaml
(per-row as_of_date), computing days since last_checked / as_of_date against today.

Flags:
  GREEN  — stale ≤ 30 days
  YELLOW — 31–60 days
  RED    — 61+ days
  MISSING — no last_checked / as_of_date field

This is a staleness check, not a re-fetch tool. It tells you which rows need
manual source re-verification; it does not re-pull the underlying sources.

Usage
  python3 check_source_freshness.py [--warn-days 30] [--fail-days 60]
  python3 check_source_freshness.py --json            # machine-readable output
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(2)


def parse_date(s):
    """Accept datetime.date, ISO string, or None."""
    if s is None:
        return None
    if isinstance(s, datetime.date):
        return s
    if isinstance(s, datetime.datetime):
        return s.date()
    try:
        return datetime.date.fromisoformat(str(s))
    except (ValueError, TypeError):
        return None


def classify(days, warn_days, fail_days):
    if days is None:
        return "MISSING"
    if days <= warn_days:
        return "GREEN"
    if days <= fail_days:
        return "YELLOW"
    return "RED"


def collect_rows(overlay_path, neocloud_path, today):
    rows = []

    # Class A / B / C commitments — last_checked sits in row_audit block
    with open(overlay_path) as f:
        ov = yaml.safe_load(f)
    row_audit = ov.get("row_audit", {}) or {}
    for bucket in ("commitments", "chip_procurement_commitments", "dollar_only_commitments"):
        for c in ov.get(bucket, []):
            cid = c["commitment_id"]
            aud = row_audit.get(cid, {}) or {}
            lc = parse_date(aud.get("last_checked"))
            # fall back to announced_date as weak signal
            announced = parse_date(c.get("announced_date"))
            days = (today - lc).days if lc else None
            rows.append({
                "source_file": "compute_commitments_overlay.yaml",
                "commitment_id": cid,
                "bucket": bucket,
                "last_checked": lc.isoformat() if lc else None,
                "days_stale": days,
                "announced_date": announced.isoformat() if announced else None,
            })

    # Neocloud rows — as_of_date per operator
    with open(neocloud_path) as f:
        nc = yaml.safe_load(f)
    for op in nc.get("neoclouds", []):
        aod = parse_date(op.get("as_of_date"))
        days = (today - aod).days if aod else None
        rows.append({
            "source_file": "neocloud_overlay.yaml",
            "commitment_id": f"neocloud_{op.get('neocloud','unknown').lower().replace(' ','_')}",
            "bucket": "neocloud",
            "last_checked": aod.isoformat() if aod else None,
            "days_stale": days,
            "announced_date": None,
        })

    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--warn-days", type=int, default=30)
    ap.add_argument("--fail-days", type=int, default=60)
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    ap.add_argument("--overlay", default="compute_commitments_overlay.yaml")
    ap.add_argument("--neocloud", default="neocloud_overlay.yaml")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (default: real today)")
    args = ap.parse_args()

    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()

    base = Path(__file__).resolve().parent
    rows = collect_rows(base / args.overlay, base / args.neocloud, today)

    for r in rows:
        r["status"] = classify(r["days_stale"], args.warn_days, args.fail_days)

    buckets = {"GREEN": [], "YELLOW": [], "RED": [], "MISSING": []}
    for r in rows:
        buckets[r["status"]].append(r)

    if args.json:
        print(json.dumps({
            "today": today.isoformat(),
            "warn_days": args.warn_days,
            "fail_days": args.fail_days,
            "total_rows": len(rows),
            "counts": {k: len(v) for k, v in buckets.items()},
            "rows": rows,
        }, indent=2))
        return 0

    print("=" * 72)
    print(f"SOURCE FRESHNESS  (today={today.isoformat()}, warn>{args.warn_days}d, fail>{args.fail_days}d)")
    print("=" * 72)
    print(f"  Total rows   : {len(rows)}")
    print(f"  GREEN   (≤{args.warn_days}d)  : {len(buckets['GREEN']):3d}")
    print(f"  YELLOW  ({args.warn_days+1}–{args.fail_days}d)    : {len(buckets['YELLOW']):3d}")
    print(f"  RED     (>{args.fail_days}d)    : {len(buckets['RED']):3d}")
    print(f"  MISSING last_checked : {len(buckets['MISSING']):3d}")
    print()

    for status in ("RED", "YELLOW", "MISSING", "GREEN"):
        group = buckets[status]
        if not group:
            continue
        print(f"  --- {status} ({len(group)}) ---")
        # Sort by days_stale desc (None last)
        group.sort(key=lambda r: (-(r["days_stale"] or -1)))
        for r in group:
            days = r["days_stale"]
            days_str = f"{days:3d}d" if days is not None else "n/a "
            lc = r["last_checked"] or "NEVER"
            print(f"    [{status[:3]}] {days_str} since {lc}  {r['commitment_id']}")
        print()

    # Exit code: 0 if clean, 1 if RED or MISSING exists
    if buckets["RED"] or buckets["MISSING"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
