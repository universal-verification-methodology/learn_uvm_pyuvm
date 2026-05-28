#!/usr/bin/env python3
"""Insert Design Architecture and Verification sections into docs/MODULEN.md.

Reads docs/module_architecture_content.yaml and inserts (or replaces) sections
before ``## Topics Covered`` in each MODULE file.

Usage:
  python3 scripts/apply_module_architecture_content.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

MARKER_START = "<!-- module-architecture:auto:start -->"
MARKER_END = "<!-- module-architecture:auto:end -->"
TOPICS_HEADING = "## Topics Covered"


def _format_section(heading: str, subsections: list[dict[str, Any]]) -> str:
    lines = [heading, ""]
    for idx, sub in enumerate(subsections, start=1):
        lines.append(f"### {idx}. {sub['title']}")
        lines.append("")
        for bullet in sub.get("bullets", []):
            lines.append(f"- {bullet}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_block(data: dict[str, Any]) -> str:
    design = _format_section("## Design Architecture", data.get("design", []))
    testing = _format_section(
        "## Verification & Testing Methods",
        data.get("testing", []),
    )
    return (
        f"{MARKER_START}\n"
        f"{design}\n"
        f"{testing}\n"
        f"{MARKER_END}\n\n"
    )


def apply_to_module(doc_path: Path, block: str, dry_run: bool) -> bool:
    text = doc_path.read_text(encoding="utf-8")
    if MARKER_START in text and MARKER_END in text:
        new_text = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n*",
            block.rstrip() + "\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    elif TOPICS_HEADING in text:
        new_text = text.replace(TOPICS_HEADING, block + TOPICS_HEADING, 1)
    else:
        print(f"SKIP {doc_path}: no marker or {TOPICS_HEADING}", file=sys.stderr)
        return False

    if new_text == text:
        print(f"UNCHANGED {doc_path}")
        return True

    if dry_run:
        print(f"WOULD UPDATE {doc_path} (+{len(new_text) - len(text)} bytes)")
        return True

    doc_path.write_text(new_text, encoding="utf-8")
    print(f"UPDATED {doc_path}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing files",
    )
    parser.add_argument(
        "--module",
        type=int,
        default=-1,
        help="Only update this module number (default: all in yaml)",
    )
    args = parser.parse_args()

    course_root = Path(__file__).resolve().parents[1]
    yaml_path = course_root / "docs" / "module_architecture_content.yaml"
    if not yaml_path.is_file():
        print(f"ERROR: missing {yaml_path}", file=sys.stderr)
        return 1

    content = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
    modules: dict[str, Any] = content.get("modules") or {}

    ok = True
    for key, data in sorted(modules.items(), key=lambda kv: int(kv[0])):
        mod = int(key)
        if args.module >= 0 and mod != args.module:
            continue
        doc_path = course_root / "docs" / f"MODULE{mod}.md"
        if not doc_path.is_file():
            print(f"ERROR: missing {doc_path}", file=sys.stderr)
            ok = False
            continue
        if not apply_to_module(doc_path, build_block(data), args.dry_run):
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
