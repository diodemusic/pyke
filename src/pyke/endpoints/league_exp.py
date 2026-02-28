from typing import Any

from .._base_riot_client import _BaseRiotClient
from ..enums.division import Division
from ..enums.queue import Queue
from ..enums.region import Region
from ..enums.tier import Tier


class LeagueExpEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def by_queue_tier_division(
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int = 1,
    ) -> list[dict[Any, Any]]:
        """# Get all the league entries

        **Example:**  
        `entries = await api.league_exp.by_queue_tier_division(Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  
            `tier (Tier)` Ranked [Tier](/pyke/pyke.html#Tier).  
            `division (Division)` Ranked [Division](/pyke/pyke.html#Division).  
            `page (int, optional)` Starts with page 1. Defaults to 1.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = f"/lol/league-exp/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"page": page}
        data = await self._client._request(region=region, path=path, params=params)

        return data
