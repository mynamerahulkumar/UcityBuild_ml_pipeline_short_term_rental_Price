"""Confirm the development environment can import the pipeline libraries."""

import numpy
import pandas
import sklearn
import mlflow
import wandb

print("Environment OK")
print(f"numpy {numpy.__version__}")
print(f"pandas {pandas.__version__}")
print(f"scikit-learn {sklearn.__version__}")
print(f"mlflow {mlflow.__version__}")
print(f"wandb {wandb.__version__}")
