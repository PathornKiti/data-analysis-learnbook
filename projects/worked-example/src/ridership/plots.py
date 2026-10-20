"""Charts that make one point each. Every function returns the Axes; titles state the takeaway."""
import calendar
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BLUE, GREY, RED = "#0072B2", "#bbbbbb", "#D55E00"


def _clean_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return ax


def plot_monthly_rides(df: pd.DataFrame, ax=None):
    """Bar chart of average daily rides per month, highlighting the peak month."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 3.8))
    monthly = df.groupby("month")["rides"].mean()
    peak = int(monthly.idxmax())
    colors = [GREY] * 12
    colors[peak - 1] = BLUE
    ax.bar(calendar.month_abbr[1:], monthly.reindex(range(1, 13)).values, color=colors)
    ax.set_title(
        f"Ridership peaks in {calendar.month_name[peak]} at about {monthly.max():,.0f} rides a day, "
        f"{monthly.max() / monthly.min():.1f}x the winter low",
        loc="left", fontsize=11,
    )
    ax.set_ylabel("Average rides per day")
    return _clean_axes(ax)


def plot_weekend_vs_weekday(df: pd.DataFrame, ax=None):
    """Bar chart of mean daily rides on weekdays vs weekends, with the percent difference in the title."""
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 3.8))
    means = df.groupby("is_weekend")["rides"].mean()
    pct = (means[1] - means[0]) / means[0] * 100
    ax.bar(["Weekdays", "Weekends"], [means[0], means[1]], color=[GREY, BLUE])
    word = "fewer" if pct < 0 else "more"
    ax.set_title(f"Weekends see {abs(pct):.0f}% {word} rides than weekdays", loc="left", fontsize=11)
    ax.set_ylabel("Average rides per day")
    ax.set_ylim(0, None)
    return _clean_axes(ax)


def plot_temperature_vs_rides(df: pd.DataFrame, r: float, ax=None):
    """Scatter of rides against temperature with a least-squares trend line."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["temp_c"], df["rides"], c=np.where(df["is_weekend"] == 1, RED, BLUE), alpha=0.55, s=18)
    slope, intercept = np.polyfit(df["temp_c"], df["rides"], 1)
    xs = np.linspace(df["temp_c"].min(), df["temp_c"].max(), 100)
    ax.plot(xs, slope * xs + intercept, color="black", linewidth=1.5)
    ax.set_title(f"Warmer days, more rides: about {slope:.0f} extra rides per degree (r = {r:.2f})", loc="left", fontsize=11)
    ax.set_xlabel("Mean temperature (°C)")
    ax.set_ylabel("Rides per day")
    ax.text(0.02, 0.95, "blue = weekday, orange = weekend", transform=ax.transAxes, va="top", fontsize=8)
    return _clean_axes(ax)


def plot_rain_effect(df: pd.DataFrame, rain_coef: float, ax=None):
    """Rain vs the part of ridership NOT explained by temperature and weekend (a partial-regression view)."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    X = np.column_stack([np.ones(len(df)), df["temp_c"], df["is_weekend"]])
    resid_rides = df["rides"] - X @ np.linalg.lstsq(X, df["rides"], rcond=None)[0]
    resid_rain = df["rain_mm"] - X @ np.linalg.lstsq(X, df["rain_mm"], rcond=None)[0]
    ax.scatter(resid_rain, resid_rides, alpha=0.5, s=18, color=BLUE)
    xs = np.linspace(resid_rain.min(), resid_rain.max(), 50)
    ax.plot(xs, rain_coef * xs, color="black")
    ax.axhline(0, color=GREY, linewidth=0.8)
    ax.set_title(f"Once temperature is accounted for, each mm of rain costs about {abs(rain_coef):.0f} rides", loc="left", fontsize=11)
    ax.set_xlabel("Rainfall, adjusted for temperature and weekend (mm)")
    ax.set_ylabel("Rides, adjusted (rides per day)")
    return _clean_axes(ax)


def plot_test_predictions(test: pd.DataFrame, predictions: np.ndarray, rmse: float, ax=None):
    """Actual vs predicted rides over the held-out final days."""
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 3.8))
    ax.plot(test["date"], test["rides"], color=GREY, linewidth=2, label="actual")
    ax.plot(test["date"], predictions, color=BLUE, linewidth=1.5, label="linear model")
    ax.set_title(f"On the last {len(test)} days, the model is typically off by about {rmse:.0f} rides", loc="left", fontsize=11)
    ax.set_ylabel("Rides per day")
    ax.legend(frameon=False)
    return _clean_axes(ax)


def save_figure(ax, path) -> Path:
    """Save the figure containing ``ax`` to ``path`` (creating folders) and close it."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(ax.figure)
    return path
