import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/summoner/v4"
PUUID = "a" * 78


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/summoners/by-puuid/{PUUID}").mock(
        return_value=Response(
            200,
            json={
                "id": "some-encrypted-id",
                "puuid": PUUID,
                "profileIconId": 1234,
                "summonerLevel": 300,
            },
        )
    )

    result = await pyke_client.summoner.by_puuid(Region.EUW, PUUID)

    assert result["puuid"] == PUUID
    assert result["summonerLevel"] == 300


@pytest.mark.asyncio
async def test_by_puuid_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/summoners/by-puuid/{PUUID}").mock(
        return_value=Response(404)
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.summoner.by_puuid(Region.EUW, PUUID)


@pytest.mark.asyncio
async def test_by_puuid_forbidden_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/summoners/by-puuid/{PUUID}").mock(
        return_value=Response(403)
    )

    with pytest.raises(exceptions.Forbidden):
        await pyke_client.summoner.by_puuid(Region.EUW, PUUID)


@pytest.mark.asyncio
async def test_by_puuid_kr_region(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(
        f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{PUUID}"
    ).mock(return_value=Response(200, json={"puuid": PUUID, "summonerLevel": 500}))

    result = await pyke_client.summoner.by_puuid(Region.KR, PUUID)

    assert result["summonerLevel"] == 500
