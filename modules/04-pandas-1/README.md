# Module 4: pandas I, working with tables

**Time:** ~1.5 weeks (6–8 h) · **Prerequisite:** Modules 1 and 3

## Learning goals
* Load a CSV and inspect it (`head`, `info`, `describe`, `shape`)
* Select columns and rows (`[]`, `loc`, `iloc`), filter with conditions
* Create new columns, sort, count categories
* Answer comparison questions with `groupby`
* Describe the centre and spread of data, and explain when mean and median differ

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | the full tour with `students` and `daily_rides` data |
| `exercises.ipynb` | 7 exercises with self-checks (do them in order; later ones reuse earlier variables) |
| `math-notes.md` | mean, median, variance, standard deviation, quantiles, skew |
| [`../../solutions/04-pandas-1/`](../../solutions/04-pandas-1/) | solutions |

## Common pitfalls
* `df[df.a > 1 & df.b < 2]` fails: wrap each condition in brackets
* `df["a"]` (Series) vs `df[["a"]]` (DataFrame)
* `loc` includes the end label of a slice; `iloc` does not
* Modifying a filtered slice: use `.copy()` first
* pandas' `.std()` uses $n-1$; NumPy's uses $n$

## 🎯 Project checkpoint: **first look at your data**
In a notebook in your project (`notebooks/01_explore.ipynb`):
1. Load your dataset. Show `shape`, `info()`, `describe()`.
2. List the columns that matter for your question and their types.
3. Answer one **describe** question and one **compare** question using `groupby`.
4. Note three things that look odd (missing values, weird categories, impossible numbers). These become your cleaning
   to-do list for Module 5.

## Further reading
* [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
