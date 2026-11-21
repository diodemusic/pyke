import pytest
from httpx import Response
from respx import MockRouter

from pyke import Division, Pyke, Queue, Region, Tier, exceptions

BASE = "https://euw1.api.riotgames.com"
PUUID = "a" * 78


@pytest.mark.asyncio
async def test_challenger_leagues_by_queue(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(
        f"{BASE}/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    ).mock(return_value=Response(200, json={"tier": "CHALLENGER", "entries": []}))

    result = await pyke_client.league.challenger_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert result["tier"] == "CHALLENGER"


@pytest.mark.asyncio
async def test_grandmaster_leagues_by_queue(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(
        f"{BASE}/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
    ).mock(return_value=Response(200, json={"tier": "GRANDMASTER", "entries": []}))

    result = await pyke_client.league.grandmaster_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert result["tier"] == "GRANDMASTER"


@pytest.mark.asyncio
async def test_master_leagues_by_queue(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5").mock(
        return_value=Response(200, json={"tier": "MASTER", "entries": []})
    )

    result = await pyke_client.league.master_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert result["tier"] == "MASTER"


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/lol/league/v4/entries/by-puuid/{PUUID}").mock(
        return_value=Response(
            200, json=[{"tier": "GOLD", "queueType": "RANKED_SOLO_5x5"}]
        )
    )

    result = await pyke_client.league.by_puuid(Region.EUW, PUUID)

    assert isinstance(result, list)
    assert result[0]["tier"] == "GOLD"


@pytest.mark.asyncio
async def test_by_queue_tier_division(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/II").mock(
        return_value=Response(200, json=[{"summonerName": "Test", "tier": "GOLD"}])
    )

    result = await pyke_client.league.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    assert isinstance(result, list)
    assert result[0]["tier"] == "GOLD"


@pytest.mark.asyncio
async def test_by_league_id(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    league_id = "some-league-id"
    respx_mock.get(f"{BASE}/lol/league/v4/leagues/{league_id}").mock(
        return_value=Response(200, json={"leagueId": league_id, "entries": []})
    )

    result = await pyke_client.league.by_league_id(Region.EUW, league_id)

    assert result["leagueId"] == league_id


@pytest.mark.asyncio
async def test_challenger_leagues_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(
        f"{BASE}/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    ).mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.league.challenger_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)


@pytest.mark.asyncio
async def test_by_puuid_rate_limit_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/lol/league/v4/entries/by-puuid/{PUUID}").mock(
        return_value=Response(429)
    )

    with pytest.raises(exceptions.RateLimitExceeded):
        await pyke_client.league.by_puuid(Region.EUW, PUUID)


@pytest.mark.asyncio
async def test_flex_queue_value(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(
        f"{BASE}/lol/league/v4/challengerleagues/by-queue/RANKED_FLEX_SR"
    ).mock(return_value=Response(200, json={"tier": "CHALLENGER", "entries": []}))

    result = await pyke_client.league.challenger_leagues_by_queue(
        Region.EUW, Queue.FLEX
    )

    assert result["tier"] == "CHALLENGER"
