#!/usr/bin/env python3
"""Build a manifest- and sha256-verified reviewer packet."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.md"
SHA256 = ROOT / "sha256_manifest.txt"
REF_RE = re.compile(r"- `([^`]+)`")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest_paths() -> list[str]:
    if not MANIFEST.exists():
        raise FileNotFoundError("MANIFEST.md is missing")

    paths: list[str] = []
    in_included = False
    for line in MANIFEST.read_text().splitlines():
        stripped = line.strip()
        if stripped == "Included:":
            in_included = True
            continue
        if stripped == "Deliberately not included:":
            break
        if not in_included:
            continue
        match = REF_RE.match(stripped)
        if match:
            paths.append(match.group(1).rstrip("/"))
    if not paths:
        raise ValueError("MANIFEST.md has no Included file entries")
    return paths


def expand_manifest_paths(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for rel in paths:
        target = ROOT / rel
        if not target.exists():
            raise FileNotFoundError(f"manifest path missing: {rel}")
        if target.is_dir():
            files.extend(path for path in sorted(target.rglob("*")) if path.is_file())
        elif target.is_file():
            files.append(target)
    return sorted(set(files), key=lambda p: p.relative_to(ROOT).as_posix())


def read_sha_manifest() -> dict[str, str]:
    if not SHA256.exists():
        raise FileNotFoundError("sha256_manifest.txt is missing")

    entries: dict[str, str] = {}
    for lineno, line in enumerate(SHA256.read_text().splitlines(), start=1):
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        parts = raw.split()
        if len(parts) < 2 or not re.fullmatch(r"[0-9a-fA-F]{64}", parts[0]):
            raise ValueError(f"sha256_manifest.txt:{lineno}: invalid sha256 line")
        rel = " ".join(parts[1:]).lstrip("*")
        entries[rel] = parts[0].lower()
    return entries


def verify(files: list[Path], sha_entries: dict[str, str]) -> None:
    errors: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if rel == SHA256.name:
            continue
        expected = sha_entries.get(rel)
        if not expected:
            errors.append(f"missing sha256 entry: {rel}")
            continue
        got = sha256_file(path)
        if got != expected:
            errors.append(f"sha256 mismatch: {rel} expected={expected} got={got}")

    if errors:
        raise ValueError("packet verification failed:\n" + "\n".join(f"  - {e}" for e in errors))


def build_zip(files: list[Path], output: Path) -> None:
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(ROOT).as_posix())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="ai-compute-reviewer-packet-rev4_2.zip")
    parser.add_argument("--no-zip", action="store_true", help="verify only")
    args = parser.parse_args()

    try:
        manifest_paths = read_manifest_paths()
        files = expand_manifest_paths(manifest_paths)
        sha_entries = read_sha_manifest()
        verify(files, sha_entries)
        if not args.no_zip:
            output = (ROOT / args.output).resolve()
            build_zip(files, output)
            print(f"wrote {output} ({len(files)} files)")
        else:
            print(f"packet verification passed ({len(files)} files)")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
