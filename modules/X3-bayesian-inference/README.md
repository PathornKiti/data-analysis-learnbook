# Module X3 (extension): Bayesian inference

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 7 and 7b (8b helps for the comparisons) · **Use it when:** you want probability statements about parameters, have genuine prior information, have small samples, need to update as data arrive, or must fit models with no frequentist shortcut

## Learning goals
* State **Bayes' rule for parameters** and explain prior, likelihood and posterior; interpret a **credible interval** and contrast it with a confidence interval
* Compute posteriors **by hand** for the **Beta–Binomial**, **Normal–Normal** and **Gamma–Poisson** models, by **grid approximation** for any prior shape, and with a **random-walk Metropolis** sampler written from scratch
* Run a **Bayesian A/B test**: $P(A>B)$, the posterior of the difference, a ROPE, odds ratios
* Judge the **influence of the prior** and do a **prior sensitivity analysis**
* Diagnose MCMC (**acceptance rate, $\hat R$, effective sample size, trace plots**) and check the model with **posterior predictive checks**
* Report a Bayesian analysis honestly (priors, diagnostics, sensitivity, limitations)

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | Bayes' rule → Beta–Binomial → prior sensitivity → grid → A/B test → Normal–Normal → Gamma–Poisson → Metropolis & diagnostics → posterior predictive checks → reporting |
| `exercises.ipynb` | 9 exercises: conjugate updates, prior sensitivity, grid posterior, A/B probabilities, Metropolis sampler, $\hat R$, interpretation |
| `math-notes.md` | conjugacy derivations, credible intervals (equal-tailed vs HPD), Metropolis–Hastings, convergence diagnostics, predictive distributions, Bayes factors |
| [`../../solutions/X3-bayesian-inference/`](../../solutions/X3-bayesian-inference/) | solutions |

(The data are the course's `app_trial.csv`, `students.csv` and `service_desk.csv`; no extra packages are needed.)

## Common pitfalls
* **Hidden priors:** "flat" priors can be informative on another scale; always state and justify the prior
* Reading a posterior probability of a hypothesis as a p-value (or the reverse); they answer different questions
* **No prior sensitivity analysis**, especially with small samples
* Using too few MCMC draws, no burn-in, **a single chain**, or ignoring $\hat R$/ESS and trace plots
* **Strongly correlated parameters** or poorly scaled proposals making Metropolis crawl (use better samplers such as Hamiltonian Monte Carlo)
* Skipping **posterior predictive checks**: a posterior can be perfectly computed for a bad model
* Treating Bayes factors as objective: they are highly prior-dependent
* Saying "confidence interval" for a credible interval (or "95% probability" for a confidence interval)

## 🎯 Project checkpoint: **a Bayesian re-analysis of your main result**
1. Pick **one** main estimate in your project (a proportion, a mean, a rate, or a difference) and write down the model and the **prior(s)** you will use, with a one-line justification each (previous studies, physical limits, or deliberately weak).
2. Compute the posterior **analytically** if a conjugate model fits, otherwise by grid or your own Metropolis sampler; report the posterior mean/median, **95% credible interval**, and one **probability statement** relevant to your decision ($P(\text{effect}>0)$, $P(\text{effect}>\text{practically important size})$).
3. Do a **prior sensitivity analysis** with at least two alternative priors; present the results in a small table.
4. If you used MCMC: report chains, burn-in, acceptance rate, $\hat R$ and ESS; include a trace plot.
5. Run **one posterior predictive check** and say what the model gets right and wrong.
6. Compare with your frequentist result from Module 8b in two sentences: where do they agree and where does the interpretation differ? Add functions and tests to `src/<package>/bayes.py` (e.g. a Beta–Binomial update checked against hand-computed values).

## Further reading
* Gelman et al., *Bayesian Data Analysis* (the standard reference) and McElreath, *Statistical Rethinking* (an excellent, intuitive course)
* Kruschke, *Doing Bayesian Data Analysis* (A/B tests, ROPE, and plenty of worked examples)
* [PyMC](https://www.pymc.io/) and [Stan](https://mc-stan.org/) documentation; [ArviZ](https://python.arviz.org/) for diagnostics
