"""Reading the raw data."""
from pathlib import Path

import pandas as pd


def load_rides(path) -> pd.DataFrame:
    """Read the daily rides CSV, parsing the `date` column as datetimes.

    Raises FileNotFoundError (mentioning the path) if the file does not exist.
    """
    # TODO: use pathlib.Path to check the file exists, then pd.read_csv(..., parse_dates=["date"])
    raise NotImplementedError("load_rides")
