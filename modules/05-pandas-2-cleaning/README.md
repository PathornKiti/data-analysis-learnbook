# Module 5: pandas II, cleaning messy data

**Time:** ~1.5 weeks (6–8 h) · **Prerequisite:** Module 4

## Learning goals
* Audit a new dataset for duplicates, missing values, inconsistent text, wrong types and outliers
* Clean text (`.str`), numbers stored as text (`to_numeric`), and dates (`to_datetime`)
* Choose *and justify* a strategy for missing values; flag what you changed
* Detect outliers with the IQR rule and decide what to do with them
* Combine tables with `merge` and check the result
* Package the steps into one reusable cleaning function with sanity checks

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | cleaning the messy coffee-shop orders, step by step |
| `exercises.ipynb` | 9 exercises with exact-answer checks, ending with a full `clean_orders()` function |
| `math-notes.md` | percentages, percent change, logarithms, quartiles & the IQR rule |
| [`../../solutions/05-pandas-2-cleaning/`](../../solutions/05-pandas-2-cleaning/) | solutions |
| [`../../data/messy_orders.csv`](../../data/messy_orders.csv) | the practice dataset (synthetic, with planted problems) |

## Common pitfalls
* Cleaning in place and losing the original; always work on a copy and keep `data/raw/` read-only
* `errors="coerce"` silently turns bad values into `NaN`; **count the missing values before and after**
* Filling missing values with the mean/median shrinks variability; flag what you filled
* Deleting outliers that are real; investigate before you drop
* Ambiguous dates (`03/04/2024`); pass an explicit `format=`
* Merging on a non-unique key multiplies rows; compare row counts before and after

## 🎯 Project checkpoint: **`clean.py`**
1. In your project's exploration notebook, work through your cleaning to-do list from Module 4.
2. Move the working steps into functions in `src/<your_package>/clean.py` (the template has the starting structure).
   One function per problem (`standardize_text`, `parse_dates`, …) plus a `clean(df)` that runs them in order.
3. Add **sanity checks** (`assert`s) at the end of `clean()` or in a test.
4. Write the **"Changes I made"** section of your data card: each fix, how many rows it affected, and *why*.
5. Save the cleaned data to `data/processed/`, never over the raw file.

## Further reading
* pandas user guide: [working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) and
  [working with text data](https://pandas.pydata.org/docs/user_guide/text.html)
