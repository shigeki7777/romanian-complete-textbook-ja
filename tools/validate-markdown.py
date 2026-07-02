#!/usr/bin/env python3
"""Validate textbook markdown files against repo conventions.

Checks:
  1. Cedilla diacritics (ş U+015F / ţ U+0163) are forbidden -> must use comma-below (ș U+0219 / ț U+021B)
  2. File names: lowercase, hyphens, .md (no spaces/underscores/uppercase)
  3. Every file starts with a single H1 ('# ')
  4. Chapter files (NN-*.md in level dirs) contain required sections

Usage: python3 tools/validate-markdown.py [--root DIR]
Exit code 0 = clean, 1 = violations found.
"""
import argparse
import re
import sys
from pathlib import Path

CEDILLA = {"ş": "ş(cedilla)", "ţ": "ţ(cedilla)", "Ş": "Ş(cedilla)", "Ţ": "Ţ(cedilla)"}
LEVEL_DIRS = {"01-a1", "02-a2", "03-b1", "04-b2", "05-c1", "06-c2"}
# Required in numbered chapter files (except overview/answer-key/bridge/test which vary)
REQUIRED_SECTIONS = ["この章の目標"]
FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9.-]*\.md$")


def validate(root: Path) -> int:
    problems = []
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        rel = md.relative_to(root)
        name = md.name
        if not FILENAME_RE.match(name) and name not in ("README.md", "LICENSE", "CHANGELOG.md",
                                                         "CONTRIBUTING.md", "ROADMAP.md", "STYLE_GUIDE.md",
                                                         "SOURCE_POLICY.md", "QUALITY_CHECKLIST.md", "PROGRESS.md"):
            problems.append(f"{rel}: filename violates convention (lowercase-hyphen.md)")
        text = md.read_text(encoding="utf-8")
        # These files document the forbidden cedilla forms as explicit warnings
        cedilla_exempt = name in ("STYLE_GUIDE.md", "02-pronunciation-overview.md",
                                  "01-pronunciation-and-alphabet.md")
        for ch, label in ({} if cedilla_exempt else CEDILLA).items():
            if ch in text:
                n = text.count(ch)
                problems.append(f"{rel}: contains {n}x {label} — use comma-below form")
        stripped = text.lstrip()
        if not stripped.startswith("# "):
            problems.append(f"{rel}: does not start with H1")
        # chapter section check
        parts = rel.parts
        if len(parts) == 2 and parts[0] in LEVEL_DIRS and re.match(r"^\d\d-", name):
            num = name[:2]
            if num not in ("00",) and "answer-key" not in name and "checkpoint" not in name and "bridge" not in name:
                for sec in REQUIRED_SECTIONS:
                    if sec not in text:
                        problems.append(f"{rel}: missing required section 「{sec}」")
    if problems:
        print(f"VIOLATIONS: {len(problems)}")
        for p in problems:
            print(f"  {p}")
        return 1
    print("OK: markdown conventions satisfied")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    sys.exit(validate(Path(args.root)))
