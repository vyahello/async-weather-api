from typing import Sequence, Dict, Any
import requests


def lat_long(zip_code: str, country: str) -> Sequence[float]:
    """Returns latitude and longitude."""
    key: str = f'{zip_code}, {country}'
    response = requests.get(f'http://www.datasciencetoolkit.org/street2coordinates/{key.replace(" ", "+")}')
    response.raise_for_status()
    city: Dict[str, Any] = response.json().get(f"{zip_code}, {country}", dict())
    return city.get("latitude", 0.00), city.get("longitude", 0.00)
