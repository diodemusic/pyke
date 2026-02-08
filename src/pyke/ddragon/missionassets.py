from typing import Any

from .._base_data_dragon_client import _BaseDataDragonClient


class MissionassetsData:
    def __init__(self, client: _BaseDataDragonClient):
        self._client = client

    def get_all(self, locale: str) -> dict[str, Any]:
        """# Get all missionassets by locale

        **Example:**
            `missionassets = ddragon.missionassets.get_all("en_GB")`

        **Args:**
            `locale (str)` Locale to use.

        **Returns:**
            `dict[str, any]`
        """  # fmt: skip

        return self._client._data_dragon_cdn_request(locale, "mission-assets")
