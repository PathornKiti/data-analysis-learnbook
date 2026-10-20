"""Reproduce the whole analysis with one command:  python run_analysis.py

Steps: load raw data -> clean -> add features -> analyse -> save outputs.
"""
import argparse
from pathlib import Path

from myproject.analysis import correlation, group_summary
from myproject.clean import clean
from myproject.features import add_score_band
from myproject.load import load_raw
from myproject.plots import save_figure, scatter_with_trend

ROOT = Path(__file__).resolve().parent


def main(input_path: Path) -> None:
    raw = load_raw(input_path)
    df = add_score_band(clean(raw))

    processed = ROOT / "data" / "processed" / "clean.csv"
    processed.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed, index=False)

    print(f"Rows: {len(raw)} raw -> {len(df)} clean")
    print("\nExam score by part-time job:")
    print(group_summary(df, by="part_time_job", value="exam_score"))
    r = correlation(df, "study_hours_week", "exam_score")
    print(f"\nCorrelation between study hours and exam score: {r:.2f}")

    ax = scatter_with_trend(df, "study_hours_week", "exam_score")
    fig_path = save_figure(ax, ROOT / "reports" / "figures" / "study_vs_score.png")
    print(f"Saved figure to {fig_path.relative_to(ROOT)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "raw" / "sample_students.csv")
    main(parser.parse_args().input)
