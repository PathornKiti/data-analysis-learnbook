import json
from pathlib import Path

import pytest

from ridership.pipeline import run

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def results(tmp_path_factory):
    out = tmp_path_factory.mktemp("project")
    res = run(ROOT / "data" / "raw" / "daily_rides.csv", out, make_figures=False)
    res["_out"] = out
    return res


def test_headline_numbers(results):
    assert results["n_raw"] == 366 and results["n_missing_temp"] == 6
    assert results["describe"]["peak_month"] == 7 and results["describe"]["low_month"] == 1
    assert results["weekend"]["pct_change"] == pytest.approx(-10.8, abs=0.1)
    assert results["temp_corr"]["r"] == pytest.approx(0.96, abs=0.01)
    assert results["rain_raw_r"] == pytest.approx(-0.02, abs=0.02)
    rain = results["coefficients"]["rain_mm"]
    assert rain["ci_high"] < 0, "after adjusting for temperature the rain effect is clearly negative"
    assert results["coefficients"]["temp_c"]["coef"] == pytest.approx(54.6, abs=1.0)


def test_linear_model_beats_baseline_and_forest_on_the_final_days(results):
    ev = results["model_eval"]
    assert ev["linear regression"]["rmse"] < ev["baseline (train mean)"]["rmse"] / 4
    assert ev["linear regression"]["rmse"] < ev["random forest"]["rmse"]


def test_imputed_temperatures_do_not_drive_the_result(results):
    assert results["sensitivity_temp_coef"] == pytest.approx(results["adjusted_temp_slope"], abs=1.5)


def test_outputs_are_written(results):
    out = results["_out"]
    assert (out / "data" / "processed" / "rides_clean.csv").exists()
    assert json.loads((out / "reports" / "results.json").read_text())["n_raw"] == 366
    assert "Weekends had" in (out / "reports" / "results.md").read_text()


def test_readme_findings_match_the_computed_numbers(results):
    readme = (ROOT / "README.md").read_text().replace("\u2212", "-")   # allow the typographic minus sign
    d, w = results["describe"], results["weekend"]
    assert f"{d['mean']:,.0f}" in readme, "mean rides in the README is out of date"
    assert f"{abs(w['pct_change']):.1f}%" in readme, "weekend effect in the README is out of date"
    assert f"{results['temp_corr']['r']:.2f}" in readme, "temperature correlation in the README is out of date"
    assert f"{results['coefficients']['rain_mm']['coef']:.1f}" in readme, "rain coefficient in the README is out of date"
    lin = results["model_eval"]["linear regression"]["rmse"]
    assert f"{lin:,.0f}" in readme, "model RMSE in the README is out of date"
