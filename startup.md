# Startup: run the project end to end

Commands are from the repository root. `scripts/run_pipeline.sh` selects Miniforge and loads `WANDB_API_KEY` from `.env`. The full explanation of each step is in [architecture.md](architecture.md).

Run the numbered sections in order. Two gates are easy to miss: add the `reference` alias before `data_check`, and add the `prod` alias before `test_regression_model`. That test step is not part of the default pipeline.

The notebook in section 3 can be run by hand, one cell at a time, or executed in one shot. Either path satisfies the EDA rubric. Do section 2 first so `sample.csv:latest` exists before you open the notebook.

W&B project: https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb
GitHub: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price

## 1. Environment and public W&B project

Rubric: public W&B project `nyc_airbnb`, with the project URL and this GitHub URL in the README.

```bash
brew install miniforge
export MLFLOW_CONDA_HOME=/opt/homebrew/Caskroom/miniforge/base
export CONDA_EXE="$MLFLOW_CONDA_HOME/bin/conda"
export PATH="$MLFLOW_CONDA_HOME/bin:$PATH"
conda env create -f environment.yml
conda activate nyc_airbnb_dev
python scripts/check_environment.py
```

`.env` contains one line, `wandb_api_key=...`. The project access must be public (`USER_READ`).

## 2. Upload sample.csv

Rubric: a `sample.csv` artifact exists in W&B.

```bash
scripts/run_pipeline.sh -P steps=download
```

`config.yaml` uses `etl.sample: sample1.csv`. The artifact name is `sample.csv`.

## 3. Exploratory notebook

Rubric: `EDA.ipynb` in the repository root fetches `sample.csv:latest`, explains the cleaning, keeps prices from 10 to 350, converts `last_review`, and does not impute. Missing values stay missing. Imputation happens later inside the training pipeline.

Create the EDA environment once. It is Python 3.12 and includes Jupyter and `ydata-profiling`. The development environment `nyc_airbnb_dev` does not have those packages.

```bash
conda env create -f src/eda/conda.yml
```

Pick one of the two options below.

### Option A: run the notebook yourself, cell by cell

Use this when you want to read each result before continuing. The notebook is already saved as `EDA.ipynb` in the repository root.

1. Start JupyterLab from the EDA environment. This opens the repository root, so `EDA.ipynb` is in the file browser:

```bash
scripts/run_eda.sh
```

2. In JupyterLab, open `EDA.ipynb`. If a kernel prompt appears, choose the Python kernel from the environment MLflow just created (the `eda` environment), not the system Python.

3. Run the cells from top to bottom with Shift+Enter. Do not use "Run All" on the first pass. Stop and read the output of each cell. The cells follow this order:

   - Start a W&B run and load `sample.csv:latest`.
   - Inspect columns, dtypes, and `describe`.
   - Count missing values and duplicates. Leave the missing values in place.
   - Plot the raw price distribution and the $10 to $350 band.
   - Plot latitude and longitude. This pass does not drop geographic outliers.
   - Count `neighbourhood_group` and `room_type`.
   - Build the raw `ydata-profiling` report.
   - Keep rows with price between 10 and 350 inclusive, and convert `last_review` to datetime.
   - Run `df.info()` and confirm the price range and the datetime dtype.
   - Build the cleaned profile.
   - Call `run.finish()` so the W&B run closes.

4. After the last cell succeeds, use **Kernel → Restart Kernel and Run All Cells**. Fix any error, then save the notebook. The file must stay at `EDA.ipynb` in the repository root.

5. Shut the notebook kernel down, then stop JupyterLab with **File → Shut Down**. `scripts/run_eda.sh` exits when that server stops.

The same cell-by-cell run works in Cursor. Open `EDA.ipynb`, choose the kernel whose Python is the EDA environment, and press Shift+Enter on each cell:

```text
/opt/homebrew/Caskroom/miniforge/base/envs/eda/bin/python
```

Finish with the checks in [notes.md](notes.md): the artifact was fetched, Markdown explains each decision, missing values were not imputed, the price range is inclusive, `last_review` is a datetime, the profile or `df.info()` was checked again, the W&B run was finished, and the kernel was restarted and run from the top.

### Option B: execute every cell in one command

Use this when you do not need to pause between cells. It runs the same notebook and writes the outputs back into `EDA.ipynb`.

```bash
source scripts/wandb_env.sh
export MPLBACKEND=Agg
export PATH="/opt/homebrew/Caskroom/miniforge/base/envs/eda/bin:$PATH"
jupyter nbconvert --to notebook --execute --inplace EDA.ipynb
```

## 4. Clean the sample and mark the reference

Rubric: `src/basic_cleaning` has `conda.yml`, `MLproject`, and `run.py`, pandas is installed, and `clean_sample.csv` is uploaded. The latest cleaned version also has the alias `reference`.

```bash
scripts/run_pipeline.sh -P steps=basic_cleaning
```

