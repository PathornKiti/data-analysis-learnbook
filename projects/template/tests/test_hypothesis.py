import numpy as np
import pytest
from scipy import stats
from statsmodels.stats.multitest import multipletests

from myproject.hypothesis import format_p, holm_adjust, paired_report, two_group_report, two_proportion_report


def test_format_p():
    assert format_p(0.0004) == "p < 0.001" and format_p(0.0724) == "p = 0.072"


def test_holm_adjust_known_and_matches_statsmodels():
    assert np.allclose(holm_adjust([0.01, 0.04, 0.03, 0.20]), [0.04, 0.09, 0.09, 0.20])
    p = np.random.default_rng(0).uniform(0, 0.1, 7)
    assert np.allclose(holm_adjust(p), multipletests(p, method="holm")[1])


def test_two_group_report_agrees_with_scipy_and_methods_agree_on_a_clear_effect():
    rng = np.random.default_rng(0)
    a, b = rng.normal(10, 2, 80), rng.normal(12, 2, 80)
    out = two_group_report(a, b)
    ref = stats.ttest_ind(a, b, equal_var=False)
    assert out["welch_t"] == pytest.approx(ref.statistic) and out["welch_p"] == pytest.approx(ref.pvalue)
    assert out["diff"] == pytest.approx(a.mean() - b.mean()) and out["diff_ci"][0] < out["diff"] < out["diff_ci"][1]
    assert out["welch_p"] < 0.001 and out["mann_whitney_p"] < 0.001 and out["permutation_p"] < 0.01
    assert out["cohens_d"] < 0 and out["prob_superiority"] < 0.5, "a is lower than b"
    assert abs(out["hedges_g"]) < abs(out["cohens_d"]), "the small-sample correction shrinks d"


def test_two_group_report_finds_no_effect_in_identical_distributions():
    rng = np.random.default_rng(3)
    out = two_group_report(rng.normal(0, 1, 60), rng.normal(0, 1, 60))
    assert out["welch_p"] > 0.05 and out["diff_ci"][0] < 0 < out["diff_ci"][1]


def test_paired_report_uses_the_differences():
    before = np.array([10.0, 12, 9, 11, 13, 10])
    after = before + np.array([2.0, 1, 3, 2, 2, 1])
    out = paired_report(before, after)
    ref = stats.ttest_rel(after, before)
    assert out["t"] == pytest.approx(ref.statistic) and out["p"] == pytest.approx(ref.pvalue) and out["df"] == 5
    assert out["mean_change"] == pytest.approx(1.8333, abs=1e-3)


def test_two_proportion_report_known_numbers():
    out = two_proportion_report(33, 100, 17, 100)
    assert out["diff"] == pytest.approx(0.16) and out["odds_ratio"] == pytest.approx(2.405, abs=1e-3)
    assert out["risk_ratio"] == pytest.approx(1.941, abs=1e-3) and out["p"] == pytest.approx(0.00898, abs=1e-4)
    assert out["diff_ci"][0] == pytest.approx(0.042, abs=2e-3) and out["diff_ci"][1] == pytest.approx(0.278, abs=2e-3)
