#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"

mkdir -p "$DIST_DIR"

echo "[build] validating source tree..."
(cd "$ROOT_DIR" && blender --command extension validate)

echo "[build] building extension artifact into dist/..."
(cd "$ROOT_DIR" && blender --command extension build --output-dir "$DIST_DIR")

echo "[build] done. artifact(s):"
ls -1 "$DIST_DIR"/*.zip
