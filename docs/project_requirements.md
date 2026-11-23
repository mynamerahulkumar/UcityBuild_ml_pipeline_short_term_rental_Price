# COMPLETE PROJECT IMPLEMENTATION
# Build an ML Pipeline for Short-term Rental Prices in NYC

## 1. ROLE AND RESPONSIBILITY

Act as a Senior Machine Learning Engineer, MLOps Architect, Python Developer, and GitHub Release Manager.

Your task is to complete the existing Udacity project:

**Build an ML Pipeline for Short-term Rental Prices in NYC**

You must implement the complete project using the existing starter repository.

The project must:
- Run locally on my MacBook Pro M4 Pro.
- Use GitHub exclusively for source control and release management.
- Use Weights & Biases (W&B) for experiment tracking and artifact management.
- Use MLflow for pipeline execution and model management.
- Use Hydra for configuration and hyperparameter optimization.
- Use Scikit-learn for machine learning.
- Satisfy all mandatory Udacity project rubric requirements.

IMPORTANT:

**GitHub is the ONLY repository and version-control platform for this project.**

Do not implement Azure DevOps, Azure Repos, Azure Pipelines, or Azure repository workflows.

---

# 2. DEVELOPMENT ENVIRONMENT

My local machine:

- MacBook Pro M4 Pro.
- Apple Silicon ARM64 architecture.
- macOS.
- Cursor IDE.
- Local Python environment.

I want to complete the entire project on my Mac without depending on Udacity Workspace or Google Colab.

Use CPU-based execution for Random Forest training. Do not introduce unnecessary CUDA or NVIDIA dependencies.

Before implementation, inspect:

```bash
uname -m
python3 --version
git --version
conda --version
```

Expected architecture:

```text
arm64
```

Use a compatible Python and package combination based on the existing starter repository.

Prefer Python 3.11 if all supplied components support it.

Create a Conda environment:

```bash
conda create -n nyc-mlops python=3.11 -y
conda activate nyc-mlops
```

Do not blindly replace the supplied Conda environments. Inspect each component's dependency requirements.

---

# 3. EXISTING STARTER REPOSITORY

The current repository already contains the following initial structure.

Preserve the existing architecture and working implementations.

```text
UCITYBUILD_ML_PIPELINE_SHORT_TERM_RENTAL_PRICE/
│
├── components/
│   ├── get_data/
│   │   ├── data/
│   │   ├── conda.yml
│   │   ├── MLproject
│   │   └── run.py
│   │
│   ├── test_regression_model/
│   │   ├── conda.yml
│   │   ├── MLproject
│   │   └── run.py
│   │
│   ├── train_val_test_split/
│   │   ├── conda.yml
│   │   ├── MLproject
│   │   └── run.py
│   │
│   └── wandb_utils/
│       ├── __init__.py
│       ├── log_artifact.py
│       └── sanitize_path.py
│
├── cookie-mlflow-step/
│
├── images/
│
├── src/
│   ├── basic_cleaning/
│   │   ├── conda.yml
│   │   ├── MLproject
│   │   └── run.py
│   │
│   ├── data_check/
│   │   ├── conda.yml
│   │   ├── conftest.py
│   │   ├── MLproject
│   │   └── test_data.py
│   │
│   ├── eda/
│   │   ├── conda.yml
│   │   ├── launch.py
│   │   └── MLproject
│   │
│   └── train_random_forest/
│       ├── conda.yml
│       ├── feature_engineering.py
│       ├── MLproject
│       └── run.py
│
├── CODEOWNERS
├── conda.yml
├── config.yaml
├── environment.yml
├── LICENSE.txt
├── main.py
├── MLproject
├── notes.md
└── README.md
```

The screenshot shows that the repository has starter implementations and component structures.

Inspect every relevant file before changing it.

The root-level EDA.ipynb is required by the Udacity rubric. Create it if it does not exist.

Do not remove the existing src/eda implementation.

---

# 4. GITHUB-ONLY REQUIREMENTS

Use my existing GitHub repository or GitHub fork.

If the GitHub remote is already configured, inspect it before changing anything.

Check:

```bash
git remote -v
git status
git branch
git log --oneline -5
```

If no remote is configured, ask me for the GitHub repository URL.