Then, once, on that first cleaned version:

```python
import wandb
api = wandb.Api()
art = api.artifact("dharacoding-dhara-coding/nyc_airbnb/clean_sample.csv:latest")
art.aliases = sorted(set(art.aliases) | {"reference"})
art.save()
```

In the W&B UI the same action is the plus button under Aliases on `clean_sample.csv:latest`. Do this before the next step. Later samples must not steal the `reference` alias.

## 5. Data tests

Rubric: `test_row_count` and `test_price_range` pass with the rest of the suite.

```bash
scripts/run_pipeline.sh -P steps=data_check
```

Expected result: 6 passed. The price test uses `etl.min_price` and `etl.max_price` (10 and 350). The row-count test requires more than 15,000 rows and fewer than 1,000,000.

## 6. Split

Rubric: `trainval_data.csv` and `test_data.csv` exist.

```bash
scripts/run_pipeline.sh -P steps=data_split
```

`test_size` is 0.2, `random_seed` is 42, and the split is stratified by `neighbourhood_group`.

## 7. Train one random forest

Rubric: the training script downloads the W&B training artifact, builds `non_ordinal_categorical_preproc` and `sk_pipe`, fits, exports an MLflow model, logs MAE, and uploads `random_forest_export`.

```bash
scripts/run_pipeline.sh -P steps=train_random_forest
```

## 8. Hydra search

Rubric: more than two W&B training runs with different hyperparameters.

```bash
scripts/run_pipeline.sh \
  -P steps=train_random_forest \
  -P hydra_options="modeling.max_tfidf_features=10,15,30 modeling.random_forest.max_features=0.1,0.33,0.5,0.75,1 -m"
```

That is 15 runs. The measured minimum validation MAE on sample1 is 33.80, from `max_tfidf_features=30` and `max_features=0.33` (W&B run `zyzw136a`).

## 9. Select the production model

Rubric: the lowest validation MAE gets the `prod` alias. Test MAE is not used for the choice.

Those two winning values are already the defaults in [config.yaml](config.yaml). The alias belongs on that run's export, `random_forest_export:v12`:

```python
import wandb
api = wandb.Api()
art = api.artifact("dharacoding-dhara-coding/nyc_airbnb/random_forest_export:v12")
art.aliases = sorted(set(art.aliases) | {"prod"})
art.save()
```

## 10. Test-set check

Rubric: `test_regression_model` loads `random_forest_export:prod` and `test_data.csv:latest`, and the test MAE is comparable to the validation MAE.

```bash
scripts/run_pipeline.sh -P steps=test_regression_model
```

Measured test MAE: 33.29. Validation MAE for the same model: 33.80.

## 11. Lineage

Rubric: the `random_forest_export` lineage view connects raw data, cleaning, splitting, and training.

Open:

https://wandb.ai/dharacoding-dhara-coding/nyc_airbnb/artifacts/model_export/random_forest_export/v12

The chain is `sample.csv` to `clean_sample.csv` to `trainval_data.csv` to `random_forest_export:prod`.

## 12. Release 1.0.0, then the expected sample2 failure

Rubric: an annotated Git tag and GitHub Release `1.0.0` point at the commit whose `config.yaml` holds the best validation hyperparameters. Running that release on `sample2.csv` fails because of a data problem.

Tag `1.0.0` is commit `dfd430d`. Release: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.0

That commit does not contain the geographic filter. Reproduce the failure with:

```bash
export MLFLOW_CONDA_HOME=/opt/homebrew/Caskroom/miniforge/base
export CONDA_EXE="$MLFLOW_CONDA_HOME/bin/conda"
source scripts/wandb_env.sh

mlflow run https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price.git \
  -v 1.0.0 \
  -P hydra_options="etl.sample='sample2.csv'"
```

`test_proper_boundaries` fails: `assert np.int64(1) == 0`. One price-valid row is outside longitude [-74.25, -73.50] and latitude [40.5, 41.2]. Leave this tag where it is.

## 13. Release 1.0.1 and the successful rerun

Rubric: `basic_cleaning` drops out-of-bounds coordinates, a new annotated tag and GitHub Release such as `1.0.1` point at that commit, and rerunning the release trains a new model.

The filter in [src/basic_cleaning/run.py](src/basic_cleaning/run.py), immediately before `to_csv`:

```python
idx = df["longitude"].between(-74.25, -73.50) & df["latitude"].between(40.5, 41.2)
df = df[idx].copy()
```

Tag `1.0.1` is commit `fb06810`. Release: https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price/releases/tag/1.0.1

```bash
mlflow run https://github.com/mynamerahulkumar/UcityBuild_ml_pipeline_short_term_rental_Price.git \
  -v 1.0.1 \
  -P hydra_options="etl.sample='sample2.csv'"
```

This run passed all six data tests, dropped that one row, and uploaded `random_forest_export:v16` with validation MAE 31.90. The `prod` alias stays on `v12`.
