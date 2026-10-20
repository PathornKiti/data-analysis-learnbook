"""pytest plugin used by check_my_tests.py: injects ONE bug (chosen by the RK_MUTANT environment variable)
into reportkit.stats before your tests are collected. Not meant to be edited."""
import os

import numpy as np
import reportkit.stats as stats

MUTANT = os.environ.get("RK_MUTANT", "")


def _percent_change(old, new, *, base="old", scale=100.0, raise_on_zero=True):
    if old == 0 and raise_on_zero:
        raise ValueError("old value must not be zero")
    if old == 0:
        return float("inf")
    denom = old if base == "old" else new
    return (new - old) / denom * scale


def _iqr(values, *, factor=1.5, inclusive=False, low_side=True):
    x = np.asarray(values, dtype=float)
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    if inclusive:
        mask = (x <= low) | (x >= high)
    else:
        mask = (x < low) | (x > high) if low_side else (x > high)
    return sorted(float(v) for v in x[mask])


if MUTANT == "pc_wrong_base":
    stats.percent_change = lambda old, new: _percent_change(old, new, base="new")
elif MUTANT == "pc_no_percent":
    stats.percent_change = lambda old, new: _percent_change(old, new, scale=1.0)
elif MUTANT == "pc_zero_no_raise":
    stats.percent_change = lambda old, new: _percent_change(old, new, raise_on_zero=False)
elif MUTANT == "iqr_factor_3":
    stats.iqr_outliers = lambda values: _iqr(values, factor=3.0)
elif MUTANT == "iqr_boundary_inclusive":
    stats.iqr_outliers = lambda values: _iqr(values, inclusive=True)
elif MUTANT == "iqr_only_high":
    stats.iqr_outliers = lambda values: _iqr(values, low_side=False)
elif MUTANT == "sm_count":
    stats.share_missing = lambda df, column: float(df[column].isna().sum())
elif MUTANT == "sm_inverted":
    stats.share_missing = lambda df, column: 0.0 if len(df) == 0 else float(df[column].notna().mean())
elif MUTANT == "sm_empty_nan":
    stats.share_missing = lambda df, column: float(df[column].isna().mean())
elif MUTANT:
    raise RuntimeError(f"unknown mutant {MUTANT!r}")
