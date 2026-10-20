# Troubleshooting your project

| symptom | likely cause | what to try |
|---|---|---|
| `ModuleNotFoundError: No module named '<your_package>'` | package not installed, or wrong environment | activate your venv; `pip install -e .` from the project folder |
| `FileNotFoundError` for the data | path relative to the wrong place | build paths from `Path(__file__)`; run commands from the project root; don't hard-code absolute paths |
| Code works in the notebook but not as a script (or vice versa) | hidden notebook state, or relying on cells run out of order | Restart & Run All; move logic into functions with arguments |
| `SettingWithCopyWarning` / a column silently didn't change | modifying a slice | work on `.copy()`; assign with `.loc[...]` |
| Merge produced more rows than expected | the join key isn't unique on one side | `df.duplicated(subset=key).sum()` before merging; compare row counts after |
| Dates parsed wrongly / won't sort | stored as text, or ambiguous formats | `pd.to_datetime(..., format=...)`; check `dtype` |
| Model score is *too good* (R² ≈ 1, accuracy ≈ 100%) | target leakage | list features; remove anything derived from, or only known after, the outcome |
| Test score much worse than training score | overfitting | simpler model, regularisation, fewer features, more data; compare with a baseline |
| Test score changes a lot between runs | a single noisy split | use cross-validation; set seeds; report mean ± sd |
| Very few rows left after cleaning | dropping too aggressively | count rows lost at each step; consider filling instead of dropping, and document |
| No relationship found | maybe there isn't one, or the data are too small/noisy | report the interval and sample size: "compatible with no effect, but we can't rule out an effect up to X". That's a result |
| Chart is unreadable | too much on one plot | one message per chart; small multiples; aggregate; log scale |
| The pipeline takes forever | big data or repeated work | develop on a sample; cache intermediate files in `data/processed/`; vectorise instead of looping |
| Tests are hard to write | functions do too much, or depend on globals/files | split into small functions taking inputs and returning outputs; build tiny DataFrames in the test |
| Running out of time | scope too big | cut scope, not quality: a smaller question done well, with tests and honest limitations |

## When you ask for help (good questions get fast answers)
1. What are you trying to do?
2. What did you run, exactly? (code or command)
3. What did you expect, and what happened? (full error message, last lines first)
4. What have you already tried?
5. A **minimal example** that reproduces the problem (a tiny DataFrame beats your 50,000-row file).
