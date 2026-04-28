#!/usr/bin/env python3
"""Validate cited URLs with redirect and content checks."""

from __future__ import annotations

import json
import re
import ssl
import sys
import time
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml  # type: ignore


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
URL_RE = re.compile(r"\\url\{(https?://[^}]+)\}|https?://[A-Za-z0-9./?&_%=:+#~,-]+")
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
SSL_CONTEXT = ssl._create_unverified_context()
YAML_FILES = [
    "canonical_capacity_atoms.yaml",
    "compute_commitments_overlay.yaml",
    "neocloud_overlay.yaml",
    "anatomy_layer_costs.yaml",
    "forecaster_capex_comparison.yaml",
    "facts_extract.yaml",
]

EXPECTED_KEYWORDS = {
    "amd.com/en/newsroom/press-releases/2025-10-6-amd-and-openai-announce-strategic-partnership-to-d.html": [
        "AMD and OpenAI Announce Strategic Partnership to Deploy 6 Gigawatts of AMD GPUs",
        "MI450",
        "second half of 2026",
    ],
    "openai.com/index/openai-amd-strategic-partnership/": [
        "AMD and OpenAI announce strategic partnership to deploy 6 gigawatts of AMD GPUs",
        "MI450",
        "2H 2026",
    ],
}
REPLACED_SOURCES = [
    {
        "old": "https://ir.amd.com/news-events/press-releases/detail/1230/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus",
        "new": "https://www.amd.com/en/newsroom/press-releases/2025-10-6-amd-and-openai-announce-strategic-partnership-to-d.html",
        "reason": "AMD IR URL redirected to unrelated AMD pages; replaced with AMD Newsroom official page.",
    },
    {
        "old": "https://ir.amd.com/news-events/press-releases/detail/1249/amd-and-humain-announce-strategic-collaboration-to-advance",
        "new": "https://www.amd.com/en/newsroom/press-releases/2025-5-13-amd-and-humain-form-strategic--10b-collaboration-.html",
        "reason": "AMD IR URL redirected to unrelated AMD pages; replaced with AMD Newsroom official page.",
    },
]


def normalize_url(url: str) -> str:
    return url.rstrip(".,;")


def comparable_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.netloc}{parsed.path}".rstrip("/")


def report_tex_urls() -> list[dict]:
    path = ROOT / "report.tex"
    text = path.read_text(errors="ignore") if path.exists() else ""
    refs = []
    for m in URL_RE.finditer(text):
        refs.append({"url": normalize_url(m.group(1) or m.group(0)), "source_file": "report.tex"})
    return refs


