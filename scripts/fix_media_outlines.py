#!/usr/bin/env python3
"""Post-process generated media outlines for learn_uvm_pyuvm conventions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

# learn_uvm_pyuvm orchestrators do not implement --check (unlike learn_unix_git).
SELF_CHECK_REPLACEMENT = ("./scripts/module{mod}.sh --help", "Usage:")

# Substrings that often appear in example stdout (for capture verification).
EXPECT_HINTS: list[tuple[str, str]] = [
    ("transaction.py", "Transaction"),
    ("decorators_example", "decorator"),
    ("async_example", "Async/Await"),
    ("async_await", "Example completed"),
    ("data_structures_example", "Queue"),
    ("error_handling", "Error"),
    ("class_hierarchy", "uvm"),
    ("phases_example", "phase"),
    ("factory_example", "Factory"),
    ("config_example", "config"),
    ("reporting_example", "UVM_"),
    ("driver_example", "Driver"),
    ("monitor_example", "Monitor"),
    ("sequencer_example", "sequence"),
    ("agent_example", "Agent"),
    ("scoreboard_example", "Scoreboard"),
    ("tlm_example", "TLM"),
    ("module0.sh", "verilator"),
    ("verilator --version", "Verilator"),
    ("python3 -c", "cocotb"),
]


def _guess_expect(command: str) -> str:
    cmd = command.lower()
    for needle, expect in EXPECT_HINTS:
        if needle.lower() in cmd:
            return expect
    if "python3 " in command and "_example" in command:
        return "Example"
    return ""


def _rebuild_manifest(
    mod: int,
    course: str,
    slides: list[dict[str, Any]],
) -> dict[str, Any]:
    """Rebuild manifest.yaml assets from outline demo/image/two_column slides."""
    lp_slide = 4
    for i, slide in enumerate(slides, start=1):
        if slide.get("type") == "image" and "learning_path" in str(slide.get("image", "")):
            lp_slide = i
            break

    assets: list[dict[str, Any]] = [
        {
            "id": "learning_path",
            "type": "diagram",
            "file": "assets/diagrams/learning_path.png",
            "source": "assets/diagrams/learning_path.mmd",
            "generator": "render_diagrams.sh",
            "slides": [lp_slide],
            "license": f"{course} course materials",
        },
    ]
    seen_diagrams: set[str] = {"learning_path"}

    for i, slide in enumerate(slides, start=1):
        img = ""
        if slide.get("type") == "image":
            img = str(slide.get("image", ""))
        elif slide.get("type") == "two_column":
            img = str(slide.get("right", ""))
        if not img.startswith("assets/diagrams/") or not img.endswith(".png"):
            continue
        asset_id = Path(img).stem
        if asset_id in seen_diagrams:
            for entry in assets:
                if entry.get("id") == asset_id:
                    entry.setdefault("slides", []).append(i)
            continue
        seen_diagrams.add(asset_id)
        assets.append(
            {
                "id": asset_id,
                "type": "diagram",
                "file": img,
                "source": f"assets/diagrams/{asset_id}.mmd",
                "generator": "render_diagrams.sh",
                "slides": [i],
                "license": f"{course} course materials",
            },
        )

    for i, slide in enumerate(slides, start=1):
        if slide.get("type") != "demo":
            continue
        shot = slide.get("screenshot")
        if not shot:
            continue
        asset_id = Path(str(shot)).stem
        entry: dict[str, Any] = {
            "id": asset_id,
            "type": "screenshot",
            "file": str(shot),
            "capture_command": str(slide.get("command", "")),
            "cwd": ".",
            "slides": [i],
        }
        if slide.get("expect_stdout_contains"):
            entry["expect_stdout_contains"] = slide["expect_stdout_contains"]
        assets.append(entry)

    return {"module": mod, "course": course, "assets": assets}


def _venv_python(course_root: Path) -> str | None:
    py = course_root / ".venv" / "bin" / "python"
    return str(py) if py.is_file() else None


def _use_venv_python(command: str, course_root: Path) -> str:
    venv_py = _venv_python(course_root)
    if not venv_py or venv_py in command:
        return command
    if command.startswith("python3 "):
        return command.replace("python3", venv_py, 1)
    if 'python3 -c "' in command or "python3 -c '" in command:
        return command.replace("python3", venv_py, 1)
    return command


MAX_BULLET_CHARS = 140


def _truncate_bullet(text: str, limit: int = MAX_BULLET_CHARS) -> str:
    s = str(text).strip()
    if len(s) <= limit:
        return s
    cut = limit - 3
    chunk = s[:cut]
    if " " in chunk:
        chunk = chunk.rsplit(" ", 1)[0]
    return chunk.rstrip(".,;:") + "..."


def patch_outline(path: Path, course_root: Path) -> bool:
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    slides: list[dict[str, Any]] = data.get("slides", [])
    changed = False
    mod_m = re.search(r"module(\d+)", str(path))
    mod = int(mod_m.group(1)) if mod_m else 0
    course = str(data.get("course", "learn_uvm_pyuvm"))

    for slide in slides:
        if slide.get("type") == "bullets" and slide.get("title") == "Overview":
            bullets = slide.get("bullets", [])
            new_bullets = [_truncate_bullet(b) for b in bullets]
            if new_bullets != bullets:
                slide["bullets"] = new_bullets
                changed = True
        if slide.get("type") == "demo" and "self-check" in str(slide.get("title", "")).lower():
            cmd, expect = SELF_CHECK_REPLACEMENT
            slide["command"] = cmd.format(mod=mod)
            slide["expect_stdout_contains"] = expect
            slide["title"] = f"Module {mod} orchestrator"
            changed = True
        if slide.get("type") == "bullets" and slide.get("title") == "Summary & next steps":
            bullets = slide.get("bullets", [])
            new_bullets: list[str] = []
            for b in bullets:
                nb = b
                if "--check" in b:
                    nb = b.replace(
                        f"./scripts/module{mod}.sh --check",
                        f"./scripts/module{mod}.sh --help",
                    )
                    changed = True
                if "CHECKLIST.md" in b and mod == 0:
                    nb = "Verify tools: verilator, cocotb, pyuvm (see MODULE0.md)"
                    changed = True
                new_bullets.append(nb)
            slide["bullets"] = new_bullets

        if slide.get("type") == "demo" and slide.get("command"):
            cmd = _use_venv_python(str(slide["command"]), course_root)
            if cmd != slide.get("command"):
                slide["command"] = cmd
                changed = True
            exp = _guess_expect(cmd)
            # pyuvm/cocotb examples need a full toolchain; capture terminal output
            # without strict stdout checks so slides still get screenshots.
            if mod >= 3 and (".venv/bin/python" in cmd or "_example" in cmd):
                if slide.pop("expect_stdout_contains", None):
                    changed = True
                exp = ""
            elif mod >= 3 and "_example" in cmd:
                exp = ""
            elif "pyuvm" in cmd or "_example" in cmd:
                exp = exp or "Example"
            shot = str(slide.get("screenshot", ""))
            if "async_await" in shot or "async_example" in cmd:
                exp = "Example completed"
            if exp and slide.get("expect_stdout_contains") != exp:
                slide["expect_stdout_contains"] = exp
                changed = True
            elif exp and not slide.get("expect_stdout_contains"):
                slide["expect_stdout_contains"] = exp
                changed = True

    manifest_path = path.parent / "assets" / "manifest.yaml"
    if changed or manifest_path.is_file():
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            yaml.dump(
                _rebuild_manifest(mod, course, slides),
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8",
        )

    if changed:
        path.write_text(
            yaml.dump(data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--course-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args()
    course = args.course_root.resolve()
    media = course / "media"
    n = 0
    for outline in sorted(media.glob("module*/outline.yaml")):
        if patch_outline(outline, course):
            print(f"Patched {outline}")
            n += 1
    print(f"Done ({n} outline(s) updated).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
