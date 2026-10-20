import pandas as pd
import pytest

from ridership.clean import clean_rides, fill_missing_temp, flag_missing_temp, validate_rides
from ridership.load import load_rides


def small_frame():
    return pd.DataFrame(
        {
            "date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03", "2024-02-01", "2024-02-02", "2024-03-01"]),
            "temp_c": [0.0, None, 10.0, 20.0, None, None],
            "rain_mm": [0.0] * 6,
            "is_weekend": [0, 0, 0, 0, 0, 0],
            "rides": [1000] * 6,
        }
    )


def test_flag_missing_temp():
    assert flag_missing_temp(small_frame())["temp_was_missing"].tolist() == [False, True, False, False, True, True]


def test_fill_uses_month_median_then_overall_median():
    out = fill_missing_temp(small_frame())
    assert out["temp_c"].tolist() == [0.0, 5.0, 10.0, 20.0, 20.0, 10.0]


def test_cleaning_does_not_modify_input():
    df = small_frame()
    before = df.copy()
    fill_missing_temp(flag_missing_temp(df))
    pd.testing.assert_frame_equal(df, before)


def test_clean_rides_on_real_data(real_rides_path):
    raw = load_rides(real_rides_path)
    out = clean_rides(raw)
    assert len(out) == len(raw) == 366
    assert out["temp_c"].notna().all()
    assert out["temp_was_missing"].sum() == 6


@pytest.mark.parametrize(
    "column, bad_value, expected_message",
    [
        ("rain_mm", -1.0, "negative rainfall"),
        ("rides", 0, "non-positive ride counts"),
        ("temp_c", 99.0, "temperature outside"),
        ("is_weekend", 1, "disagrees with the calendar"),   # 2024-01-01 is a Monday
    ],
)
def test_validate_rides_flags_each_problem(real_rides_path, column, bad_value, expected_message):
    df = clean_rides(load_rides(real_rides_path))
    assert validate_rides(df) == []
    df.loc[0, column] = bad_value
    assert any(expected_message in problem for problem in validate_rides(df))


def test_clean_rides_raises_on_invalid_data(real_rides_path):
    raw = load_rides(real_rides_path)
    raw.loc[0, "rain_mm"] = -5
    with pytest.raises(ValueError, match="validation failed"):
        clean_rides(raw)
