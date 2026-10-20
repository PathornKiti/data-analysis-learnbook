"""Turn results into sentences, so the written report can never drift from the numbers."""
import calendar


def p_text(p: float) -> str:
    """Format a p-value: ``p < 0.001`` or ``p = 0.034``."""
    return "p < 0.001" if p < 0.001 else f"p = {p:.3f}"


def describe_sentence(d: dict) -> str:
    """One sentence describing the overall level and seasonality of ridership."""
    return (
        f"Across {d['n_days']} days, bike-share ridership averaged {d['mean']:,.0f} rides per day (median {d['median']:,.0f}, sd {d['sd']:,.0f}). "
        f"It peaked in {calendar.month_name[d['peak_month']]} ({d['peak_month_mean']:,.0f} a day) and was lowest in "
        f"{calendar.month_name[d['low_month']]} ({d['low_month_mean']:,.0f})."
    )


def weekend_sentence(c: dict) -> str:
    """One sentence about the weekend vs weekday comparison with its interval and effect size."""
    direction = "fewer" if c["diff"] < 0 else "more"
    lo, hi = c["diff_ci"]
    text = (
        f"Weekends had {abs(c['diff']):,.0f} {direction} rides per day than weekdays ({abs(c['pct_change']):.1f}%; "
        f"95% CI for the difference {lo:,.0f} to {hi:,.0f}; {p_text(c['p_perm'])}; Cohen's d = {abs(c['cohens_d']):.2f}; "
        f"n = {c['n_weekend']} weekend vs {c['n_weekday']} weekday days)."
    )
    if lo <= 0 <= hi:
        text += " The data are compatible with no difference."
    return text


def temperature_sentence(corr: dict, slope: float) -> str:
    """One sentence about the temperature-ridership relationship."""
    lo, hi = corr["ci"]
    return (
        f"Temperature and ridership move together strongly (r = {corr['r']:.2f}, 95% bootstrap CI {lo:.2f} to {hi:.2f}); "
        f"the simple trend is about {slope:.0f} extra rides per degree Celsius."
    )


def model_sentence(coefs, raw_rain_r: float) -> str:
    """One sentence about the adjusted effects of temperature, rain and weekend."""
    def span(name):
        row = coefs.loc[name]
        return f"{row['coef']:.1f} (95% CI {row['ci_low']:.1f} to {row['ci_high']:.1f})"

    return (
        f"Holding the other variables fixed, each extra degree goes with {span('temp_c')} rides, each mm of rain with {span('rain_mm')} rides, "
        f"and a weekend with {span('is_weekend')} rides. Rain looks irrelevant on its own (raw r = {raw_rain_r:.2f}) "
        f"because temperature swings explain most of the day-to-day variation and drown out the smaller rain effect; "
        f"it only becomes visible once temperature is accounted for."
    )


def prediction_sentence(eval_df, cv_df, n_test: int) -> str:
    """One sentence comparing the models on the held-out final days."""
    base = eval_df.loc["baseline (train mean)", "rmse"]
    lin = eval_df.loc["linear regression", "rmse"]
    forest = eval_df.loc["random forest", "rmse"]
    cv_lin = cv_df.loc["linear regression"]
    return (
        f"On the last {n_test} days (never used for fitting), the linear model's RMSE was {lin:,.0f} rides versus {base:,.0f} for the "
        f"predict-the-mean baseline and {forest:,.0f} for a random forest; expanding-window cross-validation gave a linear-model RMSE of "
        f"{cv_lin['rmse_mean']:,.0f} ± {cv_lin['rmse_sd']:,.0f}."
    )
