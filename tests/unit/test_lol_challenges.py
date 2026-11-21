import pytest
from httpx import Response
from respx import MockRouter

from pyke import Level, Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/challenges/v1"
PUUID = "a" * 78
CHALLENGE_ID = 101


@pytest.mark.asyncio
async def test_config(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/challenges/config").mock(
        return_value=Response(
            200,
            json=[{"id": 101, "localizedNames": {}, "state": "ENABLED"}],
        )
    )

    result = await pyke_client.lol_challenges.config(Region.EUW)

    assert isinstance(result, list)
    assert result[0]["id"] == 101


@pytest.mark.asyncio
async def test_percentiles(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/challenges/percentiles").mock(
        return_value=Response(200, json={"101": {"GOLD": 0.15}})
    )

    result = await pyke_client.lol_challenges.percentiles(Region.EUW)

    assert isinstance(result, dict)
    assert "101" in result


@pytest.mark.asyncio
async def test_config_by_challenge_id(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/challenges/{CHALLENGE_ID}/config").mock(
        return_value=Response(200, json={"id": CHALLENGE_ID, "state": "ENABLED"})
    )

    result = await pyke_client.lol_challenges.config_by_challenge_id(
        Region.EUW, CHALLENGE_ID
    )

    assert result["id"] == CHALLENGE_ID


@pytest.mark.asyncio
async def test_leaderboards_by_level(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(
        f"{BASE}/challenges/{CHALLENGE_ID}/leaderboards/by-level/MASTER"
    ).mock(
        return_value=Response(
            200,
            json=[{"puuid": PUUID, "value": 1500.0, "position": 1}],
        )
    )

    result = await pyke_client.lol_challenges.leaderboards_by_level(
        Region.EUW, Level.MASTER, CHALLENGE_ID
    )

    assert isinstance(result, list)
    assert result[0]["position"] == 1


@pytest.mark.asyncio
async def test_percentiles_by_challenge_id(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/challenges/{CHALLENGE_ID}/percentiles").mock(
        return_value=Response(200, json={"GOLD": 0.15, "PLATINUM": 0.05})
    )

    result = await pyke_client.lol_challenges.percentiles_by_challenge_id(
        Region.EUW, CHALLENGE_ID
    )

    assert isinstance(result, dict)
    assert "GOLD" in result


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/player-data/{PUUID}").mock(
        return_value=Response(
            200,
            json={
                "puuid": PUUID,
                "totalPoints": {"level": "GOLD", "current": 500},
            },
        )
    )

    result = await pyke_client.lol_challenges.by_puuid(Region.EUW, PUUID)

    assert result["puuid"] == PUUID


@pytest.mark.asyncio
async def test_config_forbidden_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/challenges/config").mock(return_value=Response(403))

    with pytest.raises(exceptions.Forbidden):
        await pyke_client.lol_challenges.config(Region.EUW)


@pytest.mark.asyncio
async def test_by_puuid_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/player-data/{PUUID}").mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.lol_challenges.by_puuid(Region.EUW, PUUID)
