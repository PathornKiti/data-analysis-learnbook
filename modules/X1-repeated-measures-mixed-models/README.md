# Module X1 (extension): Repeated measures and mixed-effects models

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 8b and 9 (7b helps) · **Use it when:** your data have repeated measurements on the same units, or rows grouped in clusters (students in classes, patients in hospitals, sites, families)

## Learning goals
* Recognise **non-independent rows** and measure the dependence with the **ICC** and the **design effect**
* Explain how ignoring clustering distorts inference (false positives or lost power) and demonstrate it by simulation
* Choose between **paired tests, summary measures (per-unit slopes), cluster-robust standard errors and mixed models**
* Fit and interpret a **linear mixed-effects model** with random intercepts and slopes in `statsmodels`: fixed effects with intervals, variance components, interaction as the effect on the *rate of change*
* Choose the random-effects structure (AIC with ML), check residuals and random effects, handle **unbalanced data and missing waves**
* Report the model in thesis wording

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | spaghetti plots → ICC & design effect → the cost of ignoring clustering → summary slopes → mixed models → structure choice → checks → missing data → figure → decision table |
| `exercises.ipynb` | 8 exercises: ICC by hand, design effect, summary slopes, mixed model, naive vs cluster-robust SEs, AIC for random effects, missing waves, choose the analysis |
| `math-notes.md` | variance components, ICC, design effect, matrix form, GLS, REML vs ML, shrinkage (BLUPs), sandwich estimator, missing-data mechanisms |
| [`../../solutions/X1-repeated-measures-mixed-models/`](../../solutions/X1-repeated-measures-mixed-models/) | solutions |
| [`../../data/longitudinal_scores.csv`](../../data/longitudinal_scores.csv) | 80 students × up to 5 waves; two groups; 4.75% of rows missing |

## Common pitfalls
* Treating repeated measurements as independent observations ("n = 400" when you have 80 students)
* Calling a **pseudo-replicated** design "big": more measurements per unit don't add units
* Dropping every unit with a missing wave (repeated-measures ANOVA's habit) instead of using all rows under a missing-at-random assumption
* **Convergence warnings** when the random-effects structure is too complex for the data (few clusters, little variation): simplify (remove the random slope, remove correlations), standardise covariates, or report the simpler model with a note
* Comparing models with different *fixed* effects using REML (use ML), or reading p-values near a variance boundary as exact
* Too few clusters (say < 10–20) for the random-effects variance or cluster-robust SEs to be trustworthy
* Interpreting random-effect estimates (BLUPs) as the units' true values: they are shrunk toward the mean
* Forgetting that "missing at random" is an *assumption*; always discuss why units dropped out

## 🎯 Project checkpoint: **is your data clustered?**
1. List every way rows in your dataset could be **related**: the same person measured repeatedly, shared class/site/household, matched pairs, repeated locations. If none: write "rows are independent because…" in your methods.
2. If there is clustering, compute the **ICC** of your main outcome and the **design effect**, and state the effective sample size.
3. Choose your analysis from the decision table **before** fitting; implement it in `src/<package>/analysis.py` (e.g. a `fit_mixed(df, formula, groups)` function returning fixed effects with CIs and variance components) and add tests on a small simulated dataset with a known effect.
4. Run **one sensitivity analysis** (e.g. summary measures or cluster-robust OLS vs the mixed model) and report whether the conclusions agree.
5. Report with the template in the lesson: model, random effects, estimate + CI, n clusters and n observations, and the missing-data assumption.

## Further reading
* Gelman & Hill, *Data Analysis Using Regression and Multilevel/Hierarchical Models*
* Bates et al. (2015), "Fitting linear mixed-effects models using lme4" (explains the model and formula syntax used by most software)
* `statsmodels` [mixed linear models](https://www.statsmodels.org/stable/mixed_linear.html) documentation
