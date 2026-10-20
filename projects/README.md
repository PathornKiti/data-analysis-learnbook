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
| 7. Analysis / model | Modules 8–10 | `src/<pkg>/analysis.py` |
| 8. Polish | Module 11 | tests, docstrings, README, report notebook |
| 9. Capstone | Module 12 | final package + report + short presentation |

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
* **Respect licences and privacy.** Never publish personal data. Cite your sources.
