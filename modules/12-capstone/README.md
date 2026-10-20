# Module 12: Capstone

**Time:** ~3 weeks (12–18 h) · **Prerequisites:** everything. You've been building towards this since Module 2.

The capstone is not a new topic. It's where you **finish, polish and present the project you have been building**: a reproducible Python package that answers *your* question about *your* data,
with honest uncertainty, tests, and a report a stranger can understand.

## What you hand in

| deliverable | where | notes |
|---|---|---|
| **Project package** | your project folder | `src/<package>/` modules, `run_analysis.py`, `requirements.txt`, tests |
| **README** | `README.md` | filled from [`PROJECT_README.md`](../../projects/templates/PROJECT_README.md); runnable in a fresh environment |
| **Report notebook** | `notebooks/02_report.ipynb` | imports from your package; numbers in sentences generated from results |
| **Proposal & data card** | `PROPOSAL.md`, `DATA_CARD.md` | updated to reflect what you actually did |
| **Ethics checklist** | `ETHICS_CHECKLIST.md` | from [`ETHICS_CHECKLIST.md`](../../projects/templates/ETHICS_CHECKLIST.md) |
| **5-minute talk** | slides or live demo | outline: [`PRESENTATION.md`](../../projects/templates/PRESENTATION.md) |
| **Project doctor output** | terminal | `python projects/check_project.py <your project>` with no ❌ |

## Minimum requirements ("meets expectations")

1. **Question:** one clear main question, plus supporting *describe / compare / relate* questions (and *predict* if it fits your data).
2. **Data:** real data of at least a few hundred rows, with a data card (source, licence, limits).
3. **Cleaning:** every decision documented and justified; raw data untouched; a validation step that stops the pipeline when data look wrong.
4. **EDA:** at least **four** purposeful charts with takeaway titles (a distribution, a comparison, a relationship, and one over time or by group); a **distribution profile** of your key variables; and a **chart audit** (Module 9b) so every figure's calculation and intervals are stated in its caption.
5. **Inference:** a **hypothesis table written before testing** (Module 8b) with the test matched to the design, assumptions checked, and each primary result reported with an estimate, **interval**, effect size and n; the full list of comparisons you ran; a sensitivity analysis.
6. **Modelling** (where it fits your question): a baseline, a sensible model, honest evaluation (held-out data or cross-validation), residual or error analysis.
7. **Code:** logic in `src/` modules; functions with docstrings; no copy-paste; at least **six meaningful tests**.
8. **Reproducibility:** `pip install -r requirements.txt && python run_analysis.py` works from a fresh clone; seeds set; relative paths.
9. **Communication:** answer-first summary, honest limitations, plain-language conclusions.

Use the [rubric](../../projects/rubric.md) to self-assess before submitting. It's the same one used for grading.

## A worked example to study

[`projects/worked-example/`](../../projects/worked-example/) is a complete project that meets every requirement above. It answers *"What drives daily bike-share demand, and can we predict it?"* using the course's bundled data. Read it **in this order**:

1. `PROPOSAL.md` → `DATA_CARD.md`: how a project starts
2. `src/ridership/clean.py` and `tests/test_clean.py`: cleaning + validation + tests that target the risky parts
3. `src/ridership/analysis.py` → `model.py`: the statistics and honest evaluation (chronological split, baseline, cross-validation)
4. `src/ridership/report.py`: sentences generated from numbers
5. `tests/test_pipeline.py`: a test that fails if the README's numbers go stale
6. `README.md` and `notebooks/02_report.ipynb`: the finished story

Copy its *structure and habits*, **not its content**. Your question and data are your own.

## The three-week plan

See [`milestones.md`](milestones.md). In short: **week 1** finish data, cleaning and EDA; **week 2** inference, modelling and tests; **week 3** polish, peer review, presentation.

## Stretch options (pick at most one or two; quality beats quantity)

* **Time series:** seasonality, rolling averages, time-series cross-validation.
* **Text data:** word counts, simple sentiment, topic exploration (with `scikit-learn`'s `CountVectorizer`/`TfidfVectorizer`).
* **Data from an API or scraping** (check the site's terms and rate limits; cache responses).
* **Model explanation:** permutation importance, partial-dependence plots, error analysis by group.
* **Uncertainty for predictions:** bootstrap or cross-validated intervals for your metric.
* **A small dashboard** (e.g. Streamlit) that imports your package's functions.
* **Reproducible report export:** `jupyter nbconvert --to html --execute`.

## If you get stuck

See [`troubleshooting.md`](troubleshooting.md). And remember: **"I found no relationship" is a legitimate, valuable finding** when you can show it was a fair test (with an interval and a sample-size caveat).

## Reflection (write ~200 words in your README or report)

* What was your first question and how did it change?
* What was the hardest cleaning or modelling decision, and what did you choose?
* If you had a week more, what would you do next? What would you *not* trust in your own results?
