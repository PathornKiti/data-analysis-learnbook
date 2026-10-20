# Module 9: Linear regression

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 3, 6 and 8

## Learning goals
* Fit and interpret a line of best fit (slope, intercept, residuals) and explain what "least squares" means
* Derive and run **gradient descent** from the idea of a derivative; explain learning rate and feature scaling
* Write multiple regression in matrix form and solve the normal equations
* Use `statsmodels` (coefficients with intervals and p-values) and `scikit-learn` (prediction)
* Interpret coefficients correctly: "holding the other variables fixed", association ≠ causation
* Diagnose a model with residual plots; understand $R^2$, adjusted $R^2$ and RMSE and their traps

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | least squares → calculus & gradient descent → matrix form → statsmodels → diagnostics → R² traps |
| `exercises.ipynb` | 9 exercises, including coding gradient descent and the normal equations |
| `math-notes.md` | lines, derivatives, partial derivatives, gradient, normal equations, R² |
| [`../../solutions/09-linear-regression/`](../../solutions/09-linear-regression/) | solutions |

## Common pitfalls
* Interpreting the intercept when $x=0$ is outside the data
* Reading coefficients causally (a regression describes associations among the variables **you included**)
* Gradient descent on unscaled features (slow or divergent)
* Forgetting the residual plot: a high $R^2$ can hide a curved relationship
* Extrapolating beyond the range of the data
* Adding predictors until $R^2$ looks good (it always rises, so use adjusted $R^2$ or, better, Module 10's test data)

## 🎯 Project checkpoint: **your first model**
1. Choose an **outcome** (a number) in your data and 2–4 predictors **chosen from your question**. Write them down first.
2. Fit it with `statsmodels` (formula syntax) in your notebook. Produce a coefficient table with intervals.
3. Make a **residuals-vs-fitted** plot and a histogram of residuals; note anything curved, funnel-shaped or extreme.
4. Add `fit_ols(df, formula)` and `coefficient_table(result)` to `src/<package>/model.py` (the template has them) and use them in your report notebook.
5. Write 3 sentences interpreting the two most important coefficients **in the units of your data**, with their intervals, and one sentence on what the model *can't* tell you.
   (If your outcome is a category, wait for Module 10's logistic regression.)

## Further reading
* *An Introduction to Statistical Learning* (James, Witten, Hastie, Tibshirani), free online; chapters 3 and 4
* 3Blue1Brown's *Essence of calculus* for the intuition behind derivatives
