from weather.services.location import lat_long


def test_lat_long() -> None:
    assert lat_long("97002", "us") == (45.224241, -122.8198)
