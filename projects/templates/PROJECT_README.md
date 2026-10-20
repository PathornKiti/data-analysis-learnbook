# <Project title: a short, specific name>

> **Question:** <one sentence: what are you trying to find out?>

## Summary of findings
* <Finding 1, with the number, its unit and its uncertainty, e.g. "Each extra study hour goes with 1.6 more points (95% CI 1.4 to 1.7).">
* <Finding 2>
* <Finding 3>
* **Biggest limitation:** <one sentence>

## Data
* **Source:** <name and link>, downloaded <date>, **licence:** <licence>
* **What a row is:** <e.g. "one day of bike-share rides">, <N> rows × <M> columns
* Full description: [`DATA_CARD.md`](DATA_CARD.md). Raw data lives in `data/raw/` and is never edited.

## How to run
```bash
git clone <your repository URL>
cd <project folder>
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_analysis.py        # reproduces the cleaned data, figures and results
pytest                        # runs the tests
```
Tested with Python <version> on <operating system>.

## Project structure
```
run_analysis.py       one command reproduces everything
src/<package>/        load.py, clean.py, features.py, analysis.py, model.py, plots.py
tests/                pytest checks
notebooks/            01_explore.ipynb (messy), 02_report.ipynb (the story)
data/raw/             original data (read-only)
data/processed/       generated
reports/figures/      generated
```

## Methods (brief)
<3–6 sentences: cleaning decisions, the analyses or models used, how you evaluated them (splits, cross-validation, intervals), random seeds.>

## Results
<1–3 key figures with takeaway titles, e.g. `![Weekends are quieter](reports/figures/weekday_vs_weekend.png)`, each followed by one or two sentences with numbers.>

## Limitations and ethics
* <What could be wrong? Sampling, measurement, confounders, unseen groups, period covered.>
* <Privacy / consent / fairness notes; see the ethics checklist.>

## Credits and licence
* Data: <citation>. Libraries: pandas, NumPy, SciPy, scikit-learn, statsmodels, matplotlib, seaborn.
* Code licence: <e.g. MIT>
