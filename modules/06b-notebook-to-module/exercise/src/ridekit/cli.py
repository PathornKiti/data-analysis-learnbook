"""Command-line entry point:  python -m ridekit --input data/daily_rides.csv"""
import argparse
import sys

from ridekit.analysis import mean_rides_by, weekend_effect
from ridekit.clean import clean_rides
from ridekit.features import add_weekday
from ridekit.load import load_rides


def main(argv=None) -> int:
    """Run the analysis and print a short report. Returns 0 on success, 1 if the input file is missing.

    Expected output (three lines, on stdout):
        Rows: 366
        Busiest weekday: <day name>
        Weekend effect: <percent with 1 decimal>%
    If the file is missing, print "error: <message>" to **stderr** and return 1.
    """
    # TODO:
    #   1. build an argparse.ArgumentParser with a required --input option and parse `argv`
    #   2. load -> clean_rides -> add_weekday
    #   3. print the three lines above (use mean_rides_by(df, "weekday") for the busiest weekday)
    raise NotImplementedError("main")