Never invent a repository URL.

## GitHub rules

1. GitHub is the only source-control platform.
2. All project source code must be committed to GitHub.
3. Maintain proper commit history.
4. Use Git tags for release versioning.
5. Publish GitHub Releases.
6. Use version 1.0.0 for the first completed pipeline.
7. Use version 1.0.1 for the geographical filtering improvement.
8. Never overwrite or move an existing release tag.
9. Do not commit secrets or API keys.
10. Do not commit local virtual environments, caches, or unnecessary generated datasets.

## GitHub branch

Use the existing default branch.

Do not create unnecessary branches or rewrite existing Git history.

## Required releases

| Version | Description |
|---|---|
| 1.0.0 | Initial completed ML pipeline |
| 1.0.1 | Improved geographical data cleaning |

Use annotated Git tags.

For example:

```bash
git tag -a 1.0.0 -m "Initial ML pipeline release"
git push origin 1.0.0
```

Create the corresponding GitHub Release using the GitHub interface or GitHub CLI.

Version 1.0.1 must point to the commit containing the geographical filtering improvement.

Example:

```bash
git tag -a 1.0.1 -m "Add NYC geographical boundary cleaning"
git push origin 1.0.1
```

Do not create a release until the relevant code has been successfully tested.

Before publishing, ask for approval if the action will publish changes or releases to GitHub.

---

# 5. W&B CONFIGURATION

Use Weights & Biases for the complete ML workflow.

W&B project name:

```text
nyc_airbnb
```

The project must be public for Udacity reviewer access.

Authenticate using:

```bash
wandb login
```

Do not hardcode API credentials.

Use environment variables where necessary.

Verify W&B connectivity before executing the pipeline.

Required W&B artifacts:

```text
sample.csv
clean_sample.csv
trainval_data.csv
test_data.csv
random_forest_export
```

Required aliases:

```text
clean_sample.csv:latest
clean_sample.csv:reference
random_forest_export:prod
```

The reference alias should point to the initial cleaned dataset version.

The prod alias must point to the best-performing model selected using validation MAE.

Verify actual artifact lineage in W&B.

Do not create fake artifacts, fake experiments, or fabricated metrics.

---

# 6. PHASE A: REPOSITORY ANALYSIS

Before modifying code, inspect:

- README.md
- notes.md
- config.yaml
- main.py
- MLproject
- All Conda environment files
- All component MLproject files
- All Python scripts under components/
- All Python scripts under src/

Identify:

1. Existing working implementations.
2. Incomplete functions.
3. TODO comments.
4. Missing files.
5. Dependency compatibility problems.
6. Incorrect artifact names.
7. Incorrect parameter definitions.
8. Missing pipeline integrations.
9. Potential macOS compatibility issues.
10. Missing Udacity rubric requirements.

Create a mapping:

| Rubric requirement | Relevant file | Status | Required change |
|---|---|---|---|

Do not modify anything until the initial analysis is complete.

Then proceed phase by phase.

---

# 7. PHASE B: LOCAL MAC ENVIRONMENT

Prepare the local environment.

Required libraries include:

- Python
- Pandas
- NumPy
- Scikit-learn
- MLflow
- W&B
- Hydra
- Pytest
- Jupyter
- Matplotlib
- Seaborn
- ydata-profiling

Inspect existing environment files before installing packages.

Ensure Apple Silicon compatibility.

Check:

```bash
python -c "import numpy, pandas, sklearn, mlflow, wandb; print('Environment OK')"
```

Do not modify global Python packages.

Add appropriate local setup instructions to README.md.

Create or update .gitignore to exclude:

```text
.env
.venv/
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
mlruns/
wandb/
*.log
```

Preserve files required for submission.

---

# 8. PHASE C: DATA INGESTION

Inspect:

```text
components/get_data/
```

Verify the existing implementation.

It must:

1. Retrieve the supplied rental dataset.
2. Support the expected dataset selection parameters.
3. Create sample.csv.
4. Upload sample.csv to W&B.
5. Use correct artifact versioning.
6. Execute through MLflow.

Expected artifact:

```text
sample.csv
```

Do not replace the original supplied dataset with an unrelated dataset.

Run and verify the download stage.

---

