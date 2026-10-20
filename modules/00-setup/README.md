# Module 0: Setup

**Time:** 30–60 minutes · **Goal:** a working Python environment and a first look at the tools.

## Choose your path

### A. Google Colab (zero install)
Open a notebook from GitHub in [Colab](https://colab.research.google.com/) (File → Open notebook → GitHub tab).
The data-loading cell in each notebook downloads the course data automatically. Good for getting started;
move to a local install by Module 6.5 because you'll write `.py` files.

### B. Local install (recommended)

1. **Install Python 3.10+** from [python.org](https://www.python.org/downloads/) (on Windows, tick *Add Python to PATH*).
2. **Get the course:**
   ```bash
   git clone https://github.com/PathornKiti/data-analysis-learnbook.git
   cd data-analysis-learnbook
   ```
   (No Git? Use the green **Code → Download ZIP** button on GitHub and unzip.)
3. **Create a virtual environment**: an isolated set of packages just for this course:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
4. **Install packages and start Jupyter:**
   ```bash
   pip install -r requirements.txt
   jupyter lab
   ```
5. Open `modules/00-setup/check_environment.ipynb` and run all cells. ✅ means you're ready.

## Notebook survival guide

| action | how |
|---|---|
| run a cell | Shift + Enter |
| add a cell below / above | `B` / `A` (in command mode, press Esc first) |
| change cell to Markdown / Code | `M` / `Y` |
| restart and run everything | Kernel → Restart Kernel and Run All Cells |

**Golden rule:** before you share a notebook, *restart and run all*. If it still works, it's reproducible.

## Git in five commands (for your project)

```bash
git status                  # what changed?
git add file.py             # stage a change
git commit -m "Add cleaning function"
git log --oneline           # history
git push                    # share (once you've connected a GitHub repo)
```

## Troubleshooting

* `python` not found → try `python3`, or reinstall with *Add to PATH*.
* `pip install` is slow or fails → upgrade pip: `python -m pip install --upgrade pip`.
* Notebook says `ModuleNotFoundError` → Jupyter is using a different Python from the one you installed into.
  Start `jupyter lab` from the same activated environment.

## Project checkpoint

None yet. Just get set up. In Module 2 you'll choose your project.
