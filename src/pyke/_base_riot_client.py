from typing import Any

from ._base_client import _BaseClient
from .enums.continent import Continent
from .enums.region import Region

__all__ = ["_BaseRiotClient"]


class _BaseRiotClient(_BaseClient):
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(self, api_key: str | None, timeout: int, print_url: bool) -> None:
        if api_key is None:
            raise ValueError("API key is required, please pass a valid Riot API key.")

        super().__init__(timeout, print_url)
        self._api_key = api_key

    async def _request(
        self,
        path: str,
        continent: Continent | None = None,
        region: Region | None = None,
        params: dict[Any, Any] | None = None,
    ) -> Any:
        if continent is not None:
            url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"
        elif region is not None:
            url = f"{self.REGION_BASE.format(region=region.value)}{path}"
        else:
            raise TypeError("missing required positional argument: continent | region")

        return await self._get(url, {"X-Riot-Token": self._api_key}, params)
