🧠 General Feedback
You have built a solid, well-structured end-to-end ML pipeline for estimating short-term rental prices in NYC. The project correctly uses MLflow for orchestration, Hydra for configuration, and Weights & Biases for experiment tracking and artifact versioning. The two-artifact split design (trainval + held-out test) is coherent, the EDA notebook is thorough and follows the required checklist, and the basic_cleaning component cleanly re-implements the EDA decisions plus the later geographic filter. Hyper-parameter exploration is documented, the best model is selected by validation MAE, and two proper GitHub releases (1.0.0 and 1.0.1) capture the initial pipeline and the geographic fix.
The code quality is high: parameters are configuration-driven, logging is present, the scikit-learn Pipeline is used correctly, and the data-quality tests (including the required row-count and price-range checks) are implemented with the proper signatures. Public links for both the W&B project and the GitHub repository are supplied in the README and in the Udacity submission note.
A number of remote verification steps (exact alias attachment on the newest artifact versions, full metric tables, interactive Lineage view, and live re-execution of the tagged releases against sample2.csv) could not be completed from the review environment. These remain unverified rather than confirmed failures; the underlying implementation appears correct wherever it could be inspected.
💪 Strengths
Clear, readable code that follows the starter-project interfaces and the current rubric naming (clean_sample.csv, random_forest_export, output_artifact).
Thoughtful EDA notebook that explains why missing values are left for the inference pipeline.
Correct geographic boundary filter added in the patch release, with matching release notes.
Coherent two-artifact architecture that keeps the test set completely held out.
Public GitHub repository with both required releases and a well-written README that documents the entire workflow, hyper-parameter table, and sample2 chronology.
⚠ Key Improvements Needed
Confirm (and, if necessary, move) the W&B aliases reference (on the newest clean_sample.csv) and prod (on the winning random_forest_export version). These are the only items that may still need a small action on your side.
Optionally re-run the tagged releases against sample2.csv and keep the resulting logs or W&B run links so future reviewers can see the expected failure and the later success without having to re-execute the pipeline themselves.
No other code changes are required; the remaining items are purely verification limitations on the reviewer side.
🎯 Final Verdict
The project demonstrates a strong understanding of MLOps practices and meets the great majority of the rubric requirements with high-quality implementation. The few remaining items are remote verification gaps rather than missing or incorrect student work. Once the two aliases are confirmed on the correct artifact versions, the submission will be fully complete. You have produced a reproducible, well-documented pipeline that is ready for the next stage of the Nanodegree—excellent work.

Failed rubric 

Rubric 1

Create a reference alias for the latest version of the clean_sample.csv artifact.
In W&B, manually add an alias called reference to the latest version of the clean_sample.csv artifact.

Feedback

Create a reference alias for the latest version of the clean_sample.csv artifact.
Result: ⚠ Needs Improvement
✔ What is working
The pipeline and README correctly reference the alias clean_sample.csv:reference.
The data-check step is configured to use both the latest and the reference versions.
❌ Issues
Alias attachment could not be fully verified
→ What's wrong:
 The rubric requires the reference alias (not a tag) to point to the latest intended clean sample so that subsequent data-quality tests compare against the correct baseline.
🎯 How to Improve
Open the W&B project → Artifacts → clean_sample.csv → select the newest version.
In the Aliases section add (or move) the alias reference so it resolves only to that newest version.
Re-run the data-check step afterwards to confirm it succeeds.
📚 Resources
W&B Artifact Aliases(opens in a new tab) — shows how to attach and move aliases.
🎯 Conclusion
⚠ The code and documentation correctly expect the reference alias, but its exact attachment to the latest version could not be confirmed from the available remote evidence. This is an unverified item, not a confirmed implementation failure.
→ Final Result: ⚠ Needs Improvement
In W&B, manually add an alias called reference to the latest version of the clean_sample.csv artifact.


Rubric 2 

