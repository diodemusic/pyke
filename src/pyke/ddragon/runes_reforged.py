from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class RunesReforgedData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    async def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all runes_reforged by locale

        **Example:**
            `runes_reforged = await ddragon.runes_reforged.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, Any]`
        """  # fmt: skip

        return await self._client._data_dragon_cdn_request(locale, "runesReforged")
