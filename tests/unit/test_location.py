from tests.markers import unit, async_
from weather.services.location import lat_long

pytestmark = [unit, async_]


async def test_lat_long() -> None:
    assert await lat_long("97002", "us") == (45.224241, -122.8198)
