import pytest
from httpx import Response
from respx import MockRouter

from pyke import Continent, Pyke, exceptions

BASE = "https://europe.api.riotgames.com"
PUUID = "a" * 78


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/riot/account/v1/accounts/by-puuid/{PUUID}").mock(
        return_value=Response(
            200, json={"puuid": PUUID, "gameName": "saves", "tagLine": "000"}
        )
    )

    result = await pyke_client.account.by_puuid(Continent.EUROPE, PUUID)

    assert result["puuid"] == PUUID
    assert result["gameName"] == "saves"
    assert result["tagLine"] == "000"


@pytest.mark.asyncio
async def test_by_riot_id(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/riot/account/v1/accounts/by-riot-id/saves/000").mock(
        return_value=Response(
            200, json={"puuid": PUUID, "gameName": "saves", "tagLine": "000"}
        )
    )

    result = await pyke_client.account.by_riot_id(Continent.EUROPE, "saves", "000")

    assert result["gameName"] == "saves"
    assert result["tagLine"] == "000"


@pytest.mark.asyncio
async def test_region_by_puuid(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/riot/account/v1/region/by-game/lol/by-puuid/{PUUID}").mock(
        return_value=Response(200, json={"puuid": PUUID, "region": "EUW"})
    )

    result = await pyke_client.account.region_by_puuid(Continent.EUROPE, PUUID)

    assert result["region"] == "EUW"


@pytest.mark.asyncio
async def test_by_puuid_not_found_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/riot/account/v1/accounts/by-puuid/{PUUID}").mock(
        return_value=Response(404)
    )

    with pytest.raises(exceptions.DataNotFound):
        await pyke_client.account.by_puuid(Continent.EUROPE, PUUID)


@pytest.mark.asyncio
async def test_by_riot_id_forbidden_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/riot/account/v1/accounts/by-riot-id/saves/000").mock(
        return_value=Response(403)
    )

    with pytest.raises(exceptions.Forbidden):
        await pyke_client.account.by_riot_id(Continent.EUROPE, "saves", "000")


@pytest.mark.asyncio
async def test_continent_routing(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    americas_base = "https://americas.api.riotgames.com"
    respx_mock.get(
        f"{americas_base}/riot/account/v1/accounts/by-riot-id/player/NA1"
    ).mock(
        return_value=Response(
            200, json={"puuid": PUUID, "gameName": "player", "tagLine": "NA1"}
        )
    )

    result = await pyke_client.account.by_riot_id(Continent.AMERICAS, "player", "NA1")

    assert result["gameName"] == "player"
