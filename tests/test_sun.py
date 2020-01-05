import datetime
from weather.services.sun import _utc_to_local


def test_utc_to_local() -> None:
    assert isinstance(_utc_to_local("2:29:50 AM"), datetime.datetime)
