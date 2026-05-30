#!/usr/bin/env python3
"""Insert slide-oriented sections into docs/MODULEN.md.

Reads docs/module_architecture_content.yaml and inserts (or replaces) auto-maintained
blocks used by generate_outline_from_module.py:

- Before You Start / Key files (before Design Architecture)
- Design Architecture / Verification & Testing Methods
- Command Reference (before Learning Outcomes)

Usage:
  python3 scripts/apply_module_architecture_content.py [--dry-run] [--module N]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ARCH_START = "<!-- module-architecture:auto:start -->"
ARCH_END = "<!-- module-architecture:auto:end -->"
SUPP_START = "<!-- module-slide-supplements:auto:start -->"
SUPP_END = "<!-- module-slide-supplements:auto:end -->"
CMD_START = "<!-- module-commands:auto:start -->"
CMD_END = "<!-- module-commands:auto:end -->"
TOPICS_HEADING = "## Topics Covered"
LEARNING_OUTCOMES = "## Learning Outcomes"


def _format_subsections(heading: str, subsections: list[dict[str, Any]]) -> str:
    lines = [heading, ""]
    for idx, sub in enumerate(subsections, start=1):
        lines.append(f"### {idx}. {sub['title']}")
        lines.append("")
        for bullet in sub.get("bullets", []):
            lines.append(f"- {bullet}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _format_numbered_steps(heading: str, steps: list[str]) -> str:
    lines = [heading, ""]
    for idx, step in enumerate(steps, start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    return "\n".join(lines)


def _format_bullet_list(heading: str, items: list[str]) -> str:
    lines = [heading, ""]
    for item in items:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def _format_command_reference(commands: list[dict[str, Any]]) -> str:
    lines = ["## Command Reference", ""]
    for entry in commands:
        lines.append(f"### {entry['title']}")
        lines.append("")
        for bullet in entry.get("bullets", []):
            lines.append(f"- {bullet}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_architecture_block(data: dict[str, Any]) -> str:
    design = _format_subsections("## Design Architecture", data.get("design", []))
    testing = _format_subsections(
        "## Verification & Testing Methods",
        data.get("testing", []),
    )
    return (
        f"{ARCH_START}\n"
        f"{design}\n"
        f"{testing}\n"
        f"{ARCH_END}\n\n"
    )


def build_supplements_block(data: dict[str, Any]) -> str:
    parts: list[str] = [SUPP_START, ""]
    before = data.get("before_you_start") or []
    if before:
        parts.append(_format_numbered_steps("## Before You Start", before).rstrip())
        parts.append("")
    key_files = data.get("key_files") or []
    if key_files:
        parts.append(_format_bullet_list("## Key files to study", key_files).rstrip())
        parts.append("")
    parts.append(SUPP_END)
    parts.append("")
    return "\n".join(parts)


def build_commands_block(data: dict[str, Any]) -> str:
    commands = data.get("commands") or []
    if not commands:
        return ""
    inner = _format_command_reference(commands)
    return f"{CMD_START}\n{inner}{CMD_END}\n\n"


def _replace_marked_block(text: str, start: str, end: str, block: str) -> str:
    pattern = re.escape(start) + r".*?" + re.escape(end) + r"\n*"
    if start in text and end in text:
        return re.sub(pattern, block.rstrip() + "\n", text, count=1, flags=re.DOTALL)
    return text


def _insert_before_heading(text: str, heading: str, block: str) -> str:
    if heading not in text:
        return text + "\n" + block
    return text.replace(heading, block + heading, 1)


def apply_to_module(doc_path: Path, data: dict[str, Any], dry_run: bool) -> bool:
    text = doc_path.read_text(encoding="utf-8")
    new_text = text

    supp_block = build_supplements_block(data)
    if data.get("before_you_start") or data.get("key_files"):
        if SUPP_START in new_text and SUPP_END in new_text:
            new_text = _replace_marked_block(new_text, SUPP_START, SUPP_END, supp_block)
        elif ARCH_START in new_text:
            new_text = new_text.replace(ARCH_START, supp_block + ARCH_START, 1)
        elif TOPICS_HEADING in new_text:
            new_text = new_text.replace(TOPICS_HEADING, supp_block + TOPICS_HEADING, 1)

    arch_block = build_architecture_block(data)
    if ARCH_START in new_text and ARCH_END in new_text:
        new_text = _replace_marked_block(new_text, ARCH_START, ARCH_END, arch_block)
    elif TOPICS_HEADING in new_text:
        new_text = new_text.replace(TOPICS_HEADING, arch_block + TOPICS_HEADING, 1)
    else:
        print(f"SKIP {doc_path}: no architecture marker or {TOPICS_HEADING}", file=sys.stderr)
        return False

    cmd_block = build_commands_block(data)
    if cmd_block:
        if CMD_START in new_text and CMD_END in new_text:
            new_text = _replace_marked_block(new_text, CMD_START, CMD_END, cmd_block)
        elif LEARNING_OUTCOMES in new_text:
            new_text = new_text.replace(LEARNING_OUTCOMES, cmd_block + LEARNING_OUTCOMES, 1)

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
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--module", type=int, default=-1)
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
        if not apply_to_module(doc_path, data, args.dry_run):
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
