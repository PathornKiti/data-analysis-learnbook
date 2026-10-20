import pandas as pd
import pytest

from ridekit.analysis import mean_rides_by, weekend_effect


def test_mean_rides_by_sorted_high_to_low():
    df = pd.DataFrame({"band": ["a", "a", "b", "b", "c"], "rides": [10, 20, 40, 60, 30]})
    out = mean_rides_by(df, "band")
    assert out.index.tolist() == ["b", "c", "a"]
    assert out.tolist() == [50.0, 30.0, 15.0]


def test_weekend_effect_is_percent_change():
    df = pd.DataFrame({"rides": [100, 100, 80, 80], "is_weekend": [0, 0, 1, 1]})
    assert weekend_effect(df) == pytest.approx(-20.0)


def test_weekend_effect_positive():
    df = pd.DataFrame({"rides": [100, 150], "is_weekend": [0, 1]})
    assert weekend_effect(df) == pytest.approx(50.0)
