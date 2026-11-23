# Startup

What to run, where to run it, and where to check the result. How the code works is in [architecture.md](architecture.md).

The nine rubrics that failed last time are already satisfied by runs from 22 Nov 2026. Do not run `scripts/run_pipeline.sh` or `mlflow run` again. A new run logs a new `:latest` artifact. Your job is to open the page in **Check** and confirm the pass value.

## Where

- **Terminal:** macOS Terminal, at `/Users/rahulkumar/Documents/GitHub/UcityBuild_ml_pipeline_short_term_rental_Price`. This is the only place a command runs. Do not use the Jupyter terminal or `/opt/anaconda3`.
- **W&B:** https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb in the browser. Left sidebar: **Runs** (jobs) or **Artifacts** (files and the model). A run page has **Overview**, **Charts**, **Logs**, and **Files**. An artifact page has **Overview**, **Files**, **Lineage**, and **Aliases**.
- **GitHub:** https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price. Click **Releases** on the right side of the repository home.

## Previously failed rubrics

### 1. reference alias

**Rubric:** `clean_sample.csv` carries an alias named `reference`.

**Run:** Do not run again.

**Where:** W&B, browser.

**Check:** open [clean_sample.csv v0](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/clean_sample/clean_sample.csv/v0). In **Aliases**, the chips are `reference` and `latest`. Both are on v0. Pass when you see those two chips on this version.

### 2. Split artifacts

**Rubric:** `train_val_test_split` produced `trainval_data.csv` and `test_data.csv` at `test_size` 0.2.

**Run:** Do not run again.

**Where:** W&B, browser.

**Check:**

1. [Run otuh2lz2](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/otuh2lz2). Job Type is `train_val_test_split`. State is finished.
2. **Artifacts** → `trainval_data.csv` version **v4**: 15,200 rows (80 percent).
3. **Artifacts** → `test_data.csv` version **v4**: 3,801 rows (20 percent).

Pass when both files exist and the row counts add up to 19,001.

### 3. Loadable random_forest_export

**Rubric:** `random_forest_export` is an MLflow sklearn model from `train_random_forest`.

**Run:** Do not run again.

**Where:** W&B, browser.

**Check:** open [random_forest_export v12](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12). **Aliases** shows `prod`. Then open [run a0crvn82](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/a0crvn82), Job Type `test_model`. It finished after loading that same model. Pass when both pages are finished and v12 has `prod`.

### 4. More than two hyperparameter runs

**Rubric:** Hydra trained more than two forests with different hyperparameters.

**Run:** Do not run again.

**Where:** W&B, browser. Left sidebar **Runs**. Filter **Job Type** to `train_random_forest`. Show columns `mae`, `max_tfidf_features`, and `max_features`.

**Check:** these three finished runs use different settings:

- [zyzw136a](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/zyzw136a): `max_tfidf_features` 30, `max_features` 0.33, validation MAE 33.80
- [ud3ajhxd](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/ud3ajhxd): 10 and 0.33, validation MAE 33.87
- [xxc3f68q](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/xxc3f68q): 30 and 0.1, validation MAE 36.04

Pass when all three are finished and the config pairs differ. The lowest sample1 MAE is 33.80 on `zyzw136a`.

### 5. prod alias

**Rubric:** the lowest validation MAE has the alias `prod`.

**Run:** Do not run again.

**Where:** W&B, browser.

**Check:** the same v12 page as step 3. **Aliases** shows `prod`. **Overview** metadata shows `max_features` 0.33. Do not use the version marked `latest`. `prod` is on v12 only. Pass when the `prod` chip is on v12.

### 6. Test MAE next to validation MAE

**Rubric:** test MAE is comparable to validation MAE.

**Run:** Do not run again.

**Where:** W&B, browser. Open **Overview** on each run.

**Check:**

- [a0crvn82](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/a0crvn82): test `mae` is **33.29**
- [zyzw136a](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/zyzw136a): validation `mae` is **33.80**

Pass when those two numbers are the ones on screen. They differ by about half a dollar.

### 7. Lineage

**Rubric:** the Lineage view connects raw data, cleaning, splitting, and the model.

**Run:** Do not run again. You still open this page yourself.

**Where:** W&B, browser.

**Check:** open [random_forest_export v12](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12) and click the **Lineage** tab. Do not use **Files** and do not use **Charts**. Pass when the graph is:

```text
sample.csv → clean_sample.csv → trainval_data.csv → random_forest_export
```

The version is `v12` and the alias chip is `prod`.

### 8. Release 1.0.0 fails on sample2.csv

**Rubric:** tag `1.0.0` run on `sample2.csv` fails because one listing is outside New York City.

**Run:** Do not run again.

**Where:** GitHub, then W&B.

**Check:**

1. [Release 1.0.0](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.0). The tag is `1.0.0` and the commit is `dfd430d`.
2. [Run 0o3tdnpk](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/0o3tdnpk), Job Type `data_tests`. `test_proper_boundaries` failed with `assert np.int64(1) == 0`. The other five tests passed.

Pass when the release page shows `dfd430d` and that run is the failed boundary test.

### 9. Release 1.0.1 trains a new model

**Rubric:** tag `1.0.1` run on `sample2.csv` passes the tests and trains a new model. `prod` stays on the sample1 winner.

