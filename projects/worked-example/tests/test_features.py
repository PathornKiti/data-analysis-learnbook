import pandas as pd

from ridership.features import add_calendar_features, add_rain_flag


def test_calendar_features():
    df = pd.DataFrame({"date": pd.to_datetime(["2024-01-01", "2024-07-06"])})   # a Monday, a Saturday
    out = add_calendar_features(df)
    assert out["month"].tolist() == [1, 7]
    assert out["weekday"].tolist() == ["Monday", "Saturday"]


def test_rain_flag_is_true_only_when_it_rained():
    out = add_rain_flag(pd.DataFrame({"rain_mm": [0.0, 0.1, 5.0]}))
    assert out["rainy"].tolist() == [False, True, True]