# 9. PHASE D: EXPLORATORY DATA ANALYSIS

Required file:

```text
EDA.ipynb
```

Create it in the repository root if missing.

Use the W&B sample.csv artifact.

Implement:

1. Dataset loading.
2. Data inspection.
3. Column analysis.
4. Data types.
5. Missing value analysis.
6. Duplicate analysis.
7. Statistical summary.
8. Price distribution.
9. Price outlier analysis.
10. Geographical exploration.
11. Categorical feature exploration.
12. Data cleaning.

Required cleaning:

- Filter prices between $10 and $350.
- Convert last_review into datetime.
- Do not impute missing values in EDA.
- Explain why imputation is deferred to the inference pipeline.

Include charts and Markdown explanations.

Complete the checks in notes.md.

Restart the notebook kernel and run all cells before committing.

---

# 10. PHASE E: BASIC CLEANING COMPONENT

Complete:

```text
src/basic_cleaning/
├── conda.yml
├── MLproject
└── run.py
```

Required parameters:

| Parameter | Type |
|---|---|
| input_artifact | string |
| output_artifact | string |
| output_type | string |
| output_description | string |
| min_price | float |
| max_price | float |

Implementation:

1. Initialize W&B.
2. Download input artifact.
3. Read CSV using Pandas.
4. Filter prices.
5. Convert last_review into datetime.
6. Preserve missing values.
7. Save clean_sample.csv.
8. Upload artifact to W&B.
9. Log cleaning operations.
10. Finish W&B run correctly.

Add Pandas to the component Conda environment.

Document all parameters in MLproject.

Integrate basic_cleaning into main.py.

Use config.yaml for min_price and max_price.

Do not hardcode configuration values.

Verify the resulting artifact in W&B.

---

# 11. PHASE F: DATA VALIDATION

Complete:

```text
src/data_check/
├── conda.yml
├── conftest.py
├── MLproject
└── test_data.py
```

Inspect the provided fixtures.

Implement:

### Row count test

```python
def test_row_count(data):
    assert 15000 < data.shape[0] < 1000000
```

### Price range test

```python
def test_price_range(data, min_price, max_price):
    assert data["price"].between(
        min_price,
        max_price
    ).all()
```

Use the exact function names and parameter names.

Add data_check to main.py.

It must:

1. Retrieve latest cleaned artifact.
2. Retrieve reference artifact.
3. Run the provided pytest tests.
4. Validate row count.
5. Validate price range.
6. Perform the supplied reference-data checks.
7. Use the configured KL threshold.
8. Stop the pipeline on failed validation.
9. Record validation runs in W&B.

Create the reference alias manually in W&B.

Verify all tests.

---

# 12. PHASE G: DATA SPLITTING

Inspect:

```text
components/train_val_test_split/
```

Use the supplied component.

Integrate it into main.py.

Required parameters:

- test_size
- random_seed
- stratify_by

Read values from config.yaml.

Expected W&B artifacts:

```text
trainval_data.csv
test_data.csv
```

Verify that both artifacts exist.

Do not rewrite a working starter component unnecessarily.

---

# 13. PHASE H: RANDOM FOREST MODEL TRAINING

Complete:

```text
src/train_random_forest/
├── conda.yml
├── feature_engineering.py
├── MLproject
└── run.py
```

Inspect the supplied feature engineering code before modifying it.

### Requirement 1: Download training data

Retrieve trainval_data.csv from W&B.

### Requirement 2: Categorical preprocessing

Create:

```python
non_ordinal_categorical_preproc
```

It must contain:

- SimpleImputer(strategy="most_frequent")
- OneHotEncoder()

### Requirement 3: Complete inference pipeline

Create:

```python
sk_pipe
```

It must combine:

- Feature preprocessing.
- Categorical preprocessing.
- Numerical preprocessing.
- RandomForestRegressor.

Preserve the existing feature engineering approach.

### Requirement 4: Training

Inside go():

1. Download the dataset.
2. Separate features and target.
3. Prepare training and validation subsets.
4. Fit the sklearn pipeline.
5. Generate validation predictions.
6. Calculate MAE.
7. Log MAE to W&B.
8. Export the model using MLflow.
9. Upload the model artifact to W&B.

Required artifact:

```text
random_forest_export
```

