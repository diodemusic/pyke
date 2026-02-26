from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class MissionAssetsData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    async def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all mission_assets by locale

        **Example:**
            `mission_assets = await ddragon.mission_assets.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, Any]`
        """  # fmt: skip

        return await self._client._data_dragon_cdn_request(locale, "mission-assets")