def walk_sources(node, source_file: str, out: list[dict]) -> None:
    if isinstance(node, dict):
        for key in ("url", "source_url", "primary_source_url"):
            if key in node and isinstance(node[key], str):
                url = node[key].strip()
                if url.startswith(("http://", "https://")):
                    out.append({
                        "url": normalize_url(url),
                        "source_file": source_file,
                        "title": node.get("title", ""),
                        "expected_claim_keywords": node.get("expected_claim_keywords", []),
                        "publisher": node.get("publisher") or node.get("source_publisher", ""),
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


def extract_title(body: bytes) -> str:
    text = body[:250000].decode("utf-8", errors="ignore")
    match = TITLE_RE.search(text)
    return unescape(TAG_RE.sub(" ", match.group(1))).strip() if match else ""


def content_text(body: bytes) -> str:
    return unescape(TAG_RE.sub(" ", body[:350000].decode("utf-8", errors="ignore"))).lower()


def expected_keywords(url: str, refs: list[dict]) -> list[str]:
    comparable = comparable_url(url)
    for key, keywords in EXPECTED_KEYWORDS.items():
        if comparable == key.rstrip("/"):
            return keywords
    for ref in refs:
        claim_keywords = ref.get("expected_claim_keywords") or []
        if claim_keywords:
            return [str(keyword) for keyword in claim_keywords]
    if urlparse(url).path.lower().endswith(".pdf"):
        return []
    for ref in refs:
        title = str(ref.get("title") or "").strip()
        if title:
            return [title]
    return []


def classify(url: str, final_url: str, status: int, body: bytes, refs: list[dict]) -> tuple[str, str, str]:
    redirected = comparable_url(url) != comparable_url(final_url)
    title = extract_title(body)
    text = content_text(body)
    keywords = expected_keywords(url, refs)
    if status in {401, 403, 429}:
        return "blocked_manual_review", title, "blocked status"
    if not (200 <= status < 300):
        return "failed", title, f"http {status}"
    if keywords:
        missing = [keyword for keyword in keywords if keyword.lower() not in text and keyword.lower() not in title.lower()]
        if missing:
            return "failed", title, f"missing expected keyword(s): {', '.join(missing)}"
    return ("redirected_verified" if redirected else "verified_ok"), title, ""


def check_url(url: str, refs: list[dict]) -> dict:
    last_error = ""
    for method in ("HEAD", "GET"):
        req = Request(url, method=method, headers={"User-Agent": "ai-compute-buildout-url-audit/4.1"})
        for attempt in range(2):
            try:
                with urlopen(req, timeout=30, context=SSL_CONTEXT) as response:
                    final_url = response.geturl()
                    body = b""
                    if method == "GET" or comparable_url(final_url) != comparable_url(url):
                        body = response.read(400000)
                    if method == "HEAD" and not body:
                        break
                    status_class, title, detail = classify(url, final_url, response.status, body, refs)
                    return {
                        "url": url,
                        "status": response.status,
                        "status_class": status_class,
                        "ok": status_class in {"verified_ok", "redirected_verified"},
                        "redirected": comparable_url(final_url) != comparable_url(url),
                        "final_url": final_url,
                        "title": title,
                        "error": detail,
                    }
            except HTTPError as exc:
                if method == "HEAD" and exc.code in {405, 501}:
                    break
                if exc.code in {401, 403, 429}:
                    return {
                        "url": url,
                        "status": exc.code,
                        "status_class": "blocked_manual_review",
                        "ok": False,
                        "redirected": False,
                        "final_url": exc.geturl() or "",
                        "title": "",
                        "error": str(exc),
                    }
                last_error = str(exc)
            except URLError as exc:
                last_error = str(exc.reason)
            except Exception as exc:
                last_error = repr(exc)
            if attempt == 0:
                time.sleep(1)
    return {
        "url": url,
        "status": None,
        "status_class": "failed",
        "ok": False,
        "redirected": False,
        "final_url": "",
        "title": "",
        "error": last_error,
    }


def main() -> int:
    refs = report_tex_urls() + yaml_urls()
    by_url: dict[str, dict] = {}
    for ref in refs:
        by_url.setdefault(ref["url"], {"url": ref["url"], "references": []})["references"].append(ref)

    results = []
    for url, item in sorted(by_url.items()):
        result = check_url(url, item["references"])
        result["references"] = item["references"]
        results.append(result)

    counts = {
        "verified_ok": sum(1 for r in results if r["status_class"] == "verified_ok"),
        "redirected_verified": sum(1 for r in results if r["status_class"] == "redirected_verified"),
        "blocked_manual_review": sum(1 for r in results if r["status_class"] == "blocked_manual_review"),
        "failed": sum(1 for r in results if r["status_class"] == "failed"),
        "replaced": len(REPLACED_SOURCES),
    }
    payload = {
        "total_urls": len(results),
        "counts": counts,
        "blocked_urls": [r for r in results if r["status_class"] == "blocked_manual_review"],
        "failed_urls": [r for r in results if r["status_class"] == "failed"],
        "redirected_urls": [r for r in results if r["redirected"]],
        "replaced_sources": REPLACED_SOURCES,
        "results": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if payload["failed_urls"] else 0


if __name__ == "__main__":
    sys.exit(main())
