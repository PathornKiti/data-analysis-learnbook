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

For your own project you will bring **real** data; see
[`projects/tracks.md`](../projects/tracks.md) for where to find it.
