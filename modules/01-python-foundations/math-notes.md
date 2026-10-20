# Math notes: Module 1

## Order of operations
Brackets → exponents → multiplication/division → addition/subtraction. `2 + 3 * 4 = 14`, but `(2 + 3) * 4 = 20`.
When unsure, add brackets: it costs nothing and makes your intent obvious.

## Exponents and roots
* $a^n$ means multiply $a$ by itself $n$ times: `a ** n`.
* $\sqrt{a} = a^{1/2}$: `a ** 0.5` (or `math.sqrt(a)`).
* $a^0 = 1$, and $a^{-1} = 1/a$.

## Percentages and ratios
* $x\%$ of $y$ is $\frac{x}{100}\,y$.
* "Part as a percentage of whole" is $\frac{\text{part}}{\text{whole}}\times 100$.
* A *percentage change* from old to new is $\frac{\text{new}-\text{old}}{\text{old}}\times 100$.
  Going from 80 to 100 is $+25\%$; going back from 100 to 80 is $-20\%$. They are not symmetric!

## Functions
A function $f$ assigns to each input $x$ exactly one output $f(x)$. For example $f(x)=2x+1$:
$f(0)=1$, $f(1)=3$, $f(10)=21$. In Python, `def f(x): return 2 * x + 1`.
Data analysis is mostly *composing functions*: load → clean → summarise → plot.

## Summation notation Σ
$$\sum_{i=1}^{n} x_i = x_1 + x_2 + \dots + x_n$$
reads "add up $x_i$ for $i$ from 1 to $n$". It is a `for` loop with a running total, or `sum(x)`.

## The mean
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$
The balance point of the data. Try: if you add 10 to every value, how does the mean change? (By exactly 10.)
If you multiply every value by 2? (The mean doubles.)

## Variance (preview)
$$\operatorname{var}(x) = \frac1n\sum_{i=1}^{n}(x_i-\bar{x})^2$$
The average squared distance from the mean. Squaring makes every distance positive and punishes big gaps more.
You'll implement it in the exercises.

## Check your understanding
1. Rewrite $\sum_{i=1}^{4} i^2$ as a Python expression. (Answer: `sum(i**2 for i in range(1, 5))` = 30.)
2. A price rises 50%, then falls 50%. Is it back where it started? (No: $100 \to 150 \to 75$.)
