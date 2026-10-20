import pandas as pd

from ridekit.clean import clean_rides, fill_missing_temp, flag_missing_temp
from ridekit.load import load_rides


def small_frame():
    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2024-01-01", "2024-01-02", "2024-01-03", "2024-02-01", "2024-02-02", "2024-03-01"]
            ),
            "temp_c": [0.0, None, 10.0, 20.0, None, None],
        }
    )


def test_flag_missing_temp():
    out = flag_missing_temp(small_frame())
    assert out["temp_was_missing"].tolist() == [False, True, False, False, True, True]


def test_fill_uses_same_month_median_then_overall_median():
    out = fill_missing_temp(small_frame())
    # Jan median of [0, 10] = 5; Feb median of [20] = 20; March has no data -> overall median of [0, 10, 20] = 10
    assert out["temp_c"].tolist() == [0.0, 5.0, 10.0, 20.0, 20.0, 10.0]


def test_functions_do_not_modify_their_input():
    df = small_frame()
    before = df.copy()
    flag_missing_temp(df)
    fill_missing_temp(df)
    clean_rides(df)
    pd.testing.assert_frame_equal(df, before)


def test_clean_rides_on_real_data(rides_csv):
    raw = load_rides(rides_csv)
    out = clean_rides(raw)
    assert len(out) == len(raw)
    assert out["temp_c"].notna().all()
    assert out["temp_was_missing"].sum() == 6, "the flag must be computed BEFORE filling"
