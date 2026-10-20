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


PRICES = {"Latte": 4.5, "Espresso": 3.0, "Mocha": 5.0, "Tea": 2.5, "Cake": 4.0}


def make_messy_orders(n: int = 300) -> pd.DataFrame:
    """Coffee-shop orders, deliberately messy for the cleaning module.

    Problems planted on purpose: duplicate rows, inconsistent text (case, spaces,
    spelling variants), dates in several formats, prices stored as text with '$'
    or 'N/A', missing quantities, and a few impossible quantities (typos).
    """
    items = rng.choice(list(PRICES), size=n)
    cities = rng.choice(["Bangkok", "Chiang Mai", "Phuket"], size=n, p=[0.5, 0.3, 0.2])
    customers = rng.choice(["Ada", "Ben", "Chai", "Dara", "Eve", "Fah", "Gus"], size=n)
    dates = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 182, size=n), unit="D")
    qty = rng.integers(1, 6, size=n).astype(float)

    def messy_text(value: str) -> str:
        style = rng.integers(0, 4)
        return [value, value.lower(), value.upper(), f"  {value} "][style]

    def messy_date(d: pd.Timestamp) -> str:
        style = rng.integers(0, 3)
        return [d.strftime("%Y-%m-%d"), d.strftime("%B %d, %Y"), d.strftime("%d %b %Y")][style]

    def messy_price(p: float) -> str:
        r = rng.random()
        if r < 0.04:
            return "N/A"
        return [f"${p:.2f}", f"{p:.2f}", f"{p:g}"][rng.integers(0, 3)]

    df = pd.DataFrame(
        {
            "order_id": np.arange(1001, 1001 + n),
            "order_date": [messy_date(d) for d in dates],
            "customer": [messy_text(c) for c in customers],
            "city": [messy_text(c) if c != "Chiang Mai" or rng.random() > 0.2 else "Chiangmai"
                     for c in cities],
            "item": [messy_text(i) for i in items],
            "quantity": qty,
            "unit_price": [messy_price(PRICES[i]) for i in items],
        }
    )
    df.loc[rng.choice(n, size=15, replace=False), "quantity"] = np.nan   # missing
    df.loc[rng.choice(n, size=4, replace=False), "quantity"] = 99        # typo: 99 not 9
    duplicates = df.sample(12, random_state=3)
    return pd.concat([df, duplicates], ignore_index=True).sample(frac=1, random_state=5).reset_index(drop=True)


def make_app_trial(n_per_group: int = 100) -> pd.DataFrame:
    """A randomised app experiment: 3 conditions, a paired before/after score, a skewed usage measure,
    a yes/no conversion, an ordinal rating and a categorical device. Own seed, so adding it never changes other files."""
    r = np.random.default_rng(101)
    groups = np.repeat(["control", "tutorial", "gamified"], n_per_group)
    n = len(groups)
    lift = pd.Series(groups).map({"control": 2.0, "tutorial": 5.0, "gamified": 7.0}).to_numpy()
    pre = r.normal(50, 10, n)
    post = pre + lift + r.normal(0, 6, n)
    median_minutes = pd.Series(groups).map({"control": 20.0, "tutorial": 24.0, "gamified": 30.0}).to_numpy()
    minutes = median_minutes * np.exp(r.normal(0, 0.7, n))                    # lognormal: right-skewed
    p_convert = pd.Series(groups).map({"control": 0.20, "tutorial": 0.26, "gamified": 0.32}).to_numpy()
    converted = (r.random(n) < p_convert).astype(int)
    rating_mean = pd.Series(groups).map({"control": 3.2, "tutorial": 3.5, "gamified": 3.8}).to_numpy()
    rating = np.clip(np.rint(rating_mean + r.normal(0, 1.0, n)), 1, 5).astype(int)
    device = r.choice(["ios", "android", "web"], size=n, p=[0.4, 0.45, 0.15])
    df = pd.DataFrame(
        {
            "user_id": np.arange(1, n + 1),
            "group": groups,
            "device": device,
            "pre_score": pre.round(1),
            "post_score": post.round(1),
            "minutes_active": minutes.round(1),
            "converted": converted,
            "rating": rating,
        }
    )
    return df.sample(frac=1, random_state=7).reset_index(drop=True)


def make_service_desk(n: int = 480) -> pd.DataFrame:
    """Hourly help-desk records with distinctly different shapes: counts (Poisson), a right-skewed time (lognormal),
    a bounded left-skewed score (beta) and a bimodal call length (mixture of two normals)."""
    r = np.random.default_rng(202)
    quick = r.random(n) < 0.6
    call = np.where(quick, r.normal(3.0, 0.8, n), r.normal(12.0, 2.0, n)).clip(0.5)
    return pd.DataFrame(
        {
            "hour_id": np.arange(1, n + 1),
            "tickets": r.poisson(4.2, n),
            "response_minutes": np.exp(r.normal(2.0, 0.6, n)).round(2),
            "satisfaction_pct": (r.beta(8, 2, n) * 100).round(1),
            "call_minutes": call.round(2),
        }
    )


if __name__ == "__main__":
    make_students().to_csv(OUT / "students.csv", index=False)
    make_daily_rides().to_csv(OUT / "daily_rides.csv", index=False)
    make_messy_orders().to_csv(OUT / "messy_orders.csv", index=False)
    make_app_trial().to_csv(OUT / "app_trial.csv", index=False)
    make_service_desk().to_csv(OUT / "service_desk.csv", index=False)
    print("Wrote students.csv, daily_rides.csv, messy_orders.csv, app_trial.csv and service_desk.csv to", OUT)
