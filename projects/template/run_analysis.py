"""Reproduce the whole analysis with one command:  python run_analysis.py

Steps: load raw data -> clean -> add features -> analyse -> save outputs.
"""
import argparse
from pathlib import Path

from myproject.analysis import cohens_d, correlation, group_summary, mean_ci, permutation_test
from myproject.clean import clean
from myproject.features import add_score_band
from myproject.load import load_raw
from myproject.model import coefficient_table, cross_val_r2, evaluate_regression, fit_ols
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

    low, high = mean_ci(df["exam_score"])
    print(f"Mean exam score: {df['exam_score'].mean():.1f} (95% CI {low:.1f} to {high:.1f})")

    job = df.loc[df["part_time_job"] == "yes", "exam_score"]
    no_job = df.loc[df["part_time_job"] == "no", "exam_score"]
    print(
        f"No job minus job: {no_job.mean() - job.mean():.1f} points, "
        f"permutation p = {permutation_test(no_job, job):.3f}, Cohen's d = {cohens_d(no_job, job):.2f}"
    )

    features = ["study_hours_week", "sleep_hours", "attendance_pct"]
    print("\nRegression of exam_score on study, sleep, attendance and job (coefficients with 95% CIs):")
    print(coefficient_table(fit_ols(df, "exam_score ~ study_hours_week + sleep_hours + attendance_pct + part_time_job")))
    held_out = evaluate_regression(df, features, "exam_score")
    cv_mean, cv_std = cross_val_r2(df, features, "exam_score")
    print(
        f"Held-out RMSE: model {held_out['model_rmse']:.1f} vs baseline {held_out['baseline_rmse']:.1f}; "
        f"cross-validated R² = {cv_mean:.2f} ± {cv_std:.2f}"
    )

    ax = scatter_with_trend(df, "study_hours_week", "exam_score")
    fig_path = save_figure(ax, ROOT / "reports" / "figures" / "study_vs_score.png")
    print(f"Saved figure to {fig_path.relative_to(ROOT)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "raw" / "sample_students.csv")
    main(parser.parse_args().input)
