"""Reading the raw data."""
from pathlib import Path

import pandas as pd


def load_rides(path) -> pd.DataFrame:
    """Read the daily rides CSV, parsing the `date` column as datetimes.

    Raises FileNotFoundError (mentioning the path) if the file does not exist.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Rides file not found: {path}")
    return pd.read_csv(path, parse_dates=["date"])
