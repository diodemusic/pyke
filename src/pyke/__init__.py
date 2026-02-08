"""# pyke

[![PyPI - Version](https://img.shields.io/pypi/v/pyke-lol)](https://pypi.org/project/pyke-lol/)
[![Documentation](https://img.shields.io/badge/Documentation-blue)](https://diodemusic.github.io/pyke/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyke-lol)](https://pypi.org/project/pyke-lol/)
![Coverage](https://img.shields.io/badge/Coverage-94%25-brightgreen.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt)

**pyke** is a thin async first Riot API wrapper specifically designed for League of Legends.

## Key Features

- **Pythonic API** - Clean, intuitive interface that mirrors Riot's API structure exactly
- **Production Logging** - Standard Python logging integration with configurable levels

---

## Installation

Install the latest version directly from PyPI:

```bash
pip install pyke-lol
```

> **Note:** You need Python 3.9+ to use pyke.

---

## Quickstart

```py
from pyke import Continent, Pyke, exceptions

# Initialize the API
api = Pyke("RGAPI-...")

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

print(f"Riot ID: {account['gameName']}#{account['tagLine']}")
print(f"PUUID:   {account['puuid']}")

# pyke throws typed exceptions matching Riot API error codes
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account["puuid"])
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()
```

---

## Configuration

pyke offers timeout configuration:

```py
from pyke import Pyke

api = Pyke(
    api_key="RGAPI-...",
    timeout=60,                    # Request timeout in seconds (default: 60)
)
```

---

## Logging

pyke uses Python's standard `logging` module for comprehensive diagnostics:

```py
import logging
from pyke import Pyke

# Configure logging before creating Pyke instance
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

api = Pyke("RGAPI-...")
```

### Log Levels

- **DEBUG:** Detailed diagnostic information
- **INFO:** Request URLs with rate limit tracking: `(45/100) - https://na1.api.riotgames.com/...`
- **WARNING:** Retries, rate limiting, malformed API responses
- **ERROR:** Critical failures

### Common Configurations

```py
# Production (quiet) - only warnings and errors
logging.basicConfig(level=logging.WARNING)

# Development (verbose) - see all requests
logging.basicConfig(level=logging.INFO)

# Debugging - maximum verbosity
logging.basicConfig(level=logging.DEBUG)

# Completely silent
logging.getLogger('pyke').setLevel(logging.CRITICAL)

# Log to file
logging.basicConfig(
    level=logging.INFO,
    filename="api_requests.log",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
```

---

## Advanced Features

### Custom Exception Handling

pyke provides typed exceptions for all HTTP status codes:

```py
from pyke import exceptions

try:
    summoner = api.summoner.by_puuid(Region.EUW, "NonExistentPuuid")
except exceptions.DataNotFound as e:
    print(f"Not found: {e}")     # Data not found (Error Code: 404)
except exceptions.RateLimitExceeded as e:
    print(f"Rate limited: {e}")  # Rate limit exceeded after 5 retries (Error Code: 429)
except exceptions.InternalServerError as e:
    print(f"Server error: {e}")  # Internal server error (Error Code: 500)
```

**Available exceptions:**
`BadRequest` (400), `Unauthorized` (401), `Forbidden` (403), `DataNotFound` (404), `MethodNotAllowed` (405), `UnsupportedMediaType` (415), `RateLimitExceeded` (429), `InternalServerError` (500), `BadGateway` (502), `ServiceUnavailable` (503), `GatewayTimeout` (504)

### Continental vs Regional Routing

pyke automatically handles Riot's routing requirements:

```py
from pyke import Continent, Region

# Continental routing (Account-V1, Match-V5)
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Regional routing (Summoner-V4, League-V4, etc.)
summoner = api.summoner.by_puuid(Region.EUW, account.puuid)
```

**Continental Routing:**

- `AMERICAS`: NA, BR, LAN, LAS
- `ASIA`: KR, JP
- `EUROPE`: EUNE, EUW, ME1, TR, RU
- `SEA`: OCE, SG2, TW2, VN2

---

## Complete Feature List

- **Production Logging** - Standard Python logging with configurable levels
- **Custom Exceptions** - 11 typed exception classes for precise error handling
- **Continental Routing** - Automatic routing for Account/Match endpoints
- **Configurable Timeouts** - Adjust request timeouts for slow endpoints
- **Mirror API Design** - Intuitive mapping to Riot's API structure
- **Pythonic Interface** - Clean, idiomatic Python code
- **94% Test Coverage** - Comprehensive integration test suite
- **Python 3.9-3.14** - Tested across 6 Python versions

---

## Documentation & Resources

- **[API Documentation](https://diodemusic.github.io/pyke/pyke.html)** - Complete API reference with examples
- **[Examples Directory](https://github.com/diodemusic/pyke/tree/master/examples)** - 15+ working examples covering all features
- **[PyPI Package](https://pypi.org/project/pyke-lol/)** - Official package distribution
- **[GitHub Repository](https://github.com/diodemusic/pyke)** - Source code and issue tracking

---

## Contributing & Support

Found a bug or have a feature request? Open an issue on [GitHub](https://github.com/diodemusic/pyke/issues).

For any questions or help, please reach out on Discord: `.irm`

---

## License

MIT License - see [LICENSE.txt](https://github.com/diodemusic/pyke/blob/main/LICENCE.txt) for details.
"""

from . import ddragon, endpoints, enums, exceptions
from .__version__ import __author__, __title__, __version__
from .enums.continent import Continent
from .enums.division import Division
from .enums.level import Level
from .enums.queue import Queue
from .enums.region import Region
from .enums.tier import Tier
from .enums.type import Type
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
    "Type",
    "DataDragon",
    "Pyke",
    "__author__",
    "__title__",
    "__version__",
    "endpoints",
    "enums",
]
