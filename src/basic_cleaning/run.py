#!/usr/bin/env python
"""Download a W&B artifact, perform basic cleaning, and log the result."""

import argparse
import logging

import pandas as pd
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    logger.info("Downloading input artifact %s", args.input_artifact)
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(artifact_local_path)
    logger.info("Loaded input data with %s rows and %s columns", df.shape[0], df.shape[1])

    # Keep missing values. Imputation belongs in the inference pipeline so the
    # same treatment is available at prediction time.
    idx = df["price"].between(args.min_price, args.max_price)
    logger.info(
        "Filtering price outliers to the inclusive range [%s, %s]; dropping %s rows",
        args.min_price,
        args.max_price,
        int((~idx).sum()),
    )
    df = df[idx].copy()

    logger.info("Converting last_review from text to datetime")
    df["last_review"] = pd.to_datetime(df["last_review"])

    idx = df["longitude"].between(-74.25, -73.50) & df["latitude"].between(40.5, 41.2)
    logger.info(
        "Filtering listings to the NYC bounding box; dropping %s rows outside longitude [-74.25, -73.50] and latitude [40.5, 41.2]",
        int((~idx).sum()),
    )
    df = df[idx].copy()

    logger.info("Saving cleaned data to clean_sample.csv (%s rows)", df.shape[0])
    df.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    logger.info("Uploading artifact %s to Weights & Biases", args.output_artifact)
    run.log_artifact(artifact)
    run.finish()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Name of the input W&B artifact, including version or alias",
        required=True,
    )
    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name of the output W&B artifact",
        required=True,
    )
    parser.add_argument(
        "--output_type",
        type=str,
        help="Type of the output W&B artifact",
        required=True,
    )
    parser.add_argument(
        "--output_description",
        type=str,
        help="Description of the output W&B artifact",
        required=True,
    )
    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum nightly price to keep, inclusive",
        required=True,
    )
    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum nightly price to keep, inclusive",
        required=True,
    )

    args = parser.parse_args()
    go(args)
