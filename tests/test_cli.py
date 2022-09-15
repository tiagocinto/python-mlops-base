from click.testing import CliRunner
from cli import predictcli


def test_predictcli_negative_patient():
    runner = CliRunner()
    args = [
        "--preg",
        "2",
        "--plas",
        "88",
        "--pres",
        "58",
        "--skin",
        "26",
        "--test",
        "16",
        "--mass",
        "28.4",
        "--pedi",
        "0.766",
        "--age",
        "22",
    ]
    result = runner.invoke(predictcli, args)
    assert result.exit_code == 0
    assert "no" in result.output


def test_predictcli_positive_patient():
    runner = CliRunner()
    args = [
        "--preg",
        "9",
        "--plas",
        "170",
        "--pres",
        "74",
        "--skin",
        "31",
        "--test",
        "0",
        "--mass",
        "44",
        "--pedi",
        "0.403",
        "--age",
        "43",
    ]
    result = runner.invoke(predictcli, args)
    assert result.exit_code == 0
    assert "yes" in result.output
