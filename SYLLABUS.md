# Syllabus

**Format:** ~14 weeks at 4–8 hours per week (self-paced; modules can be stretched, merged or run as an intensive: see the [instructor guide](INSTRUCTOR_GUIDE.md)).
**Prerequisites:** none beyond high-school arithmetic and the ability to install software.
**Outcome:** a reproducible data-analysis package, built with Python on a topic of the student's choice, with tests, honest uncertainty and a clear report.

## Learning outcomes

By the end, a student can:

1. Write and read Python functions, loops and data structures.
2. Load, clean, reshape and summarise tabular data with NumPy and pandas, documenting each decision.
3. Explore a dataset visually and numerically, and describe what they see honestly.
4. Use probability and inference (intervals, bootstrap, tests, power) to say how much a result can be trusted.
5. Fit, interpret and evaluate linear and logistic models; recognise overfitting, leakage and the limits of causal claims.
6. Organise analysis code into importable `.py` modules with docstrings, tests and a single entry point.
7. Communicate findings in a clear report, README and short talk; handle data ethically and reproducibly.

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
| 8 | [Statistical inference](modules/08-statistical-inference/) | scipy, bootstrap, permutation tests | standard error, CIs, p-values, power, effect size | **`analysis.py`** |
| 9 | [Linear regression](modules/09-linear-regression/) | statsmodels, scikit-learn, NumPy | least squares, derivatives & gradient descent, matrix form, R² | first model |
| 10 | [Prediction & evaluation](modules/10-prediction-evaluation/) | train/test, CV, pipelines, logistic regression | bias–variance, odds & sigmoid, precision/recall, ROC | **`model.py`** + model comparison |
| 11 | [Communicating results](modules/11-communicating-results/) | docstrings, doctest, pytest, validation | reporting uncertainty in words | tests + README + report |
| 12 | [Capstone](modules/12-capstone/) | everything | whatever the question needs | **final package + report + talk** |

Optional extensions (see the capstone): time series · text analysis · web APIs & scraping · Streamlit dashboards.

## Suggested pacing (14 weeks)

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
| 9 | 8 | `analysis.py` with intervals |
| 10 | 9 | first model |
| 11 | 10 | model comparison |
| 12 | 11 | tests, docs, README |
| 13–14 | 12 | capstone: polish, peer review, present |

## Assessment

* **Module self-checks:** auto-checked exercises (formative); Modules 6.5 and 11 add test-driven package exercises.
* **Project milestones:** proposal → data card → cleaned data → EDA → analysis/model → tests & docs → final write-up.
* **Final project:** graded with [`projects/rubric.md`](projects/rubric.md) and the **project doctor** (`python projects/check_project.py <project>`).

## Teaching suggestions

* Spend the first 10 minutes of each session on the previous project checkpoint (show-and-tell).
* Pair students with different interests so they explain their data to each other.
* Encourage students to break code on purpose; reading error messages is a core skill.
* Run the capstone peer review as a fresh-clone exercise; it exposes missing instructions better than any rubric.
