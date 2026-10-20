# Bundled datasets

All files are **synthetic**: invented by `generate_datasets.py` (seeded, so
reproducible) purely for teaching. Do not draw real-world conclusions from them.

## `students.csv` (200 rows)

| column | meaning |
|---|---|
| `student_id` | 1–200 |
| `major` | Science, Arts, Business or Engineering |
| `study_hours_week` | hours of study per week |
| `sleep_hours` | average hours of sleep per night |
| `attendance_pct` | percentage of classes attended |
| `part_time_job` | `yes` / `no` |
| `exam_score` | final exam score, 0–100 |

## `daily_rides.csv` (366 rows, 2024)

| column | meaning |
|---|---|
| `date` | `YYYY-MM-DD` |
| `temp_c` | mean daily temperature in °C (6 values are missing on purpose) |
| `rain_mm` | rainfall in mm |
| `is_weekend` | 1 = Saturday/Sunday, 0 = weekday |
| `rides` | number of bike-share rides that day |

## `messy_orders.csv` (312 rows, coffee-shop orders)

Deliberately messy, for Module 5 (cleaning). Problems planted on purpose:

| column | meaning | problems |
|---|---|---|
| `order_id` | order number | – |
| `order_date` | when the order was placed | text in three different formats |
| `customer` | first name | inconsistent case and stray spaces |
| `city` | Bangkok, Chiang Mai or Phuket | case, spaces, and a `Chiangmai` misspelling |
| `item` | Latte, Espresso, Mocha, Tea or Cake | inconsistent case and stray spaces |
| `quantity` | number of items | 16 missing values; 4 typos of `99` |
| `unit_price` | price per item | text with `$` signs; 15 missing (the text `N/A`, which pandas reads as missing) |

There are also 12 exact duplicate rows, so a clean table has 300 rows.


## `app_trial.csv` (300 rows): a randomised app experiment (Modules 7b, 8b, 9b)

300 users randomly assigned to three onboarding versions (100 each).

| column | meaning |
|---|---|
| `user_id` | 1–300 |
| `group` | `control`, `tutorial` or `gamified` |
| `device` | `ios`, `android` or `web` (unrelated to group, as expected from randomisation) |
| `pre_score`, `post_score` | skill-test score before and after (**paired**); about 0.85 correlated |
| `minutes_active` | time in the app: **strongly right-skewed** (lognormal) |
| `converted` | 1 if the user converted, else 0 (**binary**) |
| `rating` | satisfaction on a 1–5 scale (**ordinal**) |

## `service_desk.csv` (480 rows): four differently shaped variables (Module 7b)

Hourly help-desk records.

| column | shape |
|---|---|
| `hour_id` | 1–480 |
| `tickets` | counts: Poisson (mean ≈ variance) |
| `response_minutes` | right-skewed, positive: lognormal |
| `satisfaction_pct` | bounded at 100, left-skewed: beta-like |
| `call_minutes` | **bimodal**: a mixture of quick calls (~61%, around 3 min) and long calls (~39%, around 12 min) |

For your own project you will bring **real** data; see
[`projects/tracks.md`](../projects/tracks.md) for where to find it.
