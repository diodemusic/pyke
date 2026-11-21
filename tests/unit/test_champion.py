import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com"


@pytest.mark.asyncio
async def test_rotations(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/lol/platform/v3/champion-rotations").mock(
        return_value=Response(
            200,
            json={
                "freeChampionIds": [1, 2, 3],
                "freeChampionIdsForNewPlayers": [4, 5],
                "maxNewPlayerLevel": 10,
            },
        )
    )

    result = await pyke_client.champion.rotations(Region.EUW)

    assert result["freeChampionIds"] == [1, 2, 3]
    assert result["freeChampionIdsForNewPlayers"] == [4, 5]


@pytest.mark.asyncio
async def test_rotations_forbidden_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/lol/platform/v3/champion-rotations").mock(
        return_value=Response(403)
    )

    with pytest.raises(exceptions.Forbidden):
        await pyke_client.champion.rotations(Region.EUW)


@pytest.mark.asyncio
async def test_rotations_unauthorized_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/lol/platform/v3/champion-rotations").mock(
        return_value=Response(401)
    )

    with pytest.raises(exceptions.Unauthorized):
        await pyke_client.champion.rotations(Region.EUW)
