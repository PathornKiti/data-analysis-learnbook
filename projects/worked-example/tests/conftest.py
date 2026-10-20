from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def real_rides_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "raw" / "daily_rides.csv"
