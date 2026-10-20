# Instructor guide

How to teach with this repository. Everything here is a suggestion; adapt freely.

## What you're getting
* **14 modules** of notebook lessons, self-checking exercises, math notes and worked solutions
* A **project spine**: students build one project across the whole course (proposal → package → report)
* Two **package exercises** (Modules 6.5 and 11) that practise `.py` modules and tests
* A **worked example** and a **project doctor** script to make "reproducible" concrete and checkable
* **CI** that guarantees every lesson, solution and example runs

## Time per module

| module | hours (self-paced) | suggested sessions (2 h) | the hard part |
|---|---|---|---|
| 0 Setup | 1–2 | 0.5 | installation problems: budget extra time |
| 1 Python foundations | 5–7 | 3 | indentation, functions, comprehensions |
| 2 Project kickoff | 3–5 | 2 | choosing a *specific* question |
| 3 NumPy | 4–6 | 2–3 | `axis`, broadcasting, dot product |
| 4 pandas I | 6–8 | 3 | boolean masks, `groupby` |
| 5 Cleaning | 6–8 | 3 | deciding what to do about missing data and outliers |
| 6 Visualization & EDA | 6–8 | 3 | honest charts; correlation limits |
| 6.5 Notebook → module | 5–7 | 2–3 | imports, packages, tests |
| 7 Probability | 6–8 | 3 | conditional probability, Bayes |
| 8 Inference | 8–10 | 4 | what a p-value *isn't*; interval interpretation |
| 9 Regression | 8–10 | 4 | gradient descent; interpreting coefficients |
| 10 Prediction | 8–10 | 4 | leakage; metrics beyond accuracy |
| 11 Communicating | 6–8 | 3 | writing good tests and honest sentences |
| 12 Capstone | 12–18 | 4–6 + presentations | scope control |

## Formats

**14-week semester (default).** One module per week roughly, as in the [pacing table](SYLLABUS.md#suggested-pacing-14-weeks).
*Flipped:* students run `lesson.ipynb` before class; class time is for `exercises.ipynb`, discussion of tricky ideas, and a 10-minute project check-in.

**8-week intensive.** Merge modules (0–1, 2–3, 4–5, 6–6.5, 7–8, 9–10, 11, 12) and keep the project small. Skip the optional parts of math notes; make the capstone a "finish and present" week.

**Self-study.** Work the modules in order; do every project checkpoint (it is what turns the exercises into skill); join or form a study group for the Module 12 peer review.

**Shorter course (no modelling).** Stop after Module 8 (+11): students finish with a descriptive/inferential project. Use the worked example's `describe`/`compare` parts as the model.

## Suggested session pattern (2 hours)
1. **10 min:** project show-and-tell (previous checkpoint, 1 minute each in pairs)
2. **20 min:** the 2–3 ideas from the lesson that students found hardest (use the "common pitfalls" in each module README)
3. **50 min:** exercises in pairs (one types, one explains, swap every exercise)
4. **30 min:** project work with circulation; use the project checkpoint as the day's goal
5. **10 min:** wrap-up: one-sentence summary from each student of what they learned and one question

## Assessment ideas
* **Formative:** the self-checking exercises (completion, not grades), plus the checkpoint each week.
* **Summative:** the capstone, using [`projects/rubric.md`](projects/rubric.md) (100 points) and the doctor output as the objective part of the "Reproducibility & tests" score.
* **Oral check (optional):** ask each student to explain one function, one chart and one limitation in their project. It quickly reveals understanding.
* **Academic integrity:** the solutions are public in this repository. If that's a problem, delete `solutions/` from the copy you distribute and keep it yourself. Projects are individual by nature (own question, own data); the oral check and the fresh-clone peer review help confirm authorship.

## Module-specific tips
* **Module 1:** let students struggle with an error message for two minutes before helping. Ask "what is the last line saying?"
* **Module 4–5:** bring a dataset from *your* local context to the live demo; students love seeing real mess.
* **Module 6:** the Anscombe and Simpson demos are worth doing live; ask students to predict the plots first.
* **Module 7:** simulate everything before deriving. The birthday problem and the medical-test example reliably produce "wait, what?" moments.
* **Module 8:** use the job-vs-no-job example (p ≈ 0.07). Have students argue both wrong conclusions, then the right one.
* **Module 9:** do gradient descent on the board with two parameters and a bowl-shaped contour plot; the learning-rate demo makes the idea stick.
* **Module 10:** have students try to *break* a model: leak a feature, shuffle time, add junk columns; see which of them survive cross-validation.
* **Module 11:** run the test-writing exercise as a competition: who catches the most injected bugs with the fewest tests?
* **Module 12:** insist on the fresh-clone peer review. It is the most valuable hour of the course.

## Adapting the course
* **Data:** swap the bundled synthetic datasets for local ones by editing `data/generate_datasets.py` or adding CSVs and updating the notebooks' `DATA / "..."` paths. Check the exercise checks, which contain exact expected values.
* **Language:** the notebooks are plain Markdown + code; translating the Markdown cells is straightforward. Code and checks need no change.
* **Tools:** the course assumes Python and pip. If your institution uses conda, `requirements.txt` works with `pip` inside a conda environment.
* **Accessibility:** charts use a colour-blind-safe palette and titles state the message; encourage students to add alt text for published figures.

## Keeping the course healthy (CI)
`.github/workflows/ci.yml` runs on every push: it executes every lesson and solution notebook, checks that exercise notebooks have no stored outputs, tests the project template and worked example, runs the project doctor on both, and verifies the package exercises (solutions must pass; the student stubs must still fail).
If you add or change an exercise, run the build locally first (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
