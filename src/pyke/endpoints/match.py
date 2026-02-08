from __future__ import annotations

from typing import Any

from pyke import Continent, Type

from .. import exceptions
from .._base_client import _BaseApiClient


class MatchEndpoint:
    """The AMERICAS routing value serves NA, BR, LAN and LAS. The ASIA routing value serves KR and JP. The EUROPE routing value serves EUNE, EUW, ME1, TR and RU. The SEA routing value serves OCE, SG2, TW2 and VN2."""

    def __init__(self, client: _BaseApiClient):
        self._client = client

    def match_ids_by_puuid(
        self,
        continent: Continent,
        puuid: str,
        start_time: int | None = None,
        end_time: int | None = None,
        queue: int | None = None,
        type: Type | None = None,
        start: int | None = None,
        count: int | None = None,
    ) -> list[str]:
        """# Get a list of match ids by puuid

        **Example:**  
            `match_ids = api.match.match_ids_by_puuid(Continent.EUROPE, "some puuid")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  
            `start_time (int | None, optional)` Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set. Defaults to None.  
            `end_time (int | None, optional)` Epoch timestamp in seconds. Defaults to None.  
            `queue (int | None, optional)` Filter the list of match ids by a specific queue id. This filter is mutually inclusive of the type filter meaning any match ids returned must match both the queue and type filters. Defaults to None.  
            `type (Type | None, optional)` Filter the list of match ids by the [Type](/pyke/pyke.html#Type) of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters. Defaults to None.  
            `start (int | None, optional)` Start index. Defaults to 0.  
            `count (int | None, optional)` Valid values: 0 to 100. Number of match ids to return. Defaults to 20.  

        **Returns:**  
            `list[str]` List of match id strings.
        """  # fmt: skip

        path = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"

        if type:
            type_str = type.value
        else:
            type_str = None

        params = {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type_str,
            "start": start,
            "count": count,
        }
        params = {k: v for k, v in params.items() if v is not None}
        data = self._client._continent_request(
            continent=continent, path=path, params=params
        )

        if not isinstance(data, list):
            raise exceptions.DataNotFound(
                message="Expected list of match IDs but received invalid response format",
                error_code=404,
            )

        if not all(
            isinstance(item, str)
            for item in data  # pyright: ignore[reportUnknownVariableType]
        ):
            raise exceptions.DataNotFound(
                message="Match ID list contains non-string values", error_code=404
            )

        return data  # pyright: ignore[reportUnknownVariableType]

    def by_match_id(self, continent: Continent, match_id: str) -> dict[Any, Any]:
        """# Get a match by match id

        **Example:**  
            `match = api.match.by_match_id(Continent.EUROPE, "EUW1_1234567890")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `match_id (str)` Match id string.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/match/v5/matches/{match_id}"
        data = self._client._continent_request(continent=continent, path=path)

        return data

    def timeline_by_match_id(
        self, continent: Continent, match_id: str
    ) -> dict[Any, Any]:
        """# Get a match timeline by match id

        **Example:**  
            `timeline = api.match.timeline_by_match_id(Continent.EUROPE, "EUW1_1234567890")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `match_id (str)` Match id string.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = f"/lol/match/v5/matches/{match_id}/timeline"
        data = self._client._continent_request(continent=continent, path=path)

        return data
