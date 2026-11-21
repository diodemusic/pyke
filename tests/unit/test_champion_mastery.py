import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com"
PUUID = "a" * 78
MASTERY_BASE = f"{BASE}/lol/champion-mastery/v4"


@pytest.mark.asyncio
async def test_masteries_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{MASTERY_BASE}/champion-masteries/by-puuid/{PUUID}").mock(
        return_value=Response(
            200,
            json=[
                {"championId": 29, "championPoints": 500000, "championLevel": 7},
                {"championId": 40, "championPoints": 200000, "championLevel": 6},
            ],
        )
    )

    result = await pyke_client.champion_mastery.masteries_by_puuid(Region.EUW, PUUID)

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["championId"] == 29
    assert result[0]["championLevel"] == 7


@pytest.mark.asyncio
async def test_by_puuid_and_champion_id(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(
        f"{MASTERY_BASE}/champion-masteries/by-puuid/{PUUID}/by-champion/29"
    ).mock(
        return_value=Response(
            200, json={"championId": 29, "championPoints": 500000, "championLevel": 7}
        )
    )

    result = await pyke_client.champion_mastery.by_puuid_and_champion_id(
        Region.EUW, PUUID, 29
    )

    assert result["championId"] == 29
    assert result["championPoints"] == 500000


@pytest.mark.asyncio
async def test_masteries_by_puuid_top_without_count(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{MASTERY_BASE}/champion-masteries/by-puuid/{PUUID}/top").mock(
        return_value=Response(
            200,
            json=[
                {"championId": 29, "championPoints": 500000},
                {"championId": 40, "championPoints": 200000},
                {"championId": 99, "championPoints": 100000},
            ],
        )
    )

    result = await pyke_client.champion_mastery.masteries_by_puuid_top(
        Region.EUW, PUUID
    )

    assert isinstance(result, list)
    assert len(result) == 3


@pytest.mark.asyncio
async def test_masteries_by_puuid_top_with_count(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{MASTERY_BASE}/champion-masteries/by-puuid/{PUUID}/top").mock(
        return_value=Response(
            200,
            json=[
                {"championId": 29, "championPoints": 500000},
                {"championId": 40, "championPoints": 200000},
            ],
        )
    )

    result = await pyke_client.champion_mastery.masteries_by_puuid_top(
        Region.EUW, PUUID, count=2
    )

    assert len(result) == 2


@pytest.mark.asyncio
async def test_score_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{MASTERY_BASE}/scores/by-puuid/{PUUID}").mock(
        return_value=Response(200, json=638)
    )

    result = await pyke_client.champion_mastery.score_by_puuid(Region.EUW, PUUID)

    assert result == 638
    assert isinstance(result, int)


@pytest.mark.asyncio
async def test_masteries_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{MASTERY_BASE}/champion-masteries/by-puuid/{PUUID}").mock(
        return_value=Response(404)
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.champion_mastery.masteries_by_puuid(Region.EUW, PUUID)


@pytest.mark.asyncio
async def test_score_internal_server_error_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{MASTERY_BASE}/scores/by-puuid/{PUUID}").mock(
        return_value=Response(500)
    )

    with pytest.raises(exceptions.InternalServerError):
        await pyke_client.champion_mastery.score_by_puuid(Region.EUW, PUUID)
