# Math notes: Module 7b (distributions of data)

## Moments and shape
For data $x_1,\dots,x_n$ with mean $\bar x$, the $k$-th **central moment** is $m_k=\frac1n\sum(x_i-\bar x)^k$ ($m_2$ is the population-style variance).

$$\text{skewness } g_1=\frac{m_3}{m_2^{3/2}},\qquad\text{excess kurtosis } g_2=\frac{m_4}{m_2^2}-3.$$

* Both are **unit-free**. A normal distribution has $g_1=0$, $g_2=0$.
* $g_1>0$: long right tail (mean $>$ median typically). $g_2>0$: heavier tails/more extremes than normal; $g_2<0$: lighter tails, flatter or bimodal.
* Sample versions (as in `scipy.stats.skew(bias=False)`) apply small-sample corrections; the biased formulas above are the SciPy default. The sampling variability of $g_1$ is roughly $\sqrt{6/n}$ for normal data, so don't over-read small samples.
* Alternative skew measures: **Pearson's second coefficient** $3(\bar x-\text{median})/s$; **Bowley's** $\frac{Q_3+Q_1-2Q_2}{Q_3-Q_1}$ (robust).

## The distribution catalogue

| | support | pmf / pdf | mean | variance |
|---|---|---|---|---|
| Bernoulli($p$) | $\{0,1\}$ | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $\{0..n\}$ | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson($\lambda$) | $\{0,1,\dots\}$ | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ |
| Uniform($a,b$) | $[a,b]$ | $1/(b-a)$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Normal($\mu,\sigma^2$) | $\mathbb R$ | $\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |
| Lognormal($\mu,\sigma^2$) | $(0,\infty)$ | $\frac{1}{x\sigma\sqrt{2\pi}}e^{-(\ln x-\mu)^2/2\sigma^2}$ | $e^{\mu+\sigma^2/2}$ | $(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$ |
| Exponential($\lambda$) | $[0,\infty)$ | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ |
| Gamma($k,\theta$) | $(0,\infty)$ | $\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}$ | $k\theta$ | $k\theta^2$ |
| Beta($\alpha,\beta$) | $(0,1)$ | $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

**Relationships worth knowing**
* Sum of $n$ Bernoulli($p$) is Binomial($n,p$). A Binomial with large $n$ and small $p$ is approximately Poisson($np$).
* Poisson process with rate $\lambda$: counts per unit time are Poisson($\lambda$); gaps between events are Exponential($\lambda$); the time until the $k$-th event is Gamma($k,1/\lambda$).
* **Memoryless property** of the exponential: $P(X>s+t\mid X>s)=P(X>t)$.
* If $\ln X\sim\text{Normal}(\mu,\sigma^2)$ then $X$ is lognormal, with **median $e^{\mu}$**, **mean $e^{\mu+\sigma^2/2}$** (mean $>$ median), and the geometric mean of the data estimates the median.
* Central limit theorem: sums/means of many independent effects tend to normal; *products* tend to lognormal.

## Maximum likelihood
**Likelihood** $L(\theta)=\prod_i f(x_i;\theta)$; **log-likelihood** $\ell(\theta)=\sum_i\ln f(x_i;\theta)$. The MLE $\hat\theta$ maximises $\ell$; set $\ell'(\theta)=0$.

*Exponential.* $\ell(\lambda)=n\ln\lambda-\lambda\sum x_i$, so $\ell'=\frac n\lambda-\sum x_i=0\Rightarrow\hat\lambda=\frac{n}{\sum x_i}=\frac1{\bar x}$.

*Poisson.* $\ell(\lambda)=\sum(x_i\ln\lambda-\lambda-\ln x_i!)$, so $\ell'=\frac{\sum x_i}{\lambda}-n=0\Rightarrow\hat\lambda=\bar x$.

*Normal.* $\ell(\mu,\sigma^2)=-\frac n2\ln(2\pi\sigma^2)-\frac1{2\sigma^2}\sum(x_i-\mu)^2$. Setting both partial derivatives to zero gives $\hat\mu=\bar x$ and $\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$ (note the $1/n$: the MLE of the variance is slightly biased; the unbiased version uses $n-1$).

MLEs are **consistent**, **asymptotically normal** and **asymptotically efficient**, and have standard errors from the curvature of $\ell$ (the Fisher information).

## Model comparison
$$\text{AIC}=2k-2\ell(\hat\theta),\qquad\text{BIC}=k\ln n-2\ell(\hat\theta)$$
with $k$ the number of estimated parameters. Lower is better. Differences $\Delta\text{AIC}>10$ give essentially no support to the worse model; $\Delta<2$ means roughly equal support. AIC targets predictive accuracy; BIC tends to pick simpler models. Both compare **only the models you fitted**; neither says the best one is adequate.

