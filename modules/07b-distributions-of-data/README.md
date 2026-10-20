# Module 7b: Distributions of data

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 6 and 7 · **Needed for:** choosing and justifying the tests in Module 8b, and for any thesis methods section

## Learning goals
* Describe a distribution with **skewness, kurtosis**, centre and spread, and know what each number is (and isn't) telling you
* Match a variable to a distribution from its **data-generating story** (binomial, Poisson, uniform, normal, lognormal, exponential, gamma, beta)
* Fit distributions by **maximum likelihood** and compare candidates with **AIC**
* **Check fit**: Q-Q plots, Kolmogorov–Smirnov, Shapiro–Wilk, chi-square goodness-of-fit, and understand how sample size changes what tests flag
* Use **transformations** (log, square root, Box–Cox) and report log-scale results as **ratios**
* Understand $t$, $\chi^2$ and $F$ as distributions of *statistics*
* Recognise **mixtures** (bimodality) and treat subgroups appropriately

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | shape numbers → catalogue → Poisson/exponential link → MLE & AIC → Q-Q, KS, Shapiro, χ² → transformations → t/χ²/F → mixtures |
| `exercises.ipynb` | 10 exercises (skewness, MLE, AIC, Q-Q coordinates, KS by hand, Poisson goodness-of-fit, ratio CIs on the log scale, probabilities, mixtures, identify the distribution) |
| `math-notes.md` | moments, catalogue formulas, MLE derivations, AIC/BIC, KS, χ², Box–Cox, lognormal facts |
| [`../../solutions/07b-distributions-of-data/`](../../solutions/07b-distributions-of-data/) | solutions |
| [`../../reference/distributions-cheatsheet.md`](../../reference/distributions-cheatsheet.md) | one-page reference |
| [`../../data/service_desk.csv`](../../data/service_desk.csv) | practice data: counts, a right-skewed time, a left-skewed score, a bimodal length |

## Common pitfalls
* Treating a "non-significant" normality test as proof of normality (small samples can't detect anything), or a "significant" one as a disaster (large samples flag trivial departures)
* Reading **KS p-values** after estimating parameters from the same data (they're too generous)
* Fitting a normal to a strictly positive, right-skewed variable (it predicts impossible negative values)
* Averaging two populations (a bimodal variable) and reporting one mean
* Forgetting that a log-transformed analysis estimates **geometric means and ratios**, not arithmetic differences
* Choosing a distribution because it fits the sample, when its *story* contradicts how the data arise
* Applying Poisson to overdispersed counts (variance ≫ mean)

## 🎯 Project checkpoint: **a distribution profile of your key variables**
In your project, create `notebooks/01b_distributions.ipynb` and add functions to `src/<package>/distributions.py` (the template has `shape_summary`, `fit_candidates` and `qq_points` to start from).
1. For each **numeric variable** that matters, produce a **shape table**: n, % missing, mean, median, sd, skewness, excess kurtosis, min, max.
2. For each, show a **histogram + KDE** and a **Q-Q plot** (with the reference line) and write one sentence describing the shape.
3. For the 2–3 most important variables, **fit candidate distributions** and compare with AIC; state which story matches your data-generating process.
4. Decide, with reasons, what you will do about skewed or non-normal variables (transform, use a distribution-free method, or leave as is because the method is robust). Write it down **before** running your main tests.
5. Check for **bimodality/mixtures** and for **overdispersion** if you have counts.
6. Add the finding to your methods section in the style of Module 7b §10: *what you checked, how, and what you did about it.*

## Further reading
* *Statistical Inference* (Casella & Berger), chapters on common families and likelihood (a standard thesis-level reference)
* `scipy.stats` [distribution documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
* *All of Statistics* (Wasserman), chapters 2–3 and 9
