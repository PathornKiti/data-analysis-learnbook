import numpy as np
import pandas as pd
import pytest

from ridership.analysis import coefficient_table, compare_weekend, correlation_with_ci, describe_rides, fit_demand_model


def test_compare_weekend_known_numbers():
    df = pd.DataFrame({"rides": [90.0, 110, 95, 105, 70, 90], "is_weekend": [0, 0, 0, 0, 1, 1]})
    out = compare_weekend(df, n_perm=200)
    assert out["weekday_mean"] == 100 and out["weekend_mean"] == 80
    assert out["diff"] == -20 and out["pct_change"] == pytest.approx(-20.0)
    assert (out["n_weekend"], out["n_weekday"]) == (2, 4)


def test_compare_weekend_on_real_data_matches_headline(real_rides_path):
    from ridership.clean import clean_rides
    from ridership.load import load_rides

    df = clean_rides(load_rides(real_rides_path))
    out = compare_weekend(df)
    assert out["pct_change"] == pytest.approx(-10.8, abs=0.1)
    assert out["diff_ci"][1] < 0, "the whole interval is below zero: weekends are quieter"
    assert out["p_perm"] < 0.05


@pytest.mark.filterwarnings("ignore::RuntimeWarning")   # SciPy warns about degenerate (zero-spread) data; that is the point here
def test_cohens_d_is_nan_when_there_is_no_spread():
    df = pd.DataFrame({"rides": [100.0, 100, 80, 80], "is_weekend": [0, 0, 1, 1]})
    assert np.isnan(compare_weekend(df, n_perm=50)["cohens_d"])


def test_correlation_with_ci_perfect_line():
    x = np.arange(30.0)
    out = correlation_with_ci(x, 2 * x + 1, n_boot=200)
    assert out["r"] == pytest.approx(1.0)
    assert out["ci"][0] <= 1.0 and out["ci"][1] >= 0.999


def test_describe_rides_peak_and_low_months():
    df = pd.DataFrame({"rides": [100.0, 300.0, 200.0, 200.0], "month": [1, 7, 7, 1]})
    d = describe_rides(df)
    assert d["peak_month"] == 7 and d["low_month"] == 1 and d["n_days"] == 4
    assert d["peak_month_mean"] == 250.0 and d["low_month_mean"] == 150.0


def test_demand_model_recovers_planted_effects():
    rng = np.random.default_rng(0)
    n = 400
    df = pd.DataFrame({"temp_c": rng.uniform(0, 30, n), "rain_mm": rng.exponential(2, n), "is_weekend": rng.integers(0, 2, n)})
    df["rides"] = 800 + 50 * df["temp_c"] - 20 * df["rain_mm"] - 150 * df["is_weekend"] + rng.normal(0, 30, n)
    table = coefficient_table(fit_demand_model(df))
    assert table.loc["temp_c", "coef"] == pytest.approx(50, abs=2)
    assert table.loc["rain_mm", "coef"] == pytest.approx(-20, abs=3)
    assert table.loc["is_weekend", "coef"] == pytest.approx(-150, abs=15)
    assert list(table.columns) == ["coef", "ci_low", "ci_high", "p_value"]
