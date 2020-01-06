from quart import Quart
from weather.services.weather import global_init
from weather.view import home, city

__version__: str = "0.5.2"
__author__: str = "Volodymyr Yahello"

application: Quart = Quart(__name__)
application.register_blueprint(home.blueprint)
application.register_blueprint(city.blueprint)


def run(key: str, bind: str = "0.0.0.0:5001", debug: bool = False) -> None:
    """Runs application in standalone mode."""
    global_init(key)
    host, port = bind.split(":")
    application.run(host, port, debug)
