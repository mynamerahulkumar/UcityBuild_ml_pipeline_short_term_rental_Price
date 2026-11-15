#!/usr/bin/env bash
# Run the pipeline from the repository root.
# Examples:
#   scripts/run_pipeline.sh
#   scripts/run_pipeline.sh -P steps=download,basic_cleaning
set -euo pipefail

cd "$(dirname "$0")/.."

# The preinstalled Anaconda at /opt/anaconda3 is not executable on this Mac.
# Point MLflow at the arm64 Miniforge install when that is the working conda.
if [[ -x /opt/homebrew/Caskroom/miniforge/base/bin/conda ]]; then
  export MLFLOW_CONDA_HOME="${MLFLOW_CONDA_HOME:-/opt/homebrew/Caskroom/miniforge/base}"
  export CONDA_EXE="${MLFLOW_CONDA_HOME}/bin/conda"
  export PATH="/opt/homebrew/Caskroom/miniforge/base/envs/nyc_airbnb_dev/bin:${MLFLOW_CONDA_HOME}/bin:${PATH}"
fi

# shellcheck disable=SC1091
source "$(dirname "$0")/wandb_env.sh"

mlflow run . "$@"
