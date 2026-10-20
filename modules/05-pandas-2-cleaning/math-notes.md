# Math notes: Module 5

## Percentages, shares and percent change
* **Share (part of whole):** $\dfrac{\text{part}}{\text{total}}\times100$. Shares of a whole add up to 100%.
* **Percent change:** $\dfrac{\text{new}-\text{old}}{\text{old}}\times100$.
  * Rising from 80 to 100 is $+25\%$; falling back from 100 to 80 is $-20\%$. The base changes!
  * **Percentage points** vs **percent**: if a rate moves from 10% to 12%, that's $+2$ percentage points but a $+20\%$ relative change.
* Missing share of a column: `df["col"].isna().mean() * 100`.

## Logarithms
$\log_b(x)$ answers "what power of $b$ gives $x$?" so $\log_{10}(1000)=3$ and $\log_2(8)=3$.

| rule | example |
|---|---|
| $\log(ab)=\log a+\log b$ | $\log_{10}(100\cdot 1000)=2+3=5$ |
| $\log(a/b)=\log a-\log b$ | |
| $\log(a^k)=k\log a$ | |

* **Why analysts use them:** products become sums, *ratios* become *differences*. On a log scale, going from 1 → 10 looks the same as
  10 → 100 → 1000, which tames right-skewed quantities (prices, incomes, populations, counts).
* A small change in $\ln(x)$ is approximately a percentage change in $x$: $\ln(1.05)\approx0.049$.
* You can't take the log of zero or negatives. Use `np.log1p(x)` (= $\ln(1+x)$) for counts that may be zero.

## Quartiles, IQR and the outlier rule
Sort the data. $Q_1$ is the 25th percentile, $Q_3$ the 75th. $\text{IQR}=Q_3-Q_1$.
The **1.5 × IQR rule** flags values below $Q_1-1.5\,\text{IQR}$ or above $Q_3+1.5\,\text{IQR}$.

* Robust: the bounds depend on the middle half of the data, not the extremes.
* It is a **flag, not a verdict.** A flagged value can be a typo (fix or drop it), a genuine extreme (keep it, maybe analyse
  separately), or evidence of a different group.
* Domain limits are often better than a formula: "a person can't be 250 years old".

## Missing data in one paragraph
Why a value is missing matters. *Missing completely at random* (a sensor glitch) is mostly harmless; *missing because of the
value itself* (high earners skip the income question) biases every statistic you compute. Filling in values (imputation) keeps rows
but invents information; dropping rows keeps honesty but loses data. Whatever you choose, **say so in your report.**

## Check your understanding
1. A shop's revenue goes from 200 to 260, then to 208. What are the two percent changes? ($+30\%$, $-20\%$)
2. $\log_{10}(0.01)=$ ? ($-2$)
3. $Q_1=10$, $Q_3=30$. What are the outlier bounds? ($10-30=-20$ and $30+30=60$)
