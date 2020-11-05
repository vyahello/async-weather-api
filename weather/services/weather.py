from typing import Dict, Any
import aiohttp

_KEY: str = ""


def global_init(api_key: str) -> None:
    """Initializes a service."""
    global _KEY
    _KEY = api_key

    if not _KEY:
        print("Warning: No weather API key.")
        print(
            "If you want the weather part of the API to work, please get your own API key (free)."
        )
        print(
            "It's available at https://api.openweathermap.org -- just sign up."
        )
        print()


async def now(zip_code: str, country_code: str) -> Dict[str, Any]:
    """Obtains weather using zip and country codes."""
    url: str = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
