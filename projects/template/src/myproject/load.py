"""Reading raw data. Nothing here modifies the original files."""
from pathlib import Path

import pandas as pd


def load_raw(path: str | Path) -> pd.DataFrame:
    """Read a raw CSV file into a DataFrame, leaving the file untouched.

    Raises FileNotFoundError with a helpful message if the file is missing.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No data file at {path}. Put your raw data in data/raw/.")
    return pd.read_csv(path)
