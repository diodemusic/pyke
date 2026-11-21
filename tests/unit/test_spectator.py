import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/spectator/v5"
PUUID = "a" * 78


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/active-games/by-summoner/{PUUID}").mock(
        return_value=Response(
            200,
            json={
                "gameId": 1234567890,
                "gameMode": "CLASSIC",
                "gameType": "MATCHED_GAME",
                "participants": [],
            },
        )
    )

    result = await pyke_client.spectator.by_puuid(Region.EUW, PUUID)

    assert result["gameId"] == 1234567890
    assert result["gameMode"] == "CLASSIC"


@pytest.mark.asyncio
async def test_by_puuid_not_in_game_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/active-games/by-summoner/{PUUID}").mock(
        return_value=Response(404)
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.spectator.by_puuid(Region.EUW, PUUID)


@pytest.mark.asyncio
async def test_by_puuid_different_region(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(
        f"https://na1.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{PUUID}"
    ).mock(return_value=Response(200, json={"gameId": 9999999999, "gameMode": "ARAM"}))

    result = await pyke_client.spectator.by_puuid(Region.NA, PUUID)

    assert result["gameMode"] == "ARAM"
