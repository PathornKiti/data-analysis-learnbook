# Choosing a hypothesis test

## Step 1: three questions
1. **What is the outcome?** numeric (continuous) · ordinal/skewed · binary (yes/no) · categorical (several classes) · count
2. **How many groups or conditions?** one sample vs a value · two · three or more · a relationship between two variables
3. **Independent or paired?** different people in each group (independent), or the same people measured twice / matched pairs (paired)

Then find your row. Always report an **estimate with an interval and an effect size**, not just a p-value.

## Step 2: the table

| design | outcome | default test | robust / non-parametric alternative | effect size | key assumptions |
|---|---|---|---|---|---|
| one sample vs a value | numeric | one-sample $t$ | Wilcoxon signed-rank (vs the value) | $d=(\bar x-\mu_0)/s$ | roughly normal or $n\gtrsim30$ |
| two independent groups | numeric | **Welch $t$** | **Mann–Whitney $U$**; permutation test; $t$ on log data | $d$ / Hedges' $g$; mean difference + CI; probability of superiority | independence; no extreme outliers |
| two paired conditions | numeric | **paired $t$** | Wilcoxon signed-rank; permutation of signs | $d_z$; mean change + CI | independent pairs; differences roughly normal |
| three+ independent groups | numeric | one-way ANOVA (Welch ANOVA if spreads differ) + Tukey/Holm | Kruskal–Wallis (+ Dunn post hoc) | $\eta^2$ / $\omega^2$ | independence; similar spreads; roughly normal residuals |
| groups + a baseline measurement | numeric | **ANCOVA** (`post ~ pre + group`) or gain-score ANOVA | rank-based ANCOVA, bootstrap | adjusted difference + CI | linear baseline–outcome relation, same slope per group |
| repeated measures, 3+ times | numeric | repeated-measures ANOVA / mixed model | Friedman | partial $\eta^2$ | sphericity (or use a mixed model) |
| repeated or clustered measurements, uneven or missing waves | numeric | **linear mixed model** (random intercept, optionally slope) *(X1)* | cluster-robust SEs; per-unit summary measure (slope) then $t$ | group × time coefficient + CI; **ICC**, design effect | correct mean model; residuals and random effects roughly normal; enough clusters (≳20-30) |
| time until an event, with censoring | time-to-event | **Kaplan–Meier + log-rank**; **Cox model** (`PHReg`) *(X2)* | stratified log-rank; restricted mean survival time (RMST) difference | median survival, hazard ratio + CI, RMST | censoring unrelated to the outcome; proportional hazards (for Cox) |
| belief about a parameter, small $n$, prior information | any | **Bayesian posterior** (conjugate, grid, Metropolis) *(X3)* | – | posterior mean/median, credible interval, $P(\text{effect}>\delta)$ | stated prior (with sensitivity analysis); model checked; MCMC diagnostics (R-hat, ESS) |
| outcome recorded in time order | numeric | OLS with **HAC standard errors** or **AR errors** *(X4)* | difference the series; chronological validation | coefficient + HAC CI; MAE / MASE of forecasts | no leftover autocorrelation (Durbin–Watson, ACF); stationary residuals |
| one proportion vs a value | binary | exact binomial test | – | $\hat p$ with Wilson CI | independent trials |
| two independent proportions | binary | two-proportion $z$ / $\chi^2$ | **Fisher exact** (small counts) | difference, risk ratio, **odds ratio** + CI | expected counts $\ge5$ for $z$/$\chi^2$ |
| two paired proportions | binary | McNemar test | exact McNemar | odds ratio of discordant pairs | paired binary outcomes |
| two categorical variables | categorical | $\chi^2$ test of independence | Fisher–Freeman–Halton / simulation | Cramér's $V$ | expected counts $\ge5$ |
| one categorical vs expected shares | categorical/counts | $\chi^2$ goodness-of-fit | exact multinomial | $w$ / Cramér's $V$ | expected counts $\ge5$; df $=k-1-\#\text{params}$ |
| association of two numeric variables | numeric | Pearson $r$ (+ Fisher-$z$ CI) | Spearman $\rho$, Kendall $\tau$ | $r$, $\rho$, $\tau$ | linearity (Pearson) / monotonic (Spearman) |
| outcome ~ several predictors | numeric | linear regression (`smf.ols`) | robust regression, bootstrap CIs | $R^2$, standardised $\beta$ | linearity, independence, constant variance, residuals roughly normal |
| binary outcome ~ predictors | binary | logistic regression (`smf.logit`) | exact/penalised logistic | odds ratios + CI | independence; enough events per predictor |
| count outcome ~ predictors | counts | Poisson / negative-binomial regression | – | rate ratios | mean≈variance (Poisson) or overdispersion (NB) |
| "no meaningful difference" | numeric | **TOST** equivalence | – | margin $\pm\Delta$ chosen in advance | as for the $t$-tests |

