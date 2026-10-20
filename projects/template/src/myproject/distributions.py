"""Describing and fitting the distribution of a variable (Module 7b)."""
import numpy as np
import pandas as pd
from scipy import stats

_POSITIVE_ONLY = {"lognorm", "gamma", "expon"}


def shape_summary(values) -> dict:
    """Summary of one numeric variable: n, % missing, centre, spread, skewness and excess kurtosis."""
    s = pd.Series(values, dtype=float)
    x = s.dropna().to_numpy()
    return {
        "n": int(len(x)),
        "pct_missing": float(s.isna().mean() * 100),
        "mean": float(x.mean()),
        "median": float(np.median(x)),
        "sd": float(x.std(ddof=1)),
        "skew": float(stats.skew(x)),
        "excess_kurtosis": float(stats.kurtosis(x)),
        "min": float(x.min()),
        "max": float(x.max()),
    }


def shape_table(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """One row of :func:`shape_summary` per numeric column (all numeric columns by default)."""
    columns = list(columns) if columns is not None else df.select_dtypes("number").columns
    return pd.DataFrame({c: shape_summary(df[c]) for c in columns}).T.round(3)


def fit_candidates(values, candidates=("norm", "lognorm", "gamma", "expon")) -> pd.DataFrame:
    """Fit candidate distributions by maximum likelihood and rank them by AIC (lower is better).

    Positive-only distributions (lognormal, gamma, exponential) are skipped, with a note, if the data contain values <= 0;
    they are fitted with the location fixed at 0.
    """
    x = pd.Series(values, dtype=float).dropna().to_numpy()
    rows = []
    for name in candidates:
        dist = getattr(stats, name)
        if name in _POSITIVE_ONLY and (x <= 0).any():
            continue
        params = dist.fit(x, floc=0) if name in _POSITIVE_ONLY else dist.fit(x)
        k = len(params) - (1 if name in _POSITIVE_ONLY else 0)          # the fixed location is not estimated
        loglik = float(dist.logpdf(x, *params).sum())
        rows.append({"distribution": name, "k": k, "log_likelihood": loglik, "aic": 2 * k - 2 * loglik})
    return pd.DataFrame(rows).set_index("distribution").sort_values("aic").round(2)


def qq_points(values, dist=stats.norm):
    """Q-Q coordinates: (theoretical quantiles at (i - 0.5) / n, sorted sample)."""
    sample = np.sort(pd.Series(values, dtype=float).dropna().to_numpy())
    p = (np.arange(1, len(sample) + 1) - 0.5) / len(sample)
    return dist.ppf(p), sample
