import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/status/v4"


@pytest.mark.asyncio
async def test_platform_data(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(f"{BASE}/platform-data").mock(
        return_value=Response(
            200,
            json={
                "id": "EUW1",
                "name": "EU West",
                "locales": ["en_GB"],
                "maintenances": [],
                "incidents": [],
            },
        )
    )

    result = await pyke_client.lol_status.platform_data(Region.EUW)

    assert result["id"] == "EUW1"
    assert result["name"] == "EU West"
    assert isinstance(result["incidents"], list)


@pytest.mark.asyncio
async def test_platform_data_na(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get("https://na1.api.riotgames.com/lol/status/v4/platform-data").mock(
        return_value=Response(200, json={"id": "NA1", "name": "North America"})
    )

    result = await pyke_client.lol_status.platform_data(Region.NA)

    assert result["id"] == "NA1"


@pytest.mark.asyncio
async def test_platform_data_service_unavailable_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/platform-data").mock(return_value=Response(503))

    with pytest.raises(exceptions.ServiceUnavailable):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_platform_data_forbidden_raises(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(f"{BASE}/platform-data").mock(return_value=Response(403))

    with pytest.raises(exceptions.Forbidden):
        await pyke_client.lol_status.platform_data(Region.EUW)
