from typing import Any

from .._base_riot_client import _BaseRiotClient
from ..enums.division import Division
from ..enums.queue import Queue
from ..enums.region import Region
from ..enums.tier import Tier


class LeagueEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def challenger_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> dict[Any, Any]:
        """# Get the challenger league for given queue

        **Example:**  
            `leagues = await api.league.challenger_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/league/v4/challengerleagues/by-queue/{queue.value}"
        data = await self._client._request(region=region, path=path)

        return data

    async def by_puuid(self, region: Region, puuid: str) -> list[dict[Any, Any]]:
        """# Get league entries in all queues for a given puuid

        **Example:**  
            `entries = await api.league.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = f"/lol/league/v4/entries/by-puuid/{puuid}"
        data = await self._client._request(region=region, path=path)

        return data

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
            `entries = await api.league.by_queue_tier_division(Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  
            `tier (Tier)` Ranked [Tier](/pyke/pyke.html#Tier).  
            `division (Division)` Ranked [Division](/pyke/pyke.html#Division).  
            `page (int, optional)` Starts with page 1. Defaults to 1.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = f"/lol/league/v4/entries/{queue.value}/{tier.value}/{division.value}"
        params = {"page": page}
        data = await self._client._request(region=region, path=path, params=params)

        return data

    async def grandmaster_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> dict[Any, Any]:
        """# Get the grandmaster league for given queue

        **Example:**  
            `leagues = await api.league.grandmaster_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/league/v4/grandmasterleagues/by-queue/{queue.value}"
        data = await self._client._request(region=region, path=path)

        return data

    async def by_league_id(self, region: Region, league_id: str) -> dict[Any, Any]:
        """# Get league with given ID, including inactive entries

        **Example:**  
            `leagues = await api.league.by_league_id(Region.EUW, "some league id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `league_id (str)` League id.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/league/v4/leagues/{league_id}"
        data = await self._client._request(region=region, path=path)

        return data

    async def master_leagues_by_queue(
        self,
        region: Region,
        queue: Queue,
    ) -> dict[Any, Any]:
        """# Get the master league for given queue

        **Example:**  
            `leagues = await api.league.master_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `queue (Queue)` Ranked [Queue](/pyke/pyke.html#Queue) type.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/league/v4/masterleagues/by-queue/{queue.value}"
        data = await self._client._request(region=region, path=path)

        return data
