# Module 6: Visualization & exploratory data analysis

**Time:** ~1.5 weeks (6–8 h) · **Prerequisite:** Modules 4 and 5

## Learning goals
* Explain why you must plot data, not just summarise it (Anscombe's quartet)
* Use matplotlib's Figure/Axes model and seaborn's shortcuts; label every chart
* Choose a chart from the question: histogram, bar, line, scatter, box, heatmap, small multiples
* Compute and interpret the correlation coefficient; know its limits (non-linearity, outliers, confounders, Simpson's paradox)
* Spot and avoid misleading charts
* Run a structured EDA and write down what you learn

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | the full tour on the `students` and `daily_rides` data |
| `exercises.ipynb` | 7 exercises. Plotting tasks are functions returning `Axes`, with checks that inspect them |
| `math-notes.md` | distributions, skew, covariance and correlation, causation, log scales |
| [`../../solutions/06-visualization-eda/`](../../solutions/06-visualization-eda/) | solutions |

## Common pitfalls
* Forgetting titles, axis labels and units
* Bar charts whose axis doesn't start at zero
* Too many colours or categories; try small multiples instead
* Quoting *r* without looking at the scatter plot
* Reading causation into correlation

## 🎯 Project checkpoint: **`plots.py` + EDA notebook**
1. Follow the mini-EDA recipe from the lesson on your cleaned data, in `notebooks/01_explore.ipynb`.
2. Make **at least four** charts that matter for your question: one distribution, one comparison across groups,
   one relationship, one over time (if you have dates).
3. Turn your best two into functions in `src/<your_package>/plots.py` that take a DataFrame and return the `Axes`
   (see `projects/template/src/myproject/plots.py`).
4. Write 3–5 bullet points of *observations* and 2 *new questions* the charts raised. They go in your report.

## Further reading
* [matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) · [seaborn gallery](https://seaborn.pydata.org/examples/index.html)
* *The Visual Display of Quantitative Information*, Edward Tufte, and *Storytelling with Data*, Cole Nussbaumer Knaflic
