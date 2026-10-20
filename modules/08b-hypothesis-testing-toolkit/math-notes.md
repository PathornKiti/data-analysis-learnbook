# Math notes: Module 8b (hypothesis testing)

## The general recipe
1. Null hypothesis $H_0$ and alternative $H_1$ (two-sided unless justified in advance).
2. A **test statistic** $T$ measuring departure from $H_0$ in standard-error units.
3. The **null distribution** of $T$ (normal, $t_\nu$, $\chi^2_\nu$, $F_{\nu_1,\nu_2}$, or by simulation).
4. **p-value** $=P(|T|\ge|t_{\text{obs}}|\mid H_0)$ (two-sided). Reject if $p<\alpha$.
5. **Duality with intervals:** a level-$\alpha$ test rejects $H_0:\theta=\theta_0$ iff the $(1-\alpha)$ CI excludes $\theta_0$.

## $t$-tests
**One sample:** $t=\dfrac{\bar x-\mu_0}{s/\sqrt n}\sim t_{n-1}$. CI: $\bar x\pm t^*_{n-1,\,1-\alpha/2}\,s/\sqrt n$.

**Paired:** with $d_i=y_i-x_i$, $t=\dfrac{\bar d}{s_d/\sqrt n}\sim t_{n-1}$; effect size $d_z=\bar d/s_d$. Variance of the difference $=\sigma_x^2+\sigma_y^2-2\rho\sigma_x\sigma_y$: **the stronger the correlation $\rho$, the smaller the noise**, hence the power gain.

**Two independent samples, Welch:** $t=\dfrac{\bar x_1-\bar x_2}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$ with Welch–Satterthwaite degrees of freedom
$$\nu=\frac{\left(\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1-1}+\frac{(s_2^2/n_2)^2}{n_2-1}}.$$
**Pooled (Student):** $s_p^2=\dfrac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$, $t=\dfrac{\bar x_1-\bar x_2}{s_p\sqrt{1/n_1+1/n_2}}\sim t_{n_1+n_2-2}$ (assumes equal variances).

## Effect sizes
| measure | formula | rough guide |
|---|---|---|
| Cohen's $d$ | $\dfrac{\bar x_1-\bar x_2}{s_p}$ | 0.2 small, 0.5 medium, 0.8 large (context matters) |
| Hedges' $g$ | $d\left(1-\dfrac{3}{4(n_1+n_2)-9}\right)$ | small-sample corrected $d$ |
| $d_z$ (paired) | $\bar d/s_d$ | |
| SE of $d$ | $\approx\sqrt{\dfrac{n_1+n_2}{n_1n_2}+\dfrac{d^2}{2(n_1+n_2)}}$ | CI: $d\pm1.96\,\text{SE}$ |
| probability of superiority | $U_1/(n_1n_2)$ | 0.5 = none; 0.56 / 0.64 / 0.71 ≈ small / medium / large $d$ |
| rank-biserial $r$ | $2U_1/(n_1n_2)-1$ | $-1$ to $1$ |
| $\eta^2$, $\omega^2$ | $\dfrac{SSB}{SST}$; $\dfrac{SSB-(k-1)MSW}{SST+MSW}$ | 0.01 / 0.06 / 0.14 small / medium / large |
| risk ratio, odds ratio | $\dfrac{p_1}{p_2}$; $\dfrac{p_1/(1-p_1)}{p_2/(1-p_2)}$ | 1 = no association; OR ≈ RR only when events are rare |
| Cramér's $V$ | $\sqrt{\dfrac{\chi^2}{N(\min(r,c)-1)}}$ | 0.1 / 0.3 / 0.5 small / medium / large (for 2×2) |

## Rank-based tests
**Mann–Whitney $U$:** rank all $N=n_1+n_2$ values together (average ranks for ties); $R_1=$ sum of group-1 ranks; $U_1=R_1-\dfrac{n_1(n_1+1)}2$, $U_1+U_2=n_1n_2$.
Under $H_0$ (no ties): $E[U]=\dfrac{n_1n_2}2$, $\operatorname{Var}(U)=\dfrac{n_1n_2(n_1+n_2+1)}{12}$, and $U$ is approximately normal for $n_i\gtrsim 10$ (tie-corrected variance is smaller).
$U_1/(n_1n_2)$ equals the **area under the ROC curve** for separating the two groups. **Wilcoxon signed-rank:** rank $|d_i|$, sum the ranks of the positive differences; null mean $n(n+1)/4$.
**Kruskal–Wallis:** $H=\dfrac{12}{N(N+1)}\sum_j\dfrac{R_j^2}{n_j}-3(N+1)\ \dot\sim\ \chi^2_{k-1}$.
A rank test compares *distributions*; it tests medians only if shapes are alike.

