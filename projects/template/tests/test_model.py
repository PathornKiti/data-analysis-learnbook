import numpy as np
import pandas as pd
import pytest

from myproject.model import coefficient_table, cross_val_r2, evaluate_regression, fit_ols


@pytest.fixture
def linear_data():
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 10, 200)
    z = rng.normal(size=200)
    return pd.DataFrame({"x": x, "z": z, "y": 3 + 2 * x + 0.5 * z + rng.normal(0, 1, 200)})


def test_fit_ols_recovers_coefficients(linear_data):
    result = fit_ols(linear_data, "y ~ x + z")
    assert result.params["x"] == pytest.approx(2.0, abs=0.1)
    assert result.params["Intercept"] == pytest.approx(3.0, abs=0.5)


def test_coefficient_table_columns_and_interval(linear_data):
    table = coefficient_table(fit_ols(linear_data, "y ~ x + z"))
    assert list(table.columns) == ["coef", "ci_low", "ci_high", "p_value"]
    assert (table["ci_low"] < table["coef"]).all() and (table["coef"] < table["ci_high"]).all()


def test_model_beats_baseline_on_held_out_data(linear_data):
    out = evaluate_regression(linear_data, ["x", "z"], "y")
    assert out["n_train"] == 150 and out["n_test"] == 50
    assert out["model_rmse"] < out["baseline_rmse"] / 2
    assert out["model_r2"] > 0.9


def test_cross_val_r2_is_high_and_repeatable(linear_data):
    mean, std = cross_val_r2(linear_data, ["x", "z"], "y")
    assert mean > 0.9 and std < 0.1
    assert (mean, std) == cross_val_r2(linear_data, ["x", "z"], "y")
