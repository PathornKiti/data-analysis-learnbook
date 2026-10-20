# Math notes: Module 6

## Distributions
A **distribution** says how often each value occurs. A histogram estimates it from data.
* **Normal (bell-shaped):** symmetric; about 68% of values within 1 standard deviation of the mean, 95% within 2.
* **Right-skewed:** long tail of large values; mean > median. Log-transform often helps.
* **Bimodal:** two peaks, often two groups mixed together.

## Covariance and correlation
For paired data $(x_i, y_i)$:

$$\operatorname{cov}(x,y)=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})\qquad
r=\frac{\operatorname{cov}(x,y)}{s_x\,s_y}$$

* Each term is positive when $x_i$ and $y_i$ are on the *same* side of their means, negative when on opposite sides.
* Dividing by $s_xs_y$ removes units and forces $-1\le r\le1$.
* **Interpreting $r$** (rough guide): $|r|<0.3$ weak, $0.3$–$0.7$ moderate, $>0.7$ strong. Context matters more than thresholds.
* **$r^2$** is the fraction of the variance of $y$ explained by the best straight line through the data.
* $r$ is unchanged if you rescale or shift either variable (e.g. °C → °F).
* **Spearman's rank correlation** (`df.corr(method="spearman")`) measures *monotonic* association and is less sensitive to outliers.

## What correlation can't tell you
1. **Non-linearity:** $y=x^2$ on symmetric $x$ has $r=0$ yet is perfectly dependent.
2. **Outliers:** one extreme point can create a high $r$ (Anscombe III, IV).
3. **Confounding:** a hidden third variable drives both (heat → ice-cream sales *and* drownings).
4. **Simpson's paradox:** a trend in the pooled data can reverse inside every subgroup. Always look for groups.
5. **Direction of cause:** $r$ is symmetric; "A causes B" and "B causes A" give the same $r$.

Evidence of causation needs a **designed experiment** (randomise who gets the treatment) or very careful reasoning. Modules 8–10 return to this.

## Scales
* **Linear scale:** equal distances = equal *differences*.
* **Log scale:** equal distances = equal *ratios* (each tick ×10). Good for data spanning orders of magnitude.
* **Normalising / standardising** ($z$-scores, min-max) puts different variables on a comparable scale for fair side-by-side comparison.

## The ethics of charts
A chart is an argument. Choices of axis range, bin width, colour and which data to show all change what a reader concludes.
Show uncertainty where you can, label your sources, and ask "would this chart still persuade me if it argued the opposite?"

## Check your understanding
1. If every temperature is converted from °C to °F, what happens to $r$ with ice-cream sales? (Unchanged)
2. Two variables have $r=0$. Does that mean they're unrelated? (No, only that there's no *linear* relationship)
3. A pooled trend is negative but positive within each group. What should you suspect? (A hidden grouping variable; Simpson's paradox)
