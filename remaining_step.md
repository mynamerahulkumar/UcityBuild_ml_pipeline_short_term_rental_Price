# Remaining steps

Checked on 20 Nov 2026 against [docs/project_rubrics.md](docs/project_rubrics.md). The pipeline scripts, W&B aliases, and GitHub releases already satisfy the rubric. The only action left is the Udacity submission form, plus one look at the lineage page before you submit.

`scripts/check_environment.py` printed `Environment OK`. An anonymous W&B query returned project `nyc_airbnb` with access `USER_READ`, so a reviewer can open it without your login. GitHub release pages for `1.0.0` and `1.0.1` both return HTTP 200.

Leave the finished pipeline as it is. Another `scripts/run_pipeline.sh`, another Hydra sweep, or another `mlflow run` of tag `1.0.0` or `1.0.1` would upload new `:latest` artifacts. `clean_sample.csv:reference` and `random_forest_export:prod` must stay where they are.

## Already satisfied

| Rubric item in docs/project_rubrics.md | Evidence |
| --- | --- |
| Public W&B project `nyc_airbnb` | Access `USER_READ`. https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb |
| Both links in the README | [README.md](README.md) Submission section |
| `sample.csv` in W&B | `sample.csv:latest` is `v0` |
| `EDA.ipynb` in the repo root | On `main`, with saved cell outputs. It loads `sample.csv:latest`, keeps prices from 10 to 350, converts `last_review`, and leaves missing values missing. [notes.md](notes.md) is the checklist that run follows. |
| `src/basic_cleaning` with `conda.yml`, `MLproject`, `run.py`, pandas, and the six parameters | Present. Parameters come from [config.yaml](config.yaml). |
| `clean_sample.csv` uploaded | `clean_sample.csv:v0` carries aliases `reference` and `latest`. Versions `v1` and `v2` exist and have no aliases. Leave `reference` on `v0`. |
| `test_row_count` and `test_price_range` | Implemented in [src/data_check/test_data.py](src/data_check/test_data.py). W&B has 3 `data_tests` runs. |
| `trainval_data.csv` and `test_data.csv` | Both exist. `:latest` is `v2` for each. |
| `train_random_forest` completed and MAE logged | 26 training runs. Best validation MAE is 33.80 on run `zyzw136a` (`max_tfidf_features=30`, `max_features=0.33`). |
| More than two hyperparameter runs | 16 distinct `(max_tfidf_features, max_features)` pairs, including the required 10 / 15 / 30 by 0.1 / 0.33 / 0.5 / 0.75 / 1 grid. |
| `prod` on the best validation model | `random_forest_export:v12` alias `prod`, logged by run `zyzw136a`. `:latest` is `v24`. Leave `prod` on `v12`. |
| Test MAE comparable to validation MAE | `test_regression_model` run `1p40q31a` scored test MAE 33.29 against validation MAE 33.80. |
| Release `1.0.0` | Annotated tag `1.0.0` is commit `dfd430d`. That commit has no geographic filter. https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.0 |
| `sample2.csv` fails on `1.0.0`, then `1.0.1` trains a new model | Tag `1.0.1` is commit `fb06810` and drops rows outside longitude [-74.25, -73.50] and latitude [40.5, 41.2]. https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.1 |

[config.yaml](config.yaml) already stores the winning defaults: `max_tfidf_features: 30` and `random_forest.max_features: 0.33`.

## What you still do

### 1. Udacity Submission Details

Open the project submission form. The field is labeled optional. [docs/project_rubrics.md](docs/project_rubrics.md) requires it anyway. Paste this:

```text
Repository platform: GitHub
Repository URL: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price
W&B project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
```

The same W&B URL and GitHub URL are already in the README. Use the `wandb.ai` link above. It redirects to the current W&B host and is the public project the reviewer can open.

### 2. Open the lineage page once

Before you submit, open:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12

Confirm the Lineage view shows this chain, and that the model version is `v12` with alias `prod`:

`sample.csv` → `clean_sample.csv` → `trainval_data.csv` → `random_forest_export`

The reviewer uses this same public page. You do not need to change anything if that chain is visible.

## Screenshots

[docs/project_rubrics.md](docs/project_rubrics.md) does not ask for screenshot files. Do not add images to the repository. The reviewer checks the public W&B project and the GitHub repository directly.

If the Udacity form has an image upload that the written rubric does not mention, capture only the lineage page above. The image must show version `v12`, alias `prod`, and the chain `sample.csv` → `clean_sample.csv` → `trainval_data.csv` → `random_forest_export`. Upload that image in the form only. Leave it out of the git repository.
