# Bundled datasets

Both files are **synthetic**: invented by `generate_datasets.py` (seeded, so
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

For your own project you will bring **real** data; see
[`projects/tracks.md`](../projects/tracks.md) for where to find it.
