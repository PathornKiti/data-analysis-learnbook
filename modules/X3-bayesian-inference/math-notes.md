# Math notes: Module X3 (Bayesian inference)

## Bayes' rule for parameters
$$p(\theta\mid y)=\frac{p(y\mid\theta)\,p(\theta)}{p(y)},\qquad p(y)=\int p(y\mid\theta)\,p(\theta)\,d\theta\ \ (\text{the marginal likelihood; a constant in }\theta).$$
So $p(\theta\mid y)\propto p(y\mid\theta)p(\theta)$. For independent data $p(y\mid\theta)=\prod_ip(y_i\mid\theta)$; the posterior after one batch becomes the prior for the next (**sequential updating**).

## Conjugate models
A prior is **conjugate** to a likelihood if the posterior is in the same family.

**Beta–Binomial.** $x\mid p\sim\text{Bin}(n,p)$, $p\sim\text{Beta}(\alpha,\beta)$ (density $\propto p^{\alpha-1}(1-p)^{\beta-1}$). The posterior density is proportional to $p^{x}(1-p)^{n-x}\cdot p^{\alpha-1}(1-p)^{\beta-1}=p^{\alpha+x-1}(1-p)^{\beta+n-x-1}$, so
$$p\mid x\sim\text{Beta}(\alpha+x,\ \beta+n-x),\qquad\text{posterior mean}=\frac{\alpha+x}{\alpha+\beta+n}=\underbrace{\frac{\alpha+\beta}{\alpha+\beta+n}}_{w}\frac{\alpha}{\alpha+\beta}+(1-w)\frac xn.$$
The posterior mean is a **weighted average of the prior mean and the sample proportion**, with weight $\propto$ "prior sample size" $\alpha+\beta$ versus $n$. Example: Beta(1,1) prior and 7 successes in 10 gives Beta(8,4) with mean $8/12=0.667$.

**Normal–Normal (known $\sigma^2$).** $\bar x\mid\mu\sim N(\mu,\sigma^2/n)$, $\mu\sim N(\mu_0,\tau^2)$. Working with **precisions** $1/\tau^2$ and $n/\sigma^2$:
$$\frac1{\tau_n^2}=\frac1{\tau^2}+\frac n{\sigma^2},\qquad\mu_n=\tau_n^2\Big(\frac{\mu_0}{\tau^2}+\frac{n\bar x}{\sigma^2}\Big).$$
Example: $\mu_0=0$, $\tau=1$, $\bar x=2$, $\sigma=1$, $n=4$: precision $1+4=5$, $\mu_n=8/5=1.6$, $\tau_n=1/\sqrt5=0.447$. As $\tau\to\infty$, $\mu_n\to\bar x$ and $\tau_n\to\sigma/\sqrt n$.
With unknown $\sigma^2$ and the reference prior $p(\mu,\sigma^2)\propto1/\sigma^2$: $\ \dfrac{\mu-\bar x}{s/\sqrt n}\,\Big|\,y\sim t_{n-1}$, the same $t$ distribution as the frequentist pivot, which is why the credible and confidence intervals coincide numerically.

**Gamma–Poisson.** $y_i\mid\lambda\sim\text{Poisson}(\lambda)$, $\lambda\sim\text{Gamma}(a,b)$ (shape $a$, **rate** $b$, mean $a/b$) $\Rightarrow\ \lambda\mid y\sim\text{Gamma}\big(a+\sum y_i,\ b+n\big)$. Example: prior Gamma(2, 0.5) and counts $3,5,4$: Gamma(14, 3.5) with mean $4.0$. (SciPy parametrises the gamma by `scale = 1/rate`.)

## Credible intervals
A $100(1-\alpha)\%$ credible interval $[a,b]$ satisfies $P(a\le\theta\le b\mid y)=1-\alpha$.
* **Equal-tailed:** the $\alpha/2$ and $1-\alpha/2$ posterior quantiles (what the course uses).
* **Highest posterior density (HPD):** the shortest such interval; for skewed posteriors it differs from the equal-tailed one.
A **ROPE** is a region of practical equivalence $[-\delta,\delta]$; report $P(\theta\in\text{ROPE}\mid y)$ and $P(\theta>\delta\mid y)$.
**Posterior probability from draws:** $P(\theta\in A\mid y)\approx\frac1M\#\{\theta^{(m)}\in A\}$; the Monte Carlo standard error of a probability $\hat q$ is $\sqrt{\hat q(1-\hat q)/M}$.