## ANOVA
$SST=\sum_{ij}(x_{ij}-\bar x)^2=SSB+SSW$ with $SSB=\sum n_j(\bar x_j-\bar x)^2$, $SSW=\sum_{ij}(x_{ij}-\bar x_j)^2$. $\text{MSB}=\dfrac{SSB}{k-1}$, $\text{MSW}=\dfrac{SSW}{N-k}$, $F=\dfrac{\text{MSB}}{\text{MSW}}\sim F_{k-1,N-k}$ under $H_0$.
Assumes independence, roughly normal residuals, equal variances (Welch's ANOVA relaxes the last). With $k=2$, $F=t^2$.
**Tukey HSD:** for every pair, $q=\dfrac{|\bar x_i-\bar x_j|}{\sqrt{\text{MSW}/2\,(1/n_i+1/n_j)}}$ compared with the studentised-range distribution; controls the family-wise error rate.
**ANCOVA:** $y_i=\beta_0+\beta\,\text{baseline}_i+\sum_j\gamma_j\,\text{group}_{ij}+\varepsilon_i$. The $\gamma_j$ are baseline-adjusted group effects; the residual variance falls by about the factor $1-\rho^2$ where $\rho$ is the baseline–outcome correlation (here $\rho\approx0.85$, so a ≈72% reduction of variance, i.e. residual sd ≈ half).

## Multiple comparisons
With $m$ tests at level $\alpha$, $P(\text{at least one false positive})=1-(1-\alpha)^m$ (for independent tests).
* **Bonferroni:** $p^{\text{adj}}_i=\min(1,\,m\,p_i)$. Simple, conservative.
* **Holm:** sort $p_{(1)}\le\dots\le p_{(m)}$; $p^{\text{adj}}_{(j)}=\max_{i\le j}\min\big(1,(m-i+1)p_{(i)}\big)$. Uniformly more powerful than Bonferroni, same guarantee.
* **Benjamini–Hochberg (FDR):** $p^{\text{adj}}_{(j)}=\min_{i\ge j}\min\big(1,\tfrac{m}{i}p_{(i)}\big)$. Controls the expected *proportion* of false discoveries; use when you run many tests (e.g. genes, survey items).
* **Pre-specification** of one or two primary hypotheses avoids the correction for those; label everything else exploratory.

## Proportions and tables
* **One proportion, Wilson interval:** $\dfrac{\hat p+\frac{z^2}{2n}\pm z\sqrt{\frac{\hat p(1-\hat p)}n+\frac{z^2}{4n^2}}}{1+\frac{z^2}n}$ (behaves well for small $n$ and $\hat p$ near 0 or 1, unlike the Wald interval).
* **Two proportions:** $z=\dfrac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}}$ with $\hat p=\frac{x_1+x_2}{n_1+n_2}$; CI for $p_1-p_2$ uses $\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}$.
  This $z$ test equals the $2\times2$ $\chi^2$ test without continuity correction ($z^2=\chi^2$).
* **$\chi^2$ test of independence:** $E_{ij}=\dfrac{R_iC_j}{N}$, $\chi^2=\sum\dfrac{(O_{ij}-E_{ij})^2}{E_{ij}}$, $\text{df}=(r-1)(c-1)$; needs $E_{ij}\gtrsim5$.
* **Fisher's exact test:** conditional on the margins, the count in one cell is hypergeometric: $P=\dfrac{\binom{a+b}{a}\binom{c+d}{c}}{\binom{N}{a+c}}$; the p-value sums the probabilities of tables as or more extreme.

## Correlation
$r$ tested with $t=r\sqrt{\dfrac{n-2}{1-r^2}}\sim t_{n-2}$. **Fisher:** $z=\operatorname{arctanh}r$, $\text{SE}=1/\sqrt{n-3}$, CI $=\tanh(z\pm z_{1-\alpha/2}\text{SE})$. **Spearman** $\rho$ is Pearson's $r$ of the ranks; **Kendall** $\tau=\dfrac{C-D}{\binom n2}$ (concordant minus discordant pairs).

## Equivalence (TOST)
Choose a margin $\Delta>0$ *in advance*. Test $H_{01}:\theta\le-\Delta$ and $H_{02}:\theta\ge+\Delta$ with two one-sided tests; the equivalence p-value is the **larger** of the two. Equivalent to checking that the **$(1-2\alpha)$ CI lies inside $(-\Delta,\Delta)$**.

## Power and sample size
Power $=P(\text{reject }H_0\mid\text{effect }\delta)=1-\beta$. For a two-sample $t$-test, the normal approximation gives
$$n_{\text{per group}}\approx\frac{2\,(z_{1-\alpha/2}+z_{1-\beta})^2}{d^2}$$
e.g. $\alpha=0.05$, power $0.80$: $n\approx 15.7/d^2$, so $d=0.5\Rightarrow\approx63$ (exact $t$-based: 64), $d=0.2\Rightarrow\approx393$.
Power rises with $n$, $|\delta|$, $\alpha$ and falls with $\sigma$. A paired or baseline-adjusted design reduces the effective $\sigma$.

## Check your understanding
1. $n=36$, $s=12$, $\bar x-\mu_0=4$. What are $t$, the df and roughly the two-sided p? ($t=4/(12/6)=2$, df 35, $p\approx0.053$: just above 0.05)
2. You test five pre-specified secondary outcomes at overall $\alpha=0.05$. What is the Bonferroni per-test threshold? ($0.05/5=0.01$)
3. Holm-adjust $p=(0.01,\,0.02,\,0.03)$. ($0.03,\ 0.04,\ 0.04$)
4. A 2×2 table has $30/100$ successes in group 1 and $20/100$ in group 2. Risk ratio and odds ratio? ($0.30/0.20=1.5$; $\frac{30/70}{20/80}\approx1.71$)
5. Why can a paired design detect a small improvement that an independent-groups design on the same data cannot? (Subtracting each person's own baseline removes the large between-person variance; with equal variances and $\rho=0.8$ the variance of the difference is $0.4\sigma^2$, only 20% of the sum of the two variances, $2\sigma^2$)
6. A study of 20 per group finds $p=0.12$. Can you conclude the treatments are equivalent? (No; the power to detect a medium effect at $n=20$ is only about 34%. Report the CI, or run a TOST with a pre-specified margin)
