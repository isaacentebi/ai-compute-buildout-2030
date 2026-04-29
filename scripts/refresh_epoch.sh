#!/usr/bin/env bash
# Pull the latest Epoch Frontier Data Centers snapshot and rebuild the tracker.
# CC BY 4.0 — Epoch AI, Frontier Data Centers, https://epoch.ai/data/data-centers
set -euo pipefail

cd "$(dirname "$0")/.."

DATE=$(date -u +%Y%m%d)
SNAP_DIR="epoch_data_centers/snapshots/$DATE"
mkdir -p "$SNAP_DIR"

echo "[refresh_epoch] downloading 2026-$DATE snapshot..."
for f in data_centers.csv data_center_timelines.csv data_center_chillers.csv data_center_cooling_towers.csv; do
  curl -fsSL -o "$SNAP_DIR/$f" "https://epoch.ai/data/data_centers/$f"
  lines=$(wc -l <"$SNAP_DIR/$f")
  echo "  OK  $f  ($lines lines)"
done

echo "[refresh_epoch] swapping into epoch_data_centers/..."
cp "$SNAP_DIR"/*.csv epoch_data_centers/

echo "[refresh_epoch] rebuilding compiled.json..."
( cd epoch_data_centers && python3 compile.py >/dev/null )

echo "[refresh_epoch] rebuilding tracker..."
python3 scripts/build_tracker.py

echo "[refresh_epoch] done."
