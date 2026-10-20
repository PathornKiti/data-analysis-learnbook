"""Reference solution: tests that pass on the correct code and catch all 9 injected bugs."""
import numpy as np
import pandas as pd
import pytest

from reportkit.stats import iqr_outliers, percent_change, share_missing


# ---- percent_change -----------------------------------------------------------------------
def test_percent_change_increase():
    assert percent_change(100, 150) == pytest.approx(50.0)


def test_percent_change_decrease_uses_old_value_as_base():
    assert percent_change(200, 100) == pytest.approx(-50.0)   # base is the OLD value, so this is -50, not -100


def test_percent_change_no_change():
    assert percent_change(80, 80) == 0


def test_percent_change_zero_old_raises():
    with pytest.raises(ValueError):
        percent_change(0, 5)


# ---- iqr_outliers -------------------------------------------------------------------------
def test_iqr_outliers_finds_high_values():
    assert iqr_outliers([1, 2, 3, 4, 5, 6, 7, 8, 15, 100]) == [15.0, 100.0]   # 15 is beyond 1.5*IQR but not 3*IQR


def test_iqr_outliers_finds_low_values():
    assert iqr_outliers([-100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [-100.0]


def test_iqr_outliers_value_on_the_fence_is_not_an_outlier():
    # Q1 = 2, Q3 = 6, IQR = 4, so the upper fence is exactly 12
    assert iqr_outliers([2, 2, 2, 6, 6, 6, 12]) == []


def test_iqr_outliers_none_in_tidy_data():
    assert iqr_outliers([1, 2, 3, 4, 5]) == []


# ---- share_missing ------------------------------------------------------------------------
def test_share_missing_is_a_fraction():
    df = pd.DataFrame({"a": [1, None, 3, 4]})
    assert share_missing(df, "a") == pytest.approx(0.25)


def test_share_missing_complete_and_all_missing():
    assert share_missing(pd.DataFrame({"a": [1, 2]}), "a") == 0.0
    assert share_missing(pd.DataFrame({"a": [np.nan, np.nan]}), "a") == 1.0


def test_share_missing_empty_dataframe_is_zero():
    assert share_missing(pd.DataFrame({"a": []}), "a") == 0.0
