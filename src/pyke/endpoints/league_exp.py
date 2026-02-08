from __future__ import annotations

from typing import Any

from pyke import Division, Queue, Region, Tier

from .._base_client import _BaseApiClient


class LeagueExpEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_queue_tier_division(
        self,
        region: Region,
        queue: Queue,
        tier: Tier,
        division: Division,
        page: int | None = None,
    ) -> list[dict[Any, Any]]:
        """# Get all the league entries

        **Example:**  
        `entries = api.league_exp.by_queue_tier_division(Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II)`

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
        data = self._client._region_request(region=region, path=path, params=params)

        return data
