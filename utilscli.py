#!/usr/bin/env python
import click
import mlib
import requests


@click.group()
@click.version_option("1.0")
def cli():
    """Machine learning toolkit"""


@cli.command("retrain")
@click.option("--test_size", default=0.2, type=float, help="Test size.")
@click.option("--estimators", default=100, type=int, help="Number of estimators.")
@click.option(
    "--criterion",
    default="gini",
    type=str,
    help="The function to measure the quality of a split. Supported ones: gini, entropy, or log_loss.",
)
@click.option(
    "--max_depth", default=None, type=int, help="The maximum depth of the tree."
)
@click.option(
    "--min_samples_split",
    default=2,
    type=int,
    help="The minimum number of samples required to split an internal node.",
)
@click.option(
    "--min_samples_leaf",
    default=1,
    type=int,
    help="The minimum number of samples required to be at a leaf node.",
)
@click.option(
    "--max_features",
    default=4,
    type=int,
    help="The number of features to consider when looking for the best split.",
)
def retrain(
    test_size,
    estimators,
    criterion,
    max_depth,
    min_samples_split,
    min_samples_leaf,
    max_features,
):
    """Retrain model"""

    click.echo(click.style("Retraining model...", bg="green", fg="white"))
    accuracy = mlib.retrain(
        tsize=test_size,
        n_estimators=estimators,
        criterion=criterion,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
    )
    click.echo(
        click.style(f"Retrained model accuracy: {accuracy}", bg="blue", fg="white")
    )


@cli.command("predict")
@click.option(
    "--host",
    type=str,
    default="http://127.0.0.1:8080/predict",
    help="Pass in the host to query.",
)
@click.option(
    "--preg",
    type=int,
    prompt="Number of times pregnant",
    help="Pass in the number of times pregnant",
)
@click.option(
    "--plas",
    type=int,
    prompt="Plasma glucose concentration after 2 hours in an oral glucose tolerance test",
    help="Pass in the plasma glucose concentration after 2 hours in an oral glucose tolerance test",
)
@click.option(
    "--pres",
    type=int,
    prompt="Diastolic blood pressure",
    help="Pass in the diastolic blood pressure (mm Hg)",
)
@click.option(
    "--skin",
    type=int,
    prompt="Triceps skin fold thickness",
    help="Pass in the triceps skin fold thickness (mm)",
)
@click.option(
    "--test",
    type=int,
    prompt="2-Hour serum insulin",
    help="Pass in the 2-Hour serum insulin (mu U/ml)",
)
@click.option(
    "--mass",
    type=float,
    prompt="Body mass index",
    help="Pass in the body mass index (weight in kg/(height in m)^2)",
)
@click.option(
    "--pedi",
    type=float,
    prompt="Diabetes pedigree function",
    help="Pass in the diabetes pedigree function)",
)
@click.option(
    "--age",
    type=int,
    prompt="Age",
    help="Pass in the age (years)",
)
def mkrequest(host, preg, plas, pres, skin, test, mass, pedi, age):
    """Sends new data to the ML endpoint for prediction"""

    click.echo(
        click.style(
            f"Querying {host} with preg: {preg}, plas: {plas}, pres: {pres}, skin: {skin}, test: {test}, mass: {mass}, pedi: {pedi}, and age: {age}",
            bg="green",
            fg="white",
        )
    )
    payload = {
        "preg": preg,
        "plas": plas,
        "pres": pres,
        "skin": skin,
        "test": test,
        "mass": mass,
        "pedi": pedi,
        "age": age,
    }
    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"result: {result.text}", bg="blue", fg="white"))


if __name__ == "__main__":
    cli()
