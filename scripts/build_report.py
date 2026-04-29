#!/usr/bin/env python3
"""Build report.tex from tracker.csv + narrative prose.

Generates LaTeX tables for each bucket from the live tracker and stitches
them into a short narrative report. Compile with:
    pdflatex -interaction=nonstopmode report.tex
"""
from __future__ import annotations
import csv, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "tracker.csv"
OUT = ROOT / "report.tex"

SOVEREIGN_HINTS = (
    "sovereign","uae","saudi","humain","reliance","culham","vizag","visakhapatnam",
    "andhra","jamnagar","ewec","srpc","wrpc","g42","khazna","amd_france","hannover","eu_",
)


def is_sov(row: dict) -> bool:
    blob = (row.get("notes","")+row.get("region_iso","")+row.get("id","")).lower()
    return any(t in blob for t in SOVEREIGN_HINTS)


def tex(s: str) -> str:
    if s is None: return ""
    s = str(s)
    return (s.replace("\\","\\textbackslash{}")
             .replace("&","\\&").replace("%","\\%").replace("_","\\_")
             .replace("#","\\#").replace("$","\\$").replace("~","\\textasciitilde{}")
             .replace("{","\\{").replace("}","\\}"))


def f(x):
    try: return float(x) if x not in ("", None) else 0.0
    except: return 0.0


def short(s: str, n: int = 38) -> str:
    if not s: return "—"
    s = re.split(r"[;]", s, maxsplit=1)[0].strip()
    return s if len(s) <= n else s[:n-1] + "…"


def fmt_range(row):
    c = f(row["gw_facility"])
    lo = f(row["gw_facility_low"]) or c
    hi = f(row["gw_facility_high"]) or c
    if abs(lo - c) < 1e-6 and abs(hi - c) < 1e-6:
        return f"{c:.3f}"
    return f"{lo:.2f}\\,/\\,{c:.3f}\\,/\\,{hi:.2f}"


def load_rows():
    with TRACKER.open() as fh:
        return list(csv.DictReader(fh))


def split(rows):
    out = defaultdict(lambda: {"western": [], "sovereign": []})
    for r in rows:
        scope = "sovereign" if is_sov(r) else "western"
        out[r["status"]][scope].append(r)
    return out


def total(rs): return sum(f(r["gw_facility"]) for r in rs)


def longtable(rows, caption: str, label: str, show_online: bool = True) -> str:
    rows = sorted(rows, key=lambda r: -f(r["gw_facility"]))
    cols = "@{}p{4.5cm} p{2.6cm} p{2.6cm} R{1.3cm} R{2.4cm}" + (" l" if show_online else "") + "@{}"
    out = []
    out.append(r"\begin{small}")
    out.append(r"\begin{longtable}{" + cols + "}")
    hdr = r"\toprule" + "\n"
    hdr += r"\textbf{Site} & \textbf{Operator} & \textbf{Anchor tenant} & \textbf{GW} & \textbf{low / central / high}"
    if show_online:
        hdr += r" & \textbf{Online}"
    hdr += r" \\" + "\n" + r"\midrule" + "\n"
    out.append(hdr + r"\endfirsthead")
    out.append(r"\multicolumn{" + ("6" if show_online else "5") + r"}{l}{\textit{(continued — " + tex(caption) + r")}} \\ \toprule")
    out.append(hdr + r"\endhead")
    out.append(r"\bottomrule \endfoot")
    for r in rows:
        gw = f(r["gw_facility"])
        site = tex(short(r.get("site",""), 38))
        op = tex(short(r.get("operator","—"), 22))
        anch = tex(short(r.get("anchor_tenant","—"), 22))
        rng = fmt_range(r)
        cells = [site, op, anch, f"{gw:.3f}", rng]
        if show_online:
            cells.append(tex(r.get("online_year","")))
        out.append(" & ".join(cells) + r" \\")
    out.append(r"\caption{" + caption + r"}\label{" + label + r"}")
    out.append(r"\end{longtable}")
    out.append(r"\end{small}")
    return "\n".join(out)


