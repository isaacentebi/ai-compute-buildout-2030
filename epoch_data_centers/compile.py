#!/usr/bin/env python3
"""
Compile Epoch AI Frontier Data Centers dataset (v2 — correct timeline logic).

Source: https://epoch.ai/data/data-centers
Files:  data_centers.csv, data_center_timelines.csv
Dataset updated: 2026-04-28  /  Retrieved: 2026-04-29  /  License: CC BY 4.0
"""
from __future__ import annotations
import csv, json
from collections import defaultdict
from pathlib import Path
from datetime import date, timedelta

ROOT = Path(__file__).parent
TODAY = date(2026, 4, 29)

# Epoch methodology: "theoretical peak capacity ... typically about
# one third of that, due to inefficiencies" -> ~33% utilization factor.
UTIL_FACTOR = 1.0 / 3.0

# ---------- helpers ----------
def f2(x):
    if x is None or x == "": return None
    try: return float(x)
    except ValueError: return None

def clean_tag(s):
    if not s: return ""
    parts = [p.strip() for p in s.split(",")]
    out = []
    for p in parts:
        bits = [b for b in p.split() if not b.startswith("#")]
        out.append(" ".join(bits).strip())
    return ", ".join([c for c in out if c])

# ---------- load ----------
sites = []
with (ROOT / "data_centers.csv").open() as f:
    for row in csv.DictReader(f):
        sites.append(row)

timelines = []
with (ROOT / "data_center_timelines.csv").open() as f:
    for row in csv.DictReader(f):
        timelines.append(row)

# ---------- Build per-site time series (forward-filled) ----------
per_site = defaultdict(list)
for t in timelines:
    per_site[t["Data center"]].append(t)

# Sort each site's rows by date.
for s in per_site:
    per_site[s].sort(key=lambda r: r["Date"])

# Per-site milestones:
#   first_operational_date: first timeline row where (H100e > 0 or
#     Buildings operational > 0 or Power (MW) > 0)
#   current_as_of_today: forward-fill values at TODAY
#   full_buildout: last row in the timeline (future-dated if forecasted)
def snapshot(site_rows, at_date):
    """Return forward-filled snapshot of power/h100e/bldgs/capex at at_date."""
    last = {"power_mw": 0.0, "h100e": 0.0, "bldgs_op": 0.0,
            "capex_usd_b": 0.0, "status_text": "",
            "last_update": None}
    for r in site_rows:
        if date.fromisoformat(r["Date"]) > at_date:
            break
        last["power_mw"]    = f2(r["Power (MW)"])              or last["power_mw"]
        last["h100e"]       = f2(r["H100 equivalents"])        or last["h100e"]
        last["bldgs_op"]    = f2(r["Buildings operational"])   or last["bldgs_op"]
        last["capex_usd_b"] = f2(r["Total capital cost (2025 USD billions)"]) or last["capex_usd_b"]
        last["status_text"] = r["Construction status"]         or last["status_text"]
        last["last_update"] = r["Date"]
    return last

def first_operational(site_rows):
    """First date where any physical capacity comes online."""
    for r in site_rows:
        if (f2(r["H100 equivalents"]) or 0) > 0 or \
           (f2(r["Buildings operational"]) or 0) > 0 or \
           (f2(r["Power (MW)"]) or 0) > 0:
            return r["Date"]
    return None

def full_buildout(site_rows):
    """Max H100e / MW / capex across whole timeline (= planned endstate)."""
    mxh = mxp = mxc = 0.0
    end_date = None
    for r in site_rows:
        mxh = max(mxh, f2(r["H100 equivalents"]) or 0)
        mxp = max(mxp, f2(r["Power (MW)"]) or 0)
        mxc = max(mxc, f2(r["Total capital cost (2025 USD billions)"]) or 0)
        end_date = r["Date"]  # last chronological date in site's timeline
    return {"h100e_max": mxh, "power_mw_max": mxp,
            "capex_usd_b_max": mxc, "end_of_timeline": end_date}

# ---------- 1. Physical compute by site ----------
site_rows = []
for s in sites:
    name = s["Name"]
    tl = per_site.get(name, [])
    first_op = first_operational(tl)
    cur = snapshot(tl, TODAY) if tl else None
    bo = full_buildout(tl) if tl else None

    site_rows.append({
        "name": name,
        "owner": clean_tag(s.get("Owner", "")),
        "users": clean_tag(s.get("Users", "")),
        "country": s.get("Country", ""),
        "project": s.get("Project", ""),
        "address": s.get("Address", ""),
        # From data_centers.csv (the "current" dataset snapshot 2026-04-20)
        "current_h100e":    f2(s.get("Current H100 equivalents")),
        "current_power_mw": f2(s.get("Current power (MW)")),
        "current_capex_usd_b_2025": f2(s.get("Current total capital cost (2025 USD billions)")),
        # From timelines
        "first_operational_date": first_op,
        "operational_today": bool(first_op and date.fromisoformat(first_op) <= TODAY),
        "timeline_now": cur,
        "full_buildout": bo,
    })