Use the correct MLflow sklearn export convention from the starter project.

### Requirement 5: Pipeline integration

Integrate train_random_forest into main.py.

Use config.yaml for all parameters.

Execute the component successfully.

---

# 14. PHASE I: HYPERPARAMETER OPTIMIZATION

Use Hydra multirun.

Required search dimensions:

```yaml
max_tfidf_features:
  - 10
  - 15
  - 30

random_forest:
  max_features:
    - 0.1
    - 0.33
    - 0.5
    - 0.75
    - 1
```

Follow the existing config.yaml hierarchy and Hydra syntax.

Run 15 parameter combinations.

Requirements:

1. Record experiments in W&B.
2. Log the different hyperparameter values.
3. Log validation MAE.
4. Compare all successful runs.
5. Select the model with the lowest validation MAE.

Do not use test-set MAE to select the model.

---

# 15. PHASE J: PRODUCTION MODEL SELECTION

Select the best Random Forest model using validation MAE.

Find its corresponding W&B artifact:

```text
random_forest_export
```

Add the artifact alias:

```text
prod
```

Verify:

```text
random_forest_export:prod
```

Use an actual W&B artifact alias.

Do not confuse aliases with ordinary W&B tags.

---

# 16. PHASE K: TEST SET VERIFICATION

Inspect:

```text
components/test_regression_model/
```

Use the existing component.

Integrate test_regression_model into main.py.

It must:

1. Download test_data.csv.
2. Retrieve random_forest_export:prod.
3. Load the MLflow model.
4. Generate predictions.
5. Calculate test MAE.
6. Compare validation and test performance.
7. Report whether overfitting is evident.

Do not train the model using the test dataset.

Verify that test performance is reasonably comparable to validation performance.

---

# 17. PHASE L: W&B PIPELINE LINEAGE

Open the final model artifact in W&B.

Verify the lineage:

```text
sample.csv
    |
basic_cleaning
    |
clean_sample.csv
    |
data_check
    |
train_val_test_split
    |
trainval_data.csv
    |
train_random_forest
    |
random_forest_export
```

Verify the test data lineage as well.

The final model artifact must have a traceable relationship to its source dataset and pipeline components.

Do not fabricate lineage screenshots.

---

# 18. PHASE M: GITHUB RELEASE 1.0.0

GitHub is the only repository platform.

Before release:

1. Complete all pipeline stages.
2. Run the complete pipeline.
3. Complete hyperparameter optimization.
4. Select the best validation MAE.
5. Update config.yaml with the best hyperparameters.
6. Run tests.
7. Inspect git status.
8. Commit the finalized code.

Example:

```bash
git add .

git commit -m "Complete NYC rental ML pipeline"

git push origin main
```

Create an annotated Git tag:

```bash
git tag -a 1.0.0 -m "Initial ML pipeline release"

git push origin 1.0.0
```

Publish a GitHub Release:

```text
Tag: 1.0.0
Title: NYC Rental Price ML Pipeline 1.0.0
```

Use the GitHub Releases page.

Ensure the release points to the correct commit.

Do not publish the release until the pipeline has been verified.

---

# 19. PHASE N: TEST THE NEW DATASET

The project supplies:

```text
sample2.csv
```

Execute the released pipeline version 1.0.0 against sample2.csv.

The first execution is expected to fail because the new dataset contains geographical records outside the allowed NYC boundaries.

This failure is required evidence.

Do not disable the geographical validation or bypass the failed test.

Capture the actual error and explain why the pipeline stopped.

---

# 20. PHASE O: GEOGRAPHICAL FILTERING

Modify:

```text
src/basic_cleaning/run.py
```

Preserve the original price filtering and datetime conversion.

Add geographical filtering:

```python
idx = (
    df["longitude"].between(-74.25, -73.50)
    &
    df["latitude"].between(40.5, 41.2)
)

df = df[idx].copy()
```

Add logging for geographical filtering.

Ensure that the cleaning component saves and uploads the updated dataset.

Verify the geographical filtering with actual data.

---

# 21. PHASE P: GITHUB RELEASE 1.0.1

Commit the geographical improvement.

```bash
git add .

git commit -m "Add NYC geographical boundary filtering"

git push origin main
```

Create an annotated tag:

