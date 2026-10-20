# Glossary

Short definitions with the module where each idea is taught. (Terms are alphabetical.)

| term | meaning | module |
|---|---|---|
| **A/B test** | A randomised experiment comparing two versions (A and B) to see which performs better | 8 |
| **adjusted R²** | R² penalised for the number of predictors; unlike R², it can fall when a useless variable is added | 9 |
| **AIC** | Akaike information criterion, $2k-2\ell$: compares fitted models, penalising the number of parameters $k$ (lower is better) | 7b |
| **ANCOVA** | Analysis of covariance: regress the outcome on group *and* a baseline measurement to get baseline-adjusted group effects with smaller residual variance | 8b |
| **ANOVA** | Analysis of variance: tests whether any of 3+ group means differ using $F=\text{MSB}/\text{MSW}$ | 8b |
| **AR(1) model** | Autoregressive model of order 1: $x_t-\mu=\phi(x_{t-1}-\mu)+\varepsilon_t$; fitted by regressing $x_t$ on $x_{t-1}$ | X4 |
| **AUC** | Area under the ROC curve; the chance that a random positive is scored higher than a random negative (0.5 = chance, 1 = perfect) | 10 |
| **augmented Dickey–Fuller (ADF) test** | Tests the null hypothesis of a unit root (non-stationarity); a small p-value suggests the series is stationary | X4 |
| **autocorrelation (ACF)** | Correlation of a series with itself $k$ steps earlier; when it is non-zero the observations are not independent | X4 |
| **baseline** | The simplest sensible prediction (e.g. the mean, or the majority class) that a model must beat | 10 |
| **base rate** | How common something is overall; ignoring it leads to the base-rate fallacy | 7 |
| **Bayes' theorem** | $P(A\mid B)=P(B\mid A)P(A)/P(B)$; updates a prior probability with evidence | 7 |
| **bias (model)** | Systematic error from a model too simple to capture the truth (underfitting) | 10 |
| **bootstrap** | Estimating uncertainty by resampling the data with replacement many times | 8 |
| **Box–Cox transformation** | A family $\frac{x^\lambda-1}{\lambda}$ ($\ln x$ at $\lambda=0$) whose $\lambda$ is chosen to make positive, skewed data more normal | 7b |
| **box plot** | Median, quartiles, whiskers (the most extreme points inside the 1.5×IQR fences) and outliers drawn as points | 6, 9b |
| **broadcasting** | NumPy's rule for combining arrays of different shapes (e.g. subtracting a column mean from every row) | 3 |
| **burn-in** | Initial MCMC draws, taken before the chain has reached its target distribution, that are discarded | X3 |
| **categorical variable** | A variable whose values are categories (major, city), not quantities | 4 |
| **censoring** | The event has not happened by the end of observation, so we only know the time is longer than what was seen (right-censoring) | X2 |
| **central limit theorem** | Means of many independent samples are approximately normal, with sd σ/√n | 7 |
| **cluster-robust standard errors** | Standard errors that allow arbitrary correlation among rows of the same cluster (student, site, patient) | X1 |
| **Cohen's d** | A difference in means expressed in standard-deviation units (effect size) | 8 |
| **confidence band vs prediction band** | Around a fitted line: the confidence band covers the *mean* response; the wider prediction band covers a *new individual* | 9b |
| **confidence interval** | A range computed so that, over repeated studies, a stated share (e.g. 95%) of such intervals contain the true value | 8 |
| **confounder** | A third variable that influences both the predictor and the outcome, creating or hiding an association | 6 |
| **conjugate prior** | A prior whose posterior has the same distribution family, giving closed-form updates (Beta–Binomial, Gamma–Poisson, Normal–Normal) | X3 |
| **correlation (r)** | A number from −1 to 1 measuring *linear* association between two variables | 6 |
| **Cox proportional-hazards model** | Regression for time-to-event data in which covariates multiply the hazard by a constant factor over time; coefficients are log hazard ratios | X2 |
| **Cramér's V** | Effect size for a χ² test of two categorical variables, from 0 (none) to 1 (perfect) | 8b |
| **credible interval** | An interval containing the parameter with a stated posterior probability (e.g. 95%), given the data and the prior | X3 |
| **cross-validation** | Splitting data into k folds, training on k−1 and testing on the remaining one in turn, to estimate out-of-sample performance | 10 |
| **data card** | A short document describing a dataset's source, contents, limits and licence | 2 |
| **DataFrame** | pandas' table object; each column is a Series | 4 |
| **data leakage** | Information the model wouldn't have at prediction time sneaking into training, giving falsely good scores | 10 |
| **data validation** | Automatic checks that the real data satisfy expectations (ranges, types, uniqueness) | 11 |
| **decomposition (time series)** | Splitting a series into trend, seasonal and remainder components, e.g. by a centred moving average and monthly means | X4 |
| **derivative** | The instantaneous rate of change (slope of the tangent line) of a function | 9 |
| **design effect** | Factor by which clustering inflates the variance of an estimate, about $1+(m-1)\,\text{ICC}$ for clusters of size $m$ | X1 |
| **differencing** | Replacing a series by its changes $y_t-y_{t-1}$ to remove a trend or unit root | X4 |
| **distribution** | Which values a variable takes and how often | 6, 7 |
| **docstring** | A string right after `def` describing what a function does; shown by `help()` | 1, 11 |
| **Durbin–Watson statistic** | Residual statistic $\approx2(1-r_1)$ for lag-1 autocorrelation: near 2 means none, near 0 strong positive | X4 |
| **ECDF** | Empirical CDF: the proportion of observations ≤ x, drawn as a step function; needs no binning | 9b |
| **EDA** | Exploratory data analysis: looking at data numerically and visually before modelling | 6 |
| **effective sample size** | How many independent observations a correlated sample is worth, e.g. $n(1-\phi)/(1+\phi)$ for an AR(1) series or for MCMC draws | X3, X4 |
| **effect size** | How big a difference or relationship is, as opposed to whether it's statistically detectable | 8 |
| **equivalence test (TOST)** | Two one-sided tests that show a difference lies inside a pre-set margin ±Δ, so "no meaningful difference" can be claimed | 8b |
| **EWMA** | Exponentially weighted moving average, $s_t=\alpha y_t+(1-\alpha)s_{t-1}$: recent values weigh most | 9b |
| **expected value** | The long-run average of a random variable, weighting each value by its probability | 7 |
| **feature** | An input variable used by a model (a predictor) | 9, 10 |
| **Fisher's exact test** | Exact test of association in a (usually 2×2) table with small counts, based on the hypergeometric distribution | 8b |
| **forest plot** | Estimates with confidence intervals for several effects drawn on one scale, with a reference line at no effect | 8b |
| **gradient descent** | Minimising a loss by repeatedly stepping opposite to its gradient | 9 |
| **HAC (Newey–West) standard errors** | Standard errors for regression that allow heteroskedasticity and autocorrelation up to a chosen lag | X4 |
| **hazard / hazard ratio** | The instantaneous event rate among those still at risk; a hazard ratio compares the rates of two groups | X2 |
| **hyperparameter** | A setting chosen by you, not learned from the data (e.g. ridge's α, tree depth) | 10 |
| **hypothesis test** | A procedure asking whether data are plausible under a null hypothesis | 8 |
| **intraclass correlation (ICC)** | Share of the total variance that lies between clusters (or subjects): $\sigma_u^2/(\sigma_u^2+\sigma^2)$ | X1 |
| **IQR** | Interquartile range, Q3 − Q1; the spread of the middle 50% | 4, 5 |
| **Kaplan–Meier estimator** | Non-parametric estimate of the survival function that handles censored observations | X2 |
| **kernel density estimate (KDE)** | A smooth density: an average of small bumps centred on each data point; the bandwidth controls smoothness | 9b |
| **Kolmogorov–Smirnov test** | Compares an empirical CDF with a model CDF (or two samples) using the largest vertical gap D | 7b, 9b |
| **Kruskal–Wallis test** | Rank-based alternative to one-way ANOVA for 3+ independent groups | 8b |
| **kurtosis** | Tail heaviness relative to a normal curve (excess kurtosis 0); positive means more extreme values | 7b |
| **learning rate** | The step size in gradient descent | 9 |
| **least squares** | Choosing model parameters that minimise the sum of squared residuals | 9 |
| **logistic regression** | A model for yes/no outcomes where the log-odds are linear in the predictors | 10 |
| **lognormal distribution** | $\ln X$ is normal; positive and right-skewed with mean > median; arises from products of many small effects | 7b |
| **log-rank test** | Compares survival curves of two or more groups by comparing observed with expected events at each event time | X2 |
| **loss function** | A measure of how bad predictions are; training minimises its average | 9, 10 |
| **Mann–Whitney U test** | Rank-sum test comparing two independent groups; effect size = probability of superiority $U/(n_1n_2)$ | 8b |
| **MASE** | Mean absolute scaled error: forecast MAE divided by the training MAE of a seasonal-naive forecast; below 1 beats that benchmark | X4 |
| **maximum likelihood estimate (MLE)** | The parameter value that makes the observed data most probable (maximises the log-likelihood) | 7b |
| **MCMC (Metropolis)** | Markov chain Monte Carlo: draws a correlated sample from a posterior by random proposals accepted with probability $\min(1,\text{ratio})$ | X3 |
| **mean / median** | Average / middle value; the median resists outliers | 4 |
| **mixed-effects model** | Regression with fixed effects (population-level) and random effects (subject- or cluster-level deviations), for repeated or clustered data | X1 |
| **mixture distribution** | A weighted combination of distributions, often shown by a bimodal histogram; indicates mixed subpopulations | 7b |
| **module (Python)** | A `.py` file you can import; a *package* is a folder of modules with `__init__.py` | 6.5 |
| **multiple comparisons** | Running many tests inflates the chance of false positives; adjust (e.g. Bonferroni) or pre-specify | 8 |
| **normal distribution** | The bell curve, described by mean μ and standard deviation σ | 7 |
| **null hypothesis** | The "no effect / no difference" assumption a test tries to find evidence against | 8 |
| **odds ratio / risk ratio** | Ratios of the odds (or probabilities) of an outcome between two groups; 1 means no association | 8b |
| **outlier** | A value far from the rest; may be an error or a genuine extreme | 5 |
| **overfitting** | A model that fits noise in the training data and generalises poorly | 9, 10 |
| **paired design** | The same units measured twice (or matched pairs); analysed through within-pair differences | 8b |
| **permutation test** | A test that shuffles labels to see what differences arise by chance alone | 8 |
| **pipeline (sklearn)** | Chains preprocessing and a model so every step is learned from training data only | 10 |
| **Poisson distribution** | Counts of independent events per interval at a constant rate λ; mean = variance = λ | 7, 7b |
| **population / sample** | Everything you want to describe / the part you observed | 7, 8 |
| **posterior predictive check** | Simulating new data from the fitted Bayesian model and comparing them with the real data to find what the model misses | X3 |
| **power** | The probability a test detects a real effect of a given size | 8 |
| **precision / recall** | Of the cases flagged positive, the share that are right / of all real positives, the share found | 10 |
| **prior / posterior** | Belief about a parameter before and after seeing data; posterior $\propto$ likelihood × prior | X3 |
| **probability of superiority** | The chance that a random member of group A exceeds a random member of group B (0.5 = no difference) | 8b |
| **p-value** | The probability, assuming the null hypothesis is true, of a result at least as extreme as observed. *Not* the probability the null is true | 8 |
| **Q-Q plot** | Sorted data against a model's quantiles; points on a straight line mean a good fit | 7b |
| **quantile / percentile** | The value below which a given share of the data falls | 4 |
| **R²** | Share of the variance in the outcome explained by the model, compared with predicting the mean | 9 |
| **random effect** | A subject- or cluster-specific deviation treated as drawn from a distribution (e.g. a random intercept) | X1 |
| **random seed** | A number that makes random draws repeatable | 3, 7 |
| **regularisation** | Penalising large coefficients to reduce overfitting (ridge, lasso) | 10 |
| **reproducibility** | Anyone can rerun your analysis and get the same results | 6.5, 11 |
| **residual** | Observed minus predicted value | 9 |
| **R-hat** | MCMC convergence diagnostic comparing variation between and within chains; values near 1 (below about 1.01) are good | X3 |
| **ROC curve** | True-positive rate vs false-positive rate across all classification thresholds | 10 |
| **sampling variation** | Differences between samples drawn from the same population purely by chance | 8 |
| **seasonality** | A pattern that repeats at a fixed period (e.g. every 12 months) | X4 |
| **Shapiro–Wilk test** | A powerful test of normality (null: the data are normal); sensitive to sample size | 7b |
| **Simpson's paradox** | A trend in pooled data that reverses within every subgroup | 6 |
| **skew** | Asymmetry of a distribution; right-skewed means a long tail of large values | 4, 6 |
| **spurious regression** | A seemingly significant relationship between unrelated trending or random-walk series; avoid by differencing or modelling the trend | X4 |
| **standard deviation / variance** | A measure of spread; variance is its square | 4 |
| **standard error** | The standard deviation of a statistic across repeated samples (σ/√n for the mean) | 8 |
| **stationarity** | Mean, variance and autocorrelations that do not change over time | X4 |
| **statistical vs practical significance** | A result can be detectable (small p) yet too small to matter; report effect sizes | 8 |
| **survival function** | $S(t)=P(T>t)$: the probability of still being event-free at time $t$ | X2 |
| **test set** | Data kept aside, untouched until final evaluation, to estimate real-world performance | 10 |
| **type I / type II error** | False positive (reject a true null) / false negative (miss a real effect) | 8 |
| **vectorisation** | Operating on whole arrays at once instead of looping | 3 |
| **virtual environment** | An isolated set of installed packages for one project | 0 |
| **Welch's t-test** | Two-sample t-test that does not assume equal variances; the default for two independent means | 8, 8b |
| **Wilson interval** | Confidence interval for a proportion that behaves well for small n and extreme proportions | 8b, 9b |
| **z-score** | $(x-\bar{x})/s$: how many standard deviations a value is from the mean | 3 |
