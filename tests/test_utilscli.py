import re
from click.testing import CliRunner
from utilscli import retrain


def test_retrain():
    runner = CliRunner()
    args = [
        "--test_size",
        "0.5",
        "--estimators",
        "50",
        "--criterion",
        "entropy",
        "--max_depth",
        "10",
        "--min_samples_split",
        "4",
        "--min_samples_leaf",
        "3",
        "--max_features",
        "4",
    ]
    result = runner.invoke(retrain, args)
    assert result.exit_code == 0
    assert bool(re.search(r"\d", result.output)) == True
