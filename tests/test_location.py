import pytest
from weather.services.location import lat_long


@pytest.mark.asyncio
async def test_lat_long() -> None:
    assert await lat_long("97002", "us") == (45.224241, -122.8198)
