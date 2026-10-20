"""Generate the small *synthetic* datasets used in the course.

Run from anywhere:  python data/generate_datasets.py

Everything is seeded, so the output is repeatable (exact values can differ slightly
across NumPy versions, so the committed CSVs are what the course uses). The data is
invented for teaching: it is NOT real student or ride-sharing data.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(42)


def make_students(n: int = 200) -> pd.DataFrame:
    """Study habits vs exam score."""
    study = rng.gamma(shape=4.0, scale=2.5, size=n).clip(0, 40)
    sleep = rng.normal(7.0, 1.0, size=n).clip(4, 10)
    attendance = rng.beta(8, 2, size=n) * 100
    job = rng.choice(["yes", "no"], size=n, p=[0.35, 0.65])
    major = rng.choice(["Science", "Arts", "Business", "Engineering"], size=n)
    noise = rng.normal(0, 6, size=n)
    score = (
        25
        + 1.6 * study
        + 2.0 * sleep
        + 0.18 * attendance
        - 2.5 * (job == "yes")
        + noise
    ).clip(0, 100)
    return pd.DataFrame(
        {
            "student_id": np.arange(1, n + 1),
            "major": major,
            "study_hours_week": study.round(1),
            "sleep_hours": sleep.round(1),
            "attendance_pct": attendance.round(1),
            "part_time_job": job,
            "exam_score": score.round(1),
        }
    )


def make_daily_rides() -> pd.DataFrame:
    """One year of daily bike-share rides with weather (2024, a leap year)."""
    dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")
    day = np.arange(len(dates))
    temp = 14 + 12 * np.sin(2 * np.pi * (day - 100) / 366) + rng.normal(0, 2.5, len(dates))
    rain = rng.exponential(2.0, len(dates)) * (rng.random(len(dates)) < 0.3)
    weekend = (dates.dayofweek >= 5).astype(int)
    rides = (
        800
        + 55 * temp
        - 25 * rain
        - 150 * weekend
        + rng.normal(0, 120, len(dates))
    ).clip(50)
    df = pd.DataFrame(
        {
            "date": dates.strftime("%Y-%m-%d"),
            "temp_c": temp.round(1),
            "rain_mm": rain.round(1),
            "is_weekend": weekend,
            "rides": rides.round().astype(int),
        }
    )
    # A few missing temperature readings (a broken sensor) so students meet NaN.
    df.loc[rng.choice(len(df), size=6, replace=False), "temp_c"] = np.nan
    return df


if __name__ == "__main__":
    make_students().to_csv(OUT / "students.csv", index=False)
    make_daily_rides().to_csv(OUT / "daily_rides.csv", index=False)
    print("Wrote students.csv and daily_rides.csv to", OUT)
