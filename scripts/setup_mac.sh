#!/usr/bin/env bash
# Create the local development environment used to launch the pipeline.
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v conda >/dev/null 2>&1; then
  echo "conda is not on PATH. Install arm64 Miniforge first: brew install miniforge"
  exit 1
fi

conda env create -f environment.yml
echo "Activate it with: conda activate nyc_airbnb_dev"
echo "Then authenticate Weights & Biases with: wandb login"