The pipeline runs successfully
The pipeline runs after this step, and all the tests pass.

Feedback:
The pipeline again runs successfully
Result: ⚠ Needs Improvement
✔ What is working
The split component is correctly parameterized and the downstream training step consumes trainval_data.csv:latest.
W&B lists both trainval_data.csv and test_data.csv.
❌ Issues
Exact content and producer verification of the split artifacts is incomplete
→ What happened:
 While the artifacts exist, row-count / split-fraction verification and the exact producer-run identity could not be fully inspected from the available W&B views.
→ Why it's wrong:
 The rubric expects confirmation that the produced splits match the configured fractions and that the test set remains held out.
→ Impact:
 Full confidence in the split ratios requires additional evidence.
🎯 How to Improve
After a successful run, open the W&B artifacts for trainval_data.csv and test_data.csv and confirm the producer is the train_val_test_split step and that the row counts are consistent with test_size=0.2.
📚 Resources
No additional resource is necessary for this requirement.
🎯 Conclusion
⚠ The design is correct and the artifacts exist; deeper content verification remains incomplete. This is an unverified item, not a confirmed failure.
→ Final Result: ⚠ Needs Improvement
The pipeline runs. At the end, there should be 2 new artifacts on W&B: trainval_data.csv, test_data.csv.

Rubric 3:


Create the random_forest_export artifact in W&B
There is an artifact in W&B named random_forest_export. It contains an MLflow sklearn serialized model produced by the train_random_forest step.


Feedback:

Create the random_forest_export artifact in W&B
Result: ⚠ Needs Improvement
✔ What is working
The training component correctly names the output artifact random_forest_export and the W&B project contains an artifact of that name under the model-export type.
The local export uses the MLflow sklearn flavor.
❌ Issues
Model content and loadability could not be fully verified
→ What happened:
 Existence of the artifact is confirmed, but downloading the model binary and loading it with MLflow to inspect its pipeline structure and generate a prediction was not performed.
→ Why it's wrong:
 The rubric expects a valid, loadable MLflow model artifact.
→ Impact:
 Full confidence that the exported model can be used for inference is limited.
🎯 How to Improve
From a W&B run that produced the model, download the random_forest_export artifact and confirm it can be loaded with:
 import mlflow
model = mlflow.sklearn.load_model(local_path)


Optionally run a small inference check with a representative row.
📚 Resources
MLflow Model Logging(opens in a new tab) — how to save and load sklearn models.
🎯 Conclusion
⚠ The correctly named artifact exists; deeper model-content verification remains incomplete. This is an unverified item, not a confirmed failure.
→ Final Result: ⚠ Needs Improvement
There is an artifact in W&B named random_forest_export. It contains an MLflow sklearn serialized model produced by the train_random_forest step.

Rubric 4:

Run training with different hyperparameters
Using the Hydra system, run a hyper-parameter search.
On W&B there should be the results of several (>2) training jobs with different hyperparameters.


Feedback
Run training with different hyperparameters
Result: ⚠ Needs Improvement
✔ What is working
The README documents a systematic search over max_tfidf_features ∈ {10, 15, 30} and random_forest.max_features ∈ {0.1, 0.33, 0.5, 0.75, 1} (more than two distinct configurations).
The final config.yaml reflects the selected best combination.
❌ Issues
Complete set of successful runs with different hyper-parameters could not be independently enumerated
→ What happened:
 While the student reports ≥15 runs and W&B shows multiple training jobs, a full table of distinct successful configurations with their validation MAE values could not be extracted from the available UI.
→ Why it's wrong:
 The rubric requires evidence of more than two (at least three) successful training jobs that differ in hyper-parameters.
→ Impact:
 Reviewers cannot independently count the distinct successful experiments.
