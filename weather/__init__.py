from typing import NamedTuple
from quart import Quart
from weather.services.weather import global_init
from weather.view import home, city

__version__: str = "0.5.2"
__author__: str = "Volodymyr Yahello"

application: Quart = Quart(__name__)
application.register_blueprint(home.blueprint)
application.register_blueprint(city.blueprint)


class Bind(NamedTuple):
    """Returns address bind (e.g `0.0.0.0:5000`) list of user's arguments."""

    host: str = "0.0.0.0"
    port: int = 5000

    def __str__(self) -> str:
        """Returns binding address as a string."""
        return f"{self.host}:{self.port}"


def run(key: str, bind: Bind = Bind(), debug: bool = False) -> None:
    """Runs application in standalone mode."""
    global_init(key)
    application.run(*bind, debug=debug)
