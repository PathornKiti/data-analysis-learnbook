from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def rides_csv() -> Path:
    """Locate the course's data/daily_rides.csv by walking up from this file."""
    for folder in Path(__file__).resolve().parents:
        candidate = folder / "data" / "daily_rides.csv"
        if candidate.exists():
            return candidate
    pytest.fail("Could not find data/daily_rides.csv above the tests folder")