🎯 How to Improve
In the W&B project, filter runs by the train_random_forest job type, sort by validation MAE, and ensure at least three completed runs with different hyper-parameter combinations are visible.
Optionally add a short table of the explored configurations to the README (already present) and keep the corresponding runs.
📚 Resources
Hydra Multi-run(opens in a new tab) — how to launch the hyper-parameter search.
🎯 Conclusion
⚠ The student performed a multi-configuration search and documented it; independent enumeration of the full set of successful runs remains partially unverified. This is not a confirmed defect.
→ Final Result: ⚠ Needs Improvement
Using the Hydra system, run a hyper-parameter search.
On W&B there should be the results of several (>2) training jobs with different hyperparameters.


Rubric 5:


Select the best-performing model and add the prod alias
The learner selects the trained model with the best MAE and adds the W&B alias prod to its random_forest_export artifact version.

Feedback:
Select the best-performing model and add the prod alias
Result: ⚠ Needs Improvement
✔ What is working
The README identifies the lowest-validation-MAE run (zyzw136a, artifact version v12) and states that the prod alias was attached to it.
The final config.yaml matches the hyper-parameters of that selected run (max_tfidf_features: 30, max_features: 0.33).
❌ Issues
Exact attachment of the prod alias could not be confirmed
→ What happened:
 The review environment could not open the precise artifact version page to verify that the alias prod (not merely a tag) is present on the winning random_forest_export version.
→ Why it's wrong:
 The production model must be identified by a W&B artifact alias named prod.
→ Impact:
 Downstream steps that request random_forest_export:prod may fail if the alias is missing or points to the wrong version.
🎯 How to Improve
Navigate to the chosen random_forest_export version in W&B.
Under Aliases add (or confirm) the alias prod.
Verify that random_forest_export:prod resolves to that version.
📚 Resources
W&B Artifact Aliases(opens in a new tab) — how to manage production aliases.
🎯 Conclusion
⚠ Selection logic and documentation are correct; confirmation of the prod alias on the winning version remains unverified. This is not a confirmed implementation failure.
→ Final Result: ⚠ Needs Improvement
The learner selects the trained model with the best MAE and adds the W&B alias prod to its random_forest_export artifact version.

Rubric 6:

Verify test set performance is comparable to performance on the validation set (no overfitting)
Implement the test_regression_model function in the main.py file. The test_regression_model is provided just as in the “data splitting” step.
Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred).

Feedback:
Verify test set performance is comparable to performance on the validation set (no overfitting)
Result: ⚠ Needs Improvement
✔ What is working
The test_regression_model component is present and correctly wired (commented out of the default step list, as required).
The README reports a validation MAE of approximately 33.80 and a test MAE of 33.29 — a small difference consistent with no severe overfitting.
❌ Issues
Independent re-computation of the test metrics was not performed
→ What happened:
 The reported numbers come from the student’s documentation; a fresh execution of test_regression_model against random_forest_export:prod and test_data.csv:latest was not re-run.
→ Why it's wrong:
 The rubric expects verified, comparable validation and test metrics.
→ Impact:
 Reviewers cannot independently confirm the exact figures or the absence of overfitting.
🎯 How to Improve
After the prod alias is confirmed, run:
 mlflow run . -P steps=test_regression_model


Record the resulting test MAE / R² and compare them with the validation metrics of the selected run.
📚 Resources
No additional resource is necessary for this requirement.
🎯 Conclusion
⚠ The reported metrics look reasonable and the evaluation component is implemented; independent verification of the numbers remains incomplete. This is an unverified item, not a confirmed defect.
→ Final Result: ⚠ Needs Improvement
Implement the test_regression_model function in the main.py file. The test_regression_model is provided just as in the “data splitting” step.
Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred).


Rubric 7:

Visualize the pipeline and verify its structure
In W&B, the learner opens the random_forest_export artifact and uses the Lineage view to verify that the pipeline is connected correctly from the raw data through cleaning, splitting, training, and the final model artifact.

