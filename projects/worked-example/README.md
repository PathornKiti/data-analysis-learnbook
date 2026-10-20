# What drives daily bike-share demand, and can we predict it?

> **Question:** How do temperature, rain and weekends affect the number of bike-share rides per day, and how well can we predict ridership for days we haven't seen?

This is the **worked example** for the course capstone: a complete project in the exact structure students are asked to produce
(package in `src/`, tests, one-command reproduction, data card, proposal, report notebook).
It uses the course's *synthetic* `daily_rides.csv`, so treat the findings as a demonstration of the method, not as facts about any real city.

## Summary of findings
* **Level and season:** ridership averaged **1,507** rides per day and peaked in July (about 2,120 a day), roughly 2.5× the January low (about 860).
* **Weekends are quieter:** about **10.8%** fewer rides than weekdays (168 fewer rides; 95% CI −284 to −51; permutation p = 0.005; Cohen's d ≈ 0.33; 104 weekend vs 262 weekday days).
* **Temperature dominates:** the correlation between temperature and rides is **0.96** (95% bootstrap CI 0.96 to 0.97), about 54 extra rides per °C.
* **Rain matters, but only once temperature is controlled for:** its raw correlation with rides is near zero (−0.02), yet in a regression holding temperature and weekend fixed, each mm of rain goes with **−24.4** rides (95% CI −32.4 to −16.3).
* **Prediction:** on the final 60 days (never used for fitting) a simple linear model is typically off by **106** rides, versus 630 for the predict-the-mean baseline and 137 for a random forest. Expanding-window cross-validation agrees (RMSE 117 ± 8).
* **Biggest limitation:** the data are synthetic and cover one year, so there is a single winter and a single summer; we cannot separate a seasonal effect from a one-off trend, and we cannot say anything about causes beyond association.

## Data
* **Source:** the course's bundled synthetic dataset (`data/daily_rides.csv` in the course repository), generated with a fixed random seed; **licence:** same as the course repository.
* **What a row is:** one day of bike-share rides in 2024; 366 rows × 5 columns (`date`, `temp_c`, `rain_mm`, `is_weekend`, `rides`). Six temperatures are missing.
* Full description: [`DATA_CARD.md`](DATA_CARD.md). Raw data lives in `data/raw/` and is never edited.

## How to run
```bash
cd projects/worked-example           # (or copy this folder anywhere)
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt      # also installs the package in editable mode
python run_analysis.py               # reproduces the cleaned data, figures and results
pytest                               # runs the tests, including the full pipeline
```
Open `notebooks/02_report.ipynb` for the narrative version. Requires Python 3.10 or newer.

## Project structure
```
run_analysis.py          one command reproduces everything
src/ridership/
    load.py              read the raw CSV
    clean.py             flag + fill missing temperatures, validate the result
    features.py          month, weekday, rain flag
    analysis.py          describe / compare / relate: CIs, permutation test, effect size, regression
    model.py             chronological split, baseline, linear model, forest, time-series CV
    plots.py             takeaway-titled charts
    report.py            turns results into sentences (so the text cannot drift from the numbers)
    pipeline.py          runs the whole analysis and returns every number used in the report
tests/                   pytest checks, including a test that this README's numbers match the computed results
notebooks/               01_explore.ipynb (messy), 02_report.ipynb (the story)
PROPOSAL.md  DATA_CARD.md  ETHICS_CHECKLIST.md
```

## Methods (brief)
Missing temperatures were flagged and filled with the median of the same calendar month (a sensitivity check refitting without those days gives the
same temperature slope: 54.9 vs 54.6 rides per °C). Cleaned data are validated (no duplicates, plausible ranges, weekend flag consistent with the calendar) and the pipeline stops if validation fails.
We described ridership, compared weekends with weekdays (Welch interval, permutation test, effect size), related ridership to temperature (correlation with bootstrap interval)
and fitted a linear regression of rides on temperature, rain and weekend. For prediction we used a **chronological** split (train on the first 306 days, test on the last 60) and expanding-window cross-validation,
comparing a mean baseline, linear regression and a random forest. All randomness is seeded.

## Results
![Ridership peaks in July](reports/figures/monthly_rides.png)
Ridership has a strong seasonal shape. The peak month is about 2.5 times busier than the quietest.

![Temperature vs rides](reports/figures/temperature_vs_rides.png)
Temperature explains most of the variation in daily rides; weekends (orange) sit below weekdays at the same temperature.

![Effect of rain](reports/figures/rain_effect.png)
Rain's effect is hidden by temperature swings until temperature is adjusted for.

![Model predictions](reports/figures/test_predictions.png)
The simple linear model tracks the held-out final days closely; the more flexible random forest did *worse* (137 vs 106 RMSE) because the underlying relationship is close to a straight line, so the forest's extra flexibility mostly adds variance (the Module 10 lesson: complexity must earn its place).

(Figures are generated by `python run_analysis.py` into `reports/figures/`. The full numbers are in `reports/results.md` and `reports/results.json`.)

## Limitations and ethics
* **Synthetic data, one year.** Real ridership would include holidays, events, trends and breakdowns that this dataset does not.
* **Association, not causation.** The model describes how rides vary with weather and weekends; it does not show that rain *causes* cancelled trips.
* **Missing data.** Six temperatures were imputed; the sensitivity check suggests this does not matter here.
* **Extrapolation.** The model is only trustworthy within the temperature range seen (about −5 to 31 °C).
* No personal data are involved; see [`ETHICS_CHECKLIST.md`](ETHICS_CHECKLIST.md).

## Credits and licence
* Data: the course's synthetic generator (`data/generate_datasets.py`). Libraries: pandas, NumPy, SciPy, scikit-learn, statsmodels, matplotlib.
