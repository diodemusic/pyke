from typing import Any

from .._base_client import _BaseApiClient
from ..enums.level import Level
from ..enums.region import Region


class ChallengesEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    async def config(self, region: Region) -> list[dict[Any, Any]]:
        """# List of all basic challenge configuration information (includes all translations for names and descriptions)

        **Example:**  
            `configs = await api.lol_challenges.config(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/config"
        data = await self._client._region_request(region=region, path=path)

        return data

    async def percentiles(self, region: Region) -> dict[Any, Any]:
        """# Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

        **Example:**  
            `percentiles = await api.lol_challenges.percentiles(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = "/lol/challenges/v1/challenges/percentiles"
        data = await self._client._region_request(region=region, path=path)

        return data

    async def config_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> dict[Any, Any]:
        """# Get challenge configuration (REST)

        **Example:**  
            `config = await api.lol_challenges.config_by_challenge_id(Region.EUW, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/config"
        data = await self._client._region_request(region=region, path=path)

        return data

    async def leaderboards_by_level(
        self, region: Region, level: Level, challenge_id: int
    ) -> list[dict[Any, Any]]:
        """# Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER

        **Example:**  
            `players = await api.lol_challenges.leaderboards_by_level(Region.EUW, Level.MASTER, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `level (Level)` Challenge [Level](/pyke/pyke.html#Level).  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level.value}"
        data = await self._client._region_request(region=region, path=path)

        return data

    async def percentiles_by_challenge_id(
        self, region: Region, challenge_id: int
    ) -> dict[str, float]:
        """# Map of level to percentile of players who have achieved it

        **Example:**  
            `percentiles = await api.lol_challenges.percentiles_by_challenge_id(Region.EUW, 123456)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `challenge_id (int)` Challenge id integer.  

        **Returns:**  
            `dict[str, float]`
        """  # fmt: skip

        path = f"/lol/challenges/v1/challenges/{challenge_id}/percentiles"
        data = await self._client._region_request(region=region, path=path)

        return data

    async def by_puuid(self, region: Region, puuid: str) -> dict[Any, Any]:
        """# Returns player information with list of all progressed challenges (REST)

        **Example:**  
            `player_info = await api.lol_challenges.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/challenges/v1/player-data/{puuid}"
        data = await self._client._region_request(region=region, path=path)

        return data
