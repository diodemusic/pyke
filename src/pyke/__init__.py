"""# pyke

[![PyPI - Version](https://img.shields.io/pypi/v/pyke-lol)](https://pypi.org/project/pyke-lol/)
[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://diodemusic.github.io/pyke/)

**pyke** is a thin async Riot API wrapper for League of Legends.

## Installation

Install the latest version directly from PyPI:

```bash
pip install pyke-lol
```

> You need Python 3.10+

---

## Quickstart

```py
import asyncio

from pyke import Continent, Pyke, exceptions

async def main() -> None:
    # Initialize the API
    async with Pyke("RGAPI-...", timeout=60, print_url=True) as api:
        # Every pyke method follows the same convention as the Riot API
        # For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
        account = await api.account.by_riot_id(Continent.EUROPE, "saves", "000")

        print(f"Riot ID: {account['gameName']}#{account['tagLine']}")
        print(f"PUUID:   {account['puuid']}")

        # pyke throws typed exceptions matching Riot API error codes
        try:
            region = await api.account.region_by_puuid(
                Continent.EUROPE, account["puuid"]
            )
        except exceptions.DataNotFound as e:
            print(e)  # Output: Data not found (Error Code: 404)
            quit()

        print(f"Region:  {region['region']}")
```

## Custom Exception Handling

Typed exceptions for all HTTP status codes:

```py
from pyke import exceptions

try:
    summoner = await api.summoner.by_puuid(Region.EUW, "NonExistentPuuid")
except exceptions.DataNotFound as e:
    print(f"Not found: {e}")     # Data not found (Error Code: 404)
except exceptions.RateLimitExceeded as e:
    print(f"Rate limited: {e}")  # Rate limit exceeded (Error Code: 429)
except exceptions.InternalServerError as e:
    print(f"Server error: {e}")  # Internal server error (Error Code: 500)
```

## Resources

- **[API Documentation](https://diodemusic.github.io/pyke/pyke.html)**
- **[Examples Directory](https://github.com/diodemusic/pyke/tree/master/examples)**
- **[PyPI Package](https://pypi.org/project/pyke-lol/)**
- **[GitHub Repository](https://github.com/diodemusic/pyke)**

---

For any questions or help, please reach out on Discord: `.irm`
"""

from . import ddragon, endpoints, enums, exceptions
from .__version__ import __author__, __title__, __version__
from .enums.continent import Continent
from .enums.division import Division
from .enums.level import Level
from .enums.match_type import MatchType
from .enums.queue import Queue
from .enums.region import Region
from .enums.tier import Tier
from .main import DataDragon, Pyke

__all__ = [
    "ddragon",
    "exceptions",
    "Continent",
    "Division",
    "Level",
    "Queue",
    "Region",
    "Tier",
    "MatchType",
    "DataDragon",
    "Pyke",
    "__author__",
    "__title__",
    "__version__",
    "endpoints",
    "enums",
]