def operator_summary(rows) -> str:
    """Aggregate Western GW by operator."""
    by_op = defaultdict(lambda: [0, 0])  # [items, gw]
    for r in rows:
        op = (r.get("operator") or "—").strip()
        # Bucket common cases
        op = re.sub(r"\s*/.*", "", op)  # take first operator if multi
        op = {
            "Microsoft": "Microsoft", "Amazon": "Amazon", "Google": "Google",
            "Meta": "Meta", "Oracle": "Oracle", "xAI": "xAI", "CoreWeave": "CoreWeave",
            "Crusoe": "Crusoe", "Nebius": "Nebius", "Nscale": "Nscale",
            "Lambda": "Lambda", "Together AI": "Together AI",
            "Voltage Park": "Voltage Park", "Applied Digital": "Applied Digital",
            "Fluidstack": "Fluidstack", "QTS": "QTS (wholesale colo)",
            "STACK Infrastructure": "STACK (wholesale colo)",
            "Vantage Data Centers": "Vantage (wholesale colo)",
            "Stream Data Centers": "Stream (wholesale colo)",
            "Hut 8": "Hut 8", "Cipher Mining": "Cipher Mining",
            "IREN (Iris Energy)": "IREN", "TeraWulf": "TeraWulf",
            "Bitdeer": "Bitdeer", "Pantheon Atlas": "Pantheon Atlas",
            "Microsoft Azure": "Microsoft", "Google Cloud": "Google",
            "Softbank": "Softbank",
        }.get(op, op)
        by_op[op][0] += 1
        by_op[op][1] += f(r["gw_facility"])
    return by_op


