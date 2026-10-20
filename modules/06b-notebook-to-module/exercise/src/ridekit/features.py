"""New columns derived from existing ones."""
import pandas as pd


def add_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Add a `weekday` column with the day name, e.g. "Monday"."""
    # Hint: df["date"].dt.day_name()
    raise NotImplementedError("add_weekday")


def add_temp_band(df: pd.DataFrame) -> pd.DataFrame:
    """Add a `temp_band` column: "cold" below 10 °C, "mild" from 10 up to (not including) 20, "warm" from 20 up."""
    # Hint: pd.cut(..., bins=[-inf, 10, 20, inf], labels=[...], right=False)  ("right=False" makes the left edge inclusive)
    raise NotImplementedError("add_temp_band")
