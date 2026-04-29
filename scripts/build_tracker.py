#!/usr/bin/env python3
"""Build the tracker.

Combines the latest Epoch snapshot (epoch_data_centers/compiled.json) with
the small hand-curated overlay.csv into a single tracker.csv (machine) and
tracker.md (human, four-bucket view).

Replaces the prior atom-database / overlay-yaml / Monte-Carlo machinery.
"""

from __future__ import annotations
import csv, json, sys, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPOCH_JSON = ROOT / "epoch_data_centers" / "compiled.json"
OVERLAY_CSV = ROOT / "overlay.csv"
TRACKER_CSV = ROOT / "tracker.csv"
TRACKER_MD = ROOT / "tracker.md"

# Sites Epoch tracks but we exclude from Western (China; sovereign-only)
EXCLUDED_FROM_WESTERN = {
    "Alibaba Zhangbei",  # China — out of scope
}
SOVEREIGN_FROM_EPOCH = {
    "OpenAI Stargate UAE",  # UAE; sovereign sidebar, not Western
}


def epoch_status(site_name: str, site: dict) -> str:
    """Map Epoch site to bucket. Operational if any current MW; otherwise under_construction."""
    cur_mw = site.get("current_power_mw") or 0
    if cur_mw and cur_mw > 0:
        # If there's also a buildout remainder, we'll generate two rows
        return "operational"
    return "under_construction"


def epoch_iso_from_country(country: str, name: str) -> str:
    """Quick ISO/grid inference from site name keywords; fall back to country."""
    s = (name or "").lower()
    rules = [
        ("wisconsin", "MISO"), ("mt pleasant", "MISO"), ("madison", "MISO-S"),
        ("ridgeland", "MISO-S"), ("new carlisle", "MISO"),
        ("cedar rapids", "MISO"), ("council bluffs", "MISO"),
        ("omaha", "SPP"), ("pryor", "SPP"), ("goodnight", "ERCOT"),
        ("new mexico", "non-ISO NM"), ("shackelford", "ERCOT"),
        ("milam", "ERCOT"), ("abilene", "ERCOT"), ("tx1", "ERCOT"),
        ("phoenix", "WECC"), ("michigan", "MISO"), ("temple", "ERCOT"),
        ("prometheus", "PJM"), ("hyperion", "MISO-S"), ("richland", "MISO-S"),
        ("lake mariner", "NYISO"), ("memphis", "TVA"), ("colossus", "TVA"),
        ("cheyenne", "WECC"), ("goodyear", "WECC"), ("richmond", "PJM"),
        ("nva02", "PJM"), ("new albany", "PJM"), ("atlanta", "SERC"),
        ("fort wayne", "MISO"), ("kuna", "WECC"), ("sines", "REE Iberian"),
    ]
    for k, v in rules:
        if k in s:
            return v
    return country or "—"


def _f(x):
    try:
        return float(x) if x not in ("", None) else 0.0
    except Exception:
        return 0.0


def epoch_buildout_year(site: dict) -> str:
    """Pull buildout completion year from Epoch's full_buildout block."""
    fb = site.get("full_buildout") or {}
    end = fb.get("end_of_timeline") or fb.get("date") or ""
    m = re.match(r"(\d{4})", str(end))
    return m.group(1) if m else "?"


