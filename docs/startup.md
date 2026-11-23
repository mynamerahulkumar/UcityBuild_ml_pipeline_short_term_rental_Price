# Startup

How to run this project in rubric order, and where to look afterward. What each step does in code is in [architecture.md](architecture.md). The Udacity resubmit text is in [remaining_steps.md](../remaining_steps.md).

This repository has already been run. `clean_sample.csv:v0` holds `reference` and `latest`. `random_forest_export:v12` holds `prod`. Steps marked **verify only** would log a new `:latest` artifact if you run them again. For a resubmission, open the W&B page in that step and confirm the numbers. The command is still written here so the rubric path is visible. It is the command that was used, not a command to launch again.

## Which window to open

**Terminal.** macOS Terminal. `cd` to the repository root:

```text
/Users/rahulkumar/Documents/GitHub/UcityBuild_ml_pipeline_short_term_rental_Price
```

This is the only CLI for pipeline commands. Do not type them into the Jupyter terminal. Do not use the old Anaconda prompt at `/opt/anaconda3`. [scripts/run_pipeline.sh](../scripts/run_pipeline.sh) and [scripts/run_eda.sh](../scripts/run_eda.sh) select Homebrew Miniforge and load `WANDB_API_KEY` from `.env`.

**Browser, W&B.** Open https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb while logged in as the project owner. The left sidebar has three items you will use:

- **Workspace** is the project home.
- **Runs** is the table of jobs. Open a run, then use the tabs **Overview** (summary numbers such as `mae`), **Charts**, **Logs**, and **Files**.
- **Artifacts** is the stored files and the model. Open a version, then use **Overview**, **Files**, **Lineage**, and the **Aliases** section.

**Browser, GitHub.** https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price and the Releases page for tags `1.0.0` and `1.0.1`.

**JupyterLab.** Opened only by `scripts/run_eda.sh`. Choose the `eda` kernel, not the system Python.

## 1. Environment

Rubric: the project can be run locally.

**Where:** Terminal, repository root.

**Run:**

```bash
brew install miniforge
export MLFLOW_CONDA_HOME=/opt/homebrew/Caskroom/miniforge/base
export CONDA_EXE="$MLFLOW_CONDA_HOME/bin/conda"
export PATH="$MLFLOW_CONDA_HOME/bin:$PATH"
conda env create -f environment.yml
conda activate nyc_airbnb_dev
python scripts/check_environment.py
```

`conda env create` is once. Later sessions only need `conda activate nyc_airbnb_dev`. The script must print `Environment OK`.

**W&B:** none.

## 2. Public project and README links

Rubric: the W&B project `nyc_airbnb` is public, and both the W&B URL and the GitHub URL are in the README and in the Udacity submission field.

**Where:** Browser. No Terminal command.

**Verify:**

1. Open the W&B project link above. The project header shows access that a reviewer can open (`USER_READ` / public).
2. On GitHub, open [README.md](../README.md) and read the **Submission** section. It must contain both of these URLs:

```text
https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price
```

## 3. Upload sample.csv

Rubric: a `sample.csv` artifact exists in W&B.

**Where:** Terminal, repository root.

**Verify only.** The command that uploaded it:

```bash
scripts/run_pipeline.sh -P steps=download
```

`config.yaml` uses `etl.sample: sample1.csv`. The artifact name is `sample.csv`.

**W&B:** left sidebar **Artifacts**. Open the type `raw_data`, then the artifact `sample.csv`, then the version that carries `latest`. Click the **Files** tab. The csv is listed there.

## 4. Exploratory notebook

Rubric: `EDA.ipynb` is in the repository root, fetches `sample.csv:latest`, explains the cleaning in Markdown, keeps prices from 10 to 350, converts `last_review`, and does not impute missing values.

**Where:** Terminal first, then JupyterLab.

**Run** (only if you need to re-execute the notebook; the saved notebook is already in the root):

```bash
scripts/run_eda.sh
```

That command opens JupyterLab at the repository root. In JupyterLab, open `EDA.ipynb`. If a kernel prompt appears, choose the Python kernel from the `eda` environment:

```text
/opt/homebrew/Caskroom/miniforge/base/envs/eda/bin/python
```

Run the cells from the top with Shift+Enter. After the last cell, use **Kernel → Restart Kernel and Run All Cells**, then save. Stop the server with **File → Shut Down**.

