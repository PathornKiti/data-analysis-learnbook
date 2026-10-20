# Module 8: Statistical inference

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 4 and 7

## Learning goals
* Distinguish population from sample and parameter from statistic
* Compute and interpret the **standard error** and **confidence intervals** (t-formula and bootstrap)
* Explain the logic of a hypothesis test; run **permutation, Welch t, correlation and chi-square** tests
* Interpret a p-value correctly (and list what it is *not*)
* Report **effect sizes**, understand **Type I/II errors and power**, and avoid **p-hacking**
* Write results that include estimate, interval, p-value, effect size, sample size and caveats

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | simulation-driven tour using the `students` data |
| `exercises.ipynb` | 8 exercises (bootstrap, permutation test, t-test, effect size, multiple testing, power, interpretation) |
| `math-notes.md` | SE, CI formulas, p-values, error types, power, effect sizes, χ² |
| [`../../solutions/08-statistical-inference/`](../../solutions/08-statistical-inference/) | solutions |

## Common pitfalls
* "p > 0.05 means no effect" (it means **inconclusive** unless the interval is narrow around 0)
* Reading a 95% CI as "95% probability the true value is inside *this* interval"
* Testing many hypotheses and reporting only the winners (p-hacking)
* Confusing statistical and practical significance; always show the effect size
* Running a test on data that are not independent (repeated measures, time series)
* Causal language from observational data

## 🎯 Project checkpoint: **`analysis.py`**
1. In `src/<your_package>/analysis.py` write functions that compute **the numbers your question needs** (group means, correlations, a model-free comparison…).
   The template already includes `mean_ci`, `bootstrap_ci`, `permutation_test` and `cohens_d`. Reuse and adapt them.
2. For each main finding report: **estimate + 95% interval + (where relevant) p-value + effect size + n**.
3. Write down, *before* testing, which comparisons answer your question. Count how many you actually run.
4. Add tests for the new functions (see `projects/template/tests/test_analysis.py`).
5. Extend `run_analysis.py` so it prints these results.

## Further reading
* *Statistics Done Wrong* (Alex Reinhart), a short, readable tour of common mistakes
* Downey, *There Is Only One Test*, on the permutation/simulation view of testing
