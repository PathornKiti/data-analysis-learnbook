# Module 8b: The hypothesis-testing toolkit

**Time:** ~2.5 weeks (10–14 h) · **Prerequisites:** Modules 7, 7b and 8 · **Needed for:** the methods and results chapters of a thesis

## Learning goals
* Run the full testing workflow: question → design → estimand → assumptions (with plots) → test + interval + effect size → plain-language report
* Compute **one-sample, two-sample (Welch), paired $t$-tests**, the **Mann–Whitney** and **Wilcoxon** rank tests, **one-way ANOVA**, **Kruskal–Wallis**, tests for **proportions** and **tables** (χ², Fisher), and **correlation** tests, each *by hand* and with a library
* Report the right **effect size** with an interval for each design (Cohen's $d$/Hedges' $g$, $d_z$, probability of superiority, $\eta^2$, risk/odds ratios, Cramér's $V$, $r$)
* Handle **multiple comparisons** (Tukey, Bonferroni, Holm, Benjamini–Hochberg) and know when you must correct and when you pre-specified a primary hypothesis
* Use a **baseline** properly (gain scores, **ANCOVA**) and understand why it changes power
* Use **equivalence testing (TOST)** when the claim is "no meaningful difference"
* Plan **power and sample size**, and read/draw **inference charts** (error bars, forest plots, p-value histograms)

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | 13 sections on a randomised app experiment: every common test, by hand and with SciPy/statsmodels, with charts |
| `exercises.ipynb` | 10 exercises implementing the tests from their formulas (checks compare with the libraries) + a choose-the-test quiz |
| `math-notes.md` | formulas, degrees of freedom, effect-size definitions, corrections, power approximations |
| [`../../solutions/08b-hypothesis-testing-toolkit/`](../../solutions/08b-hypothesis-testing-toolkit/) | solutions |
| [`../../reference/choosing-a-test.md`](../../reference/choosing-a-test.md) | decision table: design → test → assumptions → effect size → code |
| [`../../reference/reporting-results.md`](../../reference/reporting-results.md) | sentence templates for reporting each test |
| [`../../data/app_trial.csv`](../../data/app_trial.csv) | practice data: 3 randomised groups, paired scores, skewed, binary, ordinal and categorical outcomes |

## Common pitfalls
* **Wrong test for the design**: treating paired data as two independent groups (or the reverse)
* Reading "not significant" as "no effect"; for that claim, use an **equivalence test** or discuss the interval
* Running many tests and reporting the smallest p without correction; **pre-specify** your primary hypotheses
* "Test the assumptions, then choose the test": a fragile two-stage rule. Prefer robust methods (Welch, rank tests, permutation/bootstrap) plus a **sensitivity analysis**
* Ignoring a baseline measurement in a before/after design (throwing away power)
* One-sided tests chosen after seeing the data
* Reporting only p-values; always add the **estimate, its interval and an effect size**
* Interpreting Mann–Whitney as a test of medians when the distribution shapes differ
* Chi-square with small expected counts (use Fisher's exact test or merge categories)
* "Observed power" calculated after the fact (it's a function of the p-value; do power analysis *before* collecting data)

## 🎯 Project checkpoint: **a hypothesis table**
Add `docs/hypotheses.md` (or a section in your proposal) **before** you run your main analyses, and implement the tests in `src/<package>/hypothesis.py` (the template has `two_group_report` as a starting point).

| # | Question | Variables & design (independent / paired?) | H₀ and H₁ | Test | Assumptions & how I'll check them | Effect size + interval | α, correction, planned n / power | Primary or exploratory? |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

1. Fill one row per hypothesis; mark **one or two as primary** (these keep the unadjusted α).
2. Do a **power / minimum-detectable-effect** calculation for each primary hypothesis given the data you actually have.
3. Run each test **and** a sensitivity analysis (a second reasonable method); report whether they agree.
4. In `run_analysis.py`, print each result in the reporting-template wording (estimate, interval, p-value, effect size, n).
5. Plot **intervals** (error bars or a forest plot), not bare bars.
6. Add tests for your test functions (e.g. a hand-computed small example).

## Further reading
* *Statistics Done Wrong* (Reinhart) and *Intuitive Biostatistics* (Motulsky): readable guides to choosing and interpreting tests
* Lakens, *Improving Your Statistical Inferences* (free online): effect sizes, equivalence tests, power, and pre-registration
* `statsmodels` documentation: [stats module](https://www.statsmodels.org/stable/stats.html) and `scipy.stats` [hypothesis tests](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests)