def main():
    rows = load_rows()
    by_status = split(rows)
    western = sum((by_status[b]["western"] for b in
                  ("operational","under_construction","contracted","announced")), [])

    op = by_status["operational"]
    uc = by_status["under_construction"]
    co = by_status["contracted"]
    an = by_status["announced"]
    cn = by_status["canceled"]

    w_op = total(op["western"]); s_op = total(op["sovereign"])
    w_uc = total(uc["western"]); s_uc = total(uc["sovereign"])
    w_co = total(co["western"]); s_co = total(co["sovereign"])
    w_an = total(an["western"]); s_an = total(an["sovereign"])
    w_total = w_op + w_uc + w_co + w_an
    s_total = s_op + s_uc + s_co + s_an

    # Operator summary on Western
    op_sum = operator_summary(western)
    op_sum_top = sorted(op_sum.items(), key=lambda kv: -kv[1][1])[:18]

    body = []
    body.append(r"""\documentclass[11pt]{article}
\usepackage[margin=2.4cm,top=2.6cm,bottom=2.6cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{libertine}
\usepackage[libertine]{newtxmath}
\usepackage[nopatch=footnote]{microtype}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\usepackage[colorlinks=true,urlcolor=blue!50!black,linkcolor=blue!50!black,citecolor=black]{hyperref}
\usepackage{xurl}
\usepackage{enumitem}
\usepackage{titlesec}

\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}

\titleformat{\section}{\large\bfseries}{\thesection}{0.7em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{0.6em}{}
\setlist{itemsep=0.2em,topsep=0.3em}

\title{\textbf{The AI Compute Build-Out, 2026--2030} \\ \large A tracker, not a forecast}
\author{Isaac Entebi}
\date{\today\ (Rev-5.0)}

\begin{document}
\maketitle

\section*{Headline}

Across the four lifecycle buckets (operational / under construction / contracted / announced), the tracker carries """)
    body.append(r"\textbf{" + f"{w_total:.1f}" + r"~GW facility power of Western capacity} and \textbf{" + f"{s_total:.1f}" + r"~GW of sovereign-sidebar capacity} through 2030. The split is ")
    body.append(r"\textbf{" + f"{w_op:.1f}" + r"~GW operational today}, \textbf{" + f"{w_uc:.1f}" + r"~GW under construction} (named site, dated buildout, permits visible), \textbf{" + f"{w_co:.1f}" + r"~GW contracted} (counterparty + capacity disclosed via 10-K, lease, take-or-pay), and \textbf{" + f"{w_an:.1f}" + r"~GW announced} (``up to N~GW'' headlines without a contracted basis or named site). Cancellations are reported separately in \S\ref{sec:canceled} so they don't silently disappear from the trail.")
    body.append(r"")
    body.append(r"There are no probability priors, tier-weighted central cases, or Monte Carlo distributions in this report. Every number resolves to a row in the companion \texttt{tracker.csv}, which combines Epoch~AI's Frontier Data Centers (the primary upstream) with a small hand-curated overlay for capacity Epoch's documented methodology does not cover. Run \texttt{bash scripts/refresh\_epoch.sh} to re-pull and rebuild.")
    body.append(r"")
    body.append(r"\textbf{The tracker is what it is.} Every row carries a primary-source URL and a date. Aggregating across the buckets is the reader's choice; the tracker does not collapse to a single ``2030 horizon'' number because the underlying claims have very different evidence quality.")
    body.append(r"")

    # Totals table
    body.append(r"\begin{table}[h]")
    body.append(r"\centering")
    body.append(r"\begin{tabular}{@{}lrrrr@{}}")
    body.append(r"\toprule")
    body.append(r"\textbf{Bucket} & \textbf{Western items} & \textbf{Western GW} & \textbf{Sovereign items} & \textbf{Sovereign GW} \\")
    body.append(r"\midrule")
    for label, key in [("Operational","operational"),("Under construction","under_construction"),("Contracted","contracted"),("Announced","announced"),("Canceled","canceled")]:
        wn = len(by_status[key]["western"]); wg = total(by_status[key]["western"])
        sn = len(by_status[key]["sovereign"]); sg = total(by_status[key]["sovereign"])
        body.append(f"{label} & {wn} & {wg:.3f} & {sn} & {sg:.3f} \\\\")
    body.append(rf"\midrule \textbf{{Total (ex-canceled)}} & & \textbf{{{w_total:.3f}}} & & \textbf{{{s_total:.3f}}} \\")
    body.append(r"\bottomrule")
    body.append(r"\end{tabular}")
    body.append(r"\caption{Bucket totals (GW facility power). Sovereign sidebar items (UAE, Saudi, India, UK, EU) are reported separately and are not added to the Western total.}")
    body.append(r"\end{table}")

    # Operator concentration
    body.append(r"\section*{Operator concentration (Western, all buckets ex-canceled)}")
    body.append(r"\begin{table}[h]")
    body.append(r"\centering\small")
    body.append(r"\begin{tabular}{@{}lrr@{}}")
    body.append(r"\toprule")
    body.append(r"\textbf{Operator (or operator class)} & \textbf{Items} & \textbf{GW facility} \\")
    body.append(r"\midrule")
    for opn, (n, gw) in op_sum_top:
        body.append(f"{tex(opn)} & {n} & {gw:.3f} \\\\")
    body.append(rf"\midrule \textbf{{Total Western}} & & \textbf{{{w_total:.3f}}} \\")
    body.append(r"\bottomrule")
    body.append(r"\end{tabular}")
    body.append(r"\caption{Western capacity by operator. ``Wholesale colo'' captures sites where Epoch tracks the facility but no AI tenant is publicly attributed. Multi-operator rows are bucketed by the lead operator.}")
    body.append(r"\end{table}")

    # Section 1: Operational today
    body.append(r"\section{Operational today}\label{sec:operational}")
    body.append(r"\noindent " + f"{len(op['western'])}" + r" Western sites totaling \textbf{" + f"{w_op:.3f}" + r"~GW facility power} are energized as of the data cutoff (Epoch snapshot 2026-04-28). Most rows come from Epoch's Frontier Data Centers operational MW field. Wholesale-colocation sites (QTS, STACK, Vantage) appear with the AI tenant marked as undisclosed.")
    body.append(r"")
    body.append(longtable(op["western"], "Operational today --- Western", "tab:op-w", show_online=False))

    # Section 2: Under construction
    body.append(r"\section{Under construction}\label{sec:under-construction}")
    body.append(r"\noindent " + f"{len(uc['western'])}" + r" Western sites totaling \textbf{" + f"{w_uc:.3f}" + r"~GW facility power} are under construction. ``Under construction'' means a named site with dated buildout evidence: utility interconnect filings, building permits, satellite imagery, or operator-disclosed completion dates. Online column shows the central energization year from the source.")
    body.append(r"")
    body.append(longtable(uc["western"], "Under construction --- Western", "tab:uc-w"))

    # Section 3: Contracted
    body.append(r"\section{Contracted (counterparty + capacity disclosed)}\label{sec:contracted}")
    body.append(r"\noindent " + f"{len(co['western'])}" + r" Western rows totaling \textbf{" + f"{w_co:.3f}" + r"~GW facility power} represent firm commercial commitments where a counterparty and a capacity have been publicly disclosed (typically via 10-K, executed lease, or take-or-pay press release). Site-level mapping is sometimes incomplete --- the contract may name the customer and the GW figure but not the underlying physical campus. Where overlap with Epoch sites is plausible, the row range is widened to honestly bracket the dedupe uncertainty.")
    body.append(r"")
    body.append(longtable(co["western"], "Contracted --- Western", "tab:co-w"))

    # Section 4: Announced
    body.append(r"\section{Announced (headline only --- no contract or named site)}\label{sec:announced}")
    body.append(r"\noindent " + f"{len(an['western'])}" + r" Western rows totaling \textbf{" + f"{w_an:.3f}" + r"~GW facility power} central are headline-only commitments: ``up to N~GW'' statements where no contract, no named physical site, or no executed lease is disclosed. Low cases for several rows include 0 because the underlying ceiling could lap entirely with already-counted capacity. Treat this bucket as the speculative tail of the tracker --- it is in the report because the sources are real, not because the buildout is.")
    body.append(r"")
    body.append(longtable(an["western"], "Announced --- Western", "tab:an-w"))

    # Section 5: Canceled
    body.append(r"\section{Canceled or paused}\label{sec:canceled}")
    body.append(r"\noindent " + f"{len(cn['western'])}" + r" Western projects (and any sovereign cancellations) are tracked here for trail integrity. Capacity is set to zero so they don't enter the totals, but the row stays in the database with the cancellation source so future audits can see what was once announced and what didn't land.")
    body.append(r"")
    body.append(longtable(cn["western"]+cn["sovereign"], "Canceled / paused", "tab:cn", show_online=False))

    # Section 6: Sovereign sidebar
    body.append(r"\section{Sovereign sidebar}\label{sec:sovereign}")
    sov_count = len(op['sovereign'])+len(uc['sovereign'])+len(co['sovereign'])+len(an['sovereign'])
    body.append(r"\noindent State-backed AI infrastructure programmes operate under different financing and disclosure norms than the Western merchant build, so they are reported as a separate sidebar. The tracker carries \textbf{" + f"{s_total:.3f}" + r"~GW facility power} across " + f"{sov_count}" + r" sovereign rows: UAE (Stargate UAE, Microsoft-G42 Khazna), Saudi Arabia (HUMAIN-xAI, HUMAIN-AMD, HUMAIN master plan residual), India (Reliance Jamnagar, Reliance Andhra, Google Visakhapatnam), the UK (Culham AI Growth Zone, BT-Nscale sovereign), and EU sovereign-AI initiatives (AMD-France LOI, Hannover Messe block).")
    body.append(r"")
    sov_all = op["sovereign"]+uc["sovereign"]+co["sovereign"]+an["sovereign"]
    body.append(longtable(sov_all, "Sovereign sidebar --- all buckets", "tab:sov"))

    # Section 7: Capex envelope
    body.append(r"\section{Capital envelope}\label{sec:capex}")
    body.append(r"\noindent The bottoms-up unit-economics analysis (companion file \texttt{anatomy\_layer\_costs.yaml}) places one 2026-vintage AI facility GW at $\$30$--$\$47$~billion all-in (low to high range across the six physical layers: shell + civil, cooling, power infrastructure, networking fabric, accelerator + server BOM, grid interconnect). The paper-adopted central is \$37~billion per facility-GW (rounded grid-tied). Applied to the " + f"{w_total:.1f}" + r"~GW Western total ex-canceled gives a capital envelope of \textbf{\$" + f"{w_total*30/1000:.2f}" + r"~T to \$" + f"{w_total*47/1000:.2f}" + r"~T} (low to high), with a central of \textbf{\$" + f"{w_total*37/1000:.2f}" + r"~T}.")
    body.append(r"")
    body.append(r"This is the build cost \emph{implied} by the announced+contracted+under-construction Western horizon, not a roll-up of disclosed company capex plans. It is also not a floor on what gets built, since Sightline Climate / Bloomberg analysis (April 2026, see \S\ref{sec:risk}) projects roughly half of the announced 2026 pipeline will slip or cancel.")
    body.append(r"")

    # Section 8: Systemic risk
    body.append(r"\section{Systemic risks}\label{sec:risk}")
    body.append(r"\noindent Three risks dominate the under-construction and announced buckets:")
    body.append(r"\begin{itemize}")
    body.append(r"\item \textbf{Grid interconnection.} Sightline Climate / Bloomberg analysis from April 2026 finds that of $\sim$16~GW of US AI data center capacity slated for 2026 delivery, only $\sim$5~GW is actually under active construction. Up to half of the announced 2026 pipeline faces material delay or outright cancellation. The bottlenecks are transformer and high-voltage switchgear lead times, Chinese tariff exposure on those components, and ISO interconnect queues that frequently exceed five years. Behind-the-meter generation (Crusoe Cheyenne with Tallgrass, Oracle Project Jupiter with Bloom Energy fuel cells, the new Pantheon Atlas Croatia campus with 8~GWh of battery storage) is the operational hedge against this.")
    body.append(r"\item \textbf{Demand-side substitution.} The $\sim$5~GW announced bucket is heavily concentrated in a small number of contracted-customer relationships (Anthropic across AWS / Google / Microsoft / Fluidstack; OpenAI across Oracle Stargate sites). If any single customer relationship reprices, capacity moves between operators rather than getting built. The April 2026 Anthropic--AWS expansion to up to 5~GW is the largest single mover in the 2026 calendar and post-dates the original Rev-4 cutoff.")
    body.append(r"\item \textbf{Permitting and community pushback.} Several large announcements are tracking through challenged regulatory environments: Oracle Saline Township MI is under Michigan AG appeal, the OpenAI Stargate UK Cobalt Park site was paused April 9~2026 over UK regulatory and energy-cost issues, the Box Elder UT Stratos Project was tabled by commissioners over Great Salt Lake water concerns, and Wisconsin PSC rejected ratepayer cost-share for new DC power plants in early April 2026. None individually breaks the totals, but the cumulative effect tightens timelines.")
    body.append(r"\end{itemize}")

    # Section 9: What we exclude
    body.append(r"\section{Scope and exclusions}\label{sec:scope}")
    body.append(r"\noindent Three exclusions apply:")
    body.append(r"\begin{itemize}")
    body.append(r"\item \textbf{China.} Epoch tracks Alibaba Zhangbei (203~MW operational) but the broader Chinese AI infrastructure is materially under-disclosed in primary sources. Alibaba's August 2025 quarterly capex of \$5.4~B (38.6~B yuan) and the February 2025 three-year 380~B-yuan ($\sim$\$53~B) commitment are within an order of magnitude of the smaller US hyperscalers in dollar terms but cannot be corroborated at site granularity. China is excluded from Western totals; the qualitative gap is acknowledged.")
    body.append(r"\item \textbf{Sub-100~MW sites.} Epoch's documented coverage threshold is roughly 100~MW. Smaller neocloud and edge deployments (Voltage Park's six-site fleet at $\sim$169~MW total, Together AI's three-site operational footprint, the BT-Nscale UK sovereign 14~MW) appear in the overlay where the operator and aggregate capacity are public, but many smaller deployments below the threshold are not tracked at all.")
    body.append(r"\item \textbf{Pre-permit speculation.} Multi-gigawatt visions without permits, financing, or anchor tenants are excluded. Fermi America's 11--17~GW Amarillo TX vision is the canonical case --- anchor tenant pulled out in April 2026, class action filed, stock down 46\% --- and stays excluded.")
    body.append(r"\end{itemize}")

    # Section 10: Methodology (kept minimal)
    body.append(r"\section{Methodology}\label{sec:methodology}")
    body.append(r"\noindent Epoch~AI's Frontier Data Centers dataset (CC BY 4.0, snapshot 2026-04-28) is the primary upstream. Epoch tracks 37 frontier sites with their own \texttt{\#confident} / \texttt{\#likely} / \texttt{\#speculative} confidence tags and publishes confidence bands of $\times 1.4$ on power, $\times 1.5$ on compute, $\times 1.6$ on cost, and $\pm 6$ months on timing. Their methodology is documented at \href{https://epoch.ai/data/data-centers-documentation}{epoch.ai/data/data-centers-documentation}.")
    body.append(r"")
    body.append(r"This report adds a small overlay (\texttt{overlay.csv}, 46 rows) for capacity Epoch's documented methodology does not cover: ceiling-style ``up to N~GW'' announcements without site mapping (Anthropic--AWS 5~GW, Anthropic--Google/Broadcom 3.5~GW, Anthropic--Azure 1~GW), contracted neocloud fleet ex-Epoch (CoreWeave 10-K, Nebius press, Applied Digital lease, Hut~8 / Cipher / TeraWulf / IREN backlogs), sub-threshold or non-US sites pending Epoch index expansion (Crusoe Nordic, BT-Nscale UK), and the sovereign sidebar.")
    body.append(r"")
    body.append(r"The pipeline is two scripts. \texttt{scripts/refresh\_epoch.sh} pulls fresh data and rebuilds; \texttt{scripts/build\_tracker.py} combines Epoch's compiled JSON with the overlay CSV into \texttt{tracker.csv} and \texttt{tracker.md}. There is no probability framework, no realization-priors model, no Monte Carlo draw, and no deterministic tier-weighted central case. The four buckets describe lifecycle stage; the reader does the aggregating.")
    body.append(r"")
    body.append(r"\textbf{Audit basis.} Three independent deep-research passes (Anthropic, OpenAI, Google Gemini) audited the prior database against primary sources between 2026-04-27 and 2026-04-29. Their findings are baked into the current overlay row magnitudes and ranges, especially around the Anthropic--AWS expansion to 5~GW, the Broadcom 8-K disclosing 3.5~GW of TPU compute commitment, the Reliance Andhra upsizing to 1.5~GW following the April 25 Andhra Pradesh IPC approval, the Crusoe Nordic operational figure correction, and the Stargate Abilene Oracle/OpenAI 600~MW expansion replacement by Crusoe-Microsoft.")

    body.append(r"")
    body.append(r"\section*{Sources and references}")
    body.append(r"\noindent Every row in \texttt{tracker.csv} carries a \texttt{source\_url} and \texttt{source\_date}. Companion files: \texttt{overlay.csv} (the hand-curated rows), \texttt{source\_claim\_map.csv} (one-line claim per atom), \texttt{anatomy\_layer\_costs.yaml} (capex unit-economics), \texttt{forecaster\_capex\_comparison.yaml} (cross-forecaster reconciliation across 18 sources: Bernstein, Bain, JLL, Cushman, Goldman, Morgan Stanley, JPM, BNEF, Synergy, Dell'Oro, IEA, LBNL, Aschenbrenner, NVIDIA, Barclays, Stargate, Hyperion, CoreWeave, Nebius), \texttt{citation\_inventory.csv} (full citation list), \texttt{url\_check\_report.json} (URL liveness), \texttt{source\_freshness\_report.json} (per-row staleness).")

    body.append(r"")
    body.append(r"\end{document}")

    OUT.write_text("\n".join(body))
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(rows)} tracker rows fed in)")
    print(f"  Western: {w_total:.3f} GW, Sovereign: {s_total:.3f} GW")


if __name__ == "__main__":
    main()
