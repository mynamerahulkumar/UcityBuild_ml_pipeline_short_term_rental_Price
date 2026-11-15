#!/usr/bin/env bash
# Run the data_check pytest suite through MLflow.
# Requires clean_sample.csv:latest and clean_sample.csv:reference in W&B.
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -x /opt/homebrew/Caskroom/miniforge/base/bin/conda ]]; then
  export MLFLOW_CONDA_HOME="${MLFLOW_CONDA_HOME:-/opt/homebrew/Caskroom/miniforge/base}"
  export CONDA_EXE="${MLFLOW_CONDA_HOME}/bin/conda"
  export PATH="/opt/homebrew/Caskroom/miniforge/base/envs/nyc_airbnb_dev/bin:${MLFLOW_CONDA_HOME}/bin:${PATH}"
fi

# shellcheck disable=SC1091
source "$(dirname "$0")/wandb_env.sh"

mlflow run . -P steps=data_check
