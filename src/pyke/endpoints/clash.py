from typing import Any

from pyke import Region

from .._base_client import _BaseApiClient


class ClashEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, region: Region, puuid: str) -> list[dict[Any, Any]]:
        """# Get players by puuid

        **Example:**  
            `players = api.clash.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = f"/lol/clash/v1/players/by-puuid/{puuid}"
        data = self._client._region_request(region=region, path=path)

        return data

    def by_team_id(self, region: Region, team_id: str) -> dict[Any, Any]:
        """# Get team by ID

        **Example:**  
            `team = api.clash.by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/clash/v1/teams/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return data

    def tournaments(self, region: Region) -> list[dict[Any, Any]]:
        """# Get all active or upcoming tournaments

        **Example:**  
            `tournaments = api.clash.tournaments(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `list[dict[Any, Any]]`
        """  # fmt: skip

        path = "/lol/clash/v1/tournaments"
        data = self._client._region_request(region=region, path=path)

        return data

    def tournament_by_team_id(self, region: Region, team_id: str) -> dict[Any, Any]:
        """# Get tournament by team ID

        **Example:**  
            `tournament = api.clash.tournament_by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/by-team/{team_id}"
        data = self._client._region_request(region=region, path=path)

        return data

    def tournament_by_tournament_id(
        self, region: Region, tournament_id: int
    ) -> dict[Any, Any]:
        """# Get tournament by ID

        **Example:**  
            `tournament = api.clash.tournament_by_tournament_id(Region.EUW, 12345)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `tournament_id (int)` Tournament id of the clash.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/{tournament_id}"
        data = self._client._region_request(region=region, path=path)

        return data
