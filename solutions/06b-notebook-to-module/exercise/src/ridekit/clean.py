"""Cleaning steps. Every function returns a NEW DataFrame and leaves its input untouched."""
import pandas as pd


def flag_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Add a boolean column `temp_was_missing` that is True where `temp_c` is missing."""
    out = df.copy()
    out["temp_was_missing"] = out["temp_c"].isna()
    return out


def fill_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing `temp_c` with the median temperature of the same calendar month.

    If a month has no readings at all, fall back to the overall median.
    """
    out = df.copy()
    month_median = out.groupby(out["date"].dt.month)["temp_c"].transform("median")
    out["temp_c"] = out["temp_c"].fillna(month_median).fillna(out["temp_c"].median())
    return out


def clean_rides(df: pd.DataFrame) -> pd.DataFrame:
    """Full cleaning pipeline: flag the missing temperatures first, then fill them."""
    return fill_missing_temp(flag_missing_temp(df))
