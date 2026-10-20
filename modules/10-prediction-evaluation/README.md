# Module 10: Prediction and evaluation

**Time:** ~2 weeks (8–10 h) · **Prerequisite:** Module 9

## Learning goals
* Distinguish explaining from predicting; explain overfitting and the bias–variance trade-off
* Split data properly (random, stratified, chronological); always compare against a **baseline**
* Use **cross-validation**, **pipelines** and **regularisation** (ridge); spot **data leakage**
* Fit **logistic regression**; understand odds, log-odds and the sigmoid
* Evaluate classifiers with a confusion matrix, precision, recall, F1, thresholds and ROC/AUC; avoid the accuracy trap
* Compare simple and flexible models (trees, forests) honestly, and report performance with its uncertainty

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | overfitting demo → splits & baselines → CV → leakage & pipelines → ridge → logistic → metrics → trees → time series |
| `exercises.ipynb` | 10 exercises (splits, CV, overfitting, pipelines, confusion-matrix maths, thresholds, chronological split, spotting leakage) |
| `math-notes.md` | loss functions, bias–variance, odds & sigmoid, metrics, ridge, ROC |
| [`../../solutions/10-prediction-evaluation/`](../../solutions/10-prediction-evaluation/) | solutions |

## Common pitfalls
* Evaluating on the training data (or tuning against the test set until it looks good)
* No baseline: "80% accuracy" means little if 80% of cases are in one class
* Preprocessing (scaling, imputing) before splitting; use a `Pipeline`
* Leakage: features derived from the target or unavailable at prediction time (a score that's too good to be true is a warning)
* Shuffling time-ordered data, or splitting related rows (same customer, same day) across train and test
* Reporting a single number without uncertainty; choosing a metric that ignores the real cost of errors

## 🎯 Project checkpoint: **model comparison**
1. Write down the **prediction task** in one sentence and which error matters more (false positives or false negatives; large or small misses).
2. Create a **baseline** and at least **two** candidate models (e.g. a simple linear/logistic model and one flexible one). Use a `Pipeline` for any preprocessing.
3. Split your data **before** exploring models; keep a test set untouched. Choose models with **cross-validation** on the training set.
4. Evaluate the final choice **once** on the test set and report: the metric(s), the baseline's score, and the CV spread.
5. Put the logic in `src/<package>/model.py` (the template has `evaluate_regression` and `cross_val_r2` to start from) and add a test.
6. List two ways your model might fail on new data (leakage? a changing world? groups unseen in training?).

## Further reading
* scikit-learn user guide: [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
* *An Introduction to Statistical Learning*, chapters 4–6