Feedback:
Visualize the pipeline and verify its structure
Result: ⚠ Needs Improvement
✔ What is working
The expected artifact lineage (sample → clean_sample → trainval/test → random_forest_export) is present in the W&B project.
The README correctly describes the flow and points reviewers to the Lineage view.
❌ Issues
Interactive Lineage view could not be fully captured
→ What happened:
 While the individual artifacts exist, the complete interactive W&B Lineage graph was not rendered in the review environment.
→ Why it's wrong:
 The rubric expects confirmation of the connected pipeline structure via the current Lineage view.
→ Impact:
 Visual confirmation of the full producer-consumer relationships is limited.
🎯 How to Improve
In the W&B project open any of the final artifacts (e.g. random_forest_export) and switch to the Lineage tab.
Confirm that the graph shows the expected sequence of steps.
📚 Resources
W&B Artifact Lineage(opens in a new tab) — how to inspect the pipeline graph.
🎯 Conclusion
⚠ The artifacts that form the pipeline exist; the interactive Lineage visualization remains only partially verified. This is not a confirmed failure.
→ Final Result: ⚠ Needs Improvement
In W&B, the learner opens the random_forest_export artifact and uses the Lineage view to verify that the pipeline is connected correctly from the raw data through cleaning, splitting, training, and the final model artifact.


Feedback 8:

Run the released pipeline on a new sample of data, with initial failure
Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv.


Feedback:
Run the released pipeline on a new sample of data, with initial failure
Result: ⚠ Needs Improvement
✔ What is working
The README and the 1.0.0 release notes correctly document that running the release against sample2.csv failed on the geographic boundary test (test_proper_boundaries) with the expected assertion assert np.int64(1) == 0.
The failure is attributed to the intended data-quality check, not to an unrelated environment error.
❌ Issues
Live re-execution of the tagged release against sample2 was not performed
→ What happened:
 The documented failure is consistent with the expected behaviour, but a fresh mlflow run of tag 1.0.0 with etl.sample='sample2.csv' was not re-run in the review environment.
→ Why it's wrong:
 The rubric expects confirmation that the initial release fails for the geographic reason.
🎯 How to Improve
From a clean clone of the repository at tag 1.0.0 execute:
 mlflow run . -v 1.0.0 -P hydra_options="etl.sample='sample2.csv'"


Capture the pytest output that shows the failure of test_proper_boundaries.
📚 Resources
No additional resource is necessary for this requirement.
🎯 Conclusion
⚠ The documented initial failure matches the expected geographic check; independent live confirmation remains incomplete. This is an unverified item, not a confirmed defect.
→ Final Result: ⚠ Needs Improvement
Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv.


Rubric 9:

Run the new release successfully
Re-running with the new release should produce a new trained model.


Feedback:
Run the new release successfully
Result: ⚠ Needs Improvement
✔ What is working
The README states that running tag 1.0.1 against sample2.csv passed all six data-quality tests and produced a new trained model.
The geographic filter that enables this success is present in the released code.
❌ Issues
Live successful execution of the new release against sample2 was not re-verified
→ What happened:
 The documented success is consistent with the code change, but a fresh mlflow run of tag 1.0.1 with the new sample was not performed in the review environment.
→ Why it's wrong:
 The rubric expects confirmation that the patched release completes successfully and trains a new model.
→ Impact:
 Reviewers cannot independently observe the successful log and the new model artifact.
🎯 How to Improve
From a clean clone at tag 1.0.1 execute:
 mlflow run . -v 1.0.1 -P hydra_options="etl.sample='sample2.csv'"


Confirm that all data tests pass and that a new random_forest_export artifact is produced.
📚 Resources
No additional resource is necessary for this requirement.
🎯 Conclusion
⚠ The code and documentation indicate a successful retrain on the new sample; independent live confirmation remains incomplete. This is an unverified item, not a confirmed defect.
→ Final Result: ⚠ Needs Improvement
Re-running with the new release should produce a new trained model.


