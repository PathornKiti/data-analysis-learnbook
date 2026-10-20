# Project proposal

**Name:** Worked example (course staff)  **Date:** 2024

## 1. Topic and why I care
Bike-share systems have to decide how many bikes to put where and when. Weather and weekends seem to matter a lot, and I'd like to know *how much*, and whether a very simple model is good enough to plan with.

## 2. Main question
How do temperature, rain and weekends affect the number of bike-share rides per day over one year, and how well can we predict ridership for days we haven't seen?

## 3. Supporting questions
* **Describe:** What is typical daily ridership, and how does it vary across the year?
* **Compare:** Are weekends different from weekdays, and by how much (with uncertainty)?
* **Relate:** How strongly are rides related to temperature, and does rain matter once temperature is accounted for?
* **Predict:** Can a simple model predict the next two months well, and does a more complex one do any better?

## 4. Data
| | Option A | Option B |
|---|---|---|
| Name & link | `daily_rides.csv` (course bundle, synthetic) | A real city's public trip data (would need aggregation and weather joined from another source) |
| Rows × columns | 366 × 5 | millions of trips |
| Columns needed for my question | all present | would need building |
| Missing / messy parts | 6 missing temperatures | much more cleaning needed |
| Licence / terms | course repository | varies by city |

**Chosen dataset and why:** Option A: it contains exactly what the question needs and is small enough to show the whole workflow clearly. A real dataset would be a natural next step.

## 5. Plan
Describe, then compare weekends, then relate to temperature and rain, then compare predictive models on a chronological holdout.
A *surprising* result would be rain having a clear effect despite a near-zero raw correlation. (Planned comparisons: weekend vs weekday; the three coefficients in one regression; three models. Nothing else will be tested.)
What might go wrong: the temperature gaps, one year of data only, a flexible model overfitting a small dataset.

## 6. Success criteria
I can answer each of the four questions with a chart and a number, say how uncertain each is, reproduce everything with one command from a fresh clone, and have tests that pass.
