#!/usr/bin/env bash
# Run the single shared Slidev install (slides/slidev-theme-dtlh) against any
# deck's slides.md. No per-deck node_modules required.
# Adapted from ops-re/.local-bin/slide.sh.
#
# Usage:
#   slides/slide.sh <deck-dir> [dev|build|export]   # default: dev
#
# Examples:
#   slides/slide.sh slides/pitch
#   slides/slide.sh slides/pitch export
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THEME="$HERE/slidev-theme-dtlh"
SLIDEV="$THEME/node_modules/.bin/slidev"

if [ ! -x "$SLIDEV" ]; then
  echo "Shared Slidev is not installed yet. Run:" >&2
  echo "  (cd \"$THEME\" && npm install)" >&2
  exit 1
fi

DECK_DIR="${1:?Usage: slide.sh <deck-dir> [dev|build|export]}"
CMD="${2:-dev}"
DECK_DIR="$(cd "$DECK_DIR" && pwd)"
[ -f "$DECK_DIR/slides.md" ] || { echo "No slides.md found in $DECK_DIR" >&2; exit 1; }

# Run from inside the deck so Vite's project root is the deck itself. Its
# workspace-root search then walks up to the repo's .git, which puts the whole
# repo (the shared addon plus the deck's images/) inside server.fs.allow.
cd "$DECK_DIR"
case "$CMD" in
  dev)    exec "$SLIDEV" slides.md --open ;;
  build)  exec "$SLIDEV" build slides.md ;;
  # --per-slide + waits: plain `slidev export` renders one print pass and races
  # on image loading, silently dropping images from ~half the slides. Per-slide
  # rendering waits for each slide's network to settle before capture.
  export) exec "$SLIDEV" export slides.md --per-slide --wait-until networkidle --wait 600 ;;
  *)      exec "$SLIDEV" "$CMD" slides.md ;;
esac
