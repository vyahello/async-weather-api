from typing import Dict, Any
import quart
from weather.services import sun, location, weather

blueprint: quart.blueprints.Blueprint = quart.blueprints.Blueprint(__name__, __name__)


@blueprint.route("/api/events/<city>/<state>/<country>", methods=["GET"])
async def events(city: str, state: str, country: str) -> quart.Response:
    """Returns current weather event."""
    player = {
        "name": "Jeff the player",
        "city": city,
        "state": state,
        "country": country,
    }
    if not player:
        quart.abort(404)
    return quart.jsonify(player)


@blueprint.route("/api/weather/<zip_code>/<country>", methods=["GET"])
async def weather_(zip_code: str, country: str) -> quart.Response:
    """Returns current weather."""
    data: Dict[str, Any] = await weather.now(zip_code, country)
    if not data:
        quart.abort(404)
    return quart.jsonify(data)


@blueprint.route("/api/sun/<zip_code>/<country>", methods=["GET"])
async def sun_(zip_code: str, country: str) -> quart.Response:
    """Returns current sunrise/sunset."""
    lat, long = await location.lat_long(zip_code, country)
    data: Dict[str, Any] = await sun.today(lat, long)
    if not data:
        quart.abort(404)
    return quart.jsonify(data)
