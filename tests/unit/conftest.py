from collections.abc import AsyncGenerator

import pytest_asyncio
import respx
from httpx import Response

from pyke import DataDragon, Pyke


@pytest_asyncio.fixture(scope="session")
async def pyke_client() -> AsyncGenerator[Pyke, None]:
    async with Pyke("RGAPI-000000000000000000000000000000000000") as client:
        yield client


@pytest_asyncio.fixture
async def ddragon_client(
    respx_mock: respx.MockRouter,
) -> AsyncGenerator[DataDragon, None]:
    respx_mock.get("https://ddragon.leagueoflegends.com/api/versions.json").mock(
        return_value=Response(200, json=["16.3.1", "16.2.1"])
    )
    async with DataDragon() as client:
        yield client


@pytest_asyncio.fixture(autouse=True)
async def respx_mock() -> AsyncGenerator[respx.MockRouter, None]:
    with respx.mock(assert_all_called=False) as mock:
        yield mock
