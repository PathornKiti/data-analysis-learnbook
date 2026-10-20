# Module 9b: Charts and the calculations behind them

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 6, 7, 8 and 9 (error bars and bands use confidence intervals; the band section uses simple regression) · **Needed for:** every figure in a thesis

## Learning goals
* For each chart type, state **what is calculated** and what the chart can and can't show
* Choose and **report** the parameters that change a chart: bin width, bandwidth, interval type, smoothing window, band type
* Compute **histograms** (with Sturges / Scott / Freedman–Diaconis rules and densities), the **ECDF**, **kernel density**, **box-plot statistics**, **error bars** (SD, SE, CI, bootstrap, Wilson), **rolling and exponential averages**, **regression confidence and prediction bands**, **correlation matrices** (Pearson and Spearman) and **2-D bin counts**, by hand
* Verify each calculation against NumPy / SciPy / pandas / matplotlib / statsmodels
* Write a thesis-grade **figure caption** that says what is plotted, the sample size and what the bars/bands mean

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | 11 sections: each chart's calculation by hand, then the library, with figures |
| `exercises.ipynb` | 10 exercises that implement the calculations and compare with the libraries |
| `math-notes.md` | formulas for bins, ECDF, KDE, quartiles, standard errors, bands, rank correlation, Wilson |
| [`../../solutions/09b-charts-and-calculations/`](../../solutions/09b-charts-and-calculations/) | solutions |
| [`../../reference/choosing-a-chart.md`](../../reference/choosing-a-chart.md) | one-page chart chooser: question → chart → calculation → pitfalls → code |

## Common pitfalls
* Histograms with too few or too many bins, or unlabelled count vs density axes
* KDE curves spilling over a boundary (negative minutes, scores above 100)
* Reading box-plot whiskers as min and max (they stop at the last point inside the fence)
* **Unlabelled error bars**: SD, SE and CI answer different questions
* Bars that don't start at zero; bars with no interval for proportions from small samples
* Rolling averages that lag turning points, reported without their window
* Confusing the **confidence band** (the mean) with the **prediction band** (a new observation)
* Sequential palettes for correlations (use a diverging palette centred at 0, limits −1 to 1)
* Overplotting thousands of points instead of binning

## 🎯 Project checkpoint: **a chart audit**
Create `reports/chart_audit.md` (or a table in your notebook) listing **every figure** in your thesis/project:

| figure | question it answers | chart type & why | calculation behind it | key parameter(s) and value | interval/band (what it is) | n | caption written? |
|---|---|---|---|---|---|---|---|

1. For each figure, fill the table. Anything you can't fill (*"what does this error bar show?"*) is a bug in the figure.
2. Replace any default that you can't justify (bins, bandwidth, smoothing window) with a deliberate choice, and state it in the caption.
3. Add at least one ECDF or Q-Q plot where you compare distributions, and one interval plot or forest plot where you compare estimates.
4. Put each chart in a function in `src/<package>/plots.py` that takes a DataFrame and returns the Axes (as in the template), and a function that **returns the numbers plotted** so they can be tested.
5. Write captions in the template: *what is plotted · n · what the bars/bands mean · source*.

## Further reading
* *Fundamentals of Data Visualization* (Claus Wilke, free online), chapters on distributions, uncertainty and colour
* *The Visual Display of Quantitative Information* (Tufte) and *Visualization Analysis & Design* (Munzner)
* matplotlib [`boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats) docs for the exact whisker rule
