#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"
ZIP_PATH="${1:-}"

if [[ -z "$ZIP_PATH" ]]; then
  ZIP_PATH="$(ls -1t "$DIST_DIR"/*.zip 2>/dev/null | head -n1 || true)"
fi

if [[ -z "$ZIP_PATH" || ! -f "$ZIP_PATH" ]]; then
  echo "No extension zip found. Run scripts/build_extension.sh first." >&2
  exit 1
fi

unzip -l "$ZIP_PATH"
