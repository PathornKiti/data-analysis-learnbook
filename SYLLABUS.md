# Syllabus

**Format:** ~18 weeks at 4–8 hours per week (14 with the compressed plan below) (self-paced; modules can be stretched, merged or run as an intensive: see the [instructor guide](INSTRUCTOR_GUIDE.md)).
**Prerequisites:** none beyond high-school arithmetic and the ability to install software.
**Outcome:** a reproducible data-analysis package, built with Python on a topic of the student's choice, with tests, honest uncertainty and a clear report.

## Learning outcomes

By the end, a student can:

1. Write and read Python functions, loops and data structures.
2. Load, clean, reshape and summarise tabular data with NumPy and pandas, documenting each decision.
3. Explore a dataset visually and numerically, and describe what they see honestly.
4. Describe, fit and check the **distribution** of a variable, and use probability and inference (intervals, bootstrap, the right hypothesis test for the design, effect sizes, power) to say how much a result can be trusted.
5. Build **charts whose calculations they understand** (bins, ECDF, KDE, box plots, error bars, confidence and prediction bands) and caption them properly.
6. Fit, interpret and evaluate linear and logistic models; recognise overfitting, leakage and the limits of causal claims.
7. Organise analysis code into importable `.py` modules with docstrings, tests and a single entry point.
8. Communicate findings in a clear report, README and short talk; handle data ethically and reproducibly.

## Module overview

| # | Module | Python | Essential maths | Project checkpoint |
|---|---|---|---|---|
| 0 | [Setup](modules/00-setup/) | venv, pip, Jupyter, Git basics | – | working environment |
| 1 | [Python foundations](modules/01-python-foundations/) | types, control flow, functions, lists/dicts | arithmetic, functions *f(x)*, Σ notation, mean | list your interests |
| 2 | [Project kickoff](modules/02-project-kickoff/) | feasibility check with pandas | what makes a question answerable | **proposal + data card** |
| 3 | [NumPy](modules/03-numpy/) | arrays, masks, vectorisation, RNG | vectors, dot product, norm, z-scores | data in `data/raw/` |
| 4 | [pandas I](modules/04-pandas-1/) | read_csv, select, filter, groupby | mean/median/variance/quantiles | first look at your data |
| 5 | [pandas II: cleaning](modules/05-pandas-2-cleaning/) | missing data, dtypes, merges, dates | percentages, ratios, logs, IQR | **`clean.py`** |
| 6 | [Visualization & EDA](modules/06-visualization-eda/) | matplotlib, seaborn | distributions, correlation, Simpson's paradox | **`plots.py`** + EDA notebook |
| 6.5 | [From notebook to module](modules/06b-notebook-to-module/) (`06b-…`) | scripts, imports, packages, argparse, pytest | – | project restructured as a package |
| 7 | [Probability](modules/07-probability/) | simulation, `scipy.stats` | probability rules, Bayes, E[X], binomial, normal, LLN & CLT | where does chance enter your data? |
| 7b | [Distributions of data](modules/07b-distributions-of-data/) | `scipy.stats` fits, Q-Q plots, Box–Cox, Gaussian mixtures | moments (skewness, kurtosis), catalogue of distributions, maximum likelihood, AIC, KS / Shapiro / χ² goodness-of-fit, lognormal & Poisson–exponential | **`distributions.py`** + distribution profile |
| 8 | [Statistical inference](modules/08-statistical-inference/) | scipy, bootstrap, permutation tests | standard error, CIs, p-values, power, effect size | **`analysis.py`** |
| 8b | [Hypothesis-testing toolkit](modules/08b-hypothesis-testing-toolkit/) | `scipy.stats`, `statsmodels` tests, power, TOST | t / Welch / paired t, ranks (U, Wilcoxon, Kruskal), ANOVA & ANCOVA, proportions, χ² & Fisher, Fisher-z, multiplicity, power | **`hypothesis.py`** + hypothesis table |
| 9 | [Linear regression](modules/09-linear-regression/) | statsmodels, scikit-learn, NumPy | least squares, derivatives & gradient descent, matrix form, R² | first model |
| 9b | [Charts & their calculations](modules/09b-charts-and-calculations/) | matplotlib/seaborn with the maths done by hand | bin rules, ECDF, KDE, quartiles & fences, SE/CI error bars, Wilson, EWMA, confidence vs prediction bands, correlation matrices | **chart audit** |
| 10 | [Prediction & evaluation](modules/10-prediction-evaluation/) | train/test, CV, pipelines, logistic regression | bias–variance, odds & sigmoid, precision/recall, ROC | **`model.py`** + model comparison |
| 11 | [Communicating results](modules/11-communicating-results/) | docstrings, doctest, pytest, validation | reporting uncertainty in words | tests + README + report |
| 12 | [Capstone](modules/12-capstone/) | everything | whatever the question needs | **final package + report + talk** |

