"""Statistics that answer the project questions (describe, compare, relate)."""
import math

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats


def describe_rides(df: pd.DataFrame) -> dict:
    """Headline description of daily rides, plus the busiest and quietest months."""
    monthly = df.groupby("month")["rides"].mean()
    return {
        "n_days": int(len(df)),
        "mean": float(df["rides"].mean()),
        "median": float(df["rides"].median()),
        "sd": float(df["rides"].std()),
        "peak_month": int(monthly.idxmax()),
        "peak_month_mean": float(monthly.max()),
        "low_month": int(monthly.idxmin()),
        "low_month_mean": float(monthly.min()),
    }


def compare_weekend(df: pd.DataFrame, n_perm: int = 5000, seed: int = 0) -> dict:
    """Compare mean daily rides on weekends and weekdays.

    Returns the two means, the difference (weekend - weekday) with a Welch 95% CI, the percent change,
    Cohen's d (NaN if both groups have zero variance) and a two-sided permutation-test p-value.
    """
    weekend = df.loc[df["is_weekend"] == 1, "rides"].to_numpy(dtype=float)
    weekday = df.loc[df["is_weekend"] == 0, "rides"].to_numpy(dtype=float)
    welch = stats.ttest_ind(weekend, weekday, equal_var=False)
    ci_low, ci_high = welch.confidence_interval(0.95)

    na, nb = len(weekend), len(weekday)
    pooled_var = ((na - 1) * weekend.var(ddof=1) + (nb - 1) * weekday.var(ddof=1)) / (na + nb - 2)

    rng = np.random.default_rng(seed)
    pooled = np.concatenate([weekend, weekday])
    observed = abs(weekend.mean() - weekday.mean())
    hits = 0
    for _ in range(n_perm):
        rng.shuffle(pooled)
        hits += abs(pooled[:na].mean() - pooled[na:].mean()) >= observed

    diff = weekend.mean() - weekday.mean()
    return {
        "weekend_mean": float(weekend.mean()),
        "weekday_mean": float(weekday.mean()),
        "diff": float(diff),
        "diff_ci": (float(ci_low), float(ci_high)),
        "pct_change": float(diff / weekday.mean() * 100),
        "cohens_d": float(diff / math.sqrt(pooled_var)) if pooled_var > 0 else float("nan"),
        "p_perm": float(hits / n_perm),
        "n_weekend": na,
        "n_weekday": nb,
    }


def correlation_with_ci(x, y, n_boot: int = 3000, seed: int = 0) -> dict:
    """Pearson correlation with a percentile-bootstrap 95% interval."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    boot = np.array([np.corrcoef(x[i], y[i])[0, 1] for i in idx])
    return {
        "r": float(np.corrcoef(x, y)[0, 1]),
        "ci": (float(np.quantile(boot, 0.025)), float(np.quantile(boot, 0.975))),
    }


def fit_demand_model(df: pd.DataFrame):
    """OLS of daily rides on temperature, rainfall and weekend (the explanatory model)."""
    return smf.ols("rides ~ temp_c + rain_mm + is_weekend", data=df).fit()


def coefficient_table(result) -> pd.DataFrame:
    """Coefficients with 95% confidence intervals and p-values."""
    ci = result.conf_int()
    return pd.DataFrame(
        {"coef": result.params, "ci_low": ci[0], "ci_high": ci[1], "p_value": result.pvalues}
    ).round(4)
