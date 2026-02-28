from typing import Any

from .._base_riot_client import _BaseRiotClient
from ..enums.continent import Continent


class AccountEndpoint:
    """There are three routing values for account-v1; americas, asia, and europe. You can query for any account in any region. We recommend using the nearest cluster."""

    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def by_puuid(self, continent: Continent, puuid: str) -> dict[Any, Any]:
        """# Get account by puuid

        **Example:**  
            `account = await api.account.by_puuid(Continent.EUROPE, "some puuid")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = await self._client._request(continent=continent, path=path)

        return data

    async def by_riot_id(
        self, continent: Continent, game_name: str, tag_line: str
    ) -> dict[Any, Any]:
        """# Get account by riot id

        **Example:**  
            `account = await api.account.by_riot_id(Continent.EUROPE, "saves", "000")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `game_name (str)` Riot id game name.  
            `tag_line (str)` Riot id tag line.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        data = await self._client._request(continent=continent, path=path)

        return data

    async def region_by_puuid(self, continent: Continent, puuid: str) -> dict[Any, Any]:
        """# Get active region (lol and tft)

        **Example:**  
            `region = await api.account.region_by_puuid(Continent.EUROPE, "some puuid")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/riot/account/v1/region/by-game/lol/by-puuid/{puuid}"
        data = await self._client._request(continent=continent, path=path)

        return data
