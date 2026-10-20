import pandas as pd

from myproject.clean import drop_duplicate_rows, remove_out_of_range, standardize_column_names


def test_standardize_column_names():
    df = pd.DataFrame({" Exam Score ": [1], "Major": ["A"]})
    assert list(standardize_column_names(df).columns) == ["exam_score", "major"]


def test_drop_duplicate_rows():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    assert len(drop_duplicate_rows(df)) == 2


def test_remove_out_of_range_keeps_missing():
    df = pd.DataFrame({"score": [50, 120, -5, None]})
    out = remove_out_of_range(df, "score", 0, 100)
    assert out["score"].fillna(-1).tolist() == [50, -1]
