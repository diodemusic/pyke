from typing import Any

from pyke import Region

from .._base_client import _BaseApiClient


class SpectatorEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> dict[Any, Any]:
        """# Get current game information for the given puuid

        **Example:**  
            `current_game = api.spectator.by_puuid(Region.EUW, "some puuid")`

        **Args:**
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.

        **Returns:**
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/spectator/v5/active-games/by-summoner/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return data
