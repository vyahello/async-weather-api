import os
import json
from typing import Dict, Any


def _absolute_filepath(name: str, extension: str) -> str:
    """Returns file name by it's prefix."""
    return os.path.join(os.path.dirname(__file__), f"{name}.{extension}")


def load(mode: str = "dev") -> Dict[str, Any]:
    """Loads configuration file."""
    if not os.path.exists(_absolute_filepath(mode, "json")):
        raise RuntimeError(f"Config not found for {mode}.")

    with open(_absolute_filepath(mode, "json"), "r", encoding="utf-8") as final:
        return json.load(final)
