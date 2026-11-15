# Load a local W&B key into the environment. The value is never printed.
# Source this file from the repository root.

if [[ -z "${WANDB_API_KEY:-}" && -f .env ]]; then
  WANDB_API_KEY="$(
    python3 - << 'PY'
from pathlib import Path

for line in Path(".env").read_text().splitlines():
    if line.startswith("wandb_api_key="):
        value = line.split("=", 1)[1].strip().strip('"').strip("'").strip()
        value = value.rstrip("\u201d").rstrip("\u201c")
        print(value, end="")
        break
PY
  )"
  export WANDB_API_KEY
fi