site_rows_sorted = sorted(
    site_rows,
    key=lambda r: (r["full_buildout"]["h100e_max"] if r["full_buildout"] else 0),
    reverse=True,
)

# ---------- 2. Rollup by owner / user ----------
def rollup(field, val_key):
    """val_key = 'current' or 'buildout' — which capacity to aggregate."""
    bucket = defaultdict(lambda: {"h100e": 0.0, "power_mw": 0.0,
                                  "capex_usd_b": 0.0, "n_sites": 0.0})
    for r in site_rows:
        names = [n.strip() for n in (r[field] or "").split(",") if n.strip()]
        if not names:
            names = ["(unspecified)"]
        share = 1.0 / len(names)
        if val_key == "current":
            h = r["current_h100e"] or 0
            p = r["current_power_mw"] or 0
            c = r["current_capex_usd_b_2025"] or 0
        else:  # buildout
            b = r["full_buildout"] or {}
            h = b.get("h100e_max", 0) or 0
            p = b.get("power_mw_max", 0) or 0
            c = b.get("capex_usd_b_max", 0) or 0
        for n in names:
            bk = bucket[n]
            bk["h100e"]       += h * share
            bk["power_mw"]    += p * share
            bk["capex_usd_b"] += c * share
            bk["n_sites"]     += share
    return bucket

by_owner_now = rollup("owner", "current")
by_owner_eob = rollup("owner", "buildout")  # end-of-buildout
by_user_now  = rollup("users", "current")
by_user_eob  = rollup("users", "buildout")

def sorted_bucket(b):
    return sorted(b.items(), key=lambda kv: kv[1]["h100e"], reverse=True)

# ---------- 3. Operational vs committed ----------
op_sites = [r for r in site_rows if r["operational_today"]]
com_sites = [r for r in site_rows if not r["operational_today"]]

# ---------- 4. Global scale-up over time ----------
# Build a sorted unique date index (union of all site timeline dates + TODAY).
all_dates = sorted(set(t["Date"] for t in timelines) | {TODAY.isoformat()})

# At each date, forward-fill each site's snapshot and aggregate.
global_ts = {}
for d_iso in all_dates:
    d = date.fromisoformat(d_iso)
    tot_h = tot_mw = tot_cx = 0.0
    n_op = 0
    for r in site_rows:
        if not r["full_buildout"]:
            continue
        tl = per_site[r["name"]]
        snap = snapshot(tl, d)
        # A site contributes to the "operational" aggregate only if any
        # physical capacity has come online by that date.
        if snap["h100e"] > 0 or snap["power_mw"] > 0 or snap["bldgs_op"] > 0:
            tot_h  += snap["h100e"]
            tot_mw += snap["power_mw"]
            tot_cx += snap["capex_usd_b"]
            n_op   += 1
    global_ts[d_iso] = {
        "operational_power_mw": tot_mw,
        "operational_h100e":    tot_h,
        "operational_capex_usd_b": tot_cx,
        "operational_n_sites":  n_op,
    }

# ---------- 5. Effective compute ----------
owner_eff_now = {k: {
    "raw_h100e": v["h100e"],
    "effective_h100e_33pct": v["h100e"] * UTIL_FACTOR,
    "raw_power_mw": v["power_mw"],
    "capex_usd_b": v["capex_usd_b"],
    "n_sites": v["n_sites"],
} for k, v in by_owner_now.items()}

owner_eff_eob = {k: {
    "raw_h100e": v["h100e"],
    "effective_h100e_33pct": v["h100e"] * UTIL_FACTOR,
    "raw_power_mw": v["power_mw"],
    "capex_usd_b": v["capex_usd_b"],
    "n_sites": v["n_sites"],
} for k, v in by_owner_eob.items()}

# ---------- Emit report ----------
OUT = []
def p(s=""):
    OUT.append(s)

p("=" * 96)
p("EPOCH AI — FRONTIER DATA CENTERS : COMPILED VIEWS")
p(f"dataset: 2026-04-20   retrieved: {TODAY.isoformat()}   "
  f"sites: {len(sites)}   timeline_rows: {len(timelines)}")
