"""Command-line entry point:  python -m ridekit --input data/daily_rides.csv"""
import argparse
import sys

from ridekit.analysis import mean_rides_by, weekend_effect
from ridekit.clean import clean_rides
from ridekit.features import add_weekday
from ridekit.load import load_rides


def main(argv=None) -> int:
    """Run the analysis and print a short report. Returns 0 on success, 1 if the input file is missing."""
    parser = argparse.ArgumentParser(description="Summarise the daily rides data.")
    parser.add_argument("--input", required=True, help="path to daily_rides.csv")
    args = parser.parse_args(argv)

    try:
        df = load_rides(args.input)
    except FileNotFoundError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1

    df = add_weekday(clean_rides(df))
    by_weekday = mean_rides_by(df, "weekday")

    print(f"Rows: {len(df)}")
    print(f"Busiest weekday: {by_weekday.index[0]}")
    print(f"Weekend effect: {weekend_effect(df):.1f}%")
    return 0
