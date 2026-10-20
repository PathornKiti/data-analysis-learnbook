import numpy as np
import pandas as pd

from ridership.model import chronological_split, evaluate_models, time_series_cv_rmse


def synthetic(n=200):
    rng = np.random.default_rng(1)
    df = pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=n),
            "temp_c": rng.uniform(0, 30, n),
            "rain_mm": rng.exponential(2, n),
            "is_weekend": rng.integers(0, 2, n),
        }
    )
    df["rides"] = 500 + 40 * df["temp_c"] - 20 * df["rain_mm"] - 100 * df["is_weekend"] + rng.normal(0, 20, n)
    return df


def test_chronological_split_never_leaks_the_future():
    train, test = chronological_split(synthetic(), n_test=40)
    assert len(train) == 160 and len(test) == 40
    assert train["date"].max() < test["date"].min()


def test_chronological_split_sorts_by_date_first():
    shuffled = synthetic().sample(frac=1, random_state=0)
    train, test = chronological_split(shuffled, n_test=40)
    assert train["date"].max() < test["date"].min()


def test_linear_model_beats_baseline_on_linear_data():
    train, test = chronological_split(synthetic(), n_test=40)
    out = evaluate_models(train, test)
    assert list(out.index) == ["baseline (train mean)", "linear regression", "random forest"]
    assert out.loc["linear regression", "rmse"] < out.loc["baseline (train mean)", "rmse"] / 3
    assert out.loc["linear regression", "r2"] > 0.9


def test_time_series_cv_shape_and_repeatability():
    df = synthetic()
    a = time_series_cv_rmse(df, n_splits=4)
    assert list(a.columns) == ["rmse_mean", "rmse_sd"] and len(a) == 3
    assert a.equals(time_series_cv_rmse(df, n_splits=4))
