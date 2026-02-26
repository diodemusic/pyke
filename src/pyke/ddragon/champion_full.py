from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class ChampionFullData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    async def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all champion_full by locale

        **Example:**
            `champion_full = await ddragon.champion_full.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, Any]`
        """  # fmt: skip

        return await self._client._data_dragon_cdn_request(locale, "championFull")
