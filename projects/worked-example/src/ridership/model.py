"""Predictive models, evaluated honestly: chronological split, baseline, and time-series cross-validation."""
import math

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

FEATURES = ["temp_c", "rain_mm", "is_weekend"]


def chronological_split(df: pd.DataFrame, n_test: int = 60) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Train on everything except the last ``n_test`` days; test on those last days (no shuffling)."""
    df = df.sort_values("date").reset_index(drop=True)
    return df.iloc[:-n_test], df.iloc[-n_test:]


def _models(seed: int = 0) -> dict:
    return {
        "baseline (train mean)": DummyRegressor(strategy="mean"),
        "linear regression": LinearRegression(),
        "random forest": RandomForestRegressor(n_estimators=200, random_state=seed),
    }


def evaluate_models(train: pd.DataFrame, test: pd.DataFrame, features=FEATURES, seed: int = 0) -> pd.DataFrame:
    """Fit each model on ``train`` and report RMSE and R² on ``test``."""
    rows = []
    for name, model in _models(seed).items():
        model.fit(train[features], train["rides"])
        pred = model.predict(test[features])
        rows.append((name, math.sqrt(mean_squared_error(test["rides"], pred)), r2_score(test["rides"], pred)))
    return pd.DataFrame(rows, columns=["model", "rmse", "r2"]).set_index("model")


def time_series_cv_rmse(df: pd.DataFrame, features=FEATURES, n_splits: int = 5, seed: int = 0) -> pd.DataFrame:
    """Expanding-window cross-validation: mean and sd of RMSE per model across ``n_splits`` future folds."""
    df = df.sort_values("date").reset_index(drop=True)
    scores = {name: [] for name in _models(seed)}
    for train_idx, test_idx in TimeSeriesSplit(n_splits=n_splits).split(df):
        tr, te = df.iloc[train_idx], df.iloc[test_idx]
        for name, model in _models(seed).items():
            model.fit(tr[features], tr["rides"])
            scores[name].append(math.sqrt(mean_squared_error(te["rides"], model.predict(te[features]))))
    return pd.DataFrame({name: {"rmse_mean": np.mean(v), "rmse_sd": np.std(v)} for name, v in scores.items()}).T
