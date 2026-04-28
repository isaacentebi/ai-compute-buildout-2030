#!/usr/bin/env python3
"""Validate URLs cited in report.tex and YAML primary_sources."""

from __future__ import annotations

import json
import re
import ssl
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml  # type: ignore

ROOT = Path(__file__).resolve().parent
URL_RE = re.compile(r"\\url\{(https?://[^}]+)\}|https?://[A-Za-z0-9./?&_%=:+#~,-]+")
SSL_CONTEXT = ssl._create_unverified_context()
YAML_FILES = [
    "compute_commitments_overlay.yaml",
    "neocloud_overlay.yaml",
    "anatomy_layer_costs.yaml",
    "forecaster_capex_comparison.yaml",
]


def report_tex_urls() -> list[dict]:
    text = (ROOT / "report.tex").read_text()
    refs = []
    for m in URL_RE.finditer(text):
        url = (m.group(1) or m.group(0)).rstrip(".,;")
        refs.append({"url": url, "source_file": "report.tex"})
    return refs


def walk_sources(node, source_file: str, out: list[dict]) -> None:
    if isinstance(node, dict):
        if "url" in node and isinstance(node["url"], str):
            url = node["url"].strip()
            if url.startswith("file:"):
                return
            out.append({
                "url": url,
                "source_file": source_file,
                "title": node.get("title", ""),
                "date": str(node.get("date", "")),
                "publisher": node.get("publisher", ""),
            })
        for value in node.values():
            walk_sources(value, source_file, out)
    elif isinstance(node, list):
        for item in node:
            walk_sources(item, source_file, out)


def yaml_urls() -> list[dict]:
    out: list[dict] = []
    for name in YAML_FILES:
        path = ROOT / name
        if not path.exists():
            continue
        with path.open() as f:
            walk_sources(yaml.safe_load(f), name, out)
    return out


def check_url(url: str) -> dict:
    last_error = ""
    for method in ("HEAD", "GET"):
        req = Request(url, method=method, headers={"User-Agent": "ai-compute-buildout-url-audit/4.1"})
        for attempt in range(2):
            try:
                with urlopen(req, timeout=30, context=SSL_CONTEXT) as response:
                    final_url = response.geturl()
                    return {
                        "url": url,
                        "status": response.status,
                        "ok": 200 <= response.status < 400,
                        "redirected": final_url != url,
                        "final_url": final_url,
                        "error": "",
                    }
            except HTTPError as exc:
                if method == "HEAD" and exc.code in {405, 501}:
                    break
                blocked = exc.code in {401, 403, 429}
                return {"url": url, "status": exc.code, "ok": blocked, "redirected": False, "final_url": "", "error": str(exc), "status_class": "blocked" if blocked else "broken"}
            except URLError as exc:
                last_error = str(exc.reason)
            except Exception as exc:
                last_error = repr(exc)
            if attempt == 0:
                time.sleep(1)
    return {"url": url, "status": None, "ok": False, "redirected": False, "final_url": "", "error": last_error, "status_class": "transport_error"}


def main() -> int:
    refs = report_tex_urls() + yaml_urls()
    by_url: dict[str, dict] = {}
    for ref in refs:
        by_url.setdefault(ref["url"], {"url": ref["url"], "references": []})["references"].append(ref)

    results = []
    for url, item in sorted(by_url.items()):
        result = check_url(url)
        result["references"] = item["references"]
        results.append(result)

    payload = {
        "total_urls": len(results),
        "broken_urls": [r for r in results if not r["ok"]],
        "redirected_urls": [r for r in results if r["redirected"]],
        "results": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if payload["broken_urls"] else 0


if __name__ == "__main__":
    sys.exit(main())
