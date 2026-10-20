"""Cleaning steps. Every function returns a NEW DataFrame and leaves its input untouched."""
import pandas as pd


def flag_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Add a boolean column `temp_was_missing` that is True where `temp_c` is missing."""
    # TODO: copy the frame first (df.copy()) so the input is not modified
    raise NotImplementedError("flag_missing_temp")


def fill_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing `temp_c` with the median temperature of the same calendar month.

    If a month has no readings at all, fall back to the overall median.
    """
    # Hint: out.groupby(out["date"].dt.month)["temp_c"].transform("median") gives each row its month's median.
    raise NotImplementedError("fill_missing_temp")


def clean_rides(df: pd.DataFrame) -> pd.DataFrame:
    """Full cleaning pipeline: flag the missing temperatures first, then fill them."""
    # Order matters! Once the values are filled you can no longer tell which ones were missing.
    raise NotImplementedError("clean_rides")
