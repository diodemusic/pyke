from typing import Any

from pyke import Region

from .._base_client import _BaseApiClient


class SummonerEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> dict[Any, Any]:
        """Get a summoner by PUUID.

        **Example:**  
            `api.summoner.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return data
