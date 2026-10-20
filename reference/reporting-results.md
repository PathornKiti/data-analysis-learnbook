# Reporting results: sentence templates

**Principles:** state the **question/comparison**, the **estimate in original units**, its **95% interval**, the **test statistic with degrees of freedom and p-value**, an **effect size**, and the **sample size**.
Round sensibly (2–3 significant figures); give exact p-values to three decimals (`p = .026`) or `p < .001`; never write `p = .000`. Name the test. Use plain language for the conclusion and hedge in proportion to the evidence.
(The examples use numbers from the course's `app_trial.csv`. Replace them with your own.)

## Descriptives and distributions
> Response times were strongly right-skewed (skewness = 2.09, excess kurtosis = 6.87; Shapiro–Wilk *p* < .001), so they were analysed on the log scale, where the distribution was approximately normal (skewness = −0.06; *p* = .58; see Figure 2).
> A lognormal model fitted better than gamma, exponential or normal models (AIC = 2,820, 2,842, 3,085 and 3,061, respectively).

## One-sample *t*-test
> Mean exam score (*M* = 67.9, *SD* = 10.5, *n* = 200) was higher than the benchmark of 65, *t*(199) = 3.95, *p* < .001, mean difference = 2.9 points, 95% CI [1.5, 4.4], *d* = 0.28.

## Two independent groups (Welch)
> Gamified users scored 3.7 points higher than control users (95% CI [0.4, 7.0]), Welch *t*(195.9) = 2.24, *p* = .026, Cohen's *d* = 0.32 (*n* = 100 per group).

## Paired *t*-test
> Tutorial users improved by 4.9 points from pre- to post-test (95% CI [3.6, 6.1]), paired *t*(99) = 7.59, *p* < .001, *d*<sub>z</sub> = 0.76. The Wilcoxon signed-rank test agreed (*p* < .001).

## Mann–Whitney *U*
> Gamified users spent more time in the app than control users (*U* = 6,231, *p* = .003; probability of superiority = .62: a randomly chosen gamified user was more active than a randomly chosen control user 62% of the time).
> Medians were about 30 and 22 minutes (IQR 15.8–48.7 and 12.0–31.8) for gamified and control. *(Report medians only if distribution shapes are similar; otherwise describe the distributions.)*

## One-way ANOVA and post hoc tests
> The three onboarding groups did not differ significantly in post-test score, *F*(2, 297) = 2.48, *p* = .085, η² = .016. Tukey-adjusted pairwise differences were all non-significant (smallest: gamified – control = 3.7 points, 95% CI [−0.2, 7.7], adjusted *p* = .068).

## ANCOVA (baseline-adjusted)
> Adjusting for pre-test score, gamified onboarding increased post-test scores by 4.4 points relative to control (95% CI [2.7, 6.1], *p* < .001) and tutorial onboarding by 2.4 points (95% CI [0.8, 4.1], *p* = .004). Pre-test score was a strong covariate (*b* = 1.01, residual *SD* = 6.0).

## Proportions
> Conversion was 33% in the gamified group (33/100; Wilson 95% CI [25%, 43%]) and 17% in control (17/100). The difference was 16 percentage points (95% CI [4, 28]), *z* = 2.61, *p* = .009; the odds ratio was 2.40 and the risk ratio 1.94.

## Chi-square test of independence
> Device type was not associated with group, χ²(4, *N* = 300) = 1.83, *p* = .77, Cramér's *V* = .06; all expected counts exceeded 5.
> *For small tables:* Fisher's exact test, odds ratio = 0.05, *p* = .020.

## Correlation
> Pre- and post-test scores were strongly correlated, *r*(298) = .85, 95% CI [.82, .88], *p* < .001 (Spearman ρ = .84).

## Equivalence (TOST)
> Baseline scores in the gamified and control groups were statistically equivalent within ±5 points (mean difference = −0.7; TOST *p* = .001), which supports the success of randomisation. The ±5-point margin was chosen in advance as the smallest difference of practical importance.

## Power and sample size (methods section)
> A sample of 64 participants per group gives 80% power to detect a standardised difference of *d* = 0.5 (two-sided α = .05, independent *t*-test; G*Power-equivalent calculation in `statsmodels`). With the available 100 per group, the minimum detectable effect at 80% power is *d* = 0.40.

## Multiple comparisons
> Two treatment-versus-control contrasts were pre-specified; *p*-values are Holm-adjusted. Secondary outcomes (time in app, conversion, rating) are exploratory and reported without adjustment, so should be interpreted cautiously.

## Assumptions and sensitivity
> Normality of residuals was assessed with Q-Q plots, and equality of variances with the ratio of group standard deviations (Levene's test *p* = .30). Because time-in-app was right-skewed, the primary analysis used log-transformed values; a Mann–Whitney test gave the same conclusion.

## Regression coefficients
> Holding sleep, attendance and job status constant, each additional weekly study hour was associated with a 1.58-point higher exam score (95% CI [1.42, 1.75], *p* < .001). The model explained 69% of the variance (adjusted *R*² = .685; residual *SD* = 5.9 points).

## Model evaluation (prediction)
> On the held-out final 60 days, the linear model's RMSE was 106 rides, compared with 630 for the predict-the-mean baseline; expanding-window cross-validation gave an RMSE of 117 ± 8.

## Figure and table captions
> **Figure 3.** Post-test score by onboarding group (*n* = 100 per group). Points are group means; error bars are 95% confidence intervals (*t*-based). Source: randomised trial, 2024.
> **Table 2.** Baseline-adjusted treatment effects (ANCOVA). Estimates are differences in points relative to control with 95% CIs; *p*-values are Holm-adjusted.

## Words to use carefully
| avoid | prefer |
|---|---|
| "proves", "confirms", "shows that X causes Y" (observational data) | "is associated with", "suggests", "is consistent with" |
| "significant" alone | "statistically significant at α = .05 (*p* = …); the estimated effect was …" |
| "no difference" (from *p* > .05) | "no statistically significant difference; the 95% CI [a, b] is compatible with effects from … to …" |
| "trend toward significance" | report the estimate and interval honestly |
| "the data were normal" | "no strong departures from normality were seen in Q-Q plots" |
