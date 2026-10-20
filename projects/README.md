# Your project

The project is the heart of the course. You'll choose a topic you care about, find real data, and build a small,
reproducible analysis, organised as a **Python package** rather than a single messy notebook.

## The journey

| milestone | when | what you produce |
|---|---|---|
| 1. Proposal + data card | Module 2 | `PROPOSAL.md`, `DATA_CARD.md` |
| 2. Data in place | Module 3 | raw data in `data/raw/`, licence noted |
| 3. First look | Module 4 | `notebooks/01_explore.ipynb` |
| 4. Cleaning | Module 5 | `src/<pkg>/clean.py` + cleaned data |
| 5. EDA & plots | Module 6 | `src/<pkg>/plots.py` + EDA section in the notebook |
| 6. Restructure | Module 6.5 | project turned into a package; `run_analysis.py` |
| 7. Distributions | Module 7b | `src/<pkg>/distributions.py` + a distribution profile of your key variables |
| 8. Hypotheses & analysis | Modules 8, 8b | **hypothesis table** (written *before* testing) + `src/<pkg>/analysis.py`, `hypothesis.py` |
| 9. Model | Modules 9–10 | `src/<pkg>/model.py` and a model comparison |
| 10. Chart audit | Module 9b | every figure justified, its calculation and intervals stated, captions written |
| 11. Polish | Module 11 | tests, docstrings, README, report notebook |
| 12. Capstone | Module 12 | final package + report + short presentation |
| (optional) Extensions | Modules X1–X4 | a mixed-model, survival, Bayesian or time-series section matching your data, with tested functions in `mixed.py`, `survival.py`, `bayes.py` or `timeseries.py` |

## Getting started

1. Browse [`tracks.md`](tracks.md) for ideas and data sources.
2. Copy [`template/`](template/) **out of this repo** to a new folder (ideally your own Git repository) and rename the
   package (see the template's README).
3. Use [`templates/PROPOSAL.md`](templates/PROPOSAL.md) and [`templates/DATA_CARD.md`](templates/DATA_CARD.md).
4. After each module, complete its **🎯 project checkpoint** and commit.
5. Self-assess with the [`rubric.md`](rubric.md) before you submit.

## Ground rules
* **Raw data is read-only.** Cleaning produces new files in `data/processed/`.
* **One command reproduces everything:** `python run_analysis.py`.
* **No copy-paste.** If you write something twice, make it a function in `src/`.
* **Pre-specify your tests.** Write your hypotheses, tests and primary outcomes down *before* running them, and report every test you ran. The [`reference/`](../reference/) sheets help you choose and write them up.
* **Respect licences and privacy.** Never publish personal data. Cite your sources.

## Worked example and the project doctor
* [`worked-example/`](worked-example/) is a finished project (bike-share demand) in exactly this structure. Study it, then build your own.
* **Project doctor:** `python projects/check_project.py path/to/your/project` checks the structure, README sections, tests, absolute paths, and runs your pipeline from a clean copy. Fix every ❌ before you submit. See also [`../modules/12-capstone/`](../modules/12-capstone/).
