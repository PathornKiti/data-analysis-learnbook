# Module 6.5: From notebook to module

**Time:** ~1 week (5–7 h) · **Prerequisites:** Modules 5 and 6 · **Needs a local install** (Module 0, option B)

## Learning goals
* Explain when to use notebooks and when to use `.py` files
* Write a script with `if __name__ == "__main__"`, import your own modules, and structure a package (`src/` layout, `__init__.py`)
* Install your package in editable mode (`pip install -e .`)
* Refactor notebook cells into clean functions (arguments in, `return` out, no mutation, docstrings)
* Build paths with `pathlib`, add command-line options with `argparse`
* Write and run tests with `pytest`

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | builds scripts, a package and tests in a temporary folder so you can watch each idea work |
| [`exercise/`](exercise/README.md) | **hands-on:** a real package, `ridekit`, with 13 failing tests for you to make pass |
| [`../../solutions/06b-notebook-to-module/exercise/`](../../solutions/06b-notebook-to-module/exercise/) | a complete implementation (try first!) |

## How to work through it
1. Run the lesson notebook top to bottom, reading each cell.
2. Do the exercise: `cd exercise && pip install -e . && pytest`. Work file by file until the tests pass.
3. Do the project checkpoint below with your own code.

## 🎯 Project checkpoint: **your project becomes a package**
1. Copy [`projects/template/`](../../projects/template/) to a new folder (ideally a new Git repo) and rename the package.
2. Move your cleaning and plotting code from the notebook into `src/<package>/` (cleaning → `clean.py`, charts → `plots.py`, loading → `load.py`),
   following the refactoring recipe at the end of the lesson. **Re-run your notebook after each move.**
3. Make the notebook `import` those functions instead of defining them.
4. Create `run_analysis.py` so `python run_analysis.py` reproduces your cleaned data and your key figures.
5. Add at least **two tests** for your cleaning functions (`tests/test_clean.py`).
6. `git commit` with a clear message.

## Common pitfalls
* Naming a file after a library (`pandas.py`, `test.py`)
* Forgetting `pip install -e .` and getting `ModuleNotFoundError`
* Hard-coded absolute paths
* Functions that print results instead of returning them, or modify the DataFrame they're given
* Changing code and not seeing an effect because the module was already imported (restart the kernel or `%autoreload 2`)

## Further reading
* Python docs: [modules](https://docs.python.org/3/tutorial/modules.html) · `pytest` [getting started](https://docs.pytest.org/en/stable/getting-started.html)
* The [Python Packaging User Guide](https://packaging.python.org/)