### Extension modules (optional)

Each takes about two weeks (8–10 h). Assign the ones that match students' data; they build on Modules 8b and 9 and use the same notebook, exercise and checkpoint format.

| # | Module | Tools | Maths | Project checkpoint |
|---|---|---|---|---|
| X1 | [Repeated measures & mixed models](modules/X1-repeated-measures-mixed-models/) | `statsmodels` `mixedlm`, cluster-robust SEs | variance components, ICC, design effect, REML vs ML, BLUPs and shrinkage | clustering check and a mixed-model re-analysis |
| X2 | [Survival analysis](modules/X2-survival-analysis/) | `statsmodels` `SurvfuncRight`, `survdiff`, `PHReg` | survival and hazard functions, Kaplan–Meier and Greenwood, log-rank, Cox partial likelihood, RMST | time-to-event analysis with censoring |
| X3 | [Bayesian inference](modules/X3-bayesian-inference/) | NumPy / SciPy (own grid and Metropolis code) | Bayes for parameters, conjugacy, credible intervals, Metropolis, R-hat and ESS, posterior predictive checks | Bayesian re-analysis of the main result with a prior sensitivity table |
| X4 | [Time-series analysis & inference](modules/X4-time-series/) | `statsmodels` (`seasonal_decompose`, `acf`, `adfuller`, HAC, GLSAR) | moving averages, ACF, AR(1), effective sample size, Durbin–Watson, HAC, forecast variance, MASE | time-series check of the project's data |

Datasets for the extensions: `longitudinal_scores.csv` (X1), `customer_churn.csv` (X2), `monthly_demand.csv` (X4); X3 reuses `app_trial.csv`, `students.csv` and `service_desk.csv`.

Other optional capstone stretch options: text analysis · web APIs & scraping · Streamlit dashboards.

## Suggested pacing

**Standard (18 weeks).**

| week | module(s) | project milestone |
|---|---|---|
| 1 | 0, 1 | environment working; interests listed |
| 2 | 1 (finish), 2 | proposal + data card |
| 3 | 3 | data downloaded; licence noted |
| 4 | 4 | first look at your data |
| 5 | 5 | `clean.py` |
| 6 | 6 | EDA charts + `plots.py` |
| 7 | 6.5 | project becomes a package |
| 8 | 7 | chance & sampling notes |
| 9 | 7b | distribution profile of your key variables |
| 10 | 8 | intervals and a first test |
| 11–12 | 8b | **hypothesis table** (pre-specified tests, power) + `hypothesis.py` |
| 13 | 9 | first model |
| 14 | 9b | **chart audit**; every figure justified and captioned |
| 15 | 10 | model comparison |
| 16 | 11 | tests, docs, README |
| 17–18 | 12 | capstone: polish, peer review, present |

**Compressed (14 weeks).** Give 7b, 8b and 9b one week each by assigning only the exercises that match your students' projects (the lessons and reference sheets stay available), and merge Module 11 into the first capstone week.
**Extensions.** After week 15 (or in place of the Module 10 week if the project is purely inferential), give each extension module one or two weeks, chosen by the project's data: clustered or repeated measurements → X1; time to an event → X2; small samples or prior information → X3; time-ordered data → X4.
**Thesis track.** Keep the standard plan and add the written deliverables: a methods section built from the reference sheets, a pre-specified hypothesis table, and a figure list with captions.

## Assessment

* **Module self-checks:** auto-checked exercises (formative); in Modules 7b, 8b, 9b and X1–X4 students implement each calculation by hand and the checks compare with SciPy/statsmodels; Modules 6.5 and 11 add test-driven package exercises.
* **Project milestones:** proposal → data card → cleaned data → EDA → analysis/model → tests & docs → final write-up.
* **Final project:** graded with [`projects/rubric.md`](projects/rubric.md) and the **project doctor** (`python projects/check_project.py <project>`).

## Teaching suggestions

* Spend the first 10 minutes of each session on the previous project checkpoint (show-and-tell).
* Pair students with different interests so they explain their data to each other.
* Encourage students to break code on purpose; reading error messages is a core skill.
* Run the capstone peer review as a fresh-clone exercise; it exposes missing instructions better than any rubric.
