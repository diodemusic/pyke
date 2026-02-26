"""
DataDragon tests.

Note: ddragon `get_all` methods are currently sync functions that return a coroutine
(since the underlying client methods are async). `await ddragon.x.get_all(...)` works
because `await` accepts any awaitable, including a coroutine returned by a sync function.
These tests will behave correctly once `get_all` is properly declared `async def`.

The `ddragon_client` fixture manually sets `_client.version` since `DataDragon.__init__`
does not yet resolve the version automatically.
"""

import pytest
from httpx import Response
from respx import MockRouter

from pyke import DataDragon, exceptions

VERSION = "16.3.1"
LOCALE = "en_GB"
BASE = f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LOCALE}"


@pytest.mark.asyncio
async def test_champion_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/champion.json").mock(
        return_value=Response(200, json={"data": {"Aatrox": {"id": "Aatrox"}}})
    )

    result = await ddragon_client.champion.get_all(LOCALE)

    assert "data" in result
    assert "Aatrox" in result["data"]


@pytest.mark.asyncio
async def test_champion_full_get_all(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/championFull.json").mock(
        return_value=Response(200, json={"data": {"Aatrox": {"id": "Aatrox"}}})
    )

    result = await ddragon_client.champion_full.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_item_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/item.json").mock(
        return_value=Response(200, json={"data": {"1001": {"name": "Boots"}}})
    )

    result = await ddragon_client.item.get_all(LOCALE)

    assert "data" in result
    assert "1001" in result["data"]


@pytest.mark.asyncio
async def test_runes_reforged_get_all(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/runesReforged.json").mock(
        return_value=Response(200, json=[{"id": 8000, "key": "Precision"}])
    )

    result = await ddragon_client.runes_reforged.get_all(LOCALE)

    assert isinstance(result, list)
    assert result[0]["key"] == "Precision"  # type: ignore


@pytest.mark.asyncio
async def test_summoner_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/summoner.json").mock(
        return_value=Response(
            200, json={"data": {"SummonerFlash": {"id": "SummonerFlash"}}}
        )
    )

    result = await ddragon_client.summoner.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_map_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/map.json").mock(
        return_value=Response(
            200, json={"data": {"11": {"MapName": "Summoner's Rift"}}}
        )
    )

    result = await ddragon_client.map.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_profileicon_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/profileicon.json").mock(
        return_value=Response(200, json={"data": {"0": {"id": 0}}})
    )

    result = await ddragon_client.profileicon.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_language_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/language.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.language.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_challenges_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/challenges.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.challenges.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_itemmodifiers_get_all(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/item-modifiers.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.item_modifiers.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_spellbuffs_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/spellbuffs.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.spellbuffs.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_sticker_get_all(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/sticker.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.sticker.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_missionassets_get_all(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/mission-assets.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    result = await ddragon_client.mission_assets.get_all(LOCALE)

    assert "data" in result


@pytest.mark.asyncio
async def test_version_in_url(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/champion.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    await ddragon_client.champion.get_all(LOCALE)

    called_url = str(respx_mock.calls.last.request.url)
    assert VERSION in called_url


@pytest.mark.asyncio
async def test_locale_in_url(ddragon_client: DataDragon, respx_mock: MockRouter):
    respx_mock.get(f"{BASE}/champion.json").mock(
        return_value=Response(200, json={"data": {}})
    )

    await ddragon_client.champion.get_all(LOCALE)

    called_url = str(respx_mock.calls.last.request.url)
    assert LOCALE in called_url


@pytest.mark.asyncio
async def test_champion_not_found_raises(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/champion.json").mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound):
        await ddragon_client.champion.get_all(LOCALE)


@pytest.mark.asyncio
async def test_champion_internal_server_error_raises(
    ddragon_client: DataDragon, respx_mock: MockRouter
):
    respx_mock.get(f"{BASE}/champion.json").mock(return_value=Response(500))

    with pytest.raises(exceptions.InternalServerError):
        await ddragon_client.champion.get_all(LOCALE)
