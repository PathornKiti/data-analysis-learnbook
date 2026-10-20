# Module X4 (extension): Time-series analysis and inference

**Time:** ~2 weeks (8–10 h) · **Prerequisites:** Modules 8 and 8b (regression, standard errors, p-values), 7 (variance) · **Use it when:** your data are ordered in time (monthly sales, daily temperature, sensor readings, prices, repeated surveys of the same unit) and you want trend/seasonality, a valid test, or a forecast

## Learning goals
* Split a series into **trend, seasonal and remainder** with a centred moving average and seasonal indices, **by hand**, and match a library
* Compute and read the **ACF and PACF**; explain why independence fails for ordered data
* Quantify the damage: **effective sample size** $n\frac{1-\phi}{1+\phi}$, the **Durbin–Watson** statistic, naive vs **HAC** standard errors, and a simulation of false-positive rates
* Recognise **non-stationarity** (trend, random walk), use **differencing** and the **ADF** test (in the right direction), and explain **spurious regression**
* Fit an **AR(1)** by least squares and forecast with its uncertainty; fit a **regression with AR errors** (Cochrane–Orcutt) and compare with a library
* Evaluate forecasts on a **chronological** hold-out against **naive and seasonal-naive baselines** with MAE, RMSE and MASE
* Write the analysis up honestly (what was assumed, what was checked, how far the results can be trusted)

## Files
| file | purpose |
|---|---|
| `lesson.ipynb` | components → decomposition by hand → ACF/PACF → why dependence breaks inference (simulation, Durbin–Watson, HAC) → stationarity and differencing → AR(1) → regression with AR errors → forecast evaluation → pitfalls and a reporting template |
| `exercises.ipynb` | 9 exercises: ACF, Durbin–Watson, effective sample size, AR(1) fit, AR(1) forecasts, baselines and MASE, decomposition, naive vs HAC standard errors, a validation-design question |
| `math-notes.md` | moving averages and seasonal indices, ACF, AR(1) moments, variance of a mean, Durbin–Watson, HAC, GLS/Cochrane–Orcutt, unit roots and spurious regression, forecast variance, accuracy measures, rolling origin |
| [`../../solutions/X4-time-series/`](../../solutions/X4-time-series/) | solutions |

(The data are the course's `monthly_demand.csv`: 144 synthetic months with a trend, yearly cycle, promotion flag and autocorrelated noise; see [`data/README.md`](../../data/README.md). Needs `statsmodels`, already used from Module 9.)

## Common pitfalls
* Treating ordered observations as independent: **standard errors too small, p-values too small**
* **Spurious regression** between trending series; differencing, or modelling the trend explicitly, before relating them
* Reading a **robust (HAC) standard error** as always larger, or as a fix for badly persistent series (it only helps when the series is long and the dependence moderate)
* The **ADF test** direction: a small p-value means stationary
* Shuffled train/test splits and tuning on the test period (**leakage**)
* Treating the decomposition remainder as "the noise" (it absorbs some dependence and the effects you did not model)
* Forecasts with no **baseline**, no horizon, no error measure, or intervals that ignore growing uncertainty
* Over-reading small differences between models on a short test set

## 🎯 Project checkpoint: **a time-series check of your own data**
1. If your project data have a time order, plot them and say in two sentences what you see: trend, seasonality, outliers, gaps, changes in level.
2. Decompose (by hand or `seasonal_decompose`) and report the seasonal pattern.
3. Compute the **ACF** of your main model's residuals and a **Durbin–Watson** statistic. If dependence is present, report **HAC** (or AR-errors) standard errors next to the naive ones and say which conclusions change.
4. If you relate two trending series, **difference them** (or model the trend) before testing, and say why.
5. If forecasting is a goal, hold out the **last** part of the series, compare with **naive and seasonal-naive** baselines, and report MAE and MASE.
6. Add tested functions to `src/<package>/timeseries.py` (e.g. an ACF checked against a hand-computed example, MASE with a known answer).