```bash
git tag -a 1.0.1 -m "Add geographical boundary cleaning"

git push origin 1.0.1
```

Publish the corresponding GitHub Release:

```text
Tag: 1.0.1
Title: NYC Rental Price ML Pipeline 1.0.1
```

Requirements:

- Keep release 1.0.0 unchanged.
- Do not move existing tags.
- Ensure 1.0.1 points to the geographical filtering commit.
- Include a release description.

---

# 22. PHASE Q: EXECUTE RELEASE 1.0.1

Execute version 1.0.1 against sample2.csv.

Expected workflow:

1. Download sample2.csv.
2. Run updated basic_cleaning.
3. Remove geographically invalid records.
4. Validate cleaned data.
5. Split the data.
6. Train a new Random Forest model.
7. Export the new model.
8. Upload the new artifact to W&B.

Verify actual execution success.

---

# 23. MAIN.PY PIPELINE REQUIREMENTS

Inspect the current main.py and preserve its MLflow and Hydra architecture.

Support the following stages using the exact step names defined by the starter:

- download
- basic_cleaning
- data_check
- data_split
- train_random_forest
- test_regression_model

Requirements:

1. Each stage must work independently where supported.
2. The full pipeline must execute in the correct order.
3. All parameters must come from config.yaml.
4. Artifact aliases must be correct.
5. MLflow failures must be propagated.
6. No unnecessary hardcoded values.
7. W&B tracking must work.
8. Components must use their respective Conda environments.

Do not replace the existing orchestration architecture with a completely different framework.

---

# 24. LOCAL DEVELOPER SCRIPTS

Create optional helper scripts if they improve local execution:

```text
scripts/
    setup_mac.sh
    check_environment.py
    run_eda.sh
    run_pipeline.sh
    run_tests.sh
```

Provide commands for:

```bash
conda activate nyc-mlops
wandb login
mlflow run .
pytest
```

Use exact step names and configuration parameters from the actual repository.

Do not claim successful execution without running the commands.

---

# 25. README DOCUMENTATION

Update README.md with:

1. Project overview.
2. Business problem.
3. Architecture.
4. Technology stack.
5. Repository structure.
6. macOS setup.
7. Conda installation.
8. W&B authentication.
9. Data ingestion.
10. EDA instructions.
11. Cleaning and validation.
12. Data splitting.
13. Random Forest training.
14. Hyperparameter optimization.
15. Model evaluation.
16. Pipeline lineage.
17. GitHub release 1.0.0.
18. GitHub release 1.0.1.
19. Troubleshooting.
20. Public W&B project URL.
21. GitHub repository URL.

Do not fabricate metrics or execution results.

---

# 26. COMPLETE UDACITY RUBRIC CHECKLIST

Before declaring the project complete, verify every requirement.

## W&B Setup
- [ ] Public W&B project named nyc_airbnb.
- [ ] W&B URL in README.
- [ ] GitHub URL in README and submission details.

## EDA
- [ ] sample.csv exists.
- [ ] EDA.ipynb exists in root.
- [ ] Notebook fetches data from W&B.
- [ ] Proper Markdown and comments.
- [ ] Price filtering.
- [ ] Datetime conversion.
- [ ] Missing values retained.
- [ ] notes.md checks completed.

## Data Cleaning
- [ ] basic_cleaning component.
- [ ] conda.yml.
- [ ] MLproject.
- [ ] run.py.
- [ ] Six required parameters.
- [ ] Pandas dependency.
- [ ] Correct parameter types.
- [ ] Integrated into main.py.
- [ ] Config-based parameters.
- [ ] Logging.
- [ ] Successful execution.
- [ ] clean_sample.csv uploaded.

## Data Testing
- [ ] reference alias.
- [ ] test_row_count.
- [ ] test_price_range.
- [ ] Integrated validation component.
- [ ] Successful validation.

## Data Splitting
- [ ] Existing split component integrated.
- [ ] Correct parameters.
- [ ] trainval_data.csv.
- [ ] test_data.csv.

