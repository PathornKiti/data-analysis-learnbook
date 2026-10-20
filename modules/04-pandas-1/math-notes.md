# Math notes: Module 4 (describing data)

## Centre

| measure | definition | when to prefer it |
|---|---|---|
| **mean** | $\bar{x}=\frac1n\sum x_i$ | roughly symmetric data; when totals matter |
| **median** | middle value of the sorted data | skewed data or outliers (incomes, prices, followers) |
| **mode** | most frequent value | categories |

If mean ≫ median, the data is **right-skewed** (a long tail of big values).

## Spread
* **Range:** max − min (very sensitive to outliers)
* **Variance:** $s^2=\frac{1}{n-1}\sum(x_i-\bar{x})^2$
* **Standard deviation:** $s=\sqrt{s^2}$, same units as the data.
  For bell-shaped data, about 68% of values lie within one $s$ of the mean and about 95% within two.
* **Interquartile range (IQR):** $Q_3-Q_1$, the width of the middle 50%. Robust to outliers.

### Why divide by $n-1$?
If your data is a *sample* from a larger population, the sample mean sits a bit closer to your data than the true mean does,
so dividing by $n$ would underestimate the spread. Dividing by $n-1$ corrects this ("Bessel's correction").
It matters for small $n$ and fades for large $n$.

## Quantiles and percentiles
The **$p$-th quantile** is the value below which a share $p$ of the data falls. $Q_1$ = 0.25, median = 0.5, $Q_3$ = 0.75.
"Scoring in the 90th percentile" means better than 90% of the group.

## Groups and conditional averages
`df.groupby("job")["score"].mean()` computes the *conditional mean* $E[\text{score}\mid \text{job}]$:
the average score *given* the group. Comparing group means is the simplest way to explore relationships.

> ⚠️ A difference between group means is **not** automatically a real effect or a cause. Is it bigger than the natural spread?
> Could another variable explain it? Those questions are Modules 8–9.

## Check your understanding
1. The data are 1, 2, 3, 4, 100. Mean? Median? (22, 3.) Which better describes a "typical" value?
2. If every value is multiplied by 10, what happens to the mean, the standard deviation and the variance? (×10, ×10, ×100)
3. If the 25th and 75th percentiles of exam scores are 60 and 80, what is the IQR? (20)
