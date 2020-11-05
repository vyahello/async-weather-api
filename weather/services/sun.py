import datetime
import time
from typing import Dict
import aiohttp


def _utc_to_local(date: str) -> datetime.datetime:
    """Converts utl to local datetime."""
    now_timestamp = time.time()
    return datetime.datetime.strptime(date, "%I:%M:%S %p") + (
        datetime.datetime.fromtimestamp(now_timestamp)
        - datetime.datetime.utcfromtimestamp(now_timestamp)
    )


async def today(latitude: float, longitude: float) -> Dict[str, str]:
    """Returns sunrise/sunset for today."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}"
        ) as response:
            response.raise_for_status()
            data = await response.json()

    sun_data = data.get("results", {})
    for key, value in tuple(sun_data.items()):  # type: str, str
        if "AM" not in value and "PM" not in value:
            continue
        sun_data[key] = datetime.datetime.strftime(
            _utc_to_local(value), "%I:%M:%S %p"
        )
    return sun_data
