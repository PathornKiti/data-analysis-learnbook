"""Reproduce the whole analysis with one command:  python run_analysis.py

Reads data/raw/daily_rides.csv and writes data/processed/, reports/results.md, reports/results.json and reports/figures/.
"""
import argparse
from pathlib import Path

from ridership.pipeline import run

ROOT = Path(__file__).resolve().parent


def main(input_path: Path) -> None:
    results = run(input_path, ROOT)
    print((ROOT / "reports" / "results.md").read_text())
    print("Figures written to reports/figures/")
    print(f"({results['n_missing_temp']} missing temperatures were filled with their month's median; see the sensitivity check in results.json)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "raw" / "daily_rides.csv")
    main(parser.parse_args().input)
