# Project rubric (100 points)

| area | points | what excellent looks like |
|---|---|---|
| **Question & motivation** | 10 | specific, measurable question; clear why it matters; scoped realistically |
| **Data understanding** | 10 | data card complete (source, licence, columns, limits); feasibility honestly assessed |
| **Cleaning** | 10 | each cleaning decision justified; raw data untouched; before/after checks |
| **Exploration & visuals** | 15 | well-chosen, labelled, honest charts with takeaway titles; variable distributions profiled (shape table, Q-Q/ECDF where relevant); every figure's calculation and interval/band type stated in its caption (chart audit) |
| **Analysis / modelling** | 20 | hypotheses and tests **pre-specified** (hypothesis table, primary vs exploratory, power considered); the test **matches the design** (paired vs independent, outcome type); assumptions checked with plots and a sensitivity analysis; estimate + interval + effect size + n reported; multiplicity handled; model evaluated on held-out data against a baseline; no overclaiming; where the data are repeated, clustered, censored or time-ordered, the method accounts for that dependence (extension modules X1–X4) |
| **Code organisation** | 15 | logic in `src/` modules, small functions with docstrings, no copy-paste, sensible names |
| **Reproducibility & tests** | 10 | `pip install -r requirements.txt` + `python run_analysis.py` works from a clean clone; at least six meaningful `pytest` tests; `python projects/check_project.py` shows no ❌ |
| **Communication** | 10 | README and report tell a clear story; plain-language conclusions; limitations section |

## Levels
* **Meets expectations (70+):** correct, reproducible, answers the question, honest about limits.
* **Exceeds (85+):** thoughtful method choices, strong visuals, clean code, insightful limitations.

## Self-review checklist
- [ ] I can state my question in one sentence
- [ ] A stranger could run my project from the README alone
- [ ] Every chart has a title, axis labels and units
- [ ] I reported uncertainty, not just point estimates
- [ ] I clearly separate "what the data shows" from "what I think it means"
- [ ] I did not claim causation from correlation
