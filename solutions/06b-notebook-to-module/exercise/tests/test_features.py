import pandas as pd

from ridekit.features import add_temp_band, add_weekday


def test_add_weekday():
    df = pd.DataFrame({"date": pd.to_datetime(["2024-01-01", "2024-01-06"])})  # a Monday and a Saturday
    out = add_weekday(df)
    assert out["weekday"].tolist() == ["Monday", "Saturday"]
    assert "weekday" not in df.columns, "do not modify the input"


def test_add_temp_band_boundaries():
    df = pd.DataFrame({"temp_c": [-5.0, 9.9, 10.0, 19.9, 20.0, 30.0]})
    out = add_temp_band(df)
    assert out["temp_band"].astype(str).tolist() == ["cold", "cold", "mild", "mild", "warm", "warm"]
    assert "temp_band" not in df.columns, "do not modify the input"
