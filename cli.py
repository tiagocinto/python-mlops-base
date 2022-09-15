#!/usr/bin/env python
import click
import numpy as np
from mlib import predict


@click.command()
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
def predictcli(preg, plas, pres, skin, test, mass, pedi, age):
    """Predicts whether someone has tested positive for diabetes"""

    din = np.array([preg, plas, pres, skin, test, mass, pedi, age])
    result = predict(din)
    has_diabetes_class = result["has_diabetes_class"]
    has_diabetes_human_readable = result["has_diabetes_human_readable"]
    (
        click.echo(
            click.style(
                f"The patient has diabetes: {has_diabetes_human_readable}",
                bg="red",
                fg="white",
            )
        )
        if has_diabetes_class == 1
        else click.echo(
            click.style(
                f"The patient has diabetes: {has_diabetes_human_readable}",
                bg="green",
                fg="white",
            )
        )
    )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    predictcli()
