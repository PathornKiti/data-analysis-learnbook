# Module 11: Communicating results

**Time:** ~1.5 weeks (6–8 h) · **Prerequisites:** Modules 6, 6.5 and 8

## Learning goals
* Structure a report so the reader gets the answer first
* Turn estimates, intervals and p-values into honest, well-calibrated sentences (and generate them from code)
* Design a chart whose title states the takeaway; check it against a communication checklist
* Write docstrings (Google style), type hints, a project README and a data card that make your work usable
* Write `pytest` tests that actually catch bugs, and add data validation to the pipeline
* Make an analysis reproducible: seeds, relative paths, pinned dependencies, one command, fresh-clone test
* Apply an ethics and privacy checklist; present results in five minutes

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | reports, sentences from numbers, takeaway charts, docstrings & doctest, pytest & validation, reproducibility, ethics, talk structure |
| `exercises.ipynb` | 7 exercises: sentence generator, takeaway chart, docstring, data validator, small-group suppression, environment report, choosing the best sentence |
| [`exercise/`](exercise/README.md) | **hands-on:** write tests, then a checker injects 9 bugs to see whether your tests catch them |
| [`../../solutions/11-communicating-results/`](../../solutions/11-communicating-results/) | solutions, including reference tests |
| [`../../projects/templates/`](../../projects/templates/) | `PROJECT_README.md`, `REPORT_OUTLINE.md`, `PRESENTATION.md`, `ETHICS_CHECKLIST.md` |

## Common pitfalls
* Burying the answer on page three; describing *what you did* instead of *what you found*
* Numbers without units, intervals or sample sizes; false precision (`2.8997 points`)
* "Significant" used as a synonym for "important"; "proves", "causes" with observational data
* Charts titled with a topic ("Rides by month") instead of a message
* Tests that only restate the code, or never check edge cases (zero, empty, boundary)
* Results pasted by hand into the report so they drift when the data change
* Absolute file paths; unpinned dependencies; notebooks that only work in a particular cell order
* Publishing tables with tiny groups that could identify individuals

## 🎯 Project checkpoint: **tests, docs and a README**
1. **Docstrings** (Google style) and type hints for every function in `src/<package>/`.
2. **Tests:** at least 2–3 sharp tests for each cleaning and analysis function (`tests/`), including an edge case. Use the exercise's checker mindset: *what bug would this test catch?*
3. **Validation:** add a `validate(df)` step at the end of cleaning that raises `ValueError` with a clear message when the data look wrong.
4. **README:** copy `projects/templates/PROJECT_README.md`, fill in every section, and **run the "How to run" commands in a fresh virtual environment** to prove they work.
5. **Report notebook:** `notebooks/02_report.ipynb` that imports your package, generates its key sentences from code, and uses takeaway-titled charts. Restart & Run All.
6. Complete `projects/templates/ETHICS_CHECKLIST.md` for your project and keep it with your data card.
7. Run `python projects/check_project.py path/to/your/project` (added in the capstone module) and fix any ❌.

## Further reading
* *Storytelling with Data* (Cole Nussbaumer Knaflic)
* The pytest documentation: [how-to guides](https://docs.pytest.org/en/stable/how-to/index.html)
* [Google Python style guide: docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
