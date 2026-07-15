#!/usr/bin/env python3
"""Validate the exact static bundle published to GitHub Pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"bundle verification failed: {message}")


site = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
if not site.is_dir():
    fail(f"site directory is missing: {site}")

required = ("index.html", "robots.txt", ".nojekyll")
for relative in required:
    if not (site / relative).is_file():
        fail(f"required file is missing: {relative}")

index_text = (site / "index.html").read_text(encoding="utf-8")
if 'name="pencil-mayhem-build" content="M1-20260715"' not in index_text:
    fail("expected M1 build marker is missing")
if 'name="robots" content="noindex, nofollow, noarchive"' not in index_text:
    fail("noindex marker is missing")

references = re.findall(r'(?:src|href)=["\']([^"\']+)', index_text)
local_references = [reference for reference in references if reference.startswith("./")]
if not local_references:
    fail("index.html has no relative asset references")

for reference in local_references:
    relative = reference[2:].split("?", 1)[0].split("#", 1)[0]
    if not (site / relative).is_file():
        fail(f"referenced asset is missing: {relative}")

maps = [path for path in site.rglob("*.map") if path.is_file()]
if maps:
    fail(f"source maps must not be published: {maps[0].relative_to(site)}")

sensitive_names = {
    ".env",
    "auth.json",
    "cookie",
    "cookies",
    "credentials.json",
}
for path in site.rglob("*"):
    if path.is_file() and path.name.lower() in sensitive_names:
        fail(f"sensitive filename must not be published: {path.relative_to(site)}")

files = [path for path in site.rglob("*") if path.is_file()]
total_bytes = sum(path.stat().st_size for path in files)
if total_bytes > 20 * 1024 * 1024:
    fail(f"bundle exceeds the 20 MiB playtest budget: {total_bytes} bytes")

print(
    f"bundle verified: files={len(files)} bytes={total_bytes} "
    f"relative_assets={len(local_references)}"
)
