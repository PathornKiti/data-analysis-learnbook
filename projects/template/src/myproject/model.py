"""Fitting and evaluating models. Keep the test set untouched until the very end."""
import math

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split


def fit_ols(df: pd.DataFrame, formula: str):
    """Fit an ordinary-least-squares model with a formula such as "y ~ x1 + x2 + category"."""
    return smf.ols(formula, data=df).fit()


def coefficient_table(result) -> pd.DataFrame:
    """Coefficients with 95% confidence intervals and p-values, as a tidy DataFrame."""
    ci = result.conf_int()
    return pd.DataFrame(
        {"coef": result.params, "ci_low": ci[0], "ci_high": ci[1], "p_value": result.pvalues}
    ).round(4)


def evaluate_regression(df: pd.DataFrame, features: list[str], target: str,
                        test_size: float = 0.25, seed: int = 0) -> dict:
    """Train a linear model and a predict-the-mean baseline; report RMSE and R² on a held-out test set."""
    X_train, X_test, y_train, y_test = train_test_split(
        df[features], df[target], test_size=test_size, random_state=seed
    )
    baseline = DummyRegressor(strategy="mean").fit(X_train, y_train)
    model = LinearRegression().fit(X_train, y_train)

    def rmse(m):
        return math.sqrt(mean_squared_error(y_test, m.predict(X_test)))

    return {
        "baseline_rmse": rmse(baseline),
        "model_rmse": rmse(model),
        "model_r2": float(r2_score(y_test, model.predict(X_test))),
        "n_train": len(X_train),
        "n_test": len(X_test),
    }


def cross_val_r2(df: pd.DataFrame, features: list[str], target: str, cv: int = 5, seed: int = 0) -> tuple[float, float]:
    """Mean and standard deviation of cross-validated R² for a linear model."""
    splitter = KFold(n_splits=cv, shuffle=True, random_state=seed)
    scores = cross_val_score(LinearRegression(), df[features], df[target], cv=splitter, scoring="r2")
    return float(scores.mean()), float(scores.std())
