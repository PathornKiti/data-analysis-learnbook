"""Statistics that answer questions about the data."""
import pandas as pd


def mean_rides_by(df: pd.DataFrame, column: str) -> pd.Series:
    """Average `rides` for each value of `column`, sorted from highest to lowest."""
    raise NotImplementedError("mean_rides_by")


def weekend_effect(df: pd.DataFrame) -> float:
    """Percent change in mean rides on weekends relative to weekdays.

    ((weekend mean - weekday mean) / weekday mean) * 100, using the `is_weekend` column (1 = weekend).
    """
    raise NotImplementedError("weekend_effect")