def make_epoch_rows() -> list[dict]:
    if not EPOCH_JSON.exists():
        print(f"[!] {EPOCH_JSON} missing — run scripts/refresh_epoch.sh first", file=sys.stderr)
        return []
    data = json.loads(EPOCH_JSON.read_text())
    rows = []
    for s in data.get("sites", []):
        name = s.get("name") or ""
        if name in EXCLUDED_FROM_WESTERN:
            continue
        cur_mw = _f(s.get("current_power_mw"))
        bo_mw = _f((s.get("full_buildout") or {}).get("power_mw_max"))
        owner = s.get("owner") or "—"
        users = s.get("users") or "—"
        country = s.get("country") or "—"
        proj = s.get("project") or ""
        # confidence tag (Epoch's own)
        conf = ""
        for tag in re.findall(r"#\w+", f"{proj} {users}"):
            conf = tag
            break
        notes = f"Epoch site; project={proj or 'n/a'}"
        scope = "sovereign" if name in SOVEREIGN_FROM_EPOCH else "western"
        # Operational slice
        if cur_mw > 0:
            rows.append({
                "id": "epoch_" + re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") + "_op",
                "status": "operational",
                "site": name, "country": country,
                "region_iso": epoch_iso_from_country(country, name),
                "operator": owner, "anchor_tenant": users,
                "gw_facility": round(cur_mw / 1000, 4),
                "gw_facility_low": round(cur_mw / 1000, 4),
                "gw_facility_high": round(cur_mw / 1000, 4),
                "basis": "facility",
                "online_year": "op.",
                "source": "Epoch AI Frontier Data Centers",
                "source_url": "https://epoch.ai/data/data-centers",
                "source_date": data.get("source", {}).get("dataset_updated", "2026-04-28"),
                "last_checked": data.get("source", {}).get("retrieved", "2026-04-29"),
                "notes": f"{notes} [{conf}] [scope={scope}]",
            })
        # Buildout-remaining slice (only the delta beyond current)
        remaining = bo_mw - cur_mw
        if remaining > 5:  # >5 MW; skip noise
            yr = epoch_buildout_year(s)
            rows.append({
                "id": "epoch_" + re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") + "_bo",
                "status": "under_construction",
                "site": name, "country": country,
                "region_iso": epoch_iso_from_country(country, name),
                "operator": owner, "anchor_tenant": users,
                "gw_facility": round(remaining / 1000, 4),
                "gw_facility_low": round(remaining / 1000, 4),
                "gw_facility_high": round(remaining / 1000, 4),
                "basis": "facility",
                "online_year": yr,
                "source": "Epoch AI Frontier Data Centers",
                "source_url": "https://epoch.ai/data/data-centers",
                "source_date": data.get("source", {}).get("dataset_updated", "2026-04-28"),
                "last_checked": data.get("source", {}).get("retrieved", "2026-04-29"),
                "notes": f"{notes} [{conf}] [scope={scope}]",
            })
    return rows


def load_overlay() -> list[dict]:
    if not OVERLAY_CSV.exists():
        return []
    rows = []
    with OVERLAY_CSV.open() as f:
        for r in csv.DictReader(f):
            for k in ("gw_facility", "gw_facility_low", "gw_facility_high"):
                r[k] = _f(r[k])
            # Mark scope from sovereign cues in id/notes/region
            scope = "sovereign" if any(
                tok in (r.get("notes", "") + r.get("region_iso", "") + r.get("id", "")).lower()
                for tok in ("sovereign", "uae", "saudi", "humain", "reliance",
                            "culham", "vizag", "visakhapatnam", "andhra", "jamnagar",
                            "ewec", "srpc", "wrpc", "g42", "khazna", "amd_france",
                            "hannover", "eu_")
            ) else "western"
            r["_scope"] = scope
            rows.append(r)
    return rows


