# Math notes: Module 9b (the calculations behind charts)

## Quantiles and percentiles
For sorted data $x_{(1)}\le\dots\le x_{(n)}$, NumPy's default (**linear interpolation**, "type 7") puts the $p$-th percentile at position $h=(n-1)p+1$ and interpolates between the neighbouring order statistics.
Different software uses different conventions (types 1–9), so quartiles can differ slightly between packages for small $n$; state which one you used. $\text{IQR}=Q_3-Q_1$.

## Histogram
Bins $[e_0,e_1),\dots,[e_{k-1},e_k]$. **Count** $c_j=\#\{x_i\in\text{bin }j\}$; **density** $\hat f_j=\dfrac{c_j}{n\,w_j}$ so that $\sum_j\hat f_jw_j=1$.
Bin-width rules:

| rule | width / number | derived from |
|---|---|---|
| Sturges | $k=\lceil\log_2n\rceil+1$ | assumes a normal-like shape; too few bins for large $n$ |
| Scott | $w=3.49\,s\,n^{-1/3}$ | minimises asymptotic mean-squared error for normal data |
| Freedman–Diaconis | $w=2\,\text{IQR}\,n^{-1/3}$ | same idea with a robust scale; better for skewed data |

(The optimal width shrinks like $n^{-1/3}$: more data supports finer detail.)

## Empirical CDF and the KS distance
$\hat F_n(t)=\frac1n\sum_i\mathbf 1\{x_i\le t\}$, a step function. By the Glivenko–Cantelli theorem it converges uniformly to the true CDF. Two-sample KS: $D=\sup_t|\hat F_{a}(t)-\hat F_{b}(t)|$ (attained at a data point).
The DKW inequality gives a **confidence band** for the whole ECDF: $\hat F_n(t)\pm\sqrt{\dfrac{\ln(2/\alpha)}{2n}}$.

## Kernel density estimate
$$\hat f_h(x)=\frac1{nh}\sum_{i=1}^nK\Big(\frac{x-x_i}{h}\Big),\qquad K(u)=\frac1{\sqrt{2\pi}}e^{-u^2/2}.$$
It is a density (integrates to 1). The **bandwidth** trades bias for variance: small $h$ = wiggly (high variance), large $h$ = blurry (high bias). Rules of thumb:
* **Scott:** $h=s\,n^{-1/5}$ (SciPy and seaborn default)
* **Silverman:** $h=0.9\,\min\!\big(s,\ \text{IQR}/1.34\big)\,n^{-1/5}$ (more robust to outliers)

The optimal $h$ shrinks like $n^{-1/5}$: slower than histogram bins. KDEs are biased near boundaries of bounded data; use reflection, a log transform, or an ECDF instead.

## Box plot (Tukey)
$Q_1,\ \tilde x=Q_2,\ Q_3$; fences $F_L=Q_1-1.5\,\text{IQR}$, $F_U=Q_3+1.5\,\text{IQR}$. **Whisker ends** $=\min\{x_i\ge F_L\}$ and $\max\{x_i\le F_U\}$. **Outliers** are points outside the fences.
For normal data the fences sit at about $\pm2.7\sigma$ and flag about 0.7% of points. **Notch** (approximate 95% CI for the median): $\tilde x\pm1.57\,\dfrac{\text{IQR}}{\sqrt n}$.
Why 1.5? A convention that works for roughly normal data; for skewed data many "outliers" are just the tail.

