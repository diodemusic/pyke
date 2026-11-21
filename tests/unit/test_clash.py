import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/clash/v1"
PUUID = "a" * 78
TEAM_ID = "some-team-id"
TOURNAMENT_ID = 12345


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/players/by-puuid/{PUUID}").mock(
        return_value=Response(
            200, json=[{"puuid": PUUID, "teamId": TEAM_ID, "position": "CAPTAIN"}]
        )
    )

    result = await pyke_client.clash.by_puuid(Region.EUW, PUUID)

    assert isinstance(result, list)
    assert result[0]["teamId"] == TEAM_ID


@pytest.mark.asyncio
async def test_by_team_id(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/teams/{TEAM_ID}").mock(
        return_value=Response(
            200,
            json={"id": TEAM_ID, "tournamentId": TOURNAMENT_ID, "name": "Test Team"},
        )
    )

    result = await pyke_client.clash.by_team_id(Region.EUW, TEAM_ID)

    assert result["id"] == TEAM_ID
    assert result["name"] == "Test Team"


@pytest.mark.asyncio
async def test_tournaments(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/tournaments").mock(
        return_value=Response(
            200,
            json=[{"id": TOURNAMENT_ID, "themeId": 1, "nameKey": "test_tournament"}],
        )
    )

    result = await pyke_client.clash.tournaments(Region.EUW)

    assert isinstance(result, list)
    assert result[0]["id"] == TOURNAMENT_ID


@pytest.mark.asyncio
async def test_tournament_by_team_id(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/tournaments/by-team/{TEAM_ID}").mock(
        return_value=Response(
            200, json={"id": TOURNAMENT_ID, "nameKey": "test_tournament"}
        )
    )

    result = await pyke_client.clash.tournament_by_team_id(Region.EUW, TEAM_ID)

    assert result["id"] == TOURNAMENT_ID


@pytest.mark.asyncio
async def test_tournament_by_tournament_id(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/tournaments/{TOURNAMENT_ID}").mock(
        return_value=Response(
            200, json={"id": TOURNAMENT_ID, "nameKey": "test_tournament"}
        )
    )

    result = await pyke_client.clash.tournament_by_tournament_id(
        Region.EUW, TOURNAMENT_ID
    )

    assert result["id"] == TOURNAMENT_ID


@pytest.mark.asyncio
async def test_tournaments_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/tournaments").mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.clash.tournaments(Region.EUW)
