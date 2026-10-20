# Exercise: write tests that catch bugs

Tests are only valuable if they **fail when the code is wrong**. In this exercise the code in `src/reportkit/stats.py` is correct, and *you* write the tests.
A checker then injects 9 realistic bugs, one at a time, and tells you which ones your tests noticed.

## Setup
```bash
cd modules/11-communicating-results/exercise
pip install -e .
python checker/check_my_tests.py      # at first: 1 test passes, 7 of the 9 bugs "SURVIVED"
```

## Your task
Open `tests/test_student.py`. Follow the `TODO` comments and write tests until the checker prints 🎉.
Run `pytest` as you go to keep your tests green on the correct code.

## Tips
* **The docstring is the specification.** Test what it promises, including edge cases (zero, empty, boundaries).
* **Work out the expected answer by hand** *before* running the code: otherwise you'll just copy whatever the code says, bugs included.
* **One behaviour per test, with a name that says which.** A failing test named `test_percent_change_zero_old_raises` tells you what broke.
* A surviving bug means "no test would notice if the code were wrong in this way". Ask yourself: *what input would behave differently under that bug?*
* Prefer a few well-chosen inputs over many similar ones. Quality over quantity.

## Why this matters for your project
Your project's cleaning and analysis functions decide what your report says. A silent bug there (a wrong denominator, a boundary off by one, a share that's really a count) corrupts every
number downstream. Two or three sharp tests per function are cheap insurance. When you find a bug in your own code, first write the test that fails because of it, then fix the bug.

Peek at `../../../solutions/11-communicating-results/exercise/tests/test_student.py` only after a real attempt.
