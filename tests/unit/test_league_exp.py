import pytest
from httpx import Response
from respx import MockRouter

from pyke import Division, Pyke, Queue, Region, Tier, exceptions

BASE = "https://euw1.api.riotgames.com/lol/league-exp/v4"


@pytest.mark.asyncio
async def test_by_queue_tier_division(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/entries/RANKED_SOLO_5x5/GOLD/II").mock(
        return_value=Response(
            200,
            json=[{"summonerName": "TestPlayer", "tier": "GOLD", "rank": "II"}],
        )
    )

    result = await pyke_client.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    assert isinstance(result, list)
    assert result[0]["tier"] == "GOLD"
    assert result[0]["rank"] == "II"


@pytest.mark.asyncio
async def test_by_queue_tier_division_with_page(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/entries/RANKED_SOLO_5x5/GOLD/II").mock(
        return_value=Response(
            200, json=[{"summonerName": "TestPlayer", "tier": "GOLD"}]
        )
    )

    result = await pyke_client.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_by_queue_tier_division_flex(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/entries/RANKED_FLEX_SR/PLATINUM/I").mock(
        return_value=Response(
            200, json=[{"summonerName": "TestPlayer", "tier": "PLATINUM"}]
        )
    )

    result = await pyke_client.league_exp.by_queue_tier_division(
        Region.EUW, Queue.FLEX, Tier.PLATINUM, Division.I
    )

    assert result[0]["tier"] == "PLATINUM"


@pytest.mark.asyncio
async def test_not_found_raises(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/entries/RANKED_SOLO_5x5/GOLD/II").mock(
        return_value=Response(404)
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.league_exp.by_queue_tier_division(
            Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
        )
