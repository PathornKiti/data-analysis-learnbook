# Math notes: Module X1 (repeated measures and mixed models)

## Variance components and the ICC
For measurement $j$ on unit $i$: $y_{ij}=\mu+u_i+\varepsilon_{ij}$ with $u_i\sim(0,\sigma_u^2)$ (between-unit) and $\varepsilon_{ij}\sim(0,\sigma^2)$ (within-unit), independent.
$\operatorname{Var}(y_{ij})=\sigma_u^2+\sigma^2$, $\operatorname{Cov}(y_{ij},y_{ij'})=\sigma_u^2$ for $j\ne j'$, so
$$\text{ICC}=\rho=\operatorname{Corr}(y_{ij},y_{ij'})=\frac{\sigma_u^2}{\sigma_u^2+\sigma^2}.$$

**ANOVA estimators (balanced: $n$ units, $k$ measurements each).** $E[\text{MSW}]=\sigma^2$ and $E[\text{MSB}]=\sigma^2+k\sigma_u^2$, so
$$\hat\sigma^2=\text{MSW},\quad\hat\sigma_u^2=\frac{\text{MSB}-\text{MSW}}{k},\quad\widehat{\text{ICC}}=\frac{\text{MSB}-\text{MSW}}{\text{MSB}+(k-1)\text{MSW}}.$$
(The estimate can be negative in small samples; truncate at 0.)

## Design effect
The variance of the mean of $n$ clusters of size $m$ is $\dfrac{\sigma_u^2+\sigma^2/m}{n}$, which is $1+(m-1)\rho$ times the variance under independence:
$$\text{DEFF}=1+(m-1)\rho,\qquad n_{\text{eff}}=\frac{nm}{\text{DEFF}}.$$
With $\rho=0.5$, $m=4$, $n=100$ clusters: $\text{DEFF}=2.5$ and $400/2.5=160$ effective observations. As $m$ grows, $n_{\text{eff}}\to n/\rho$: **more measurements per unit cannot beat having more units.**

## The linear mixed model
$$\mathbf y_i=X_i\beta+Z_i\mathbf u_i+\boldsymbol\varepsilon_i,\qquad\mathbf u_i\sim N(0,G),\quad\boldsymbol\varepsilon_i\sim N(0,\sigma^2I).$$
Marginally $\mathbf y_i\sim N(X_i\beta,\;V_i)$ with $V_i=Z_iGZ_i^\top+\sigma^2I$. For a random intercept and slope in time $t$: $Z_i=[\mathbf 1,\ \mathbf t_i]$ and $G=\begin{pmatrix}\sigma_0^2&\sigma_{01}\\\sigma_{01}&\sigma_1^2\end{pmatrix}$.

**Fixed effects** (generalised least squares, given $V$): $\hat\beta=\Big(\sum X_i^\top V_i^{-1}X_i\Big)^{-1}\sum X_i^\top V_i^{-1}\mathbf y_i$, with $\operatorname{Cov}(\hat\beta)=\Big(\sum X_i^\top V_i^{-1}X_i\Big)^{-1}$.
Units with more data and smaller $V_i$ get more weight: this is why the mixed model uses unbalanced data efficiently.

**Estimating the variance components.** Maximum likelihood (ML) maximises the likelihood of $\mathbf y$; its variance estimates are biased downward. **REML** maximises the likelihood of residual contrasts (accounting for the estimated $\beta$) and gives less biased variance components. Use **REML** for the final model and for comparing random-effects structures *within the same fixed effects*; use **ML** to compare models with *different fixed effects* (likelihood-ratio tests, AIC). Tests of a variance component being 0 lie on the boundary of the parameter space, so the usual $\chi^2$ reference is conservative.

**Random effects (BLUPs).** For a random intercept model, the predicted deviation of unit $i$ is a **shrunken** version of its raw deviation:
$$\hat u_i=\lambda_i\,(\bar y_i-\bar x_i^\top\hat\beta),\qquad\lambda_i=\frac{\sigma_u^2}{\sigma_u^2+\sigma^2/m_i}.$$
With $\sigma_u^2=64$, $\sigma^2=16$, $m_i=4$: $\lambda=64/68\approx0.94$. Units with few measurements (small $m_i$) or noisy data are pulled more strongly toward the overall mean.

**Conditional vs marginal interpretation.** $\beta$ in a *linear* mixed model has both a subject-specific and a population-average meaning. In *generalised* mixed models (logistic, Poisson) they differ, and GEE estimates the population-average one.

## Cluster-robust ("sandwich") standard errors
OLS point estimates are kept; the covariance is $\widehat{\operatorname{Cov}}(\hat\beta)=(X^\top X)^{-1}\Big(\sum_{g}X_g^\top\hat{\mathbf e}_g\hat{\mathbf e}_g^\top X_g\Big)(X^\top X)^{-1}$ (with small-sample corrections). It is consistent as the **number of clusters** grows, but unreliable with few clusters (say < 30), and it does not model the correlation, so it is less efficient than a correct mixed model.

## Repeated-measures ANOVA and sphericity
Repeated-measures ANOVA assumes **sphericity**: equal variances of all pairwise differences between time points. Violations inflate $F$; Greenhouse–Geisser or Huynh–Feldt corrections adjust the degrees of freedom. Mixed models (or multivariate approaches) avoid this assumption by modelling the covariance directly, and handle missing waves.

## Missing data mechanisms
* **MCAR** (completely at random): missingness unrelated to any data. Complete-case analysis is unbiased (but inefficient).
* **MAR** (at random): missingness depends only on *observed* data. Likelihood-based analyses (mixed models) are valid.
* **MNAR** (not at random): missingness depends on the unobserved value itself. No standard analysis is safe; use sensitivity analyses or joint models.

## Check your understanding
1. $\sigma_u^2=64$, $\sigma^2=16$. What is the ICC? ($64/80=0.8$)
2. $\rho=0.5$, $m=4$: DEFF and the effective size of 400 observations? ($1+3\times0.5=2.5$; $160$)
3. You have 8 hospitals with 200 patients each. Is a cluster-robust SE trustworthy? (Doubtful: only 8 clusters; prefer a mixed model or report cautiously)
4. Why compare fixed-effect structures with ML, not REML? (REML likelihoods are only comparable between models with the same fixed effects)
5. Students with only 2 of 5 measurements: are their random intercepts shrunk more or less than those with 5? (More: $\lambda_i$ is smaller when $m_i$ is small)
