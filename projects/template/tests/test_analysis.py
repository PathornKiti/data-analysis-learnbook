import numpy as np
import pandas as pd
import pytest
from scipy import stats

from myproject.analysis import bootstrap_ci, cohens_d, correlation, mean_ci, permutation_test


def test_mean_ci_matches_scipy():
    x = np.array([4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    expected = stats.t.interval(0.95, df=len(x) - 1, loc=x.mean(), scale=stats.sem(x))
    assert mean_ci(x) == pytest.approx(expected)


def test_mean_ci_ignores_missing_values():
    assert mean_ci([1.0, 2.0, 3.0, np.nan]) == pytest.approx(mean_ci([1.0, 2.0, 3.0]))


def test_bootstrap_ci_surrounds_the_estimate_and_is_repeatable():
    x = np.random.default_rng(1).normal(50, 5, size=100)
    low, high = bootstrap_ci(x, seed=3)
    assert low < x.mean() < high
    assert (low, high) == bootstrap_ci(x, seed=3)


def test_permutation_test_detects_a_clear_difference_but_not_noise():
    rng = np.random.default_rng(0)
    same_a, same_b = rng.normal(0, 1, 60), rng.normal(0, 1, 60)
    far_a, far_b = rng.normal(0, 1, 60), rng.normal(2, 1, 60)
    assert permutation_test(far_a, far_b, n_perm=1000) < 0.01
    assert permutation_test(same_a, same_b, n_perm=1000) > 0.05


def test_cohens_d_known_value():
    assert cohens_d([2, 3, 4], [1, 2, 3]) == pytest.approx(1.0)


def test_correlation_perfect_line():
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]})
    assert correlation(df, "x", "y") == pytest.approx(1.0)
