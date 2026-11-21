# Remaining steps

The pipeline checks that can be run from this machine were run on 22 Nov 2026. Tags `1.0.0` and `1.0.1` were not moved. `prod` is still on `random_forest_export:v12`. `reference` and `latest` are both on `clean_sample.csv:v0`.

Do not start another Hydra sweep, and do not run `mlflow run` of either release again. Another run would log new `:latest` artifacts.

## 1. Confirm lineage in the browser

Open:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12

Open the Lineage tab. The graph should show:

`sample.csv` → `clean_sample.csv` → `trainval_data.csv` → `random_forest_export`

The version on that page is `v12` and the alias is `prod`.

The same links are in the Submission section of [README.md](README.md).

## 2. Resubmit on Udacity

Paste this into Submission Details:

```text
Repository platform: GitHub
Repository URL: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price
W&B project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
```

If the form asks for an image, upload a screenshot of the lineage page only. The image must show version `v12`, alias `prod`, and the chain above. Do not add that image to the git repository.
