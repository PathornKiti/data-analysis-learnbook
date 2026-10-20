# Math notes: Module 8 (inference)

## Estimation and standard error
* **Parameter** (population, fixed, unknown): $\mu,\ p,\ \rho$. **Statistic** (sample, random): $\bar x,\ \hat p,\ r$.
* **Standard error** of the mean: $\text{SE}(\bar x)=\dfrac{\sigma}{\sqrt n}$, estimated by $\dfrac{s}{\sqrt n}$.
  It's the standard deviation of the *sampling distribution* of $\bar x$. Halving it needs 4× the data.

## Confidence intervals
* **Mean (t-interval):** $\bar x\pm t^*_{n-1}\,\dfrac{s}{\sqrt n}$, where $t^*_{n-1}$ is the 97.5th percentile of the $t$ distribution with $n-1$ degrees of freedom
  ($\approx2.0$ for $n\approx60$, $\to1.96$ as $n\to\infty$).
* **Proportion:** $\hat p\pm1.96\sqrt{\hat p(1-\hat p)/n}$ (fine when $n\hat p$ and $n(1-\hat p)$ are both $\ge10$).
* **Interpretation:** a 95% CI is produced by a procedure that captures the true value in 95% of repeated studies. A wider interval means more uncertainty; higher confidence also means wider.
* **Bootstrap percentile CI:** resample the data with replacement $B$ times, compute the statistic each time, take the 2.5th and 97.5th percentiles.

## Hypothesis tests
1. State $H_0$ (default, "no effect") and $H_1$ (alternative).
2. Choose $\alpha$ (e.g. 0.05) **before** looking.
3. Compute a test statistic from the data.
4. **p-value** $=P(\text{statistic at least this extreme}\mid H_0\text{ true})$.
5. If $p<\alpha$, "reject $H_0$"; otherwise "fail to reject". It is *never* "accept $H_0$".

**Welch's two-sample t:** $t=\dfrac{\bar x_1-\bar x_2}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$ (doesn't assume equal variances).
**Chi-square test of independence:** $\chi^2=\sum\dfrac{(O-E)^2}{E}$ with $E=\dfrac{\text{row total}\times\text{column total}}{\text{grand total}}$, degrees of freedom $(r-1)(c-1)$.

### What a p-value is not
* Not $P(H_0\text{ true}\mid\text{data})$
* Not the probability the result happened "by chance"
* Not the size or importance of the effect
* Not a measure of replicability

## Errors and power
* **Type I error** (false positive): reject a true $H_0$; probability $=\alpha$.
* **Type II error** (false negative): fail to reject a false $H_0$; probability $=\beta$.
* **Power** $=1-\beta$. Rises with: larger effect, larger $n$, larger $\alpha$, lower noise.
* Rough sample size for 80% power, two groups, $\alpha=0.05$: $n\approx\dfrac{16}{d^2}$ per group (e.g. $d=0.5\Rightarrow 64$; $d=0.2\Rightarrow 400$).

## Effect sizes
* **Cohen's $d$** $=\dfrac{\bar x_1-\bar x_2}{s_p}$ with $s_p=\sqrt{\dfrac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}$. Rough guide: 0.2 small, 0.5 medium, 0.8 large.
* **Correlation** $r$ and $r^2$ are also effect sizes.
* Always report in **original units** too (points, dollars, minutes), since that's what readers can judge.

## Multiple comparisons
With $m$ independent tests at level $\alpha$, $P(\ge1\text{ false positive})=1-(1-\alpha)^m$: for $m=20$, about 64%.
**Bonferroni:** use $\alpha/m$ per test. (Holm and false-discovery-rate methods are less conservative.)
The best defence is a **pre-specified** question and a **confirmation** on fresh data.

## Check your understanding
1. $s=12$, $n=36$. What's the SE? ($12/6=2$.) Roughly, what's the 95% CI half-width? ($\approx2\times2=4$)
2. A study of 10 people finds "no significant effect." Does that show there's no effect? (No: probably low power.)
3. Why is "we tested 40 foods and found jelly beans linked to acne (p=0.03)" unconvincing? (Multiple comparisons: expect ~2 false positives in 40 tests.)
