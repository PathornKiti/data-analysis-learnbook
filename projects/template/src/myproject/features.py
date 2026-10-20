"""Creating new columns from existing ones."""
import pandas as pd


def add_score_band(df: pd.DataFrame, column: str = "exam_score") -> pd.DataFrame:
    """Add a `score_band` column: fail / ok / good / great."""
    out = df.copy()
    out["score_band"] = pd.cut(
        out[column],
        bins=[0, 50, 65, 80, 100],
        labels=["fail", "ok", "good", "great"],
        include_lowest=True,
    )
    return out
