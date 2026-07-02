#!/usr/bin/env python3
"""Check that all relative markdown links in the repo resolve to existing files.

Usage: python3 tools/check-links.py [--root DIR]
Exit code 0 = no broken links, 1 = broken links found.
"""
import argparse
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def check(root: Path) -> int:
    broken = []
    md_files = sorted(root.rglob("*.md"))
    for md in md_files:
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(2).strip()
            if target.startswith(SKIP_PREFIXES):
                continue
            # strip anchor and title
            target = target.split("#", 1)[0].split(" ", 1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                line = text[: m.start()].count("\n") + 1
                broken.append((md.relative_to(root), line, m.group(2)))
    if broken:
        print(f"BROKEN LINKS: {len(broken)}")
        for f, line, tgt in broken:
            print(f"  {f}:{line} -> {tgt}")
        return 1
    print(f"OK: {len(md_files)} markdown files, no broken relative links")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    sys.exit(check(Path(args.root)))
