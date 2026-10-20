# Choosing a chart

Start from the **question**, not the chart. Then check the **calculation** behind it (Module 9b) and its **pitfalls**.

| question about… | chart | calculation behind it | watch out for | code |
|---|---|---|---|---|
| the **shape** of one number | histogram | bin counts or density | bin width; count vs density; say which | `ax.hist(x, bins="fd", density=True)` |
| the shape, without binning | **ECDF** | $\#\{x_i\le t\}/n$ | little: great for comparing groups | `ax.step(xs, ys, where="post")` |
| the shape, smooth | density (KDE) | kernel average, bandwidth $h$ | leaking beyond bounds; small $n$ | `sns.kdeplot(x, cut=0)` |
| does it look normal / fit a model? | **Q-Q plot** | sorted data vs model quantiles | judge the line, not the tails alone | `stats.probplot(x, plot=ax)` |
| distributions across groups | box plot / violin / strip | quartiles, fences; KDE mirrored | hidden bimodality; overlay points for small $n$ | `sns.boxplot` / `sns.violinplot` |
| **compare group means** | dot/bar + **95% CI** | mean ± $t^*$ SE (or bootstrap) | SD vs SE vs CI: **label it**; bars from 0 | `ax.errorbar(x, m, yerr=half, fmt="o")` |
| compare **proportions** | dot/bar + Wilson CI | $x/n$ and Wilson interval | no interval for small $n$ | `proportion_confint(x, n, method="wilson")` |
| **effects** across outcomes or studies | **forest plot** | estimate and CI per row (e.g. Cohen's $d$) | put them on one scale; mark 0/1 | `ax.errorbar(est, y, xerr=…, fmt="s")` |
| a change over **time** | line (+ rolling mean / EWMA) | moving average with window $w$ or $\alpha$ | lag; always report the smoothing | `y.rolling(7).mean()` |
| composition of a whole | 100% stacked bar / grouped bar | cross-tab then normalise | pies; unequal baselines | `pd.crosstab(a, b, normalize="index")` |
| **relationship** of two numbers | scatter (+ trend line) | fitted line with CI or prediction band | overplotting; confidence vs prediction band | `sns.regplot`, `get_prediction()` |
| a relationship with thousands of points | hexbin / 2-D KDE | 2-D counts / density | colour scale choice | `ax.hexbin(x, y, gridsize=20)` |
| relationships among many numbers | correlation heatmap | $Z^\top Z/(n-1)$ (or on ranks) | diverging palette, fixed ±1 limits; linear only | `sns.heatmap(corr, center=0, vmin=-1, vmax=1)` |
| many variables at once | pair plot / small multiples | repeated 2-D views | clutter; keep scales shared | `sns.pairplot`, `sns.FacetGrid` |
| model **residuals** | residual vs fitted; histogram/Q-Q of residuals | $e_i=y_i-\hat y_i$ | curvature = missing structure; funnel = changing variance | `ax.scatter(fitted, resid)` |
| classifier **performance** | confusion matrix, ROC, precision–recall | counts; TPR vs FPR over thresholds | accuracy trap with rare classes | `ConfusionMatrixDisplay`, `roc_curve` |
| **power / sample size** | power curve | power vs $n$ for several $d$ | – | `TTestIndPower().power(d, n, 0.05)` |
| p-values across many tests | histogram of p-values | counts per bin | uniform = no effects | `ax.hist(p, bins=20)` |

## Rules for every chart
1. **One message per chart**, stated in the title (e.g. "Weekends see 11% fewer rides than weekdays").
2. **Label axes with units**; label lines/bars directly if possible.
3. **Bars start at zero** (lines, dots and scatter don't have to).
4. **Say what the error bars/bands are** (SD, SE, 95% CI, bootstrap; confidence vs prediction band) and the **$n$**.
5. Use **colour-blind-safe** palettes; don't rely on colour alone; diverging palettes for signed values, sequential for magnitudes.
6. **Show the data** (points, ECDF, distribution) when $n$ is small instead of only a summary.
7. **Don't smooth without saying how** (bins, bandwidth, window).
8. Avoid pie charts, 3-D charts, dual axes, and truncated bars.
9. Caption template: *what is plotted · n · what bars/bands mean · source*.

## Calculations at a glance (by hand, see Module 9b)
```python
# histogram bins:  k_sturges = ceil(log2(n)) + 1 ;  width_fd = 2 * IQR * n**(-1/3)
# ECDF:            xs = np.sort(x);  ys = np.arange(1, n+1) / n
# KDE:             f(p) = mean(norm.pdf((p - x) / h)) / h ,   h = s * n**(-1/5)
# box plot:        q1, med, q3 = np.percentile(x, [25, 50, 75]);  fences = q1 - 1.5*iqr, q3 + 1.5*iqr
# error bars:      se = s / sqrt(n);  ci = t.ppf(0.975, n-1) * se
# rolling / EWMA:  mean of last w values ;  s_t = alpha*x_t + (1-alpha)*s_{t-1}
# regression band: yhat +/- t* s sqrt(1/n + (x0-xbar)^2/Sxx)   (add 1 inside the sqrt for a prediction band)
# correlation:     Z.T @ Z / (n - 1)  with Z the standardised columns (ranks for Spearman)
```
