import pandas as pd
import pytest

from ridekit.load import load_rides


def test_load_rides_parses_dates(rides_csv):
    df = load_rides(rides_csv)
    assert len(df) == 366
    assert pd.api.types.is_datetime64_any_dtype(df["date"]), "`date` should be parsed as datetime"


def test_load_rides_missing_file_mentions_path(tmp_path):
    missing = tmp_path / "nope.csv"
    with pytest.raises(FileNotFoundError, match="nope.csv"):
        load_rides(missing)
