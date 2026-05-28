#!/usr/bin/env bash
#
# Build slides (pptx), PDF, and video for all learn_uvm_pyuvm modules.
#
# Usage (from repo root):
#   ./scripts/build_all_media.sh
#   ./scripts/build_all_media.sh --pptx-only
#   ./scripts/build_all_media.sh --module 1
#   ./scripts/build_all_media.sh --regenerate-outlines
#   ./scripts/build_all_media.sh --install-deps
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILL_ROOT="${SKILL_ROOT:-$HOME/.cursor/skills/module-to-slides-video}"
SKILL_SCRIPTS="$SKILL_ROOT/scripts"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

PPTX_ONLY=0
REGENERATE=0
INSTALL_DEPS=0
MODULES_FILTER=""
SECONDS_PER_SLIDE=8
RUN_DEMOS=0
SKIP_CAPTURE=0
EXTRA_ARGS=()

usage() {
  sed -n '3,14p' "$0" | sed 's/^# \{0,1\}//'
  echo ""
  echo "Options:"
  echo "  --pptx-only            Skip PDF and video"
  echo "  --module N             Only module N or list 0,1,2"
  echo "  --regenerate-outlines  EXAMPLES.md + outline.yaml from docs/"
  echo "  --install-deps         sudo apt install libreoffice ffmpeg poppler-utils"
  echo "  --seconds-per-slide N  Video timing (default: 8)"
  echo "  --run-demos            Run capture commands during verify (slow)"
  echo "  --skip-capture         Reuse existing screenshots"
  echo "  --no-narration         Silent video (no TTS)"
  echo "  -h, --help             Show help"
}

log() { echo -e "${CYAN}==>${NC} $*"; }
ok() { echo -e "${GREEN}OK:${NC} $*"; }
warn() { echo -e "${YELLOW}WARN:${NC} $*" >&2; }
die() { echo -e "${RED}ERROR:${NC} $*" >&2; exit 1; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pptx-only) PPTX_ONLY=1; shift ;;
    --regenerate-outlines) REGENERATE=1; shift ;;
    --install-deps) INSTALL_DEPS=1; shift ;;
    --module) MODULES_FILTER="$2"; shift 2 ;;
    --seconds-per-slide) SECONDS_PER_SLIDE="$2"; shift 2 ;;
    --run-demos) RUN_DEMOS=1; shift ;;
    --skip-capture) SKIP_CAPTURE=1; shift ;;
    --no-narration) EXTRA_ARGS+=(--no-narration); shift ;;
    -h|--help) usage; exit 0 ;;
    *) EXTRA_ARGS+=("$1"); shift ;;
  esac
done

[[ -d "$SKILL_SCRIPTS" ]] || die "Skill not found: $SKILL_SCRIPTS (run: bash ~/.cursor/skills/module-to-slides-video/scripts/setup.sh)"

install_system_deps() {
  log "Installing system packages (sudo required)..."
  sudo DEBIAN_FRONTEND=noninteractive apt-get update -qq
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
    libreoffice-impress libreoffice-core libreoffice-writer \
    default-jre-headless ffmpeg poppler-utils
  ok "System dependencies installed"
}

check_system_deps() {
  local missing=0
  if [[ $PPTX_ONLY -eq 0 ]]; then
    command -v soffice >/dev/null 2>&1 || command -v libreoffice >/dev/null 2>&1 || {
      warn "LibreOffice not found — PDF/video may be skipped (--install-deps)"
      missing=1
    }
    command -v ffmpeg >/dev/null 2>&1 || {
      warn "ffmpeg not found — video will be skipped"
      missing=1
    }
  fi
  return $missing
}

log "Course: $COURSE_ROOT"
log "Skill:  $SKILL_ROOT"

if [[ $INSTALL_DEPS -eq 1 ]]; then
  install_system_deps
fi

log "Setting up Python skill venv..."
bash "$SKILL_SCRIPTS/setup.sh" | tail -3

if [[ $REGENERATE -eq 1 ]]; then
  log "Generating moduleN/EXAMPLES.md from docs..."
  "$SKILL_SCRIPTS/run_python.sh" "$COURSE_ROOT/scripts/generate_examples_md.py" --course-root "$COURSE_ROOT"
  log "Generating outline.yaml for all modules..."
  "$SKILL_SCRIPTS/run_python.sh" "$SKILL_SCRIPTS/generate_outline_from_module.py" "$COURSE_ROOT"
  log "Patching outlines (expect strings, summary bullets)..."
  "$SKILL_SCRIPTS/run_python.sh" "$COURSE_ROOT/scripts/fix_media_outlines.py" --course-root "$COURSE_ROOT"
fi

BUILD_ARGS=("$COURSE_ROOT")
[[ -n "$MODULES_FILTER" ]] && BUILD_ARGS+=(--module "$MODULES_FILTER")
[[ $PPTX_ONLY -eq 1 ]] && BUILD_ARGS+=(--pptx-only)
[[ $RUN_DEMOS -eq 1 ]] && BUILD_ARGS+=(--run-demos)
[[ $SKIP_CAPTURE -eq 1 ]] && BUILD_ARGS+=(--skip-capture)
BUILD_ARGS+=(--seconds-per-slide "$SECONDS_PER_SLIDE")
BUILD_ARGS+=(--no-narration)
BUILD_ARGS+=("${EXTRA_ARGS[@]}")

check_system_deps || true

log "Building media..."
bash "$SKILL_SCRIPTS/build_course_media.sh" "${BUILD_ARGS[@]}"

echo ""
log "Outputs:"
for f in "$COURSE_ROOT"/media/module*/slides.pptx; do
  [[ -f "$f" ]] && echo "  pptx: $f"
done
if [[ $PPTX_ONLY -eq 0 ]]; then
  for f in "$COURSE_ROOT"/media/module*/slides.pdf; do
    [[ -f "$f" ]] && echo "  pdf:  $f"
  done
  for f in "$COURSE_ROOT"/media/module*/video.mp4; do
    [[ -f "$f" ]] && echo "  mp4:  $f"
  done
fi

ok "Done. See $COURSE_ROOT/media/INDEX.md"
