# Course media — slides, PDF, and video

Generated teaching assets for each module. Source content: `docs/MODULEN.md` and `moduleN/EXAMPLES.md` (generated from doc examples).

See [INDEX.md](INDEX.md) for links to every module’s PPTX, PDF, and video.

## Build (one command)

From the `learn_uvm_pyuvm` repo root:

```bash
./scripts/build_all_media.sh
```

| Flag | Purpose |
|------|---------|
| `--install-deps` | `sudo apt install` LibreOffice Impress, ffmpeg, poppler |
| `--pptx-only` | Skip PDF and video |
| `--module 1` | Single module (supports `0` for setup) |
| `--regenerate-outlines` | Refresh `EXAMPLES.md`, `outline.yaml`, `manifest.yaml` |
| `--run-demos` | Capture terminal screenshots (slow; needs `.venv` + tools) |
| `--skip-capture` | Reuse existing screenshots |

Requires the Cursor skill: `~/.cursor/skills/module-to-slides-video` (run `bash …/scripts/setup.sh` once).

## Regenerate content from docs

```bash
./scripts/generate_examples_md.py
./scripts/build_all_media.sh --regenerate-outlines --pptx-only --skip-capture
```

Edit `docs/MODULEN.md` first; optional per-demo fixes in `media/outline_overrides.yaml`.

### Design architecture and testing methods (slides)

Each `docs/MODULEN.md` includes auto-maintained sections (before **Topics Covered**):

- **Design Architecture** — DUT hierarchy, testbench/UVM structure, repo layout
- **Verification & Testing Methods** — stimulus, checking, regression, closure

Source of truth for slide supplements: `docs/module_architecture_content.yaml` (also injects **Before You Start**, **Key files to study**, and **Command Reference** into each `docs/MODULEN.md`). Architecture code slides: `media/outline_overrides.yaml`. Apply and refresh slides:

```bash
python3 scripts/apply_module_architecture_content.py
python3 scripts/generate_module_diagrams.py
./scripts/build_all_media.sh --regenerate-outlines
```

Per-module diagrams: `media/moduleN/assets/diagrams/{rtl_architecture,verification_architecture,testing_methods}.mmd` → PNG via the skill’s `render_diagrams.sh`.

## Per-module outputs

| File | Description |
|------|-------------|
| `outline.yaml` | Slide plan for `build_slides.py` |
| `script.md` | Narration / timing notes for video |
| `assets/manifest.yaml` | Images and demo capture commands |
| `slides.pptx` | Primary deck |
| `slides.pdf` | PDF export |
| `video.mp4` | Silent preview (~8 s/slide; add `audio/narration.wav` for voice) |

## Git

`frames/` and `*.log` are gitignored. Large binaries (`slides.pptx`, `video.mp4`) may be omitted from git; use release artifacts or LFS if needed.
