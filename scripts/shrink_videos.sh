#!/usr/bin/env bash
# Shrink autoplay loop MP4s in docs/videos/ (or any dir) using ffmpeg.
#
# Usage:
#   scripts/shrink_videos.sh                       # shrink docs/videos in place, defaults
#   scripts/shrink_videos.sh path/to/dir           # shrink a different dir
#   WIDTH=480 CRF=30 FPS=24 scripts/shrink_videos.sh
#   DRY_RUN=1 scripts/shrink_videos.sh             # just print what would be done
#   KEEP_BACKUP=1 scripts/shrink_videos.sh         # keep originals as *.orig.mp4

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

TARGET_DIR="${1:-$REPO_ROOT/docs/videos}"
WIDTH="${WIDTH:-720}"
CRF="${CRF:-28}"
FPS="${FPS:-24}"
PRESET="${PRESET:-slow}"
DRY_RUN="${DRY_RUN:-0}"
KEEP_BACKUP="${KEEP_BACKUP:-0}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found. Install it: sudo apt install ffmpeg" >&2
  exit 1
fi

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Directory not found: $TARGET_DIR" >&2
  exit 1
fi

shopt -s nullglob nocaseglob
mapfile -t FILES < <(find "$TARGET_DIR" -maxdepth 1 -type f -iname '*.mp4' | sort)
shopt -u nocaseglob

if (( ${#FILES[@]} == 0 )); then
  echo "No .mp4 files in $TARGET_DIR"
  exit 0
fi

printf 'Target dir : %s\n' "$TARGET_DIR"
printf 'Files      : %d\n' "${#FILES[@]}"
printf 'Encoder    : libx264 crf=%s preset=%s\n' "$CRF" "$PRESET"
printf 'Scale/FPS  : width<=%s, fps=%s, audio stripped\n' "$WIDTH" "$FPS"
printf 'Dry run    : %s\n' "$DRY_RUN"
printf 'Keep backup: %s\n' "$KEEP_BACKUP"
echo

total_before=0
total_after=0

for src in "${FILES[@]}"; do
  base="$(basename "$src")"
  case "$base" in
    *.orig.mp4|*.min.mp4) continue ;;
  esac

  size_before=$(stat -c '%s' "$src")
  total_before=$(( total_before + size_before ))
  printf '→ %-40s %6.2f MB ' "$base" "$(awk "BEGIN{print $size_before/1048576}")"

  tmp="${src%.mp4}.__tmp__.mp4"

  if [[ "$DRY_RUN" == "1" ]]; then
    echo "(dry run)"
    continue
  fi

  ffmpeg -y -nostdin -loglevel error \
    -i "$src" \
    -vf "scale='min($WIDTH,iw)':-2,fps=$FPS" \
    -c:v libx264 -crf "$CRF" -preset "$PRESET" \
    -pix_fmt yuv420p -movflags +faststart -an \
    "$tmp"

  if [[ "$KEEP_BACKUP" == "1" ]]; then
    mv "$src" "${src%.mp4}.orig.mp4"
  fi
  mv "$tmp" "$src"

  size_after=$(stat -c '%s' "$src")
  total_after=$(( total_after + size_after ))
  pct=$(awk "BEGIN{printf \"%.1f\", (1 - $size_after/$size_before) * 100}")
  printf '→ %6.2f MB  (-%s%%)\n' "$(awk "BEGIN{print $size_after/1048576}")" "$pct"
done

if [[ "$DRY_RUN" != "1" && "$total_before" -gt 0 ]]; then
  echo
  pct=$(awk "BEGIN{printf \"%.1f\", (1 - $total_after/$total_before) * 100}")
  printf 'TOTAL: %.2f MB → %.2f MB  (-%s%%)\n' \
    "$(awk "BEGIN{print $total_before/1048576}")" \
    "$(awk "BEGIN{print $total_after/1048576}")" \
    "$pct"
fi
