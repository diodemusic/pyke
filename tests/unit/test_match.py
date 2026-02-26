import pytest
from httpx import Response
from respx import MockRouter

from pyke import Continent, MatchType, Pyke, exceptions

BASE = "https://europe.api.riotgames.com/lol/match/v5"
PUUID = "a" * 78
MATCH_ID = "EUW1_1234567890"


@pytest.mark.asyncio
async def test_match_ids_by_puuid(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(
            200,
            json=[
                "EUW1_1111111111",
                "EUW1_2222222222",
                "EUW1_3333333333",
            ],
        )
    )

    result = await pyke_client.match.match_ids_by_puuid(Continent.EUROPE, PUUID)

    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(m, str) for m in result)


@pytest.mark.asyncio
async def test_match_ids_by_puuid_with_type(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(200, json=["EUW1_1111111111"])
    )

    result = await pyke_client.match.match_ids_by_puuid(
        Continent.EUROPE, PUUID, match_type=MatchType.RANKED
    )

    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_match_ids_by_puuid_with_count(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(200, json=["EUW1_1111111111", "EUW1_2222222222"])
    )

    result = await pyke_client.match.match_ids_by_puuid(
        Continent.EUROPE, PUUID, count=2
    )

    assert len(result) == 2


@pytest.mark.asyncio
async def test_match_ids_invalid_response_raises(
    pyke_client: Pyke, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(200, json={"not": "a list"})
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.match.match_ids_by_puuid(Continent.EUROPE, PUUID)


@pytest.mark.asyncio
async def test_match_ids_non_string_items_raises(
    pyke_client: Pyke, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(200, json=[1, 2, 3])
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.match.match_ids_by_puuid(Continent.EUROPE, PUUID)


@pytest.mark.asyncio
async def test_by_match_id(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/{MATCH_ID}").mock(
        return_value=Response(
            200,
            json={
                "metadata": {"matchId": MATCH_ID, "participants": [PUUID]},
                "info": {"gameDuration": 1800, "gameMode": "CLASSIC"},
            },
        )
    )

    result = await pyke_client.match.by_match_id(Continent.EUROPE, MATCH_ID)

    assert result["metadata"]["matchId"] == MATCH_ID
    assert result["info"]["gameMode"] == "CLASSIC"


@pytest.mark.asyncio
async def test_timeline_by_match_id(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/{MATCH_ID}/timeline").mock(
        return_value=Response(
            200,
            json={
                "metadata": {"matchId": MATCH_ID},
                "info": {"frames": []},
            },
        )
    )

    result = await pyke_client.match.timeline_by_match_id(Continent.EUROPE, MATCH_ID)

    assert result["metadata"]["matchId"] == MATCH_ID
    assert "frames" in result["info"]


@pytest.mark.asyncio
async def test_by_match_id_not_found_raises(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/{MATCH_ID}").mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.match.by_match_id(Continent.EUROPE, MATCH_ID)


@pytest.mark.asyncio
async def test_match_ids_rate_limit_raises(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/matches/by-puuid/{PUUID}/ids").mock(
        return_value=Response(429)
    )

    with pytest.raises(exceptions.RateLimitExceeded):
        await pyke_client.match.match_ids_by_puuid(Continent.EUROPE, PUUID)
