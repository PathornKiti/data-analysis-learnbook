"""Statistics that answer questions about the data."""
import pandas as pd


def mean_rides_by(df: pd.DataFrame, column: str) -> pd.Series:
    """Average `rides` for each value of `column`, sorted from highest to lowest."""
    return df.groupby(column)["rides"].mean().sort_values(ascending=False)


def weekend_effect(df: pd.DataFrame) -> float:
    """Percent change in mean rides on weekends relative to weekdays.

    ((weekend mean - weekday mean) / weekday mean) * 100, using the `is_weekend` column (1 = weekend).
    """
    weekend = df.loc[df["is_weekend"] == 1, "rides"].mean()
    weekday = df.loc[df["is_weekend"] == 0, "rides"].mean()
    return float((weekend - weekday) / weekday * 100)