def main() -> int:
    epoch = make_epoch_rows()
    overlay = load_overlay()
    rows = epoch + overlay

    # Inject _scope on epoch rows from notes
    for r in epoch:
        r["_scope"] = "sovereign" if "scope=sovereign" in r["notes"] else "western"

    # Write tracker.csv (one row per item)
    cols = ["id", "status", "site", "country", "region_iso", "operator",
            "anchor_tenant", "gw_facility", "gw_facility_low", "gw_facility_high",
            "basis", "online_year", "source", "source_url", "source_date",
            "last_checked", "notes"]
    with TRACKER_CSV.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})

    # Aggregate per bucket
    buckets = ["operational", "under_construction", "contracted", "announced", "canceled"]
    by_bucket = {b: {"western": [], "sovereign": []} for b in buckets}
    for r in rows:
        scope = r.get("_scope", "western")
        b = r["status"]
        if b in by_bucket:
            by_bucket[b][scope].append(r)

    def total(rs):
        return sum(_f(r["gw_facility"]) for r in rs)

    # Write tracker.md
    with TRACKER_MD.open("w") as f:
        f.write("# AI Compute Build-Out — Tracker\n\n")
        f.write("Last refreshed from Epoch: 2026-04-28 snapshot. Overlay last revised: 2026-04-29.\n\n")
        f.write("This is a tracker, not a forecast. Each row is a real capacity claim with a real source. ")
        f.write("Four buckets describe the lifecycle stage: **operational** (energized today), ")
        f.write("**under construction** (named site + dated buildout/permit/utility), ")
        f.write("**contracted** (counterparty + capacity disclosed via 10-K / lease / take-or-pay), ")
        f.write("**announced** (\"up to N GW\" headline without contracted basis or named site).\n\n")
        f.write("Sovereign sidebar items (UAE / Saudi / India / UK / EU / Asia) are reported separately and ")
        f.write("not added to the Western total.\n\n")

        # Headline totals
        f.write("## Totals (GW facility)\n\n")
        f.write("| Bucket | Western atoms | Western GW | Sovereign atoms | Sovereign GW |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for b in buckets:
            wn = len(by_bucket[b]["western"]); wg = total(by_bucket[b]["western"])
            sn = len(by_bucket[b]["sovereign"]); sg = total(by_bucket[b]["sovereign"])
            label = b.replace("_", " ").title()
            f.write(f"| {label} | {wn} | {wg:.3f} | {sn} | {sg:.3f} |\n")
        wtot = sum(total(by_bucket[b]["western"]) for b in buckets if b != "canceled")
        stot = sum(total(by_bucket[b]["sovereign"]) for b in buckets if b != "canceled")
        f.write(f"| **Total (ex-canceled)** |  | **{wtot:.3f}** |  | **{stot:.3f}** |\n\n")
        f.write("---\n\n")

        # Per bucket
        bucket_titles = {
            "operational": "1. Operational today",
            "under_construction": "2. Under construction (named site + dated buildout / permit)",
            "contracted": "3. Contracted (counterparty + capacity, site mapping may be incomplete)",
            "announced": "4. Announced (headline only — no contract or named site)",
            "canceled": "5. Canceled / paused",
        }
        for b in buckets:
            f.write(f"## {bucket_titles[b]}\n\n")
            for scope_label, scope_key in [("Western", "western"), ("Sovereign sidebar", "sovereign")]:
                items = sorted(by_bucket[b][scope_key], key=lambda r: -_f(r["gw_facility"]))
                if not items:
                    continue
                f.write(f"### {scope_label} — {len(items)} items, {total(items):.3f} GW facility\n\n")
                f.write("| Site | Operator | Anchor | GW (low / central / high) | Online | Source |\n")
                f.write("|---|---|---|---:|:---:|---|\n")
                for r in items:
                    gw = _f(r["gw_facility"])
                    lo = _f(r["gw_facility_low"]) or gw
                    hi = _f(r["gw_facility_high"]) or gw
                    rng = (f"{gw:.3f}" if abs(lo - gw) < 1e-6 and abs(hi - gw) < 1e-6
                           else f"{lo:.2f} / {gw:.3f} / {hi:.2f}")
                    src = r.get("source") or ""
                    url = r.get("source_url") or ""
                    src_link = f"[{src}]({url})" if url else src
                    site = (r.get("site") or "")[:55]
                    op = r.get("operator") or "—"
                    anch = (r.get("anchor_tenant") or "—")[:32]
                    f.write(f"| {site} | {op} | {anch} | {rng} | {r.get('online_year','')} | {src_link} |\n")
                f.write("\n")

    print(f"Wrote {TRACKER_CSV.relative_to(ROOT)}: {len(rows)} rows ({len(epoch)} Epoch + {len(overlay)} overlay)")
    print(f"Wrote {TRACKER_MD.relative_to(ROOT)}")
    print()
    print("Headline totals (GW facility, ex-canceled):")
    for b in buckets:
        if b == "canceled":
            continue
        wg = total(by_bucket[b]["western"])
        sg = total(by_bucket[b]["sovereign"])
        print(f"  {b:>20}: Western {wg:.3f} GW | Sovereign {sg:.3f} GW")
    print(f"  {'TOTAL':>20}: Western {wtot:.3f} GW | Sovereign {stot:.3f} GW")
    return 0


if __name__ == "__main__":
    sys.exit(main())
