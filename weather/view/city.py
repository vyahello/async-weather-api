from typing import Dict, Any
import flask
from weather.services import sun, location, weather

blueprint: flask.blueprints.Blueprint = flask.blueprints.Blueprint(__name__, __name__)


@blueprint.route("/api/events/<city>/<state>/<country>", methods=("GET",))
def events(city: str, state: str, country: str) -> Dict[str, Any]:
    """Returns current weather event."""
    player = {
        "name": "Jeff the player",
        "city": city,
        "state": state,
        "country": country,
    }
    if not player:
        flask.abort(404)
    return flask.jsonify(player)


@blueprint.route("/api/weather/<zip_code>/<country>", methods=("GET",))
def weather_(zip_code: str, country: str) -> Dict[str, Any]:
    """Returns current weather."""
    data: Dict[str, Any] = weather.now(zip_code, country)
    if not data:
        flask.abort(404)
    return flask.jsonify(data)


@blueprint.route("/api/sun/<zip_code>/<country>", methods=("GET",))
def sun_(zip_code: str, country: str) -> Dict[str, Any]:
    """Returns current sunrise/sunset."""
    lat, long = location.lat_long(zip_code, country)
    data: Dict[str, Any] = sun.today(lat, long)
    if not data:
        flask.abort(404)
    return flask.jsonify(data)
