# Syllabus

**Format:** ~12–14 weeks at 4–6 hours per week (self-paced; modules can be stretched or merged).
**Prerequisites:** none beyond high-school arithmetic and the ability to install software.
**Outcome:** a reproducible data-analysis project, built with Python, on a topic of the student's choice.

## Learning outcomes

By the end, a student can:

1. Write and read Python functions, loops and data structures.
2. Load, clean, reshape and summarise tabular data with NumPy and pandas.
3. Explore a dataset visually and numerically and describe what they see honestly.
4. Use probability and basic inference to say how much a result can be trusted.
5. Fit and evaluate simple predictive models, and explain the maths in plain language.
6. Organise analysis code into importable `.py` modules with tests and a single entry point.
7. Communicate findings in a clear written report and README.

## Module overview

| # | Module | Python | Essential maths | Project checkpoint |
|---|---|---|---|---|
| 0 | Setup | venv, pip, Jupyter, Git basics | – | working environment |
| 1 | Python foundations | types, control flow, functions, lists/dicts | arithmetic, functions *f(x)*, Σ notation | – |
| 2 | Project kickoff | feasibility check with pandas | what makes a question answerable | **proposal + data card** |
| 3 | NumPy | arrays, masks, vectorisation, RNG | vectors, dot product, norm, z-scores | shortlist of 2 datasets |
| 4 | pandas I | read_csv, select, filter, groupby | mean/median/variance/quantiles | first look at your data |
| 5 | pandas II: cleaning | missing data, dtypes, merges, dates | percentages, ratios, logs | **`clean.py`** |
| 6 | Visualization & EDA | matplotlib, seaborn | distributions, correlation | **`plots.py`** + EDA notebook |
| 6.5 | From notebook to module | scripts, imports, packages, refactoring | – | project restructured as a package |
| 7 | Probability | simulation | probability rules, distributions, LLN | – |
| 8 | Statistical inference | scipy, bootstrap | sampling, confidence intervals, hypothesis tests | **`analysis.py`** |
| 9 | Linear regression | scikit-learn, statsmodels | slope/intercept, least squares, derivatives & gradient descent | first model |
| 10 | Prediction & evaluation | classification, cross-validation | odds, logistic function, precision/recall, overfitting | model comparison |
| 11 | Communicating results | reports, README, docstrings, pytest | – | tests + README |
| 12 | Capstone | everything | whatever the question needs | **final package + report + presentation** |

Optional extensions: time series · text analysis · web APIs & scraping · Streamlit dashboards.

## Assessment

* **Module self-checks:** auto-checked exercises (formative).
* **Project milestones:** proposal → data card → cleaned data → EDA → analysis/model → final write-up.
* **Final project:** graded with [`projects/rubric.md`](projects/rubric.md).

## Teaching suggestions

* Spend the first 10 minutes of each session on the previous project checkpoint (show-and-tell).
* Pair students with different interests so they explain their data to each other.
* Encourage students to break code on purpose; reading error messages is a core skill.