p("license: CC BY 4.0  |  url: https://epoch.ai/data/data-centers")
p("=" * 96)

# ----- 1. By site -----
p()
p("### 1. PHYSICAL COMPUTE BY SITE ###")
p("    current_* = snapshot as of dataset date (2026-04-20)")
p("    buildout_* = max across the site's full timeline (end-state capacity)")
p()
p(f"{'SITE':<44} {'OP?':<3} {'FIRST_OP':<12} {'CUR_H100e':>12} {'CUR_MW':>7} "
  f"{'BO_H100e':>12} {'BO_MW':>7} {'BO_CAPEX$B':>11}  OWNER -> USERS")
p("-" * 160)
for r in site_rows_sorted:
    bo = r["full_buildout"] or {"h100e_max":0,"power_mw_max":0,"capex_usd_b_max":0}
    ch = f"{r['current_h100e']:,.0f}" if r['current_h100e'] else "-"
    cm = f"{r['current_power_mw']:,.0f}" if r['current_power_mw'] else "-"
    bh = f"{bo['h100e_max']:,.0f}" if bo['h100e_max'] else "-"
    bm = f"{bo['power_mw_max']:,.0f}" if bo['power_mw_max'] else "-"
    bc = f"{bo['capex_usd_b_max']:.2f}" if bo['capex_usd_b_max'] else "-"
    fo = r["first_operational_date"] or "-"
    op = "Y" if r["operational_today"] else "N"
    p(f"{r['name'][:43]:<44} {op:<3} {fo:<12} {ch:>12} {cm:>7} "
      f"{bh:>12} {bm:>7} {bc:>11}  {r['owner']} -> {r['users']}")

tot_ch = sum(r['current_h100e']    or 0 for r in site_rows)
tot_cm = sum(r['current_power_mw'] or 0 for r in site_rows)
tot_cc = sum(r['current_capex_usd_b_2025'] or 0 for r in site_rows)
tot_bh = sum((r['full_buildout'] or {}).get('h100e_max',0)      for r in site_rows)
tot_bm = sum((r['full_buildout'] or {}).get('power_mw_max',0)   for r in site_rows)
tot_bc = sum((r['full_buildout'] or {}).get('capex_usd_b_max',0) for r in site_rows)
p("-" * 160)
p(f"{'TOTAL':<44} {'':<3} {'':<12} {tot_ch:>12,.0f} {tot_cm:>7,.0f} "
  f"{tot_bh:>12,.0f} {tot_bm:>7,.0f} {tot_bc:>11.1f}")

# ----- 2. By owner -----
p()
p("### 2a. PHYSICAL COMPUTE BY OWNER — CURRENT (2026-04-20) ###")
p(f"{'OWNER':<36} {'H100e':>12} {'MW':>8} {'CAPEX$B':>10} {'#sites':>8}")
p("-" * 78)
for k, v in sorted_bucket(by_owner_now):
    p(f"{k[:35]:<36} {v['h100e']:>12,.0f} {v['power_mw']:>8,.0f} "
      f"{v['capex_usd_b']:>10.1f} {v['n_sites']:>8.1f}")

p()
p("### 2b. PHYSICAL COMPUTE BY OWNER — END-OF-BUILDOUT (planned endstate) ###")
p(f"{'OWNER':<36} {'H100e':>12} {'MW':>8} {'CAPEX$B':>10} {'#sites':>8}")
p("-" * 78)
for k, v in sorted_bucket(by_owner_eob):
    p(f"{k[:35]:<36} {v['h100e']:>12,.0f} {v['power_mw']:>8,.0f} "
      f"{v['capex_usd_b']:>10.1f} {v['n_sites']:>8.1f}")

p()
p("### 2c. PHYSICAL COMPUTE BY USER (workload tenant) — CURRENT ###")
p(f"{'USER':<36} {'H100e':>12} {'MW':>8} {'CAPEX$B':>10} {'#sites':>8}")
p("-" * 78)
for k, v in sorted_bucket(by_user_now):
    p(f"{k[:35]:<36} {v['h100e']:>12,.0f} {v['power_mw']:>8,.0f} "
      f"{v['capex_usd_b']:>10.1f} {v['n_sites']:>8.1f}")

p()
p("### 2d. PHYSICAL COMPUTE BY USER — END-OF-BUILDOUT ###")
p(f"{'USER':<36} {'H100e':>12} {'MW':>8} {'CAPEX$B':>10} {'#sites':>8}")
p("-" * 78)
for k, v in sorted_bucket(by_user_eob):
    p(f"{k[:35]:<36} {v['h100e']:>12,.0f} {v['power_mw']:>8,.0f} "
      f"{v['capex_usd_b']:>10.1f} {v['n_sites']:>8.1f}")