## Step 3: code (SciPy / statsmodels)

```python
from scipy import stats
import statsmodels.formula.api as smf
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.oneway import anova_oneway
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from statsmodels.stats.weightstats import ttost_ind

stats.ttest_1samp(x, mu0)                              # one-sample t
stats.ttest_ind(a, b, equal_var=False)                 # Welch t  (result.confidence_interval() gives the CI)
stats.ttest_rel(after, before)                         # paired t
stats.mannwhitneyu(a, b, alternative="two-sided")      # Mann-Whitney U (effect size: U / (n1*n2))
stats.wilcoxon(after - before)                         # Wilcoxon signed-rank
stats.f_oneway(*groups)                                # one-way ANOVA
anova_oneway(values, groups, use_var="unequal")        # Welch ANOVA
pairwise_tukeyhsd(values, groups)                      # Tukey HSD post hoc
stats.kruskal(*groups)                                 # Kruskal-Wallis
smf.ols("post ~ pre + C(group)", data=df).fit()        # ANCOVA

stats.binomtest(k, n, p0)                              # exact binomial (.proportion_ci(method="wilson"))
proportions_ztest([x1, x2], [n1, n2])                  # two-proportion z
stats.chi2_contingency(table)                          # chi-square independence (returns chi2, p, dof, expected)
stats.fisher_exact(table_2x2)                          # Fisher exact (odds ratio, p)
stats.chisquare(observed, expected, ddof=n_params)     # goodness of fit

stats.pearsonr(x, y); stats.spearmanr(x, y); stats.kendalltau(x, y)

stats.shapiro(x); stats.levene(*groups); stats.kstest(x, dist.cdf)   # assumption checks (use with plots!)
multipletests(pvals, method="holm")                    # also "bonferroni", "fdr_bh"
smf.mixedlm("score ~ wave * group", df, groups=df["id"], re_formula="~wave").fit()   # mixed model (X1)
PHReg.from_formula("time ~ basic + spend", df, status=df["event"].to_numpy()).fit()    # Cox model (X2)
sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": 6})                              # HAC standard errors (X4)
ttost_ind(a, b, -margin, margin)                       # equivalence
TTestIndPower().solve_power(effect_size=0.5, power=0.8, alpha=0.05)  # sample size per group
stats.permutation_test((a, b), statistic, ...)         # permutation test for any statistic
stats.bootstrap((x,), np.mean)                         # bootstrap CI for any statistic
```

## Step 4: checks before you trust the result
- [ ] **Independence**: are observations really independent (no repeated measures, clusters, time series)? If not, use paired tests, mixed models or cluster-robust errors (Module X1) or time-series methods (Module X4).
- [ ] **Plot the data**: histogram/ECDF/Q-Q per group; look for outliers, skew, ties, floor/ceiling effects.
- [ ] **Sample size** per group and **power**: can this study detect the effect you care about? (Report the minimum detectable effect.)
- [ ] **Sensitivity analysis**: does a second reasonable method (Welch ↔ Mann–Whitney ↔ permutation ↔ log transform) give the same conclusion?
- [ ] **Multiplicity**: how many tests? Which are primary (pre-specified) and which exploratory? Adjust (Holm/BH) where needed.
- [ ] **One- vs two-sided**: two-sided unless one direction was justified *before* seeing data.

## Common mistakes
| mistake | fix |
|---|---|
| independent test on paired data (or the reverse) | match the test to the design; pairing is a *design* fact, not a choice after the fact |
| many $t$-tests instead of ANOVA + post hoc | one omnibus test, then corrected pairwise comparisons |
| "not significant ⇒ no effect" | report the CI; for "no difference" use equivalence (TOST) |
| ignoring the baseline in a before/after trial | ANCOVA or gain-score analysis |
| $\chi^2$ with expected counts $<5$ | Fisher exact or merge categories |
| choosing the test after seeing which gives $p<0.05$ | decide in advance; report all that you ran |
| reporting p-values only | add estimate, interval, effect size, $n$ |
