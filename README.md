# Data Analysis Learnbook

A hands-on course that takes you from **zero Python** to a **complete data-analysis project of your own**, using
**Python + data analysis + the essential mathematics** you actually need.

You don't finish this course with exercises. You finish it with *something you built*, about something *you care about*.

## Who it's for

* Complete beginners to programming (high-school maths is enough)
* Students, career-changers and curious people who want to answer questions with data
* Teachers who want a ready-to-use, project-based syllabus

## How it works

1. **Learn in notebooks.** Each module has a Jupyter `lesson.ipynb` (read and run), an `exercises.ipynb` with built-in
   self-checks, and short `math-notes.md`. Solutions live in [`solutions/`](solutions/).
2. **Math at the point of need.** Mean, variance, vectors, probability, least squares… each appears exactly when the code needs it.
3. **Build your own project from week 1.** In Module 2 you pick a topic you love. Every module after that ends with a
   *project checkpoint*. By the capstone, your project is a small **Python package** (`.py` modules, tests, a one-command
   `run_analysis.py`) plus a report notebook, which anyone can reproduce.

## Course map

| # | Module | Status |
|---|---|---|
| 0 | [Setup](modules/00-setup/) | ✅ available |
| 1 | [Python foundations](modules/01-python-foundations/) | ✅ available |
| 2 | [Project kickoff](modules/02-project-kickoff/) | ✅ available |
| 3 | [NumPy](modules/03-numpy/) | ✅ available |
| 4 | [pandas I: tables](modules/04-pandas-1/) | ✅ available |
| 5 | [pandas II: cleaning](modules/05-pandas-2-cleaning/) | ✅ available |
| 6 | [Visualization & EDA](modules/06-visualization-eda/) | ✅ available |
| 6.5 | [From notebook to module](modules/06b-notebook-to-module/) | ✅ available |
| 7 | Probability | 🚧 planned |
| 8 | Statistical inference | 🚧 planned |
| 9 | Linear regression | 🚧 planned |
| 10 | Prediction & evaluation | 🚧 planned |
| 11 | Communicating results | 🚧 planned |
| 12 | Capstone | 🚧 planned |

See [`SYLLABUS.md`](SYLLABUS.md) for outcomes, pacing and the maths covered in each module.

## Quick start

**Option A: run locally**

```bash
git clone https://github.com/PathornKiti/data-analysis-learnbook.git
cd data-analysis-learnbook
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open `modules/00-setup/check_environment.ipynb`. Full instructions: [`modules/00-setup/`](modules/00-setup/README.md).

**Option B: Google Colab (nothing to install).** Open any notebook from GitHub in Colab; the data-loading cell
clones the repo automatically.

## Repository layout

```
modules/NN-name/     README (goals, project checkpoint), lesson, exercises, math-notes
solutions/NN-name/   worked solutions (try first!)
projects/            tracks & dataset ideas, proposal/data-card templates, rubric, project template package
data/                small bundled (synthetic) datasets + generator script
.github/workflows/   CI that runs every lesson, solution and the project template
```

## Contributing

Notebooks are the source of truth. Keep outputs cleared in committed notebooks. CI executes every lesson and solutions
notebook, so run them top-to-bottom before opening a pull request.