The notebook must show: the artifact was fetched, prices stay between 10 and 350 inclusive, `last_review` is a datetime, and missing values are still missing. [notes.md](../notes.md) is the checklist.

**W&B:** left sidebar **Runs**. Open the run whose group is `eda`. The **Overview** tab shows the run finished. The rubric grades the notebook, not a chart on this run.

## 5. Clean the sample

Rubric: `src/basic_cleaning` has `conda.yml`, `MLproject`, and `run.py`, pandas is installed, parameters come from config, and `clean_sample.csv` is uploaded.

**Where:** Terminal, repository root.

**Verify only.** The command that cleaned sample1:

```bash
scripts/run_pipeline.sh -P steps=basic_cleaning
```

**W&B:** left sidebar **Artifacts**. Open the type `clean_sample`, then the artifact `clean_sample.csv`. Version **v0** is the in-bounds sample1 clean (19,001 rows). Click **Files** to see `clean_sample.csv`.

## 6. reference alias

Rubric: the alias `reference` is on the cleaned sample that data tests compare against.

**Where:** Browser, W&B. Do not run `basic_cleaning` again.

**Verify:** open `clean_sample.csv` version **v0**:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/clean_sample/clean_sample.csv/v0

In the **Aliases** section, the chips read `reference` and `latest`. Do not click the plus button, and do not move either alias onto a higher version number.

On a first-time run, after the first successful `basic_cleaning`, the same result is this Python snippet in the Terminal (`conda activate nyc_airbnb_dev`). It is already done for v0:

```python
import wandb
api = wandb.Api()
art = api.artifact("dharacoding-dhara-coding/nyc_airbnb/clean_sample.csv:latest")
art.aliases = sorted(set(art.aliases) | {"reference"})
art.save()
```

## 7. Data tests

Rubric: `test_row_count` and `test_price_range` pass with the rest of the suite.

**Where:** Terminal, repository root.

**Verify only.** The command:

```bash
scripts/run_pipeline.sh -P steps=data_check
```

The Terminal prints `6 passed`.

**W&B:** left sidebar **Runs**. Filter **Job Type** to `data_tests`. Open run `214g6keg`:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/214g6keg

Click the **Logs** tab for the pytest output. This step has no metric chart.

## 8. Split

Rubric: `trainval_data.csv` and `test_data.csv` exist, from `train_val_test_split`, with `test_size` 0.2.

**Where:** Terminal, repository root.

**Verify only.** The command:

```bash
scripts/run_pipeline.sh -P steps=data_split
```

**W&B:**

1. Left sidebar **Runs**. Open run `otuh2lz2`. Job Type is `train_val_test_split`.
   https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/otuh2lz2
2. Left sidebar **Artifacts**. Open `trainval_data.csv` version **v4** (15,200 rows, 80 percent) and `test_data.csv` version **v4** (3,801 rows, 20 percent). Together they are the 19,001-row clean sample.

## 9. Train one random forest

Rubric: the training script downloads the W&B training artifact, builds `non_ordinal_categorical_preproc` and `sk_pipe`, fits, exports an MLflow model, logs MAE, and uploads `random_forest_export`.

**Where:** Terminal, repository root.

**Verify only.** The command for a single forest:

```bash
scripts/run_pipeline.sh -P steps=train_random_forest
```

**W&B:** left sidebar **Runs**. Filter **Job Type** to `train_random_forest`. Open run `zyzw136a`:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/zyzw136a

- **Overview:** `mae` is 33.80.
- **Charts**, and the media panel on the run: the feature-importance bar chart.
- **Config** (or the config section of Overview): `max_tfidf_features` is 30 and `max_features` is 0.33.

## 10. Hydra search

Rubric: more than two finished training runs with different hyperparameters.

**Where:** Terminal, repository root.

**Do not run again.** The command that launched the 15-run search:

```bash
scripts/run_pipeline.sh \
  -P steps=train_random_forest \
  -P hydra_options="modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m"
```

**W&B:** left sidebar **Runs**. Filter **Job Type** to `train_random_forest`. Add the columns `mae`, `max_tfidf_features`, and `max_features`. Sort by `mae` ascending. You should see more than two finished rows, and the config pairs should differ.

Open these three next to each other:

- [zyzw136a](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/zyzw136a): 30 / 0.33, validation MAE 33.80. This is the lowest sample1 MAE.
- [ud3ajhxd](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/ud3ajhxd): 10 / 0.33, validation MAE 33.87.
- [xxc3f68q](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/xxc3f68q): 30 / 0.1, validation MAE 36.04.