# ----- 3. Operational vs committed -----
p()
p(f"### 3. OPERATIONAL vs COMMITTED  (as of {TODAY.isoformat()}) ###")
p(f"operational_today: {len(op_sites)}   "
  f"committed_not_yet_online: {len(com_sites)}")
p()
p("--- Operational today (at least partial build online) ---")
p(f"{'SITE':<44} {'first_op':<12} {'cur_H100e':>12} {'cur_MW':>8} "
  f"{'buildout_H100e':>15} {'buildout_date':>14}")
p("-" * 115)
for r in sorted(op_sites, key=lambda x: x["first_operational_date"] or ""):
    bo = r["full_buildout"] or {}
    p(f"{r['name'][:43]:<44} {r['first_operational_date']:<12} "
      f"{(r['current_h100e'] or 0):>12,.0f} "
      f"{(r['current_power_mw'] or 0):>8,.0f} "
      f"{bo.get('h100e_max',0):>15,.0f} "
      f"{bo.get('end_of_timeline','-'):>14}")
p()
p("--- Committed / under construction / planned (no physical capacity online today) ---")
p(f"{'SITE':<44} {'first_op':<12} {'buildout_H100e':>15} {'buildout_MW':>12} "
  f"{'buildout_date':>14}")
p("-" * 110)
for r in sorted(com_sites,
                key=lambda x: x["full_buildout"]["end_of_timeline"] if x["full_buildout"] else ""):
    bo = r["full_buildout"] or {}
    p(f"{r['name'][:43]:<44} {(r['first_operational_date'] or '-'):<12} "
      f"{bo.get('h100e_max',0):>15,.0f} "
      f"{bo.get('power_mw_max',0):>12,.0f} "
      f"{bo.get('end_of_timeline','-'):>14}")

# ----- 4. Global scale-up -----
p()
p("### 4. GLOBAL SCALE-UP — OPERATIONAL CAPACITY OVER TIME ###")
p("(Forward-filled per-site, aggregated across all tracked frontier sites.")
p(" Physical-peak H100e figures; apply the 33% haircut for effective compute.)")
p()
# Pick sparse date checkpoints for the narrative.
checkpoints = ["2023-01-01", "2024-01-01", "2025-01-01", "2025-06-01",
               "2025-12-01", "2026-01-01", TODAY.isoformat(),
               "2026-06-30", "2026-12-31", "2027-06-30", "2027-12-31",
               "2028-06-30", "2028-12-31", "2029-06-30", "2029-12-31",
               "2030-06-30"]
# Evaluate each checkpoint.
p(f"{'DATE':<12} {'OP_SITES':>8} {'OP_MW':>10} {'OP_H100e':>16} {'OP_CAPEX$B':>12}  EFF_H100e_33%")
p("-" * 90)
for cp in checkpoints:
    d = date.fromisoformat(cp)
    tot_h = tot_mw = tot_cx = 0.0
    n_op = 0
    for r in site_rows:
        tl = per_site[r["name"]]
        if not tl: continue
        snap = snapshot(tl, d)
        if snap["h100e"] > 0 or snap["power_mw"] > 0 or snap["bldgs_op"] > 0:
            tot_h  += snap["h100e"]
            tot_mw += snap["power_mw"]
            tot_cx += snap["capex_usd_b"]
            n_op   += 1
    eff = tot_h * UTIL_FACTOR
    p(f"{cp:<12} {n_op:>8} {tot_mw:>10,.0f} {tot_h:>16,.0f} {tot_cx:>12.1f}  {eff:>14,.0f}")

# ----- 5. Effective compute -----
p()
p("### 5. EFFECTIVE COMPUTE AFTER UTILIZATION HAIRCUT ###")
p("Epoch methodology (verbatim): 'theoretical peak capacity ... typically")
p("about one third of that, due to inefficiencies'")
p(f"Utilization factor applied: 1/3 = {UTIL_FACTOR:.4f}")
p("(Compute can be further haircut for PUE, power delivery, training-vs-")
p(" inference split, precision-mode conversion — not modeled here.)")
p()
p(f"{'OWNER':<30} {'RAW_H100e_cur':>14} {'EFF_H100e_cur':>14} {'RAW_H100e_bo':>14} {'EFF_H100e_bo':>14}")
p("-" * 92)
owners_both = sorted(set(by_owner_now) | set(by_owner_eob),
                     key=lambda k: by_owner_eob.get(k, {"h100e":0})["h100e"],
                     reverse=True)
