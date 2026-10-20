"""Cleaning and validation. Every cleaning function returns a NEW DataFrame."""
import pandas as pd


def flag_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Add a boolean column ``temp_was_missing`` (True where the temperature reading is missing)."""
    out = df.copy()
    out["temp_was_missing"] = out["temp_c"].isna()
    return out


def fill_missing_temp(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing ``temp_c`` with the median of the same calendar month (overall median if a month has none).

    Why: the sensor outages are short and temperature is strongly seasonal, so a monthly median is a
    reasonable, simple estimate. The ``temp_was_missing`` flag lets us check that the results do not depend on it.
    """
    out = df.copy()
    month_median = out.groupby(out["date"].dt.month)["temp_c"].transform("median")
    out["temp_c"] = out["temp_c"].fillna(month_median).fillna(out["temp_c"].median())
    return out


def validate_rides(df: pd.DataFrame) -> list[str]:
    """Return a list of problems found in the (cleaned) rides table; an empty list means it is fine."""
    problems = []
    if df["date"].duplicated().any():
        problems.append("duplicate dates")
    if df[["temp_c", "rain_mm", "rides", "is_weekend"]].isna().any().any():
        problems.append("missing values remain")
    if not df["is_weekend"].isin([0, 1]).all():
        problems.append("is_weekend must be 0 or 1")
    if (df["rain_mm"] < 0).any():
        problems.append("negative rainfall")
    if (df["rides"] <= 0).any():
        problems.append("non-positive ride counts")
    if not df["temp_c"].between(-30, 50).all():
        problems.append("temperature outside -30..50 C")
    expected_weekend = (df["date"].dt.dayofweek >= 5).astype(int)
    if (df["is_weekend"] != expected_weekend).any():
        problems.append("is_weekend disagrees with the calendar")
    return problems


def clean_rides(df: pd.DataFrame) -> pd.DataFrame:
    """Full cleaning pipeline: flag, fill, then validate. Raises ValueError if the result is not valid."""
    out = fill_missing_temp(flag_missing_temp(df))
    problems = validate_rides(out)
    if problems:
        raise ValueError("Data validation failed: " + "; ".join(problems))
    return out