## 11. prod alias

Rubric: the lowest validation MAE gets the alias `prod`. Test MAE is not used for the choice.

**Where:** Browser, W&B. Do not start another training run.

**Verify:** left sidebar **Artifacts** → type `model_export` → artifact `random_forest_export` → version **v12**. Do not stop on the version marked `latest`.

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12

The **Aliases** section shows the chip `prod`. **Overview** metadata shows `max_features` 0.33. Those two winning values are already the defaults in [config.yaml](../config.yaml): `max_tfidf_features: 30` and `random_forest.max_features: 0.33`.

On a first-time run the alias is attached with this snippet. It is already done for v12:

```python
import wandb
api = wandb.Api()
art = api.artifact("dharacoding-dhara-coding/nyc_airbnb/random_forest_export:v12")
art.aliases = sorted(set(art.aliases) | {"prod"})
art.save()
```

## 12. Test MAE

Rubric: `test_regression_model` loads `random_forest_export:prod` and `test_data.csv:latest`, and the test MAE is comparable to the validation MAE.

**Where:** Terminal, repository root.

**Verify only.** The command:

```bash
scripts/run_pipeline.sh -P steps=test_regression_model
```

**W&B:** left sidebar **Runs**. Filter **Job Type** to `test_model`. Open run `a0crvn82`:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/a0crvn82

**Overview** shows `mae` **33.29**. Go back to run `zyzw136a` and read validation `mae` **33.80** on its Overview. The two numbers differ by about half a dollar.

## 13. Lineage graph

Rubric: the `random_forest_export` lineage view connects raw data, cleaning, splitting, and training.

**Where:** Browser, W&B. No command.

**Verify:** open version v12 and click the **Lineage** tab. Do not use the **Files** tab and do not use **Charts**.

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12

The graph reads:

```text
sample.csv → clean_sample.csv → trainval_data.csv → random_forest_export
```

The version on that page is `v12` and the alias chip is `prod`.

## 14. Release 1.0.0 on sample2.csv

Rubric: running the released pipeline on `sample2.csv` fails because of a data problem.

**Where:** GitHub in the browser, and the W&B Runs page. Do not run the tag again.

**Verify:** open the GitHub release `1.0.0`:

https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.0

The command that was used, from the Terminal at the repository root, after `source scripts/wandb_env.sh`:

```bash
export MLFLOW_CONDA_HOME=/opt/homebrew/Caskroom/miniforge/base
export CONDA_EXE="$MLFLOW_CONDA_HOME/bin/conda"
source scripts/wandb_env.sh

mlflow run https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price.git \
  -v 1.0.0 \
  -P hydra_options="etl.sample='sample2.csv'"
```

The Terminal log shows `FAILED test_data.py::test_proper_boundaries` and `assert np.int64(1) == 0`. The other five tests passed. One price-valid row is outside longitude [-74.25, -73.50] and latitude [40.5, 41.2].

**W&B:** left sidebar **Runs**.

- Data tests: [0o3tdnpk](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/0o3tdnpk), Job Type `data_tests`. Click **Logs**.
- Cleaning: [espaauo6](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/espaauo6). This tag does not drop the out-of-bounds row, so training never starts.

## 15. Release 1.0.1 on sample2.csv

Rubric: after the geographic filter, the new release trains a new model. Do not create another tag.

**Where:** GitHub in the browser, and the W&B Runs and Artifacts pages. Do not run the tag again.

**Verify:** open the GitHub release `1.0.1`:

https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.1

The command that was used is the same as step 14 with `-v 1.0.1`:

```bash
mlflow run https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price.git \
  -v 1.0.1 \
  -P hydra_options="etl.sample='sample2.csv'"
```

**W&B:**

1. **Runs** → [163tjnrw](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/163tjnrw), Job Type `data_tests`. All six tests passed. The filter dropped the one out-of-bounds row.
2. **Runs** → [8c120q11](https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/runs/8c120q11), Job Type `train_random_forest`. **Overview** `mae` is 31.90.
3. **Artifacts** → `model_export` → `random_forest_export` → version **v25**. That is the new export from this release.
4. Open version **v12** again and confirm the **Aliases** chip is still `prod`.

Leave both tags where they are. Another `mlflow run` of either tag uploads new `:latest` artifacts.
