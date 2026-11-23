# Manual verification

These runs were executed on 23 Nov 2026 in the public W&B project `nyc_airbnb`. The commands already finished. This page is the click-through that confirms each rubric, especially the nine that failed review because the reviewer could not open the live pages.

Do not run `scripts/run_pipeline.sh` or `mlflow run` again. A new run moves the `:latest` alias.

Project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb

Repository: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price

## What you still do

1. Open the W&B project in a private browser window. Pass when the project page loads and does not ask you to log in as the owner. If it asks for a login, open the project settings and set the visibility to public, then check the private window again.
2. Walk the failed-rubric list below. Each item has the page to open and the value that must be on that page.
3. On the production model, open the **Lineage** tab and save a screenshot for the Udacity form. The image must show version `v29`, the alias `prod`, and the chain `sample.csv` → `clean_sample.csv` → `trainval_data.csv` → `random_forest_export`. Do not add that image to the git repository.
4. Paste the submission block at the bottom of this file into the Udacity submission field.

## Version map

Use these versions. `:latest` is not the production model, and it is not the sample1 split.

| Artifact | Version to open | Aliases | What it is |
| --- | --- | --- | --- |
| `clean_sample.csv` | [v0](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/clean_sample/clean_sample.csv/v0) | `reference` and `latest` | Sample1 clean file, 19,001 rows |
| `trainval_data.csv` | [v5](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/trainval_data/trainval_data.csv/v5) | none required | Sample1 train/validation file, 15,200 rows |
| `test_data.csv` | [v5](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/test_data/test_data.csv/v5) | none required | Sample1 test file, 3,801 rows |
| `random_forest_export` | [v29](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v29) | `prod` only | Sample1 winner, validation MAE 33.80 |
| `random_forest_export` | [v30](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v30) | `latest` | Sample2 model from tag `1.0.1`, validation MAE 31.90 |

`prod` was moved from the older v12 onto v29, which is the model trained today with the same winning settings (`max_tfidf_features` 30, `max_features` 0.33).

After the release runs, `sample.csv:latest` is v1 (sample2). The sample1 raw file is [sample.csv v0](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/raw_data/sample.csv/v0). The production model's lineage uses v0.

## Failed rubrics

### 1. `reference` alias

Open [clean_sample.csv v0](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/clean_sample/clean_sample.csv/v0).

Pass when **Aliases** shows both `reference` and `latest` on v0.

Today's cleaning run [hrs718pt](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/hrs718pt) logged this same file (19,001 rows, 0 rows outside the NYC box). W&B kept it as v0 because the file matches the existing version.

### 2. Split artifacts

Open [run gr50k0j7](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/gr50k0j7). Job type is `train_val_test_split`. State is finished.

Then open the two artifacts that run logged:

- [trainval_data.csv v5](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/trainval_data/trainval_data.csv/v5): 15,200 rows
- [test_data.csv v5](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/test_data/test_data.csv/v5): 3,801 rows

Pass when both exist and 15,200 + 3,801 = 19,001. That is `test_size` 0.2. The newer v6 files are the sample2 split from tag `1.0.1`. Use v5 for this check.

### 3. Loadable `random_forest_export`

Open [random_forest_export v29](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v29). **Aliases** shows `prod`. Overview metadata shows `max_features` 0.33.

Open [run q93hch9a](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/q93hch9a). Job type is `test_model`. State is finished. That run loaded `random_forest_export:prod`.

A local `mlflow.sklearn.load_model` of v29 returned a scikit-learn `Pipeline` with steps `preprocessor` and `random_forest`.

Pass when v29 has `prod` and the test run is finished.

### 4. More than two hyperparameter runs

In the project, open **Runs** and filter **Job Type** to `train_random_forest`. Show `mae`, `max_tfidf_features`, and `max_features`.

These four finished today with different settings:

| Run | max_tfidf_features | max_features | Validation MAE | Artifact |
| --- | --- | --- | --- | --- |
| [o6zcj2pc](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/o6zcj2pc) | 10 | 0.1 | 36.28 | v26 |
| [efwr3p3j](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/efwr3p3j) | 10 | 0.33 | 33.87 | v27 |
| [sloz32wc](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/sloz32wc) | 30 | 0.1 | 36.04 | v28 |
| [enbqfpe1](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/enbqfpe1) | 30 | 0.33 | 33.80 | v29 |

Pass when at least three of these are finished and the config pairs differ. The lowest sample1 MAE is 33.80 on `enbqfpe1`. Its **Charts** tab has the feature-importance plot.

### 5. `prod` alias

Open the same [v29](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v29) page. **Aliases** shows `prod`. Overview metadata shows `max_features` 0.33.

Pass when the `prod` chip is on v29. `latest` is on v30, the sample2 model. Leave `prod` on v29.

### 6. Test MAE next to validation MAE

Open **Overview** on each run:

- [q93hch9a](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/q93hch9a): test `mae` is **33.29** (r2 0.581)
- [enbqfpe1](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/enbqfpe1): validation `mae` is **33.80** (r2 0.565)