## Uncertainty of a mean: SD vs SE vs CI
$$s=\sqrt{\tfrac1{n-1}\sum(x_i-\bar x)^2},\qquad \text{SE}=\frac{s}{\sqrt n},\qquad \text{CI}_{95}=\bar x\pm t^*_{n-1}\,\text{SE}.$$
SD does **not** shrink with $n$; SE and the CI do. $t^*\approx2$ for $n\ge 30$ (2.26 for $n=10$, 4.30 for $n=3$).
**Two groups:** the CI of the *difference* uses $\sqrt{\text{SE}_1^2+\text{SE}_2^2}$. Overlap of the two groups' 95% CIs is a *conservative* check: if they don't overlap, the difference is significant at $<5\%$; if they overlap *somewhat* it can still be significant.
**Wilson interval** for a proportion: $\dfrac{\hat p+\frac{z^2}{2n}\pm z\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}}{1+\frac{z^2}{n}}$.
**Bootstrap percentile CI:** resample with replacement $B$ times, take the 2.5th and 97.5th percentiles of the statistic.

## Smoothing time series
* Trailing moving average (window $w$): $\bar y_t=\frac1w\sum_{j=0}^{w-1}y_{t-j}$; it **lags** a trend by about $(w-1)/2$ steps. A centred window avoids lag but needs future values.
* EWMA: $s_t=\alpha y_t+(1-\alpha)s_{t-1}=\alpha\sum_{j\ge0}(1-\alpha)^jy_{t-j}$ (weights decay geometrically); effective window $\approx(2-\alpha)/\alpha$ (e.g. $\alpha=0.2\to9$ days).
* **Percent change** $\frac{y_t-y_{t-1}}{y_{t-1}}$; **index** $100\,y_t/y_0$; **log differences** $\ln y_t-\ln y_{t-1}\approx$ growth rate for small changes.

## Regression bands
With $\hat y(x_0)=b_0+b_1x_0$, $s^2=\dfrac{\sum e_i^2}{n-2}$, $S_{xx}=\sum(x_i-\bar x)^2$, leverage $h(x_0)=\dfrac1n+\dfrac{(x_0-\bar x)^2}{S_{xx}}$:
$$\text{mean:}\ \ \hat y\pm t^*_{n-2}\,s\sqrt{h(x_0)}\qquad\qquad\text{new observation:}\ \ \hat y\pm t^*_{n-2}\,s\sqrt{1+h(x_0)}$$
* The mean band shrinks to 0 as $n\to\infty$; the prediction band tends to $\pm t^*s$ (the irreducible scatter).
* Both are narrowest at $x_0=\bar x$ and widen with distance from the centre (extrapolation is the riskiest).
* A **simultaneous (Working–Hotelling)** band for the whole line uses $\sqrt{2F_{2,n-2}}$ in place of $t^*$ and is wider.

## Correlation matrix
$R=\dfrac1{n-1}Z^\top Z$ where $Z$ holds the standardised columns (each with mean 0, sd 1, `ddof=1`). $R$ is symmetric with unit diagonal and is **positive semi-definite**. Spearman: replace each column by its ranks.
Pearson's $r$ measures linear association; Spearman's $\rho$ any monotonic association. A single outlier can swing Pearson's $r$ much more than $\rho$.

## 2-D binning
$c_{ij}=\#\{(x_k,y_k):x_k\in\text{bin}_i,\ y_k\in\text{bin}_j\}$. A 2-D KDE uses a product (or bivariate) kernel with bandwidths per axis; contour lines enclose the regions of equal density.

## Check your understanding
1. $n=64$, $s=16$: SE and the approximate 95% CI half-width? ($16/8=2$; about $2\times2=4$). If $n$ is quadrupled to 256? (SE 1, half-width ≈ 2; the SD stays 16)
2. For $n=1000$ normal data, Freedman–Diaconis width with IQR $=1.35\sigma$ is? ($2\times1.35\sigma\times1000^{-1/3}=0.27\sigma$)
3. Quartiles $Q_1=40$, $Q_3=60$. What are the fences, and is a value of 95 an outlier? ($10$ and $90$; yes)
4. A 7-day trailing moving average of a steadily rising series lags by about how many days? (3)
5. Which is wider at $x_0=\bar x$ for $n=100$: the mean band or the prediction band? (The prediction band, by roughly a factor $\sqrt{n}$)
