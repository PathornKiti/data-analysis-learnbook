import re

import pandas as pd
import pytest

from ridekit.cli import main


def test_cli_report(rides_csv, capsys):
    assert main(["--input", str(rides_csv)]) == 0
    out = capsys.readouterr().out

    df = pd.read_csv(rides_csv, parse_dates=["date"])
    busiest = df.groupby(df["date"].dt.day_name())["rides"].mean().idxmax()
    weekend = df.loc[df["is_weekend"] == 1, "rides"].mean()
    weekday = df.loc[df["is_weekend"] == 0, "rides"].mean()
    expected_effect = (weekend - weekday) / weekday * 100

    assert "Rows: 366" in out
    assert f"Busiest weekday: {busiest}" in out
    match = re.search(r"Weekend effect: (-?\d+\.\d)%", out)
    assert match, f"missing 'Weekend effect: X.X%' line in:\n{out}"
    assert float(match.group(1)) == pytest.approx(expected_effect, abs=0.06)


def test_cli_missing_file_returns_1(tmp_path, capsys):
    assert main(["--input", str(tmp_path / "missing.csv")]) == 1
    assert "missing.csv" in capsys.readouterr().err
