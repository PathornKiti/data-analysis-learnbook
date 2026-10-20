"""Reading the raw data. Nothing here modifies the original file."""
from pathlib import Path

import pandas as pd


def load_rides(path) -> pd.DataFrame:
    """Read the daily rides CSV with `date` parsed as datetimes, sorted by date.

    Args:
        path: Location of ``daily_rides.csv``.

    Returns:
        A DataFrame with columns date, temp_c, rain_mm, is_weekend, rides.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Rides file not found: {path}. Put the raw data in data/raw/.")
    return pd.read_csv(path, parse_dates=["date"]).sort_values("date").reset_index(drop=True)
