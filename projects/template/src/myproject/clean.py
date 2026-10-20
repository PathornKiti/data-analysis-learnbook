"""Cleaning steps. Each function takes a DataFrame and returns a new one."""
import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Lower-case column names, strip spaces and replace inner spaces with underscores."""
    out = df.copy()
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]
    return out


def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate rows."""
    return df.drop_duplicates().reset_index(drop=True)


def remove_out_of_range(df: pd.DataFrame, column: str, low: float, high: float) -> pd.DataFrame:
    """Keep rows whose `column` lies in [low, high]; rows with a missing value are kept."""
    keep = df[column].between(low, high) | df[column].isna()
    return df[keep].reset_index(drop=True)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Run the whole cleaning pipeline. Extend this as you discover problems in your data."""
    df = standardize_column_names(df)
    df = drop_duplicate_rows(df)
    # TODO (Module 5): add steps for your own data, e.g. fixing types, handling missing values.
    df = remove_out_of_range(df, "exam_score", 0, 100)
    return df