**Run:** Do not run again.

**Where:** GitHub, then W&B.

**Check:**

1. [Release 1.0.1](https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.1). The tag is `1.0.1` and the commit is `fb06810`.
2. [Run 163tjnrw](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/163tjnrw), Job Type `data_tests`. All six tests passed.
3. [Run 8c120q11](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/8c120q11), Job Type `train_random_forest`. **Overview** `mae` is 31.90. The artifact is `random_forest_export:v25`.
4. Return to v12 and confirm **Aliases** still shows `prod`.

Pass when v25 exists, its validation MAE is 31.90, and `prod` is still on v12.

## After those nine checks

Paste this into the Udacity submission field:

```text
Repository platform: GitHub
Repository URL: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price
W&B project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
```

If the form asks for an image, upload a screenshot of the v12 **Lineage** tab only. The image must show version `v12`, alias `prod`, and the chain in step 7. Do not add that image to the git repository.

## The other rubrics

These already passed. Same rule: do not run the pipeline again. Open the check.

### Public project and both links

**Rubric:** project `nyc_airbnb` is public, and the README has the W&B URL and the GitHub URL.

**Run:** Do not run again.

**Where:** W&B, then GitHub.

**Check:** the W&B project opens without asking the reviewer to log in as you. In [README.md](../README.md), the **Submission** section contains both URLs from the box above.

### sample.csv

**Rubric:** a `sample.csv` artifact is in W&B.

**Run:** Do not run again.

**Where:** W&B, **Artifacts**.

**Check:** type `raw_data` → `sample.csv` → the version with alias `latest`. The **Files** tab lists the csv.

### EDA notebook

**Rubric:** `EDA.ipynb` is in the repository root, next to `main.py` and `config.yaml`. It loads `sample.csv:latest`, keeps prices from 10 to 350, converts `last_review`, and leaves missing values missing.

**Run:** Do not run again.

**Where:** GitHub, the repository root.

**Check:** [EDA.ipynb](../EDA.ipynb) is beside [main.py](../main.py) and [config.yaml](../config.yaml). [notes.md](../notes.md) is the checklist that notebook follows.

### basic_cleaning files

**Rubric:** `src/basic_cleaning` has `conda.yml` (pandas), `MLproject` (six parameters), and `run.py`. Prices come from config. The geographic filter drops rows outside the NYC box. `clean_sample.csv` is in W&B.

**Run:** Do not run again.

**Where:** GitHub, then W&B.

**Check:** open [src/basic_cleaning/conda.yml](../src/basic_cleaning/conda.yml), [src/basic_cleaning/MLproject](../src/basic_cleaning/MLproject), and [src/basic_cleaning/run.py](../src/basic_cleaning/run.py). The MLproject parameters are `input_artifact`, `output_artifact`, `output_type`, `output_description` (strings) and `min_price`, `max_price` (floats). `run.py` filters price, converts `last_review`, and keeps longitude [-74.25, -73.50] and latitude [40.5, 41.2]. W&B artifact `clean_sample.csv` v0 is the uploaded file from step 1.

### Data tests, including row count and price range

**Rubric:** `test_row_count` and `test_price_range` are implemented, and all tests pass.

**Run:** Do not run again.

**Where:** GitHub, then W&B.

**Check:** [src/data_check/test_data.py](../src/data_check/test_data.py) defines `test_row_count` (more than 15,000 rows and fewer than 1,000,000) and `test_price_range` (prices from 10 to 350). [Run 214g6keg](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/214g6keg), Job Type `data_tests`, is the passing run against `clean_sample.csv:latest` and `clean_sample.csv:reference`. Pass when **Logs** show 6 passed.

### Training script

**Rubric:** `src/train_random_forest/run.py` downloads the data, builds `non_ordinal_categorical_preproc` and `sk_pipe`, fits, exports with MLflow, uploads the artifact, and logs MAE.

**Run:** Do not run again.

**Where:** GitHub, then the W&B run from step 4.

**Check:** [src/train_random_forest/run.py](../src/train_random_forest/run.py) contains `SimpleImputer(strategy="most_frequent")`, `OneHotEncoder`, `sk_pipe.fit`, `mlflow.sklearn.save_model`, and `run.summary["mae"]`. Run `zyzw136a` **Overview** shows `mae` 33.80. **Charts** shows the feature-importance bar chart.

### Git tags 1.0.0 and 1.0.1

**Rubric:** an annotated tag and a GitHub Release exist for `1.0.0`, and a later annotated tag and Release exist for `1.0.1`.

**Run:** Do not create a tag, and do not run `git tag -f`.

**Where:** Terminal, then GitHub **Releases**.

**Check:** in the Terminal at the repository root:

```bash
git rev-parse --short 1.0.0
git rev-parse --short 1.0.1
```

Pass when the first command prints `dfd430d` and the second prints `fb06810`. The GitHub pages are the ones in steps 8 and 9.

### Environment

**Rubric:** the local environment can import the libraries the pipeline uses.

**Run:** this command is safe. It does not upload artifacts.

**Where:** Terminal, repository root.

```bash
conda activate nyc_airbnb_dev
python scripts/check_environment.py
```

**Check:** the Terminal prints `Environment OK`.
