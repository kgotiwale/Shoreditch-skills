#!/usr/bin/env bash
# Symlink every skill in this repo into ~/.claude/skills/ so they're available
# in any project. Symlinks (not copies) mean `git pull` updates them in place.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills"
DEST="$HOME/.claude/skills"

mkdir -p "$DEST"

for skill in "$SRC"/*/; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  target="$DEST/$name"

  if [ -L "$target" ]; then
    ln -sfn "$skill" "$target"
    echo "  relinked  $name"
  elif [ -e "$target" ]; then
    echo "  SKIPPED   $name — $target exists and is not a symlink."
    echo "            Move or delete it, then re-run."
    continue
  else
    ln -s "$skill" "$target"
    echo "  linked    $name"
  fi
done

echo
echo "Done. Restart Claude Code — the skills above are now available in any project."
