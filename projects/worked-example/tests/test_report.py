from ridership.report import p_text, weekend_sentence


def test_p_text():
    assert p_text(0.0004) == "p < 0.001"
    assert p_text(0.0724) == "p = 0.072"


def comparison(ci):
    return {"diff": -168.0, "pct_change": -10.8, "diff_ci": ci, "p_perm": 0.005, "cohens_d": -0.33, "n_weekend": 104, "n_weekday": 262}


def test_weekend_sentence_states_direction_size_and_uncertainty():
    s = weekend_sentence(comparison((-284.0, -51.0)))
    assert "168 fewer" in s and "10.8%" in s and "-284 to -51" in s and "n = 104" in s
    assert "compatible with no difference" not in s


def test_weekend_sentence_hedges_when_interval_includes_zero():
    assert "compatible with no difference" in weekend_sentence(comparison((-300.0, 20.0)))
