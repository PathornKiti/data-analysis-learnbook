# Module 7: Probability

**Time:** ~1.5 weeks (6–8 h) · **Prerequisites:** Modules 3 and 4

## Learning goals
* Treat probability as long-run frequency and **simulate** random processes with NumPy
* Apply the complement, addition and multiplication rules; count with combinations
* Use conditional probability and Bayes' theorem, and recognise the base-rate effect
* Compute expected value and variance of a random variable
* Work with the binomial and normal distributions via `scipy.stats`
* Explain the law of large numbers and the central limit theorem

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | simulate → compute → compare, for dice, birthdays, medical tests, games, normal curves, CLT |
| `exercises.ipynb` | 7 exercises (several seeded simulations with tolerant checks) |
| `math-notes.md` | probability rules, Bayes, E[X]/Var, distributions, LLN & CLT |
| [`../../solutions/07-probability/`](../../solutions/07-probability/) | solutions |

## Common pitfalls
* Treating events as independent when they aren't (multiplying probabilities blindly)
* "At least one" problems: use the complement, `1 - P(none)`
* Mixing up $P(A\mid B)$ and $P(B\mid A)$ (the prosecutor's fallacy)
* Ignoring base rates (rare condition → most positive tests are false alarms)
* Forgetting `cdf` is "probability of ≤ x"; "at least 5" is `1 - cdf(4)`
* Gambler's fallacy: a fair coin has no memory

## 🎯 Project checkpoint: **where does chance enter your data?**
No new code files. Write 6–10 sentences (in your project README or notebook) answering:
1. What is your **population** (everything you'd like to describe) and what is your **sample** (the rows you have)?
2. How was the sample collected? Is it random, or might some kinds of rows be more likely to appear (**sampling bias**)?
3. Which variables are best treated as random, and which one (if any) could be a rough **normal**? Check by overlaying a fitted normal curve on a histogram, as in the lesson.
4. Name one thing in your data that might look like a pattern but could be **chance**. In Module 8 you'll test it.
5. Run **one simulation** relevant to your project (e.g. "if there were no relationship, how big a correlation would random shuffling give?").

## Further reading
* Khan Academy [Statistics and probability](https://www.khanacademy.org/math/statistics-probability)
* *Think Bayes* (Allen Downey, free online) for Bayesian thinking with Python
