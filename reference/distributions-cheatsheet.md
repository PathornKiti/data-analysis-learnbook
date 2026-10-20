# Distributions cheat-sheet

## Which distribution? (match the data-generating story)

| your variable | think of | check | Module |
|---|---|---|---|
| yes/no outcome of one trial | Bernoulli($p$) | – | 7 |
| number of successes in $n$ independent trials | Binomial($n,p$) | $np(1-p)$ ≈ variance | 7 |
| count of events in a fixed interval (independent events, constant rate) | Poisson($\lambda$) | **mean ≈ variance**; χ² goodness-of-fit | 7b |
| counts with variance > mean (overdispersed) | Negative binomial | variance/mean ratio | 7b |
| time between events / lifetimes (memoryless) | Exponential($\lambda$) | Q-Q plot vs exponential | 7b |
| time until the $k$-th event; positive, right-skewed | Gamma($k,\theta$) | AIC vs lognormal | 7b |
| positive, right-skewed, multiplicative effects (income, response times, sizes) | **Lognormal** | log is normal: Q-Q, Shapiro on $\ln x$ | 7b |
| symmetric noise around a mean; sums/averages | Normal | Q-Q, skew ≈ 0, kurtosis ≈ 0 | 7, 7b |
| proportion between 0 and 1 | Beta($\alpha,\beta$) | bounded; check skew | 7b |
| all values equally likely on an interval | Uniform($a,b$) | flat histogram, ECDF is a line | 7 |
| heavy tails / extremes | Student $t$, Pareto, extreme-value | S-shaped Q-Q | 7b |
| two bumps | **mixture** | BIC for number of components | 7b |
| standardised mean with estimated sd | Student $t_{n-1}$ | – | 7b |
| sum of squared standard normals | $\chi^2_k$ | – | 7b |
| ratio of variances | $F_{\nu_1,\nu_2}$ | – | 7b |

## Formulas

| | support | pmf / pdf | mean | variance |
|---|---|---|---|---|
| Binomial($n,p$) | $0..n$ | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson($\lambda$) | $0,1,\dots$ | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ |
| Uniform($a,b$) | $[a,b]$ | $\frac1{b-a}$ | $\frac{a+b}2$ | $\frac{(b-a)^2}{12}$ |
| Normal($\mu,\sigma^2$) | $\mathbb R$ | $\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |
| Lognormal($\mu,\sigma^2$) | $x>0$ | $\frac1{x\sigma\sqrt{2\pi}}e^{-(\ln x-\mu)^2/2\sigma^2}$ | $e^{\mu+\sigma^2/2}$ (median $e^\mu$) | $(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$ |
| Exponential($\lambda$) | $x\ge0$ | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ |
| Gamma($k,\theta$) | $x>0$ | $\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$ | $k\theta$ | $k\theta^2$ |
| Beta($\alpha,\beta$) | $(0,1)$ | $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ | $\frac\alpha{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

## SciPy parameter conventions (the usual source of bugs)

| distribution | SciPy object | how the usual parameters map |
|---|---|---|
| Binomial($n,p$) | `stats.binom(n, p)` | direct |
| Poisson($\lambda$) | `stats.poisson(mu=lam)` | `mu` is the rate $\lambda$ |
| Uniform on $[a,b]$ | `stats.uniform(loc=a, scale=b-a)` | **scale is the width**, not $b$ |
| Normal($\mu,\sigma$) | `stats.norm(loc=mu, scale=sigma)` | `scale` is the **standard deviation**, not the variance |
| Lognormal($\mu,\sigma$) | `stats.lognorm(s=sigma, scale=np.exp(mu))` | `s` is $\sigma$ of $\ln X$; `scale` is $e^\mu$ (the median) |
| Exponential(rate $\lambda$) | `stats.expon(scale=1/lam)` | **scale is the mean $1/\lambda$**, not the rate |
| Gamma($k,\theta$) | `stats.gamma(a=k, scale=theta)` | `a` is the shape $k$; `scale` is $\theta$ |
| Beta($\alpha,\beta$) | `stats.beta(a, b)` | direct |
| Student $t_\nu$ | `stats.t(df=nu)` | |
| $\chi^2_k$ | `stats.chi2(df=k)` | |
| $F$ | `stats.f(dfn, dfd)` | |

## Everyday calls
```python
d = stats.norm(loc=100, scale=15)
d.pdf(x)            # density (continuous)        d.pmf(k)  # probability mass (discrete)
d.cdf(x)            # P(X <= x)                   d.sf(x)   # P(X > x) = 1 - cdf (more accurate in the tail)
d.ppf(0.95)         # quantile: the x with cdf = 0.95
d.rvs(size=1000, random_state=0)                  # random samples
d.mean(), d.var(), d.std(), d.median(), d.interval(0.95)

params = stats.lognorm.fit(x, floc=0)             # maximum-likelihood fit; floc=0 fixes the location (positive data)
loglik = stats.lognorm.logpdf(x, *params).sum()   # AIC = 2k - 2*loglik
stats.kstest(x, stats.lognorm(*params).cdf)       # KS (p-value is optimistic when parameters are fitted)
stats.probplot(x, dist="norm", plot=ax)           # Q-Q plot
stats.boxcox(x)                                   # Box-Cox transform; returns (transformed, lambda)
```

## Fitting and checking recipe
1. Plot: histogram + KDE, ECDF, Q-Q plot; compute skewness and kurtosis.
2. Pick candidates from the *story*; fit by maximum likelihood.
3. Compare with **AIC/BIC**; look at **Q-Q plots** of the finalists.
4. Check goodness-of-fit (Shapiro for normality, χ² for counts, KS as a rough guide); remember that tests depend on $n$.
5. Transform (log, Box–Cox) or switch to distribution-free methods if the chosen method needs normality and the data are clearly skewed.
6. Write down what you checked and what you did about it (see [`reporting-results.md`](reporting-results.md)).

## Handy facts
* Normal: 68–95–99.7 within $1,2,3\sigma$; 97.5th percentile $=1.96$; 99th $=2.33$.
* Poisson ↔ Exponential: counts per unit time are Poisson($\lambda$); gaps are Exponential($\lambda$).
* Lognormal: product of many small independent factors; **mean > median**; log-scale differences are ratios.
* Binomial → Normal when $np$ and $n(1-p)$ are both $\gtrsim10$; → Poisson for large $n$, small $p$.
* Central limit theorem: means of many independent draws are approximately normal with sd $\sigma/\sqrt n$.
* Student $t$ has heavier tails than the normal; $\to N(0,1)$ as df $\to\infty$.