for k in owners_both:
    rn = by_owner_now.get(k, {"h100e":0})["h100e"]
    re_ = by_owner_eob.get(k, {"h100e":0})["h100e"]
    p(f"{k[:29]:<30} {rn:>14,.0f} {rn*UTIL_FACTOR:>14,.0f} "
      f"{re_:>14,.0f} {re_*UTIL_FACTOR:>14,.0f}")

# Global totals
g_now = {"h100e":0,"mw":0,"cx":0,"n":0}
g_bo  = {"h100e":0,"mw":0,"cx":0,"n":0}
for r in site_rows:
    g_now["h100e"] += r["current_h100e"] or 0
    g_now["mw"]    += r["current_power_mw"] or 0
    g_now["cx"]    += r["current_capex_usd_b_2025"] or 0
    bo = r["full_buildout"] or {}
    g_bo["h100e"]  += bo.get("h100e_max",0) or 0
    g_bo["mw"]     += bo.get("power_mw_max",0) or 0
    g_bo["cx"]     += bo.get("capex_usd_b_max",0) or 0
p()
p(f"### GLOBAL TOTALS (sum across all {len(sites)} tracked frontier sites) ###")
p(f"  CURRENT (2026-04-20 snapshot)")
p(f"    peak H100e:           {g_now['h100e']:>14,.0f}")
p(f"    effective H100e 33%:  {g_now['h100e']*UTIL_FACTOR:>14,.0f}")
p(f"    power (MW):           {g_now['mw']:>14,.0f}")
p(f"    capex (2025 USD B):   {g_now['cx']:>14.1f}")
p(f"  END-OF-BUILDOUT (planned endstate across entire timeline)")
p(f"    peak H100e:           {g_bo['h100e']:>14,.0f}")
p(f"    effective H100e 33%:  {g_bo['h100e']*UTIL_FACTOR:>14,.0f}")
p(f"    power (MW):           {g_bo['mw']:>14,.0f}")
p(f"    capex (2025 USD B):   {g_bo['cx']:>14.1f}")

# Context numbers from Epoch's page (not in CSV, stated in prose).
p()
p("### EPOCH CONTEXT (from /data/data-centers page, prose) ###")
p("  Dataset covers ~15% of global AI compute delivered as of Nov 2025")
p("  Global install base (ex-China): ~11.5M H100e (chip shipments basis)")
p("  Global install base (incl TPU/AMD/Trainium): ~15-17M H100e")
p("  Confidence bands: power ×1.4   compute ×1.5   cost ×1.6   timing ±6mo")

report = "\n".join(OUT)
(ROOT / "report.txt").write_text(report)
print(report)

# JSON output
out_json = {
    "source": {
        "provider": "Epoch AI",
        "dataset": "Frontier Data Centers",
        "url": "https://epoch.ai/data/data-centers",
        "dataset_updated": "2026-04-20",
        "retrieved": TODAY.isoformat(),
        "license": "CC BY 4.0",
        "files": ["data_centers.csv", "data_center_timelines.csv"],
    },
    "utilization_factor_applied": UTIL_FACTOR,
    "utilization_source_quote": ("theoretical peak capacity ... typically "
                                  "about one third of that, due to inefficiencies"),
    "sites": site_rows_sorted,
    "by_owner_current": dict(by_owner_now),
    "by_owner_buildout": dict(by_owner_eob),
    "by_user_current": dict(by_user_now),
    "by_user_buildout": dict(by_user_eob),
    "operational_sites": op_sites,
    "committed_sites": com_sites,
    "global_scale_up_timeseries": global_ts,
    "global_totals_current": {
        "peak_h100e": g_now["h100e"],
        "effective_h100e_33pct": g_now["h100e"] * UTIL_FACTOR,
        "power_mw": g_now["mw"],
        "capex_usd_b_2025": g_now["cx"],
    },
    "global_totals_buildout": {
        "peak_h100e": g_bo["h100e"],
        "effective_h100e_33pct": g_bo["h100e"] * UTIL_FACTOR,
        "power_mw": g_bo["mw"],
        "capex_usd_b_2025": g_bo["cx"],
    },
    "epoch_context_prose": {
        "share_of_global_ai_compute_pct": 15,
        "share_as_of": "2025-11",
        "global_install_base_h100e_ex_china_millions": 11.5,
        "global_install_base_h100e_incl_other_accelerators_millions_range": [15, 17],
        "confidence_factor_power":   1.4,
        "confidence_factor_compute": 1.5,
        "confidence_factor_cost":    1.6,
        "confidence_timing_months":  6,
    },
}
(ROOT / "compiled.json").write_text(json.dumps(out_json, indent=2, default=str))
