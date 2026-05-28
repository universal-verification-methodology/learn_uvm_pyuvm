# Scripts

| Script | Purpose |
|--------|---------|
| `module0.sh` … `module8.sh` | Run examples and tests per module |
| `build_all_media.sh` | Build slides (pptx), PDF, and video for all modules |
| `verify_all_media.sh` | Verify `media/moduleN/` assets and outlines |
| `generate_examples_md.py` | Create `moduleN/EXAMPLES.md` from `docs/MODULEN.md` |
| `fix_media_outlines.py` | Post-process outlines (venv python, orchestrator demos) |
| `install_*.sh` / `uninstall_*.sh` | Tool setup |

## Media pipeline

Requires [module-to-slides-video](~/.cursor/skills/module-to-slides-video) (`bash …/scripts/setup.sh` once).

```bash
# Full regenerate + pptx (recommended first pass)
./scripts/build_all_media.sh --regenerate-outlines --pptx-only

# All modules with PDF + silent video
./scripts/build_all_media.sh --install-deps

# Single module
./scripts/build_all_media.sh --module 3

./scripts/verify_all_media.sh
```

Outputs live under `media/moduleN/` — see [media/README.md](../media/README.md).
