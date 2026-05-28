#!/usr/bin/env python3
"""Generate moduleN/EXAMPLES.md from docs/MODULEN.md #### Example sections.

The module-to-slides-video skill expects EXAMPLES.md with headers like:

  ## 1. Title (`folder/`)

This script extracts ``#### Example N.M: ... (`path`)`` blocks and bash under
**Execution:** so ``generate_outline_from_module.py`` can add demo slides.

Usage:
  ./scripts/generate_examples_md.py
  ./scripts/generate_examples_md.py --module 1
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EXAMPLE_LINE = re.compile(
    r"^#### Example\s+(\d+)\.(\d+):\s+(.+?)\s+\(`([^`]+)`\)\s*$",
    re.MULTILINE,
)
BASH_FENCE = re.compile(r"```bash\s*\n(.*?)```", re.DOTALL)
EXECUTION = re.compile(
    r"\*\*Execution:\*\*\s*\n```bash\s*\n(.*?)```",
    re.DOTALL,
)


def _example_folder(module: int, path_str: str) -> str:
    """Return EXAMPLES.md folder name (under moduleN/examples/)."""
    p = path_str.strip().replace("\\", "/")
    marker = f"module{module}/examples/"
    if marker in p:
        rest = p.split(marker, 1)[1]
        parts = rest.split("/")
        if len(parts) >= 2 and parts[-1].endswith(".py"):
            return parts[0] + "/"
        if parts:
            return parts[0].rstrip("/") + "/"
    if "/examples/" in p:
        sub = p.split("/examples/", 1)[1]
        return sub.split("/")[0] + "/"
    return "examples/"


def _python_runner(course_root: Path) -> str:
    """Course venv python when present, else system python3."""
    venv_py = course_root / ".venv" / "bin" / "python"
    if venv_py.is_file():
        return ".venv/bin/python"
    return "python3"


def _pick_command(
    body: str,
    module: int,
    folder: str,
    path_str: str,
    course_root: Path,
) -> str:
    """Build a repo-root command that runs the example file reliably."""
    runner = _python_runner(course_root)
    if path_str.endswith(".py"):
        base = f"{runner} {path_str}"
        m = EXECUTION.search(body)
        if m:
            for ln in m.group(1).splitlines():
                ln = ln.strip()
                if not ln or ln.startswith("#"):
                    continue
                if re.match(r"^\+[\w]", ln):
                    return f"{base} {ln}"
        return base

    m = EXECUTION.search(body)
    if m:
        lines = [
            ln.strip()
            for ln in m.group(1).splitlines()
            if ln.strip() and not ln.strip().startswith("#")
        ]
        for ln in lines:
            if ln.startswith("python") or "/python" in ln:
                return ln.replace("python3", runner, 1)
        if lines:
            return lines[-1]
    return f"cd module{module}/examples/{folder.rstrip('/')} && ls -la"


def _section_body(text: str, start: int) -> str:
    rest = text[start:]
    nxt = re.search(r"\n#### Example\s+\d+\.\d+:", rest[1:])
    if nxt:
        return rest[: nxt.start() + 1]
    nxt2 = re.search(r"\n##\s+", rest[1:])
    if nxt2:
        return rest[: nxt2.start() + 1]
    return rest


def examples_for_module(course_root: Path, module: int) -> str:  # noqa: PLR0915
    """Build EXAMPLES.md content for one module."""
    doc = course_root / "docs" / f"MODULE{module}.md"
    if not doc.is_file():
        return ""

    text = doc.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+Module\s+\d+:\s+(.+)$", text, re.MULTILINE)
    mod_title = title_m.group(1).strip() if title_m else f"Module {module}"

    matches = list(EXAMPLE_LINE.finditer(text))
    if not matches:
        return ""

    parts = [
        f"# Module {module} Examples",
        "",
        f"Hands-on examples for **{mod_title}**. "
        f"Generated from `docs/MODULE{module}.md` — edit there, then re-run "
        "`./scripts/generate_examples_md.py`.",
        "",
        "---",
        "",
    ]

    for idx, hm in enumerate(matches, start=1):
        title = hm.group(3).strip()
        path_str = hm.group(4).strip()
        folder = _example_folder(module, path_str)
        body = _section_body(text, hm.end())
        command = _pick_command(body, module, folder, path_str, course_root)

        parts.extend(
            [
                f"## {idx}. {title} (`{folder}`)",
                "",
                f"Source: `{path_str}`",
                "",
                "**Try this** (from course repo root):",
                "",
                "```bash",
                command,
                "```",
                "",
                "---",
                "",
            ]
        )

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--course-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    parser.add_argument("--module", type=int, default=0, help="Single module (0 = all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    course_root = args.course_root.resolve()
    doc_dir = course_root / "docs"
    if not doc_dir.is_dir():
        print(f"ERROR: no docs/: {doc_dir}", file=sys.stderr)
        return 1

    modules: list[int] = []
    for p in sorted(doc_dir.glob("MODULE*.md")):
        m = re.match(r"MODULE(\d+)\.md$", p.name)
        if m:
            modules.append(int(m.group(1)))

    if args.module:
        modules = [args.module]

    written = 0
    for mod in modules:
        if mod == 0:
            ex_dir = course_root / "module0"
            if not ex_dir.is_dir():
                continue
        content = examples_for_module(course_root, mod)
        if not content:
            print(f"SKIP module {mod}: no #### Example sections")
            continue
        out = course_root / f"module{mod}" / "EXAMPLES.md"
        if args.dry_run:
            print(f"DRY module {mod}: would write {out} ({content.count('## ')} sections)")
            written += 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"OK: {out} ({content.count('## ') - 1} examples)")
        written += 1

    if written == 0 and not args.dry_run:
        print("No EXAMPLES.md files written.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
