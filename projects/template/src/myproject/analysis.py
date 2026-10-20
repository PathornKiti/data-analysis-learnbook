"""Statistics and models that answer the project question."""
import math

import numpy as np
import pandas as pd
from scipy import stats


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


def mean_ci(values, confidence: float = 0.95) -> tuple[float, float]:
    """t-based confidence interval for the mean (missing values are ignored)."""
    x = pd.Series(values).dropna().to_numpy(dtype=float)
    se = x.std(ddof=1) / math.sqrt(len(x))
    half = stats.t.ppf((1 + confidence) / 2, df=len(x) - 1) * se
    return float(x.mean() - half), float(x.mean() + half)


def bootstrap_ci(values, stat=np.mean, n_boot: int = 5000, confidence: float = 0.95, seed: int = 0):
    """Percentile bootstrap CI for any statistic (e.g. np.median). `seed` makes it repeatable."""
    x = pd.Series(values).dropna().to_numpy(dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    boot = np.apply_along_axis(stat, 1, x[idx])
    alpha = (1 - confidence) / 2
    low, high = np.quantile(boot, [alpha, 1 - alpha])
    return float(low), float(high)


def permutation_test(a, b, n_perm: int = 5000, seed: int = 0) -> float:
    """Two-sided permutation-test p-value for a difference in means between samples `a` and `b`."""
    a = pd.Series(a).dropna().to_numpy(dtype=float)
    b = pd.Series(b).dropna().to_numpy(dtype=float)
    observed = abs(a.mean() - b.mean())
    pooled = np.concatenate([a, b])
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(pooled)
        count += abs(pooled[: len(a)].mean() - pooled[len(a):].mean()) >= observed
    return float(count / n_perm)


def cohens_d(a, b) -> float:
    """Standardised difference in means (pooled standard deviation)."""
    a = pd.Series(a).dropna().to_numpy(dtype=float)
    b = pd.Series(b).dropna().to_numpy(dtype=float)
    na, nb = len(a), len(b)
    pooled_var = ((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)
    return float((a.mean() - b.mean()) / math.sqrt(pooled_var))
