"""Small helpers used when writing up results. They are correct as shipped. Your job is to
write tests good enough to catch the bugs the checker injects."""
import numpy as np
import pandas as pd


def percent_change(old: float, new: float) -> float:
    """Percent change from `old` to `new`: (new - old) / old * 100.

    Raises ValueError if `old` is zero (the change is undefined).
    """
    if old == 0:
        raise ValueError("old value must not be zero")
    return (new - old) / old * 100


def iqr_outliers(values) -> list[float]:
    """Return the sorted values lying strictly outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR].

    Quartiles use numpy's default linear-interpolation percentiles. A value exactly on a fence is NOT an outlier.
    """
    x = np.asarray(values, dtype=float)
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return sorted(float(v) for v in x[(x < low) | (x > high)])


def share_missing(df: pd.DataFrame, column: str) -> float:
    """Fraction (between 0 and 1) of missing values in `df[column]`. An empty DataFrame gives 0.0."""
    if len(df) == 0:
        return 0.0
    return float(df[column].isna().mean())
