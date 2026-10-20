# Math notes: Module X4 (time-series analysis and inference)

## Components and the additive model
$y_t=T_t+S_t+R_t$ with $S_{t+m}=S_t$ ($m=12$ for monthly data). If the seasonal swings grow with the level, use $y_t=T_tS_tR_t$ and take logs.

**Centred $2\times12$ moving average.** A plain 12-point average of months $t-5,\dots,t+6$ is centred half a month off, so average two neighbouring ones. The result is a 13-point average with weights $\tfrac1{12}(\tfrac12,1,\dots,1,\tfrac12)$. Every calendar month appears exactly once (the end months with half weight, together one full month), so a pure seasonal cycle of period 12 averages out to zero and only the trend survives. The first and last 6 values are lost.

**Seasonal indices.** $\hat S_j=\overline{(y-\hat T)}_{\text{month }j}-\overline{\overline{(y-\hat T)}}$: the monthly means of the detrended series, shifted so that $\sum_j\hat S_j=0$ (otherwise level and season are confounded).

## Autocovariance and autocorrelation
For a (weakly) stationary series, $\gamma_k=\operatorname{Cov}(x_t,x_{t-k})$ and $\rho_k=\gamma_k/\gamma_0$. The sample version is
$$r_k=\frac{\sum_{t=k+1}^{n}(x_t-\bar x)(x_{t-k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}.$$
Example: $x=(1,2,3,4,5)$, $\bar x=3$, denominator $4+1+0+1+4=10$; for $k=1$ the numerator is $(2-3)(1-3)+(3-3)(2-3)+(4-3)(3-3)+(5-3)(4-3)=2+0+0+2=4$, so $r_1=0.4$.
Under independence $r_k$ is approximately $N(0,1/n)$, hence the $\pm1.96/\sqrt n$ bands on an ACF plot. They apply to each lag separately: with 24 lags about one bar in twenty will cross the band by chance.
The **partial autocorrelation** at lag $k$ is the coefficient on $x_{t-k}$ in a regression of $x_t$ on $x_{t-1},\dots,x_{t-k}$. An AR($p$) process has a PACF that cuts off after lag $p$.

## The AR(1) process
$x_t-\mu=\phi(x_{t-1}-\mu)+\varepsilon_t$, $\varepsilon_t$ independent with variance $\sigma^2$, $|\phi|<1$. Then
$$\gamma_0=\frac{\sigma^2}{1-\phi^2},\qquad\rho_k=\phi^k .$$
*Derivation:* take variances of both sides, $\gamma_0=\phi^2\gamma_0+\sigma^2$.

**Least-squares estimation.** Regress $x_t$ on $(1,x_{t-1})$, $t=2,\dots,n$: $\hat\phi=\dfrac{\sum(x_t-\bar x_{(2)})(x_{t-1}-\bar x_{(1)})}{\sum(x_{t-1}-\bar x_{(1)})^2}$, intercept $\hat c$, and $\hat\mu=\hat c/(1-\hat\phi)$. This is the conditional maximum-likelihood estimate (it conditions on the first observation) and it is what `AutoReg` returns. $\hat\sigma^2=\text{RSS}/(n-3)$ is the usual residual variance with two fitted coefficients on $n-1$ rows.

## Variance of a mean, and effective sample size
$$\operatorname{Var}(\bar x)=\frac{\gamma_0}{n}\Big[1+2\sum_{k=1}^{n-1}\Big(1-\frac kn\Big)\rho_k\Big]\ \xrightarrow{\ \text{AR(1), large }n\ }\ \frac{\gamma_0}{n}\Big(1+2\sum_{k\ge1}\phi^k\Big)=\frac{\gamma_0}{n}\cdot\frac{1+\phi}{1-\phi}=\frac{\sigma^2}{n(1-\phi)^2}.$$
Matching this with $\gamma_0/n_\text{eff}$ gives $\boxed{n_\text{eff}=n\dfrac{1-\phi}{1+\phi}}$ and a standard-error inflation of $\sqrt{(1+\phi)/(1-\phi)}$ over the iid formula.
Examples: $n=144,\ \phi=0.6$: $n_\text{eff}=144\cdot0.4/1.6=36$, inflation $\sqrt{1.6/0.4}=2$. $n=100,\ \phi=0.8$: $n_\text{eff}=100\cdot0.2/1.8=11.1$. $\phi=0.9$: inflation $\sqrt{19}=4.36$. For $\phi<0$ the formula gives $n_\text{eff}>n$: a zig-zag series averages *better* than independent data.

## Durbin–Watson
$$DW=\frac{\sum_{t=2}^n(e_t-e_{t-1})^2}{\sum_{t=1}^ne_t^2}=\frac{\sum e_t^2+\sum e_{t-1}^2-2\sum e_te_{t-1}}{\sum e_t^2}\approx2-2r_1 .$$
(The two sums of squares differ only by one end term.) So $DW\approx2$ means $r_1\approx0$, $DW\to0$ means $r_1\to1$, $DW\to4$ means $r_1\to-1$. Example: residuals $(1,-1,1,-1)$: squared steps $3\times4=12$, sum of squares 4, $DW=3$. Durbin–Watson has bounds-table critical values that depend on $X$; in practice look at the residual ACF too. It tests lag 1 only and is not valid with lagged dependent variables.

## HAC (Newey–West) standard errors
With errors that are autocorrelated up to lag $L$, the OLS coefficients are still unbiased but
$$\widehat{\operatorname{Var}}(\hat\beta)=(X^\top X)^{-1}\,\hat S\,(X^\top X)^{-1},\qquad \hat S=\sum_{j=-L}^{L}w_j\sum_t e_te_{t-j}\,x_tx_{t-j}^\top,\quad w_j=1-\frac{|j|}{L+1}$$
(Bartlett weights, which keep $\hat S$ positive semi-definite). With $L=0$ this reduces to the White (heteroskedasticity-robust) estimator. The effect depends on the regressor: when $x_t$ is itself persistent (a trend), the cross-products $x_tx_{t-j}$ are large and the standard error grows; when $x_t$ is unrelated to the persistent part of the noise, the correction can be small or even go the other way. HAC is an asymptotic result: with short or very persistent series it remains too optimistic (see the simulation in the lesson).

## Regression with AR(1) errors
Model $y_t=x_t^\top\beta+u_t$, $u_t=\rho u_{t-1}+\varepsilon_t$. Subtracting $\rho$ times the lagged equation:
$$y_t-\rho y_{t-1}=(x_t-\rho x_{t-1})^\top\beta+\varepsilon_t,$$
which has independent errors, so OLS on the transformed data is efficient (generalised least squares). **Cochrane–Orcutt** alternates between estimating $\rho$ from the residuals, $\hat\rho=\sum u_tu_{t-1}/\sum u_{t-1}^2$, and refitting; it drops the first observation (Prais–Winsten keeps it, scaled by $\sqrt{1-\rho^2}$). Library routines (`GLSAR`, `ARIMA` with `exog`) differ in how they estimate $\rho$, so they agree with a hand version closely but not to every digit.

## Stationarity, differencing, spurious regression
* **Random walk:** $y_t=y_{t-1}+\varepsilon_t$ has $\operatorname{Var}(y_t)=t\sigma^2$, which grows without bound.
* **Differencing:** $\Delta y_t=y_t-y_{t-1}$ turns a random walk into the iid sequence $\varepsilon_t$ and a linear trend $a+bt$ into the constant $b$.
* **Spurious regression** (Granger and Newbold, 1974): regressing one independent random walk on another yields $R^2$ that does not shrink with $n$ and $t$-statistics that grow like $\sqrt n$ (Phillips, 1986), so the rejection rate tends to 1, not 5%. Differencing restores valid inference (if the series are *cointegrated*, differencing throws away information; see error-correction models).
* **Augmented Dickey–Fuller test:** estimate $\Delta y_t=\alpha+\gamma y_{t-1}+\sum_{i=1}^{p}\delta_i\Delta y_{t-i}+\varepsilon_t$ and test $H_0:\gamma=0$ (unit root) against $\gamma<0$. The $t$-ratio does **not** follow a $t$ distribution under $H_0$; Dickey–Fuller critical values (more negative than $-1.96$) are used. Rejecting means "no unit root", not "proven stationary".

## Forecasting the AR(1)
Substituting repeatedly, $x_{T+h}-\mu=\phi^h(x_T-\mu)+\sum_{j=0}^{h-1}\phi^j\varepsilon_{T+h-j}$. Hence
$$\hat x_{T+h}=\mu+\phi^h(x_T-\mu),\qquad\operatorname{Var}(x_{T+h}-\hat x_{T+h})=\sigma^2\sum_{j=0}^{h-1}\phi^{2j}=\sigma^2\,\frac{1-\phi^{2h}}{1-\phi^2}.$$
The forecast decays geometrically to $\mu$ and the error variance rises from $\sigma^2$ to $\gamma_0=\sigma^2/(1-\phi^2)$. Example: $\mu=50,\ \phi=0.5,\ \sigma=4,\ x_T=70$: $h=1$: mean $60$, sd $4$. $h=3$: mean $50+0.125\cdot20=52.5$, sd $4\sqrt{(1-1/64)/0.75}=4.58$. The forecast is within 1 of $\mu$ from $h=5$ ($20\cdot0.5^5=0.625$). Intervals built this way ignore parameter uncertainty and so are too narrow, particularly for small $n$.

## Accuracy measures
For forecast errors $e_i=y_i-\hat y_i$ on the test set: $\text{MAE}=\frac1k\sum|e_i|$, $\text{RMSE}=\sqrt{\frac1k\sum e_i^2}$ (a few big misses count more), and
$$\text{MASE}=\frac{\text{MAE}}{\frac1{n-m}\sum_{t=m+1}^{n}|y_t-y_{t-m}|}$$
with the denominator computed on the **training** data ($m=12$ for monthly seasonality). Values below 1 beat the in-sample seasonal-naive forecast; MASE has no units, so it compares series of different scales. Percentage errors (MAPE) are undefined at zero and heavily penalise over-forecasts, so prefer MAE/MASE unless stakeholders insist.

## Honest validation
Training data must precede test data in time. **Rolling origin** (expanding window): for origins $T_0<T_1<\cdots$ fit on observations up to $T_i$ and forecast $T_i+1,\dots,T_i+H$; average the errors per horizon. Do not tune on the test period, and do not use random k-fold on a series (neighbouring months leak).

## Further reading
Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* (free online); Shumway & Stoffer, *Time Series Analysis and Its Applications*; Hamilton, *Time Series Analysis* (spurious regression, unit roots).
