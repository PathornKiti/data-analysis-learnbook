# Capstone milestones (3 weeks)

Each milestone has a **check-in**: show a classmate, instructor or study buddy (or yourself, honestly) what you have. Short and concrete beats long and vague.

## Week 1: Data, cleaning, exploration

| day | goal | check-in question |
|---|---|---|
| 1 | Re-read your proposal. Is the question still the right one? Update `PROPOSAL.md` if it changed. | Can you state your question in one sentence? |
| 1–2 | Data in `data/raw/`; **data card** complete; run the feasibility check one more time. | Do you know what one row is, and what's missing? |
| 2–3 | `clean.py` finished with documented decisions and a **validation step**. Two or three tests for it. | Which cleaning decision could change your results most? |
| 4–5 | EDA: at least four charts; list of observations and *new questions*. | What surprised you? What looks like it might be an artefact? |

**Deliverable:** cleaned data + exploration notebook + updated data card. Run `python projects/check_project.py . --skip-run`.

## Week 2: Inference, modelling, tests

| day | goal | check-in question |
|---|---|---|
| 6–7 | Write down your planned comparisons **before** running them. Implement them in `analysis.py` with intervals and effect sizes. | How many comparisons will you run in total? |
| 8–9 | Model (if applicable): baseline, one simple model, one alternative; honest evaluation (split before exploring models, cross-validation). Residual/error analysis. | Does your model beat the baseline by a meaningful margin? Could there be leakage? |
| 10 | Tests for analysis and model code; `run_analysis.py` reproduces results and figures. | Which of your numbers would be wrong if a function had a bug? Is it tested? |

**Deliverable:** full pipeline running from `run_analysis.py`; tests passing. Run the doctor *with* the run step.

## Week 3: Polish, peer review, present

| day | goal | check-in question |
|---|---|---|
| 11–12 | Report notebook with generated sentences and takeaway-titled charts; README complete; ethics checklist done; docstrings for all functions. | Could a stranger run this in ten minutes? |
| 13 | **Peer review** (see [`peer-review.md`](peer-review.md)): swap projects, fresh-clone and run each other's work. | What did your reviewer fail to understand? That is a bug in your write-up. |
| 14 | Apply feedback; final doctor run (no ❌); self-assess with the [rubric](../../projects/rubric.md). Write your reflection. | Is your summary still true after the last changes? |
| 15 | **Present** (5 minutes + questions). | What's the strongest and the weakest claim in your project? |

## Time-boxing advice
* **Resist adding features in week 3.** Polish, don't expand.
* If you're behind, **cut scope** (a smaller question done well beats a large one done badly), never cut tests, uncertainty or limitations.
* Commit at the end of every working session with a message saying *what changed and why*.