## Random Forest
- [ ] Training script completed.
- [ ] W&B dataset download.
- [ ] SimpleImputer.
- [ ] OneHotEncoder.
- [ ] non_ordinal_categorical_preproc.
- [ ] sk_pipe.
- [ ] Model training.
- [ ] MLflow model export.
- [ ] W&B model artifact.
- [ ] MAE logged.
- [ ] Training integrated into main.py.
- [ ] Successful execution.

## Optimization
- [ ] Hydra multirun.
- [ ] Multiple experiments.
- [ ] Different hyperparameter values.
- [ ] W&B experiment tracking.

## Model Selection
- [ ] Lowest validation MAE selected.
- [ ] prod alias.

## Test Evaluation
- [ ] test_regression_model implemented.
- [ ] Test dataset loaded.
- [ ] Production model loaded.
- [ ] Test MAE evaluated.
- [ ] Validation and test results compared.

## Pipeline Visualization
- [ ] W&B lineage opened.
- [ ] Raw data to final model verified.

## GitHub Release 1.0.0
- [ ] Best hyperparameters saved in config.yaml.
- [ ] Final code committed.
- [ ] Tag 1.0.0 created.
- [ ] GitHub Release 1.0.0 published.
- [ ] Release points to the correct commit.

## New Dataset
- [ ] sample2.csv executed using release 1.0.0.
- [ ] Expected failure demonstrated.
- [ ] Geographical filtering implemented.
- [ ] Updated code committed.
- [ ] Tag 1.0.1 created.
- [ ] GitHub Release 1.0.1 published.
- [ ] Release 1.0.1 executed successfully.
- [ ] New model artifact created.

---

# 27. IMPLEMENTATION WORKFLOW

Work in the following sequence.

| Phase | Work |
|---|---|
| A | Repository analysis |
| B | Local Mac environment |
| C | W&B configuration |
| D | Data ingestion |
| E | EDA notebook |
| F | Basic cleaning |
| G | Data validation |
| H | Data splitting |
| I | Random Forest training |
| J | Hyperparameter optimization |
| K | Production model selection |
| L | Test evaluation |
| M | W&B lineage |
| N | GitHub release 1.0.0 |
| O | New dataset failure |
| P | Geographical filtering |
| Q | GitHub release 1.0.1 |
| R | Final documentation and rubric audit |

For each phase:

1. Inspect the relevant existing code.
2. Explain the implementation plan.
3. Modify only relevant files.
4. Run syntax checks.
5. Run unit tests.
6. Execute the relevant pipeline component.
7. Fix errors.
8. Verify W&B artifacts where relevant.
9. Update the checklist.
10. Summarize the result.

Do not proceed past a critical failure without diagnosis.

---

# 28. GITHUB SECURITY AND APPROVAL RULES

GitHub operations must be safe.

You may inspect:

- Git status.
- Git history.
- Git remotes.
- Branches.
- Tags.
- Release metadata.

You may prepare code changes and local commits.

Before pushing code, creating public releases, or changing remote tags, request my approval.

Never:

- Force push.
- Delete an existing tag.
- Rewrite Git history.
- Commit API keys.
- Commit personal credentials.
- Make a private repository public without permission.
- Invent GitHub URLs.
- Claim a release was published when it was not.

---

# 29. FINAL DELIVERABLE

At the end of the project, provide:

1. Final repository structure.
2. Modified files.
3. Newly created files.
4. Local Mac installation commands.
5. Exact pipeline execution commands.
6. W&B artifact inventory.
7. Hyperparameter experiment summary.
8. Best validation MAE.
9. Test MAE.
10. W&B production model alias.
11. Pipeline lineage verification.
12. GitHub commit history.
13. GitHub release 1.0.0 URL.
14. GitHub release 1.0.1 URL.
15. Test execution results.
16. Completed Udacity rubric checklist.
17. Remaining manual actions.

Only report actual results.

If W&B authentication or GitHub approval is required, stop and ask me to complete that step.

# FINAL OBJECTIVE

Deliver a fully functional, locally executable, reproducible MLOps pipeline that satisfies every mandatory Udacity rubric requirement.

Use:

- GitHub exclusively for version control and releases.
- W&B for artifacts and experiment tracking.
- MLflow for pipeline execution and model export.
- Hydra for configuration and hyperparameter search.
- Scikit-learn for model development.
- Local MacBook Pro M4 Pro for execution.

No Azure DevOps or Azure Repos implementation.