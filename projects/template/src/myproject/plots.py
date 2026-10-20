"""Reusable plotting functions. They return the Axes so callers can tweak them."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def scatter_with_trend(df: pd.DataFrame, x: str, y: str, ax=None):
    """Scatter plot of y against x with a least-squares trend line."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df[x], df[y], alpha=0.6)
    slope, intercept = np.polyfit(df[x], df[y], deg=1)
    xs = np.linspace(df[x].min(), df[x].max(), 100)
    ax.plot(xs, slope * xs + intercept, color="tab:red", label=f"trend: slope {slope:.2f}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{y} vs {x}")
    ax.legend()
    return ax


def save_figure(ax, path: str | Path) -> Path:
    """Save the figure that contains `ax` to `path`, creating folders as needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(path, dpi=150, bbox_inches="tight")
    return path
