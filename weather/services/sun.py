import datetime
import time
import requests


def _utc_to_local(date: str) -> datetime.datetime:
    """Converts utl to local datetime."""
    now_timestamp = time.time()
    return datetime.datetime.strptime(date, "%I:%M:%S %p") + (
        datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    )


def today(latitude: float, longitude: float) -> dict:
    """Returns sunrise/sunset for today."""
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}")
    response.raise_for_status()
    sun_data = response.json().get("results", {})
    for key, value in tuple(sun_data.items()):  # type: str, str
        if "AM" not in value and "PM" not in value:
            continue
        sun_data[key] = datetime.datetime.strftime(_utc_to_local(value), "%I:%M:%S %p")
    return sun_data

