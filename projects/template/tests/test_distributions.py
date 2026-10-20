import numpy as np
import pandas as pd
import pytest
from scipy import stats

from myproject.distributions import fit_candidates, qq_points, shape_summary, shape_table


def test_shape_summary_matches_scipy_and_counts_missing():
    x = [1.0, 2.0, 2.0, 3.0, 10.0, np.nan]
    out = shape_summary(x)
    clean = np.array([1.0, 2.0, 2.0, 3.0, 10.0])
    assert out["n"] == 5 and out["pct_missing"] == pytest.approx(100 / 6)
    assert out["skew"] == pytest.approx(stats.skew(clean)) and out["excess_kurtosis"] == pytest.approx(stats.kurtosis(clean))
    assert out["skew"] > 0, "a long right tail has positive skewness"


def test_shape_table_has_a_row_per_numeric_column():
    df = pd.DataFrame({"a": [1.0, 2, 3], "b": [2.0, 4, 9], "name": ["x", "y", "z"]})
    assert list(shape_table(df).index) == ["a", "b"]


def test_fit_candidates_prefers_the_true_family():
    rng = np.random.default_rng(0)
    assert fit_candidates(rng.lognormal(1.0, 0.7, 600)).index[0] == "lognorm"
    assert fit_candidates(rng.normal(50, 5, 600)).index[0] == "norm"


def test_fit_candidates_skips_positive_only_models_when_data_are_not_positive():
    out = fit_candidates(np.random.default_rng(1).normal(0, 1, 200))
    assert list(out.index) == ["norm"]


def test_qq_points_known_values():
    th, sm = qq_points([5.0, 1.0, 3.0])
    assert list(sm) == [1.0, 3.0, 5.0]
    assert np.allclose(th, stats.norm.ppf([1 / 6, 0.5, 5 / 6]))
