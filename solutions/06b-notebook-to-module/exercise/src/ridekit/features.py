"""New columns derived from existing ones."""
import pandas as pd


def add_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Add a `weekday` column with the day name, e.g. "Monday"."""
    out = df.copy()
    out["weekday"] = out["date"].dt.day_name()
    return out


def add_temp_band(df: pd.DataFrame) -> pd.DataFrame:
    """Add a `temp_band` column: "cold" below 10 °C, "mild" from 10 up to (not including) 20, "warm" from 20 up."""
    out = df.copy()
    out["temp_band"] = pd.cut(
        out["temp_c"],
        bins=[float("-inf"), 10, 20, float("inf")],
        labels=["cold", "mild", "warm"],
        right=False,
    )
    return out
