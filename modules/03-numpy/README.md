# Module 3: NumPy

**Time:** ~1 week (5 h) · **Prerequisite:** Module 1

## Learning goals
* Create arrays and understand `shape`, `dtype` and `axis`
* Replace loops with vectorised operations; filter with boolean masks
* Compute summary statistics and simulate with a seeded random generator
* Use vectors, dot products, norms and z-scores, and understand why they matter for modelling

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | arrays, masks, axis, random numbers, vectors, z-scores |
| `exercises.ipynb` | 7 exercises with self-checks |
| `math-notes.md` | vectors, dot product, norm, matrices, standardisation |
| [`../../solutions/03-numpy/`](../../solutions/03-numpy/) | solutions |

## Common pitfalls
* `axis=0` goes *down* the rows (one result per column); `axis=1` goes *across* (one per row)
* Use `&` / `|` (with brackets) for masks, not `and` / `or`
* Integer arrays can silently truncate floats; check `dtype`
* Forgetting a seed makes results unrepeatable

## 🎯 Project checkpoint: **shortlist your data**
Finalise the choice between your two candidate datasets. Download your chosen dataset into your project's `data/raw/` folder
(never edit raw files by hand) and write down in your data card the licence and the download date.

## Further reading
* NumPy's [absolute beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
* 3Blue1Brown's *Essence of linear algebra* video series (search for it on [3blue1brown.com](https://www.3blue1brown.com/))
