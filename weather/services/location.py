from typing import Sequence, Dict, Any
import aiohttp


async def lat_long(zip_code: str, country: str) -> Sequence[float]:
    """Returns latitude and longitude."""
    key: str = f"{zip_code}, {country}"
    url: str = f'http://www.datasciencetoolkit.org/street2coordinates/{key.replace(" ", "+")}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()

    city: Dict[str, Any] = data.get(f"{zip_code}, {country}", dict())
    return city.get("latitude", 0.00), city.get("longitude", 0.00)