Pass when those two numbers are the ones on screen. They differ by about half a dollar.

### 7. Lineage

Open [random_forest_export v29](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v29) and click the **Lineage** tab.

Pass when the graph is:

```text
sample.csv → clean_sample.csv → trainval_data.csv → random_forest_export
```

The version is `v29` and the alias chip is `prod`. Save this screenshot for the submission form. This is the one check that still requires your eyes. The API cannot render the graph.

### 8. Release 1.0.0 fails on sample2.csv

1. Open [Release 1.0.0](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.0). The tag is `1.0.0` and the commit is `dfd430d`.
2. Open [run tys16ox1](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/tys16ox1). Job type is `data_tests`.

The tag was run today with `etl.sample='sample2.csv'`. Pytest result:

- `test_proper_boundaries` **failed** with `assert np.int64(1) == 0`
- the other five tests passed
- the cleaned file had 46,428 price-valid rows and one row outside the NYC box
- MLflow stopped, so training did not start

Related runs: download [twgbuh8y](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/twgbuh8y), cleaning [fvle70c6](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/fvle70c6).

Pass when the release page shows `dfd430d` and you can see that this data-test run belongs to that release. The W&B console for `tys16ox1` is short. The failure text above is the pytest output from the live `mlflow run -v 1.0.0`. The earlier run with the same failure is [0o3tdnpk](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/0o3tdnpk).

### 9. Release 1.0.1 trains a new model

1. Open [Release 1.0.1](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.1). The tag is `1.0.1` and the commit is `fb06810`.
2. Open [run zkt33i1l](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/zkt33i1l). Job type is `data_tests`. The live pytest printed **6 passed**. Cleaning run [c427zy1v](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/c427zy1v) dropped the one out-of-bounds row.
3. Open [run h5jmcd2y](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/h5jmcd2y). Job type is `train_random_forest`. **Overview** `mae` is **31.90**. The artifact is [random_forest_export v30](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v30).
4. Return to [v29](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v29) and confirm **Aliases** still shows `prod`.

Pass when v30 exists, its validation MAE is 31.90, and `prod` is still on v29.

## Other rubrics

### Public project and both links

The W&B project URL above opens for a reviewer. In [README.md](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/README.md), the **Submission** section contains:

- https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
- https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price

### sample.csv

Open **Artifacts**, type `raw_data`, [sample.csv](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/raw_data/sample.csv/v0). The **Files** tab lists the csv. Today's sample1 upload is [run 5u0qqphp](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/5u0qqphp). `:latest` is currently the sample2 file, v1.

### EDA notebook

On GitHub, [EDA.ipynb](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/EDA.ipynb) is in the repository root next to [main.py](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/main.py) and [config.yaml](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/config.yaml). [notes.md](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/notes.md) is the checklist that notebook follows.

### basic_cleaning files

Open these three files:

- [src/basic_cleaning/conda.yml](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/src/basic_cleaning/conda.yml) pins pandas
- [src/basic_cleaning/MLproject](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/src/basic_cleaning/MLproject) has `input_artifact`, `output_artifact`, `output_type`, `output_description` (strings) and `min_price`, `max_price` (floats)
- [src/basic_cleaning/run.py](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/src/basic_cleaning/run.py) filters price, converts `last_review`, and keeps longitude [-74.25, -73.50] and latitude [40.5, 41.2]

The uploaded file is `clean_sample.csv` v0 from rubric 1.

### Data tests, including row count and price range

[src/data_check/test_data.py](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/src/data_check/test_data.py) defines `test_row_count` (more than 15,000 rows and fewer than 1,000,000) and `test_price_range` (prices from 10 to 350).

Today's check against `clean_sample.csv:latest` and `clean_sample.csv:reference` printed **6 passed**. The step resumes [run 214g6keg](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/214g6keg) (`wandb.init(..., resume=True)`), job type `data_tests`. Pass when **Logs** show 6 passed.

### Training script

[src/train_random_forest/run.py](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/blob/main/src/train_random_forest/run.py) contains `SimpleImputer(strategy="most_frequent")`, `OneHotEncoder`, `sk_pipe.fit`, `mlflow.sklearn.save_model`, and `run.summary["mae"]`.

[Run enbqfpe1](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/enbqfpe1) **Overview** shows `mae` 33.80. **Charts** shows the feature-importance bar chart.

### Git tags 1.0.0 and 1.0.1

In the terminal at the repository root, peel the annotated tags. `git rev-parse --short 1.0.0` alone prints the tag object, not the commit.

```bash
git rev-parse --short '1.0.0^{commit}'
git rev-parse --short '1.0.1^{commit}'
```

Pass when the first command prints `dfd430d` and the second prints `fb06810`. The GitHub pages are the ones in steps 8 and 9. Both release pages returned HTTP 200 and contain those commits. `gh` is not logged in on this machine, so confirm the release titles in the browser.

## Submission text

```text
Repository platform: GitHub
Repository URL: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price
W&B project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
```

If the form asks for an image, upload the v29 **Lineage** screenshot only.