## Checking fit
**Q-Q plot.** Plot the sorted data $x_{(i)}$ against $F^{-1}\big(\frac{i-0.5}{n}\big)$ (other conventions exist: $\frac{i-3/8}{n+1/4}$, Filliben's). Under the model the points follow the line $y=\mu+\sigma x$ (for the normal). Deviations: curvature = skewness, S-shape = tail weight, steps = discreteness/bimodality.

**Empirical CDF.** $F_n(x)=\frac1n\#\{x_i\le x\}$.

**Kolmogorov–Smirnov.** $D_n=\sup_x|F_n(x)-F(x)|=\max_i\max\Big(\frac in-F(x_{(i)}),\,F(x_{(i)})-\frac{i-1}n\Big)$. Under a fully specified $F$, the null distribution of $\sqrt n\,D_n$ is distribution-free (Kolmogorov). With parameters estimated from the data the null distribution changes: for normality use the **Lilliefors** correction.

**Shapiro–Wilk.** $W=\frac{\left(\sum a_ix_{(i)}\right)^2}{\sum(x_i-\bar x)^2}$, with weights $a_i$ from the expected order statistics of a normal; $W\le1$, values near 1 indicate normality. Powerful for $n<5000$.

**Chi-square goodness-of-fit.** For $c$ bins with observed counts $O_j$ and expected $E_j=n\,p_j(\hat\theta)$: $\chi^2=\sum_j\frac{(O_j-E_j)^2}{E_j}$, compared to $\chi^2_{\,c-1-m}$ where $m$ is the number of parameters estimated. Merge bins so that $E_j\gtrsim5$.

## Transformations
**Box–Cox:** $y(\lambda)=\begin{cases}\dfrac{x^\lambda-1}{\lambda},&\lambda\ne0\\[2mm]\ln x,&\lambda=0\end{cases}$ for $x>0$, with $\lambda$ chosen to maximise the normal log-likelihood of the transformed data. $\lambda\approx1$: no transform needed; $\lambda\approx0.5$: square root; $\lambda\approx0$: log; $\lambda\approx-1$: reciprocal.

**Back-transforming:** $\ln a-\ln b=\ln(a/b)$, so a difference of means of logs is the log of a **ratio of geometric means**; exponentiate the estimate *and* the interval limits. The mean of $\ln X$ back-transforms to the **median/geometric mean**, not the arithmetic mean.

## Distributions of statistics
* **Student's $t_\nu$:** if $Z\sim N(0,1)$ and $V\sim\chi^2_\nu$ independent, $T=Z/\sqrt{V/\nu}$. For normal data, $\frac{\bar x-\mu}{s/\sqrt n}\sim t_{n-1}$. Variance $\nu/(\nu-2)>1$ (heavier tails), $\to N(0,1)$ as $\nu\to\infty$.
* **$\chi^2_k$:** $\sum_{j=1}^kZ_j^2$. Mean $k$, variance $2k$. For normal data $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$.
* **$F_{\nu_1,\nu_2}$:** $\dfrac{V_1/\nu_1}{V_2/\nu_2}$. For normal data the ratio of two sample variances is $F_{n_1-1,\,n_2-1}$ under equal variances; ANOVA's $F=\text{MSB}/\text{MSW}$.

## Mixtures
A $K$-component mixture has density $f(x)=\sum_{k=1}^K\pi_kf_k(x)$ with weights $\pi_k\ge0$, $\sum\pi_k=1$. Its mean is $\sum\pi_k\mu_k$ and its variance exceeds the average within-component variance (the extra is the between-component spread). Fitted by the EM algorithm; choose $K$ by BIC.

## Check your understanding
1. A sample has mean 50, median 42, and a long right tail. Which sign of skewness do you expect? (Positive)
2. For counts with mean 6 and variance 15, is a Poisson model reasonable? (No: overdispersed; try the negative binomial)
3. If the Box–Cox $\hat\lambda\approx0.03$ with a 95% CI containing 0, which transform do you use and how do you report differences? (The log; as ratios of geometric means)
4. Ten times more data, same tiny skewness: what happens to the Shapiro–Wilk p-value on average? (It falls; trivial departures become "significant")
5. $X\sim\text{Exponential}(\lambda=2/\text{hour})$. What is $P(X>1\text{ hour})$ and the median? ($e^{-2}\approx0.135$; $\ln2/2\approx0.35$ hours)
