# Math notes: Module X2 (survival analysis)

## Data and notation
For unit $i$: observed time $y_i=\min(T_i,C_i)$ (event time $T_i$, censoring time $C_i$) and indicator $\delta_i=\mathbf 1\{T_i\le C_i\}$ (1 = event observed, 0 = right-censored). Assume **non-informative censoring**: $T_i$ and $C_i$ independent (given covariates).

## Core functions
$$S(t)=P(T>t),\qquad h(t)=\lim_{\Delta\downarrow0}\frac{P(t\le T<t+\Delta\mid T\ge t)}{\Delta}=\frac{f(t)}{S(t)},\qquad H(t)=\int_0^t h(u)\,du,\qquad S(t)=e^{-H(t)}.$$
Median survival: $t$ with $S(t)=0.5$. Mean survival $=\int_0^\infty S(t)\,dt$ (only estimable if the curve reaches 0; otherwise use the **restricted mean** up to a horizon $\tau$: $\text{RMST}(\tau)=\int_0^\tau S(t)\,dt$).

**Exponential:** $h(t)=\lambda$, $S(t)=e^{-\lambda t}$, median $\ln2/\lambda$, mean $1/\lambda$. **Weibull:** $h(t)=\lambda\gamma t^{\gamma-1}$ (increasing for $\gamma>1$, decreasing for $\gamma<1$).

## Kaplan–Meier
At distinct event times $t_{(1)}<\dots<t_{(m)}$ let $n_j$ = number at risk just before $t_{(j)}$ and $d_j$ = number of events at $t_{(j)}$.
$$\hat S(t)=\prod_{t_{(j)}\le t}\Big(1-\frac{d_j}{n_j}\Big).$$
It is the nonparametric maximum-likelihood estimator of $S$. **Greenwood's formula** (delta method applied to $\ln\hat S=\sum\ln(1-d_j/n_j)$ with binomial variances):
$$\widehat{\operatorname{Var}}\big[\hat S(t)\big]=\hat S(t)^2\sum_{t_{(j)}\le t}\frac{d_j}{n_j(n_j-d_j)}.$$
**Confidence intervals:** plain $\hat S\pm z\,\text{SE}$ (can exit $[0,1]$); **log-log** $\hat S^{\exp(\pm z\,s)}$ with $s=\dfrac{\sqrt{\sum d_j/(n_j(n_j-d_j))}}{|\ln\hat S|}$ (stays in $(0,1)$; preferred).

**Worked example.** Times $2,\,3^{+},\,5,\,7,\,8^{+}$ ($^+$ = censored): at $t=2$: $n=5,d=1\Rightarrow\hat S=0.8$; at $t=5$ ($n=3$): $0.8\times\tfrac23=0.533$; at $t=7$ ($n=2$): $0.533\times\tfrac12=0.267$. The median is the first time $\hat S\le0.5$, so **7**. The censored value at 3 left the risk set after $t=3$ without dropping $\hat S$.

## Log-rank test
At each event time $t_{(j)}$, with $n_{1j},n_j$ at risk in group 1 and overall and $d_{1j},d_j$ events,
$$O_1=\sum d_{1j},\quad E_1=\sum d_j\frac{n_{1j}}{n_j},\quad V=\sum d_j\frac{n_{1j}}{n_j}\Big(1-\frac{n_{1j}}{n_j}\Big)\frac{n_j-d_j}{n_j-1},\quad\chi^2=\frac{(O_1-E_1)^2}{V}\ \dot\sim\ \chi^2_1.$$
It is most powerful when hazards are proportional. With $G$ groups, use the $(G-1)$-df version. Weighted variants (Wilcoxon/Gehan, Fleming–Harrington) emphasise early or late differences. The log-rank test is equivalent to the score test of a Cox model with the group as covariate.

## Exponential model with censoring
Likelihood $L(\lambda)=\prod_i\big[\lambda e^{-\lambda y_i}\big]^{\delta_i}\big[e^{-\lambda y_i}\big]^{1-\delta_i}=\lambda^{d}e^{-\lambda\sum y_i}$, with $d=\sum\delta_i$. Then $\ell'(\lambda)=\frac d\lambda-\sum y_i=0$:
$$\hat\lambda=\frac{d}{\sum y_i}=\frac{\text{events}}{\text{total time at risk}},\qquad\operatorname{Var}(\hat\lambda)\approx\frac{\lambda^2}{d}\ \Rightarrow\ \hat\lambda\,e^{\pm1.96/\sqrt d}.$$
**Worked example.** 20 events in 400 customer-months: $\hat\lambda=0.05$ per month, median $\ln2/0.05\approx13.9$ months.

## Cox proportional-hazards model
$$h(t\mid x)=h_0(t)\exp(\beta^\top x),\qquad\text{HR for }x_j+1\text{ vs }x_j=e^{\beta_j}.$$
Equivalently $S(t\mid x)=S_0(t)^{\exp(\beta^\top x)}$: a hazard ratio of 2 **squares** the baseline survival probability (a baseline $S_0=0.6$ becomes $0.36$). It does not halve survival *times* unless hazards are constant.
**Partial likelihood** (Breslow handling of ties): with risk set $R(t_i)=\{j:y_j\ge t_i\}$,
$$L(\beta)=\prod_{i:\delta_i=1}\frac{\exp(\beta^\top x_i)}{\sum_{j\in R(t_i)}\exp(\beta^\top x_j)}.$$
$h_0$ cancels, so no baseline shape is needed. $\hat\beta$ maximises $\ln L$; $\operatorname{Cov}(\hat\beta)\approx\big(-\partial^2\ln L/\partial\beta\partial\beta^\top\big)^{-1}$; Wald, score and likelihood-ratio tests are available. A CI for $\text{HR}$ is $\exp(\hat\beta\pm1.96\,\text{SE})$; for a $k$-unit change use $\exp(k\hat\beta)$ and $\exp(k\,\text{CI})$.
**Events per variable:** the information is in the *number of events*; aim for at least ~10 per predictor.

## Checking proportional hazards
* **Graphical:** $\ln(-\ln\hat S_g(t))$ vs $\ln t$ for each group: parallel curves (vertical gap $=\beta$) support PH; for exponential survival the curves are straight lines with slope 1.
* **Time-split HRs:** estimate the HR in disjoint follow-up windows; large systematic change signals non-PH.
* **Schoenfeld residuals:** under PH they are uncorrelated with time (a formal test).
* **Remedies:** stratify on the offending variable (separate baselines), add a covariate × time interaction, use an accelerated-failure-time model, or report RMST differences.

## Related ideas
* **Competing risks:** use cumulative incidence functions and cause-specific or Fine–Gray models; 1 − KM overstates the event probability when other events remove people from risk.
* **Time-varying covariates** need the counting-process data layout (one row per interval).
* **Left truncation/delayed entry** changes the risk set (units enter at their own start times).
* **Frailty models** are the survival analogue of random effects for clustered data (Module X1).

## Check your understanding
1. Times $2,\,3^+,\,5,\,7,\,8^+$: compute $\hat S$ at 5 and the median. ($0.533$; $7$)
2. 20 churn events observed over a total of 400 customer-months: the exponential rate and median? ($0.05$/month; $\ln2/0.05\approx13.9$ months)
3. If $S_0(12)=0.6$ for premium and the HR for basic is 2, what is $S(12)$ for basic? ($0.6^2=0.36$)
4. Why shouldn't you average the survival times of only the customers who churned? (It excludes those still loyal, so the average is biased low)
5. A study has 500 patients but only 30 events. How many predictors in a Cox model? (About 3: 30/10)