## Grid approximation
For one or two parameters: evaluate $\text{prior}\times\text{likelihood}$ on a grid and normalise: $\hat p(\theta_k\mid y)=\dfrac{p(y\mid\theta_k)p(\theta_k)}{\sum_jp(y\mid\theta_j)p(\theta_j)}$. Cost grows exponentially with the number of parameters.

## Random-walk Metropolis (a special case of Metropolis–Hastings)
Given the current $\theta$ and a symmetric proposal $q(\theta^*\mid\theta)=N(\theta,\text{step}^2)$: accept $\theta^*$ with probability
$$\alpha=\min\Big(1,\ \frac{p(y\mid\theta^*)p(\theta^*)}{p(y\mid\theta)p(\theta)}\Big)$$
(work with logs: accept if $\ln u<\ln\text{post}(\theta^*)-\ln\text{post}(\theta)$). The normalising constant $p(y)$ cancels. The chain satisfies **detailed balance** with the posterior as its stationary distribution, so after burn-in the draws are (dependent) samples from it. If the ratio is $0.5$, the proposal is accepted half the time.
**Tuning:** the optimal acceptance rate is about 44% in one dimension, falling to about 23% in many dimensions. Too-small steps give high acceptance but slow exploration; too-large steps give frequent rejection.

## MCMC diagnostics
For $m$ chains of length $L$: within-chain variance $W=\frac1m\sum s_j^2$, between-chain $B=\frac{L}{m-1}\sum(\bar\theta_j-\bar\theta)^2$,
$$\hat R=\sqrt{\frac{\frac{L-1}{L}W+\frac1LB}{W}}\ \ (\text{aim for}\ \lesssim1.01).$$
**Effective sample size** $\text{ESS}=\dfrac{N}{1+2\sum_{k\ge1}\rho_k}$ where $\rho_k$ is the lag-$k$ autocorrelation. Use ESS (not $N$) to judge Monte Carlo precision: $\text{MCSE}=\text{sd}/\sqrt{\text{ESS}}$. Always inspect **trace plots**; run several chains from dispersed starting points; discard **burn-in**.

## Predictive distributions and model checking
**Posterior predictive:** $p(\tilde y\mid y)=\int p(\tilde y\mid\theta)p(\theta\mid y)\,d\theta$. Simulate by drawing $\theta^{(m)}$ from the posterior and then $\tilde y^{(m)}\sim p(\cdot\mid\theta^{(m)})$. A **posterior predictive p-value** for a statistic $T$ is $P\big(T(\tilde y)\ge T(y)\mid y\big)$; values near 0 or 1 indicate the model fails to reproduce that feature (not that the model is "false").
For Beta–Binomial the posterior predictive for one new trial is $P(\tilde y=1\mid x)=\dfrac{\alpha+x}{\alpha+\beta+n}$.

## Model comparison (briefly)
**Bayes factor** $\text{BF}_{12}=\dfrac{p(y\mid M_1)}{p(y\mid M_2)}$ (ratio of marginal likelihoods); it depends strongly on the priors within each model and is undefined for improper priors. Alternatives that are less prior-sensitive and aimed at prediction: **WAIC** and **leave-one-out cross-validation (LOO)**, available in ArviZ.

## Check your understanding
1. Prior Beta(2,3) has what mean? After 7 successes in 10 trials, what is the posterior and its mean? ($0.4$; Beta(9,6), mean $0.6$)
2. Flat prior, 7 successes in 10: posterior? Mean? ($\text{Beta}(8,4)$; $0.667$; $P(p>0.5)\approx0.887$)
3. Normal prior $N(0,1)$, $\bar x=2$, $\sigma=1$, $n=4$: posterior mean and sd? ($1.6$; $0.447$)
4. A Metropolis proposal has posterior ratio $0.25$. With what probability is it accepted? ($0.25$)
5. Four chains have $\hat R=1.4$. What do you do? (Don't trust the draws: run longer, check trace plots, reparametrise or tune the proposal)
6. Which is correct for a 95% credible interval (0.11, 0.26): "95% probability the parameter is in it (given model and prior)", or "95% of repeated studies' intervals would contain it"? (The first; the second describes a confidence interval)
