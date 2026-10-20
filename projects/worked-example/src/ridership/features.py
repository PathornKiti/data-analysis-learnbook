"""New columns derived from existing ones."""
import pandas as pd


def add_calendar_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add ``month`` (1-12) and ``weekday`` (day name)."""
    out = df.copy()
    out["month"] = out["date"].dt.month
    out["weekday"] = out["date"].dt.day_name()
    return out


def add_rain_flag(df: pd.DataFrame) -> pd.DataFrame:
    """Add ``rainy`` (True on days with any rain)."""
    out = df.copy()
    out["rainy"] = out["rain_mm"] > 0
    return out
