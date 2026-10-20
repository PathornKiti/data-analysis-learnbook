# Math notes: Module 9

## Lines
$y=b_0+b_1x$: $b_1$ is the slope (change in $y$ per unit of $x$, "rise over run"), $b_0$ the intercept (value at $x=0$).
A **residual** is observed minus predicted: $e_i=y_i-\hat y_i$.

## Least squares
Choose $b_0,b_1$ to minimise
$$L(b_0,b_1)=\frac1n\sum_{i}(y_i-b_0-b_1x_i)^2.$$
**Closed form (simple regression):**
$$b_1=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}=r\,\frac{s_y}{s_x},\qquad b_0=\bar y-b_1\bar x.$$
Consequences: the line passes through $(\bar x,\bar y)$; the residuals sum to zero; and $b_1$ has the same sign as the correlation $r$.

## Derivatives in two minutes
The **derivative** $f'(x)$ is the slope of the tangent line: the instantaneous rate of change.

| function | derivative |
|---|---|
| constant $c$ | $0$ |
| $x^n$ | $n\,x^{n-1}$ (so $x^2\to2x$) |
| $c\,f(x)$ | $c\,f'(x)$ |
| $f(x)+g(x)$ | $f'(x)+g'(x)$ |
| $g(h(x))$ (chain rule) | $g'(h(x))\,h'(x)$ |

At a smooth minimum, $f'(x)=0$. For a function of several variables, the **partial derivative** $\partial f/\partial b_j$ treats the other variables as constants. The **gradient** $\nabla L$ stacks the partials into a vector that points in the direction of steepest *increase*.

For the loss above, by the chain rule (the "inside" is $y_i-b_0-b_1x_i$, whose derivative with respect to $b_0$ is $-1$ and to $b_1$ is $-x_i$):
$$\frac{\partial L}{\partial b_0}=-\frac2n\sum e_i,\qquad\frac{\partial L}{\partial b_1}=-\frac2n\sum e_i x_i.$$
Setting both to 0 gives the closed-form solution above.

## Gradient descent
Start anywhere and repeat $b\leftarrow b-\eta\,\nabla L(b)$ where $\eta>0$ is the **learning rate**.
* For this (convex, bowl-shaped) loss it reaches the global minimum if $\eta$ is small enough.
* Too small → slow; too large → overshoots and diverges. The largest safe $\eta$ shrinks as the features' scale grows, which is why we **standardise** features first.
* **Stochastic** gradient descent uses a small random batch of rows per step. It's the engine behind training most large models.

## Matrix form and the normal equations
With $X$ the $n\times(p+1)$ design matrix (a column of ones then the $p$ predictors) and $\beta$ the coefficient vector, predictions are $\hat y=X\beta$ and
$$L(\beta)=\tfrac1n\lVert y-X\beta\rVert^2\;\Rightarrow\;X^\top X\,\hat\beta=X^\top y\;\Rightarrow\;\hat\beta=(X^\top X)^{-1}X^\top y.$$
$X^\top X$ must be invertible: if predictors are perfectly collinear, it isn't (and with near-collinearity the estimates become unstable). Software solves the system rather than literally inverting.

## Fit statistics
* $\text{SSE}=\sum(y_i-\hat y_i)^2$, $\text{SST}=\sum(y_i-\bar y)^2$, $R^2=1-\text{SSE}/\text{SST}$.
* **RMSE** $=\sqrt{\text{SSE}/n}$: typical miss in the units of $y$.
* **Adjusted $R^2$** $=1-(1-R^2)\dfrac{n-1}{n-p-1}$ penalises each extra predictor $p$.
* In simple regression $R^2=r^2$.
* **Standard error of a coefficient** reflects noise in the residuals, the spread of that predictor, and its overlap with other predictors. Confidence interval: $\hat b\pm t^*\,\text{SE}(\hat b)$.

## Assumptions (roughly, in order of importance)
1. **Linearity** of the average relationship (check residual plots)
2. **Independence** of observations
3. **Constant variance** of residuals (look for funnels)
4. **Approximately normal residuals** (matters most for intervals with small $n$)

## Check your understanding
1. $\bar x=10,\ \bar y=50,\ r=0.8,\ s_x=2,\ s_y=10$. Slope and intercept? ($b_1=0.8\cdot10/2=4$, $b_0=50-40=10$)
2. If you convert $x$ from hours to minutes, what happens to $b_1$? (Divided by 60: the same relationship, different units)
3. $L(b)=(b-3)^2$. Derivative? Where is the minimum? ($2(b-3)$; at $b=3$)
4. A gradient-descent run's loss keeps growing. What's the most likely cause? (Learning rate too large and/or unscaled features)
