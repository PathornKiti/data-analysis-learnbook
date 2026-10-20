# Module X2 (extension): Survival analysis (time-to-event data)

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 7b, 8b and 9 · **Use it when:** your outcome is *how long until something happens* and some units haven't had it yet when observation ends (churn, relapse, failure, graduation, recovery, time to first purchase)

## Learning goals
* Explain **censoring** and why averages, "did it happen?" models and dropping censored units all give biased answers
* Define and use the **survival function, hazard and cumulative hazard**
* Compute the **Kaplan–Meier** estimate, its **Greenwood** standard error and a **log-log confidence interval** by hand; read medians and $S(t)$ off the curve; draw KM curves with a risk table
* Compare groups with the **log-rank test** (by hand) and describe the effect size
* Fit the **exponential model with censoring** (events ÷ total time) and compare it with Kaplan–Meier
* Fit and interpret **Cox proportional-hazards** regression, including the **partial likelihood** by hand; **check proportional hazards**
* Report survival results with the right quantities and caveats

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | censoring → S/h/H → Kaplan–Meier & Greenwood → log-rank → exponential MLE → Cox (by hand and `PHReg`) → PH checks → pitfalls & reporting |
| `exercises.ipynb` | 8 exercises: KM, reading the curve, Greenwood CI, log-rank, exponential rates, Cox HRs, partial likelihood, restricted mean survival, concept check |
| `math-notes.md` | definitions, KM and Greenwood derivation sketch, log-rank, exponential MLE, Cox partial likelihood, PH checks, RMST |
| [`../../solutions/X2-survival-analysis/`](../../solutions/X2-survival-analysis/) | solutions |
| [`../../data/customer_churn.csv`](../../data/customer_churn.csv) | 400 customers, 24.5% censored, plan and spend covariates |

## Common pitfalls
* Treating **censored times as event times**, or **dropping censored units**
* Reporting only a p-value from the log-rank test (use medians or $S(t)$ at a horizon *and* a hazard ratio with its interval)
* Reading the **far right tail** of a KM curve: few people are at risk there; always show the number at risk
* Interpreting a hazard ratio as "twice as long/short": it is a ratio of **instantaneous rates**, not of survival times
* **Informative censoring** (people drop out *because* they're about to have the event) and **immortal-time bias**
* Ignoring **competing risks** (another event prevents the one you study)
* Too many covariates for the number of **events** (about 10 events per predictor is a minimum)
* Not checking proportional hazards; reporting a single HR when it clearly changes over time
* Vague time origin or unit ("tenure" from sign-up? from first payment?)

## 🎯 Project checkpoint (if your outcome is time-to-event)
1. Define **the event, the time origin, the time unit** and the **end of follow-up** in your data card. Count events and censored units (and the reasons for censoring).
2. Plot **Kaplan–Meier curves** (by your main group) with confidence bands and a **risk table**; report medians or $S(t)$ at a meaningful horizon with intervals.
3. Run the **log-rank test** *and* report an effect size (hazard ratio from Cox, or a median/RMST difference).
4. Fit a **Cox model** with the covariates in your pre-specified hypothesis table; report HRs with 95% CIs; **check proportional hazards**.
5. Implement `kaplan_meier`, `logrank` and your model fit in `src/<package>/survival.py` with tests on tiny hand-worked examples (like the one in `math-notes.md`).
6. State the censoring assumption (non-informative?) and one sensitivity analysis (e.g. different follow-up cut-off).

*If your outcome is not a time-to-event, write one paragraph explaining why survival methods don't apply.*

## Further reading
* Kleinbaum & Klein, *Survival Analysis: A Self-Learning Text*
* Collett, *Modelling Survival Data in Medical Research*
* `statsmodels` [duration analysis](https://www.statsmodels.org/stable/duration.html) documentation (the specialised `lifelines` package is a popular alternative with more plotting and models)
