import os
import pytest
from weather.config.settings import load, _absolute_filepath


def test_absolute_path() -> None:
    assert _absolute_filepath("fake", "txt") == os.path.abspath("weather/config/fake.txt")


@pytest.mark.parametrize(
    "mode, result", (("dev", {"dev": True, "weather_key": ""}), ("prod", {"dev": False, "weather_key": ""}))
)
def test_load(mode: str, result: dict) -> None:
    assert load(mode) == result


def test_load_error() -> None:
    with pytest.raises(RuntimeError):
        load("fake")
