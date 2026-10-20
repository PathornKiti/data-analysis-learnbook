# Glossary

Short definitions with the module where each idea is taught. (Terms are alphabetical.)

| term | meaning | module |
|---|---|---|
| **A/B test** | A randomised experiment comparing two versions (A and B) to see which performs better | 8 |
| **adjusted R²** | R² penalised for the number of predictors; unlike R², it can fall when a useless variable is added | 9 |
| **AUC** | Area under the ROC curve; the chance that a random positive is scored higher than a random negative (0.5 = chance, 1 = perfect) | 10 |
| **baseline** | The simplest sensible prediction (e.g. the mean, or the majority class) that a model must beat | 10 |
| **base rate** | How common something is overall; ignoring it leads to the base-rate fallacy | 7 |
| **Bayes' theorem** | $P(A\mid B)=P(B\mid A)P(A)/P(B)$; updates a prior probability with evidence | 7 |
| **bias (model)** | Systematic error from a model too simple to capture the truth (underfitting) | 10 |
| **bootstrap** | Estimating uncertainty by resampling the data with replacement many times | 8 |
| **broadcasting** | NumPy's rule for combining arrays of different shapes (e.g. subtracting a column mean from every row) | 3 |
| **categorical variable** | A variable whose values are categories (major, city), not quantities | 4 |
| **central limit theorem** | Means of many independent samples are approximately normal, with sd σ/√n | 7 |
| **Cohen's d** | A difference in means expressed in standard-deviation units (effect size) | 8 |
| **confidence interval** | A range computed so that, over repeated studies, a stated share (e.g. 95%) of such intervals contain the true value | 8 |
| **confounder** | A third variable that influences both the predictor and the outcome, creating or hiding an association | 6 |
| **correlation (r)** | A number from −1 to 1 measuring *linear* association between two variables | 6 |
| **cross-validation** | Splitting data into k folds, training on k−1 and testing on the remaining one in turn, to estimate out-of-sample performance | 10 |
| **data card** | A short document describing a dataset's source, contents, limits and licence | 2 |
| **DataFrame** | pandas' table object; each column is a Series | 4 |
| **data leakage** | Information the model wouldn't have at prediction time sneaking into training, giving falsely good scores | 10 |
| **data validation** | Automatic checks that the real data satisfy expectations (ranges, types, uniqueness) | 11 |
| **derivative** | The instantaneous rate of change (slope of the tangent line) of a function | 9 |
| **distribution** | Which values a variable takes and how often | 6, 7 |
| **docstring** | A string right after `def` describing what a function does; shown by `help()` | 1, 11 |
| **EDA** | Exploratory data analysis: looking at data numerically and visually before modelling | 6 |
| **effect size** | How big a difference or relationship is, as opposed to whether it's statistically detectable | 8 |
| **expected value** | The long-run average of a random variable, weighting each value by its probability | 7 |
| **feature** | An input variable used by a model (a predictor) | 9, 10 |
| **gradient descent** | Minimising a loss by repeatedly stepping opposite to its gradient | 9 |
| **hyperparameter** | A setting chosen by you, not learned from the data (e.g. ridge's α, tree depth) | 10 |
| **hypothesis test** | A procedure asking whether data are plausible under a null hypothesis | 8 |
| **IQR** | Interquartile range, Q3 − Q1; the spread of the middle 50% | 4, 5 |
| **learning rate** | The step size in gradient descent | 9 |
| **least squares** | Choosing model parameters that minimise the sum of squared residuals | 9 |
| **logistic regression** | A model for yes/no outcomes where the log-odds are linear in the predictors | 10 |
| **loss function** | A measure of how bad predictions are; training minimises its average | 9, 10 |
| **mean / median** | Average / middle value; the median resists outliers | 4 |
| **module (Python)** | A `.py` file you can import; a *package* is a folder of modules with `__init__.py` | 6.5 |
| **multiple comparisons** | Running many tests inflates the chance of false positives; adjust (e.g. Bonferroni) or pre-specify | 8 |
| **normal distribution** | The bell curve, described by mean μ and standard deviation σ | 7 |
| **null hypothesis** | The "no effect / no difference" assumption a test tries to find evidence against | 8 |
| **outlier** | A value far from the rest; may be an error or a genuine extreme | 5 |
| **overfitting** | A model that fits noise in the training data and generalises poorly | 9, 10 |
| **permutation test** | A test that shuffles labels to see what differences arise by chance alone | 8 |
| **pipeline (sklearn)** | Chains preprocessing and a model so every step is learned from training data only | 10 |
| **population / sample** | Everything you want to describe / the part you observed | 7, 8 |
| **power** | The probability a test detects a real effect of a given size | 8 |
| **precision / recall** | Of the cases flagged positive, the share that are right / of all real positives, the share found | 10 |
| **p-value** | The probability, assuming the null hypothesis is true, of a result at least as extreme as observed. *Not* the probability the null is true | 8 |
| **quantile / percentile** | The value below which a given share of the data falls | 4 |
| **R²** | Share of the variance in the outcome explained by the model, compared with predicting the mean | 9 |
| **random seed** | A number that makes random draws repeatable | 3, 7 |
| **regularisation** | Penalising large coefficients to reduce overfitting (ridge, lasso) | 10 |
| **reproducibility** | Anyone can rerun your analysis and get the same results | 6.5, 11 |
| **residual** | Observed minus predicted value | 9 |
| **ROC curve** | True-positive rate vs false-positive rate across all classification thresholds | 10 |
| **sampling variation** | Differences between samples drawn from the same population purely by chance | 8 |
| **Simpson's paradox** | A trend in pooled data that reverses within every subgroup | 6 |
| **skew** | Asymmetry of a distribution; right-skewed means a long tail of large values | 4, 6 |
| **standard deviation / variance** | A measure of spread; variance is its square | 4 |
| **standard error** | The standard deviation of a statistic across repeated samples (σ/√n for the mean) | 8 |
| **statistical vs practical significance** | A result can be detectable (small p) yet too small to matter; report effect sizes | 8 |
| **test set** | Data kept aside, untouched until final evaluation, to estimate real-world performance | 10 |
| **type I / type II error** | False positive (reject a true null) / false negative (miss a real effect) | 8 |
| **vectorisation** | Operating on whole arrays at once instead of looping | 3 |
| **virtual environment** | An isolated set of installed packages for one project | 0 |
| **z-score** | $(x-\bar{x})/s$: how many standard deviations a value is from the mean | 3 |
