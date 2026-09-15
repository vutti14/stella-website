#!/usr/bin/env python3
"""Deterministic static-site checks for STELLA (GitHub Pages, relative URLs)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHONE_PLACEHOLDER = "___ ____"
ROOT_ABS = re.compile(
    r"""\b(?:href|src)\s*=\s*["'](/(?!/).+?)["']""",
    re.IGNORECASE,
)
IMG_REF = re.compile(
    r"""\b(?:href|src)\s*=\s*["'](images/[^"']+)["']""",
    re.IGNORECASE,
)
NAV_HREF = re.compile(
    r"""<ul class="nav-menu"[^>]*>(.*?)</ul>""",
    re.IGNORECASE | re.DOTALL,
)
A_HREF = re.compile(r"""<a\b[^>]*\bhref\s*=\s*["']([^"']+)["']""", re.IGNORECASE)


def rel_page_to_file(href: str) -> Path | None:
    """Map a same-directory nav href to a file under ROOT, or None if skipped."""
    path = href.split("#", 1)[0].split("?", 1)[0].strip()
    if not path:
        return None
    if path.startswith(("mailto:", "tel:", "http://", "https://", "javascript:")):
        return None
    if path.startswith("/"):
        return ROOT / path.lstrip("/")  # flagged separately as root-absolute
    if path in (".", "./"):
        return ROOT / "index.html"
    candidate = ROOT / path
    if candidate.suffix:
        return candidate
    html = ROOT / f"{path}.html"
    if html.is_file():
        return html
    if (ROOT / path / "index.html").is_file():
        return ROOT / path / "index.html"
    return html


def main() -> int:
    errors: list[str] = []
    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        errors.append("No HTML files found at repo root.")

    required = ("gallery.html", "knowledge.html")
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"Required page missing: {name}")

    nav_targets: set[str] = set()

    for html in html_files:
        text = html.read_text(encoding="utf-8")
        rel = html.name

        if PHONE_PLACEHOLDER in text:
            errors.append(f"{rel}: blank phone placeholder ({PHONE_PLACEHOLDER!r})")

        for match in ROOT_ABS.finditer(text):
            errors.append(
                f"{rel}: root-absolute path {match.group(1)!r} "
                "(GitHub Pages project sites need relative URLs)"
            )

        for match in IMG_REF.finditer(text):
            img = ROOT / match.group(1)
            if not img.is_file():
                errors.append(f"{rel}: missing file {match.group(1)}")

        nav = NAV_HREF.search(text)
        if not nav:
            errors.append(f"{rel}: no nav-menu list found")
            continue

        hrefs = A_HREF.findall(nav.group(1))
        if not hrefs:
            errors.append(f"{rel}: nav-menu has no links")
        for href in hrefs:
            nav_targets.add(href)
            if href.startswith("/"):
                errors.append(f"{rel}: nav href is root-absolute: {href!r}")
                continue
            dest = rel_page_to_file(href)
            if dest is None:
                continue
            if not dest.is_file():
                errors.append(f"{rel}: nav link {href!r} does not resolve to a file")

    # Every distinct nav href used on the site must resolve (checked per page above).
    if "knowledge" not in nav_targets and "knowledge.html" not in nav_targets:
        errors.append("No nav link to knowledge was found on any page")

    if errors:
        print("ci_check: FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"ci_check: OK ({len(html_files)} HTML pages, images and nav resolve)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
