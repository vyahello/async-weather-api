import datetime
import pytest
from weather.services.sun import _utc_to_local, today


def test_utc_to_local() -> None:
    assert isinstance(_utc_to_local("2:29:50 AM"), datetime.datetime)


@pytest.mark.asyncio
async def test_today() -> None:
    assert isinstance(await today(4.122, -122.31), dict)
