from typing import Any

from .._base_riot_client import _BaseRiotClient
from ..enums.region import Region


class SpectatorEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def by_puuid(self, region: Region, puuid: str) -> dict[Any, Any]:
        """# Get current game information for the given puuid

        **Example:**  
            `current_game = await api.spectator.by_puuid(Region.EUW, "some puuid")`

        **Args:**
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.

        **Returns:**
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/spectator/v5/active-games/by-summoner/{puuid}"
        data = await self._client._request(region=region, path=path)

        return data
