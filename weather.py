"""Main weather application api entrypoint."""
from typing import Dict, Any
from flask import Flask
from weather.config import settings
from weather.services.weather import global_init
from weather.view import home

is_debug: bool = False
application: Flask = Flask(__name__)
application.register_blueprint(home.blueprint)


def _configure_weather() -> None:
    """Performs pre-setup for weather app."""
    data: Dict[str, Any] = settings.load("dev" if is_debug else "prod")
    global_init(data.get("weather_key"))


def _run_weather() -> None:
    """Runs weather app."""
    application.run(host="0.0.0.0", debug=is_debug, port=5001)


if __name__ == "__main__":
    _run_weather()
