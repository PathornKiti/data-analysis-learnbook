# Math notes: Module 10

## Loss functions
A **loss** measures how bad one prediction is; **training** minimises the average loss.
| task | loss | notes |
|---|---|---|
| regression | squared error $(y-\hat y)^2$ | punishes big misses; leads to RMSE/least squares |
| regression | absolute error $\lvert y-\hat y\rvert$ | robust to outliers; leads to MAE |
| classification | log-loss $-[y\log p+(1-y)\log(1-p)]$ | used to fit logistic regression; punishes confident wrong answers |

## Generalisation and the bias–variance trade-off
Expected test error $\approx$ **bias**$^2$ + **variance** + irreducible noise.
* **Bias:** error from a model too simple to capture the truth (underfitting).
* **Variance:** error from a model so flexible that its fit changes a lot between training samples (overfitting).
* More flexibility lowers bias and raises variance; the best test error is at an intermediate flexibility.
* More **data** reduces variance; **regularisation** trades a little bias for much less variance.

## Cross-validation
Split into $k$ folds; for each fold, train on the other $k-1$ and score on it. The estimate is the mean of the $k$ scores; their spread shows how unstable the estimate is.
$k=5$ or $10$ is typical. Use **stratified** folds for classification and **time-ordered** (expanding window) folds for time series.

## Ridge and lasso
$$\text{ridge: }\ \sum(y_i-\hat y_i)^2+\alpha\sum_j b_j^2\qquad\text{lasso: }\ \sum(y_i-\hat y_i)^2+\alpha\sum_j\lvert b_j\rvert$$
Larger $\alpha$ ⇒ smaller coefficients ⇒ simpler model. Standardise predictors first. Lasso can set coefficients exactly to zero (a kind of feature selection). $\alpha$ is a **hyperparameter** chosen by CV.

## Odds, log-odds and the sigmoid
$$\text{odds}=\frac{p}{1-p}\ \ (\text{e.g. }p=0.8\Rightarrow4:1),\qquad\text{logit}(p)=\ln\frac{p}{1-p},\qquad\sigma(z)=\frac1{1+e^{-z}}$$
Logistic regression assumes $\text{logit}(p)=b_0+b_1x_1+\dots$, so $p=\sigma(b_0+b_1x_1+\dots)$.
* $e^{b_j}$ is the **odds ratio**: the multiplicative change in odds per unit increase in $x_j$ (others fixed).
* $\sigma(0)=0.5$; $\sigma$ is symmetric: $\sigma(-z)=1-\sigma(z)$.
* The decision boundary at threshold 0.5 is where $b_0+b_1x_1+\dots=0$, a straight line/plane.

## Classification metrics
From the confusion matrix (TP, FP, FN, TN):
$$\text{accuracy}=\frac{TP+TN}{n},\quad\text{precision}=\frac{TP}{TP+FP},\quad\text{recall}=\frac{TP}{TP+FN},\quad\text{specificity}=\frac{TN}{TN+FP},\quad F_1=\frac{2PR}{P+R}$$
* **Base rate:** if positives are 1% of cases, "always negative" has 99% accuracy.
* Raising the threshold: fewer positives flagged ⇒ precision tends to rise, recall falls. Lowering it does the opposite.
* **ROC curve:** true-positive rate (recall) vs false-positive rate $=FP/(FP+TN)$ over all thresholds. **AUC** = probability that a random positive gets a higher score than a random negative. 0.5 = chance, 1 = perfect.
* With very rare positives, the **precision–recall curve** is more informative than ROC.

## Trees and forests (idea only)
A tree repeatedly picks the split that best separates the outcomes (lower **impurity**, e.g. Gini $=1-\sum p_k^2$). An unlimited tree memorises the training set (train accuracy 100%). A **random forest** averages many trees grown on bootstrap samples with random feature subsets, which cuts variance.

## Check your understanding
1. A test finds 8 of 10 true cases and raises 12 false alarms among 90 healthy people. Recall? Precision? (0.8; 8/20 = 0.4)
2. $\sigma(0)$, and the probability when the log-odds are $+2$? (0.5; $\approx0.88$)
3. Your model's training $R^2$ is 0.95 and test $R^2$ is 0.40. Diagnosis and two remedies? (Overfitting; more data, simpler model/regularisation, fewer features)
4. Odds ratio 2.0 for a feature: what does it mean? (One more unit doubles the odds of the positive class, holding others fixed)
