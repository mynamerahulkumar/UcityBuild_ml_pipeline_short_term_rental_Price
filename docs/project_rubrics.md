se this project rubric to understand and assess the project criteria.

W&B Set-Up
Criteria	Submission Requirements
Public W&B project nyc_airbnb

Your W&B project nyc_airbnb is public so that the reviewer can access it and verify that the required W&B steps have been executed successfully.

Include both of the following links in both the project README.md and the Submission Details (optional) field:

your public W&B project; and
your GitHub or Azure Repos repository.
In Submission Details (optional), include:

Repository platform: GitHub or Azure DevOps; and
Repository URL: your GitHub or Azure Repos repository URL.
Although the field is labeled optional, this information is required for this project submission.

For a GitHub submission, the repository must be accessible to the reviewer.

For an Azure DevOps submission, the Azure Repos URL identifies the source repository but does not need to be accessible to the reviewer. The submission must instead include a complete-repository ZIP created from a fresh clone, including the .git directory.

Exploratory Data Analysis
Criteria	Submission Requirements
Obtain sample data

There is a sample.csv artifact in W&B.

The pipeline has been run to get a sample of the data, which has been uploaded to W&B.

Utilize an EDA notebook

There is a notebook called EDA.ipynb in the repository root, alongside main.py and config.yaml.

The notebook is properly formatted and uses comments and Markdown to explain exploration and cleaning decisions.

Fetch data into the notebook

At the beginning of the notebook, fetch the sample.csv artifact from W&B.

Clean the sample data

Clean the data without imputing missing values, explain why imputation is deferred to the inference pipeline, and complete the notes.md checks.

Data Cleaning
Criteria	Submission Requirements
Create a basic_cleaning step in the project repository

There is a new basic_cleaning step under the src directory in the submitted project files.

For a GitHub submission, inspect the files in the accessible repository. For an Azure DevOps submission, inspect the files in the submitted complete-repository ZIP.

The basic_cleaning step follows the MLflow structure and contains conda.yml, MLproject, and run.py. It has the parameters input_artifact, output_artifact, output_type, output_description, min_price, and max_price.

Update the conda.yml file

The conda.yml file has been updated to add the pandas dependency.

Update all parameters

Document all parameters in run.py and MLproject. Artifact metadata uses Python str / MLproject string; min_price and max_price use float.

Run basic_cleaning without errors

The basic_cleaning step re-implements in an MLFlow step the data cleaning you performed during the EDA. It should be added to the main.py file and run without errors.

In the main.py file, all parameters are taken from the configuration file rather than being hard-coded.

Log the main cleaning operations using the provided logger.

Create clean_data.csv in W&B.

At the end of the basic_cleaning step, a clean_sample.csv artifact is uploaded to W&B.

Data Testing
Criteria	Submission Requirements
Create a reference alias for the latest version of the clean_sample.csv artifact.

In W&B, manually add an alias called reference to the latest version of the clean_sample.csv artifact.

Implement the test_row_count and the test_price_range tests in src/data_check/test_data.py

Implements the test_row_count and the test_price_range tests in src/data_check/test_data.py.

The added tests are checking respectively for a proper size of the dataset, and for a proper price range.

The pipeline runs successfully

The pipeline runs after this step, and all the tests pass.

Data Splitting
Criteria	Submission Requirements
Split data into training, validation and test sets.

Adds the train_val_test_split component to the main.py file.

The train_val_test_split has been provided to you. You can just add it to the main.py file and fill in the parameters appropriately.

The pipeline again runs successfully

The pipeline runs. At the end, there should be 2 new artifacts on W&B: trainval_data.csv, test_data.csv.

Train the Random Forest
Criteria	Submission Requirements
Complete the src/train_random_forest/run.py script

The src/train_random_forest/run.py script is completed.

When checking the script, there should be the following steps in the script, marked by clear comments:

Download the train data using W&B.
In the get_inference_pipeline function, implement a pipeline called non_ordinal_categorical_preproc with two steps: a SimpleImputer(strategy="most_frequent") and a OneHotEncoder() step
In the get_inference_pipeline function, create the inference pipeline called sk_pipe containing the preprocessing step and the Random Forest
In the go function, fit the pipeline.
In the go function, export the pipeline using MLFlow model export.
Upload the artifact to W&B
Log the variable MAE to W&B
The pipeline again runs successfully

The pipeline again runs successfully.

The train_random_forest step is added to the main.py file.

Create the random_forest_export artifact in W&B

There is an artifact in W&B named random_forest_export. It contains an MLflow sklearn serialized model produced by the train_random_forest step.

Optimize Hyperparameters
Criteria	Submission Requirements
Run training with different hyperparameters

Using the Hydra system, run a hyper-parameter search.

On W&B there should be the results of several (>2) training jobs with different hyperparameters.

Select the Best Model
Criteria	Submission Requirements
Select the best-performing model and add the prod alias

The learner selects the trained model with the best MAE and adds the W&B alias prod to its random_forest_export artifact version.

Test Set Verification
Criteria	Submission Requirements
Verify test set performance is comparable to performance on the validation set (no overfitting)

Implement the test_regression_model function in the main.py file. The test_regression_model is provided just as in the “data splitting” step.

Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred).

Visualize the Pipeline
Criteria	Submission Requirements
Visualize the pipeline and verify its structure

In W&B, the learner opens the random_forest_export artifact and uses the Lineage view to verify that the pipeline is connected correctly from the raw data through cleaning, splitting, training, and the final model artifact.

Release the Pipeline
Criteria	Submission Requirements
Create version 1.0.0 of the pipeline

Commit the code and config.yaml with the default hyperparameters from the lowest validation MAE run, then create the release tag from that commit.

GitHub submissions contain a GitHub Release and corresponding Git tag named 1.0.0 or similar.
Azure DevOps submissions contain an annotated Git tag named 1.0.0 or similar in the Git metadata included in the complete-repository ZIP.
If the learner needed additional attempts, an incremented version such as 1.0.1 or 1.0.2 is acceptable.

Train the Model on a New Data Sample
Criteria	Submission Requirements
Run the released pipeline on a new sample of data, with initial failure

Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv.

Add a new cleaning step in basic_cleaning

Implement a new cleaning step that removes data points that are outside of the area of NYC in basic_cleaning.

Prepare a new release

After adding the geographical-boundary cleaning logic, the learner commits and pushes the change to the submitted repository and creates a new version that points to that commit:

GitHub submissions contain a new GitHub Release and corresponding Git tag, such as 1.0.1.
Azure DevOps submissions contain a new annotated Git tag, such as 1.0.1, in the Git metadata included in the complete-repository ZIP.
The new version number increments the patch component of the earlier release, using a 1.0.x version such as 1.0.1.

Run the new release successfully

Re-running with the new release should produce a new trained model.

Suggestions to Make Your Project Stand Out
In the data exploration step, you can go far beyond what is shown here, such as including visualizations and other data cleaning steps. This should allow you to get even better performance from the model.
Explore other models beyond the RandomForest trained here, creating a new separate step or customizing the random forest one to accommodate different types of models.
Add discussion to a README file concerning other changes you might consider in future releases of your pipeline.
