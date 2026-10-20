# Data Analysis Learnbook

A hands-on course that takes you from **zero Python** to a **complete data-analysis project of your own**, using
**Python + data analysis + the essential mathematics** you actually need.

You don't finish this course with exercises. You finish it with *something you built*, about something *you care about*,
as a small Python package that anyone can run, test and understand.

## Who it's for

* Complete beginners to programming (high-school maths is enough)
* Students, career-changers and curious people who want to answer questions with data
* Teachers who want a ready-to-use, project-based syllabus (see the [instructor guide](INSTRUCTOR_GUIDE.md))

## How it works

1. **Learn in notebooks.** Each module has a Jupyter `lesson.ipynb` (read and run), an `exercises.ipynb` with built-in
   self-checks, and short `math-notes.md`. Solutions live in [`solutions/`](solutions/).
2. **Math at the point of need.** Mean, variance, vectors, probability, least squares, gradient descent, odds… each appears exactly when the code needs it.
3. **Build your own project from week 1.** In Module 2 you pick a topic you love. Every module after that ends with a
   *project checkpoint*. In Module 6.5 you move from notebooks to **`.py` modules**; by the capstone your project is a package with tests,
   a one-command `run_analysis.py`, and a report notebook, checked by a **project doctor** script.

## Course map

| # | Module | You will… |
|---|---|---|
| 0 | [Setup](modules/00-setup/) | install Python, Jupyter and Git; run your first notebook |
| 1 | [Python foundations](modules/01-python-foundations/) | write functions, loops and comprehensions; see Σ as a loop |
| 2 | [Project kickoff](modules/02-project-kickoff/) | turn an interest into an answerable question; pick a dataset |
| 3 | [NumPy](modules/03-numpy/) | compute with arrays; vectors, dot products, z-scores |
| 4 | [pandas I: tables](modules/04-pandas-1/) | load, filter, group and summarise; mean/median/variance |
| 5 | [pandas II: cleaning](modules/05-pandas-2-cleaning/) | fix messy data; percentages, logs, the IQR rule |
| 6 | [Visualization & EDA](modules/06-visualization-eda/) | choose honest charts; correlation and its limits |
| 6.5 | [From notebook to module](modules/06b-notebook-to-module/) | scripts, packages, `pytest`; hands-on package exercise |
| 7 | [Probability](modules/07-probability/) | simulate chance; Bayes, expected value, the CLT |
| 7b | [Distributions of data](modules/07b-distributions-of-data/) | skewness, a distribution catalogue, MLE & AIC, Q-Q plots, goodness-of-fit, transformations |
| 8 | [Statistical inference](modules/08-statistical-inference/) | confidence intervals, bootstrap, tests, power |
| 8b | [Hypothesis-testing toolkit](modules/08b-hypothesis-testing-toolkit/) | t / paired / rank tests, ANOVA, ANCOVA, proportions, χ², equivalence, power; choose and report the right test |
| 9 | [Linear regression](modules/09-linear-regression/) | least squares, gradient descent, interpretation |
| 9b | [Charts & their calculations](modules/09b-charts-and-calculations/) | the maths behind every chart: bins, ECDF, KDE, box plots, error bars, confidence bands, heatmaps |
| 10 | [Prediction & evaluation](modules/10-prediction-evaluation/) | avoid overfitting; cross-validation; logistic regression; metrics |
| 11 | [Communicating results](modules/11-communicating-results/) | write honest reports, charts, docs and tests; ethics |
| 12 | [Capstone](modules/12-capstone/) | finish, review and present your project |

**Extension modules** (optional, 1–2 weeks each; take the ones your project's data call for, after Modules 8b–9):

| # | Module | Use it when your data are… |
|---|---|---|
| X1 | [Repeated measures & mixed models](modules/X1-repeated-measures-mixed-models/) | measured repeatedly on the same units, or grouped in clusters: ICC, design effect, cluster-robust SEs, random intercepts and slopes |
| X2 | [Survival analysis](modules/X2-survival-analysis/) | time until an event with censoring: Kaplan–Meier, log-rank, hazard ratios, Cox regression |
| X3 | [Bayesian inference](modules/X3-bayesian-inference/) | small samples, prior knowledge, or a need for probability statements: conjugate models, grids, Metropolis, credible intervals |
| X4 | [Time-series analysis & inference](modules/X4-time-series/) | ordered in time: decomposition, autocorrelation, HAC and AR-error inference, spurious regression, honest forecasts |

See [`SYLLABUS.md`](SYLLABUS.md) for outcomes, pacing and the maths in each module, the [`GLOSSARY.md`](GLOSSARY.md) for terms, and the [`reference/`](reference/) sheets
(**which test? which chart? which distribution? how do I write it up?**) to keep open while writing a thesis.

## Quick start

**Option A: run locally (recommended)**

```bash
git clone https://github.com/PathornKiti/data-analysis-learnbook.git
cd data-analysis-learnbook
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open `modules/00-setup/check_environment.ipynb`. Full instructions: [`modules/00-setup/`](modules/00-setup/README.md).

**Option B: Google Colab (nothing to install).** Open any notebook from GitHub in Colab; the data-loading cell
clones the repo automatically. (Modules 6.5, 11 and 12 and your project work best locally, because you'll create `.py` files.)

**Curious what the finished product looks like?** Try the worked example (a few seconds once the packages are installed):

```bash
cd projects/worked-example
pip install -r requirements.txt
python run_analysis.py
```

## Repository layout

```
modules/NN-name/     README (goals, pitfalls, project checkpoint), lesson, exercises, math-notes
solutions/NN-name/   worked solutions (try first!)
projects/
  tracks.md          interest tracks and dataset sources
  templates/         proposal, data card, project README, report outline, ethics checklist, presentation
  template/          a runnable project skeleton to copy
  worked-example/    a finished project (bike-share demand) to study
  check_project.py   the "project doctor"
  rubric.md          how projects are assessed
reference/           one-page sheets: choosing a test, choosing a chart, distributions, reporting results
  (modules X1-X4 are optional extensions: mixed models, survival, Bayesian, time series)
data/                small bundled (synthetic) datasets + generator script
.github/workflows/   CI that runs every lesson, solution, package and project
```

## Contributing

Notebooks are the source of truth. See [`CONTRIBUTING.md`](CONTRIBUTING.md): keep outputs cleared, make exercises self-checking,
and run everything top-to-bottom before opening a pull request. CI executes every lesson and solutions notebook.
