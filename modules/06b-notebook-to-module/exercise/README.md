# Exercise: build `ridekit`

A small analysis **package** for `data/daily_rides.csv`, with a test suite already written. Your job is to make the tests pass.
This is the notebook→module workflow in miniature.

## Setup
```bash
cd modules/06b-notebook-to-module/exercise
pip install -e .        # installs the package in "editable" mode: code changes take effect immediately
pytest                  # everything fails at first. That's the point!
```
(Without installing, `pytest` still works because `pyproject.toml` adds `src/` to the import path.)

## Do the work in this order
| step | file | tests |
|---|---|---|
| 1 | `src/ridekit/load.py` | `pytest tests/test_load.py` |
| 2 | `src/ridekit/clean.py` | `pytest tests/test_clean.py` |
| 3 | `src/ridekit/features.py` | `pytest tests/test_features.py` |
| 4 | `src/ridekit/analysis.py` | `pytest tests/test_analysis.py` |
| 5 | `src/ridekit/cli.py` | `pytest tests/test_cli.py` |

When all pass, run your package like a real tool:
```bash
python -m ridekit --input ../../../data/daily_rides.csv
```

## Rules
* Functions **return new DataFrames** and never modify their input (tests check this).
* Read each test before writing the code; the tests are the specification.
* Stuck? Use `pytest -x -q` (stop at first failure) and read the assertion message. Peek at
  `../../../solutions/06b-notebook-to-module/exercise/` only after a real attempt.

## Then, go further (optional)
* Add a function `rain_effect(df)` and write the test for it *first*.
* Add a `--plot` flag to the CLI that saves a chart.
