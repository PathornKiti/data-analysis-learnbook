# Math notes: Module 7 (probability)

## Basics
* **Sample space** $S$: all possible outcomes. An **event** $A\subseteq S$.
* $0\le P(A)\le1$, $P(S)=1$.
* **Complement:** $P(A^c)=1-P(A)$.
* **Addition:** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$. If $A,B$ can't both happen (**mutually exclusive**) the last term is 0.
* **Independence:** $P(A\cap B)=P(A)P(B)$. Knowing $A$ tells you nothing about $B$. (Rolling two dice; **not** drawing cards without replacement.)

## Counting
* Orderings of $n$ distinct things: $n!=n(n-1)\cdots1$
* Choosing $k$ of $n$ (order ignored): $\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$ ("n choose k")
* If all outcomes are equally likely, $P(A)=\dfrac{\#\text{ways }A\text{ can happen}}{\#\text{total outcomes}}$.

## Conditional probability and Bayes
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\qquad\text{so}\qquad P(A\cap B)=P(A\mid B)P(B)$$

**Law of total probability:** $P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)$.

**Bayes' theorem:**
$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B\mid A)\,P(A)+P(B\mid A^c)\,P(A^c)}$$
* $P(A)$ is the **prior** (before the evidence), $P(A\mid B)$ the **posterior** (after).
* **Base-rate fallacy:** with a rare $A$, even a very accurate test yields mostly false positives (1% prevalence, 90% sensitivity, 5% false-positive rate → 15% chance of disease after a positive result).
* Natural frequencies ("out of 1,000 people…") make Bayes' problems far easier.

## Random variables
* **Expected value:** $E[X]=\sum_x x\,P(X=x)$ (continuous: an integral). Linear: $E[aX+b]=aE[X]+b$, $E[X+Y]=E[X]+E[Y]$.
* **Variance:** $\operatorname{Var}(X)=E[(X-\mu)^2]=E[X^2]-\mu^2$. $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$.
  For *independent* $X,Y$: $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)$.
* **Standard deviation:** $\sigma=\sqrt{\operatorname{Var}(X)}$.

## Key distributions
| distribution | models | pmf / pdf | mean | variance | scipy |
|---|---|---|---|---|---|
| Bernoulli($p$) | one yes/no trial | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ | `stats.bernoulli` |
| Binomial($n,p$) | successes in $n$ independent trials | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | `stats.binom` |
| Uniform($a,b$) | all values equally likely | $1/(b-a)$ | $(a+b)/2$ | $(b-a)^2/12$ | `stats.uniform` |
| Normal($\mu,\sigma$) | bell curve; sums/averages | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | `stats.norm` |
| Poisson($\lambda$) | counts of rare events per interval | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ | `stats.poisson` |

**Z-score:** $z=(x-\mu)/\sigma$ converts any normal to the *standard* normal. 68–95–99.7 rule: within 1, 2, 3 $\sigma$.

## Two big theorems
* **Law of large numbers:** the sample mean $\bar X_n\to\mu$ as $n\to\infty$. Averages of more data are closer to the truth.
* **Central limit theorem:** for independent draws with mean $\mu$ and sd $\sigma$, the distribution of $\bar X_n$ is approximately
  $\text{Normal}\!\big(\mu,\ \sigma/\sqrt n\big)$ for large $n$, regardless of the original shape. $\sigma/\sqrt n$ is the **standard error**.

## Check your understanding
1. Two fair coins: what's $P(\text{at least one head})$? ($1-\tfrac14=0.75$)
2. $P(A)=0.3$, $P(B)=0.5$, independent. $P(A\text{ or }B)$? ($0.3+0.5-0.15=0.65$)
3. A game pays \$10 with probability 0.1, else \$0. Entry costs \$2. Expected net? ($1-2=-\$1$)
4. How does the SE change if you go from $n=25$ to $n=100$? (Halves)
