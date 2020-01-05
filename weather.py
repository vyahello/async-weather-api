"""Main weather application api entrypoint."""
from typing import Dict, Any
from flask import Flask
from weather.config import settings
from weather.services.weather import global_init
from weather.view import home, city

_is_debug: bool = False
_application: Flask = Flask(__name__)

_application.register_blueprint(home.blueprint)
_application.register_blueprint(city.blueprint)


def _configure_weather() -> None:
    """Performs pre-setup for weather app."""
    data: Dict[str, Any] = settings.load("dev" if _is_debug else "prod")
    global_init(data.get("weather_key"))


def _run_weather() -> None:
    """Runs weather app."""
    _configure_weather()
    _application.run(host="0.0.0.0", debug=_is_debug, port=5001)


if __name__ == "__main__":
    _run_weather()
