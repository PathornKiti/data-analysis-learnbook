"""Statistics and models that answer the project question."""
import pandas as pd


def group_summary(df: pd.DataFrame, by: str, value: str) -> pd.DataFrame:
    """Count, mean, median and standard deviation of `value` for each group in `by`."""
    return (
        df.groupby(by)[value]
        .agg(n="count", mean="mean", median="median", std="std")
        .round(2)
    )


def correlation(df: pd.DataFrame, a: str, b: str) -> float:
    """Pearson correlation between two numeric columns (between -1 and 1)."""
    return float(df[a].corr(df[b]))
