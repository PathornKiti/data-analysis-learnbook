"""Write your tests here. Run the checker to see whether they are any good:

    python checker/check_my_tests.py

The functions live in src/reportkit/stats.py: read their docstrings; the docstring is the specification.
Each test should be small, have a clear name, and check ONE behaviour.
"""
import numpy as np
import pandas as pd
import pytest

from reportkit.stats import iqr_outliers, percent_change, share_missing


# ---- percent_change -----------------------------------------------------------------------
def test_percent_change_increase():
    assert percent_change(100, 150) == pytest.approx(50.0)     # an example to get you started


# TODO: a decrease. Choose numbers where dividing by the wrong value would give a different answer.

# TODO: no change at all.

# TODO: old == 0 must raise ValueError (hint: `with pytest.raises(ValueError):`).


# ---- iqr_outliers -------------------------------------------------------------------------
# TODO: a list with an unusually HIGH value. Work out the quartiles and fences by hand first!
#       (Make sure it would also be caught if someone used 3 * IQR instead of 1.5 * IQR.)

# TODO: a list with an unusually LOW value.

# TODO: a value that lies EXACTLY on a fence is not an outlier. Design data where Q1, Q3 and the fence are round numbers.

# TODO: data with no outliers returns an empty list.


# ---- share_missing ------------------------------------------------------------------------
# TODO: a column with some missing values: the result is a FRACTION between 0 and 1.

# TODO: nothing missing, and everything missing.

# TODO: an empty DataFrame returns 0.0 (not NaN).
