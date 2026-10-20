"""Hypothesis tests reported with estimates, intervals and effect sizes (Module 8b).

Each ``*_report`` returns a dictionary so results can be printed, saved or tested. ``two_group_report`` runs several
methods side by side as a built-in sensitivity analysis: if they disagree, say so.
"""
import math

import numpy as np
import pandas as pd
from scipy import stats

from myproject.analysis import cohens_d, permutation_test


def format_p(p: float) -> str:
    """Format a p-value for reporting: ``p < 0.001`` or ``p = 0.026`` (never ``p = 0.000``)."""
    return "p < 0.001" if p < 0.001 else f"p = {p:.3f}"


def holm_adjust(pvals) -> np.ndarray:
    """Holm-adjusted p-values in the original order (controls the family-wise error rate)."""
    p = np.asarray(pvals, dtype=float)
    m = len(p)
    order = np.argsort(p)
    adjusted = np.maximum.accumulate(np.minimum(1.0, p[order] * (m - np.arange(m))))
    out = np.empty(m)
    out[order] = adjusted
    return out


def two_group_report(a, b, seed: int = 0) -> dict:
    """Compare two independent samples with Welch's t, Mann-Whitney U and a permutation test.

    Args:
        a: First sample.
        b: Second sample.
        seed: Seed for the permutation test.

    Returns:
        Means, the difference (a - b) with its Welch 95% CI, Welch t / df / p, Cohen's d and Hedges' g,
        Mann-Whitney U / p / probability of superiority, and the permutation p-value.
    """
    a = pd.Series(a, dtype=float).dropna().to_numpy()
    b = pd.Series(b, dtype=float).dropna().to_numpy()
    welch = stats.ttest_ind(a, b, equal_var=False)
    ci = welch.confidence_interval(0.95)
    mw = stats.mannwhitneyu(a, b, alternative="two-sided")
    d = cohens_d(a, b)
    return {
        "n_a": len(a), "n_b": len(b),
        "mean_a": float(a.mean()), "mean_b": float(b.mean()),
        "diff": float(a.mean() - b.mean()), "diff_ci": (float(ci.low), float(ci.high)),
        "welch_t": float(welch.statistic), "welch_df": float(welch.df), "welch_p": float(welch.pvalue),
        "cohens_d": d, "hedges_g": d * (1 - 3 / (4 * (len(a) + len(b)) - 9)),
        "mann_whitney_u": float(mw.statistic), "mann_whitney_p": float(mw.pvalue),
        "prob_superiority": float(mw.statistic / (len(a) * len(b))),
        "permutation_p": permutation_test(a, b, seed=seed),
    }


def paired_report(before, after) -> dict:
    """Paired t-test (and Wilcoxon signed-rank) on within-person changes ``after - before``."""
    d = pd.Series(np.asarray(after, dtype=float) - np.asarray(before, dtype=float)).dropna().to_numpy()
    t = stats.ttest_1samp(d, 0.0)
    ci = t.confidence_interval(0.95)
    return {
        "n": len(d), "mean_change": float(d.mean()), "change_ci": (float(ci.low), float(ci.high)),
        "t": float(t.statistic), "df": len(d) - 1, "p": float(t.pvalue),
        "dz": float(d.mean() / d.std(ddof=1)), "wilcoxon_p": float(stats.wilcoxon(d).pvalue),
    }


def two_proportion_report(x1: int, n1: int, x2: int, n2: int) -> dict:
    """Two-proportion z-test with the difference, its unpooled 95% CI, risk ratio and odds ratio."""
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    z = (p1 - p2) / math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    return {
        "p1": p1, "p2": p2, "diff": p1 - p2,
        "diff_ci": (p1 - p2 - 1.96 * se, p1 - p2 + 1.96 * se),
        "z": z, "p": float(2 * stats.norm.sf(abs(z))),
        "risk_ratio": p1 / p2, "odds_ratio": (p1 / (1 - p1)) / (p2 / (1 - p2)),
    }
