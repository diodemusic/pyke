from typing import Any

import httpx

from ._base_client import _BaseClient

__all__ = ["_BaseDataDragonClient"]


class _BaseDataDragonClient(_BaseClient):
    DATA_DRAGON_BASE = "https://ddragon.leagueoflegends.com"

    def __init__(self, timeout: int, print_url: bool) -> None:
        super().__init__(timeout, print_url)
        self._version = self._get_latest_version()

    def _get_latest_version(self) -> str:
        with httpx.Client(timeout=self.timeout) as client:
            try:
                response = client.get(f"{self.DATA_DRAGON_BASE}/api/versions.json")
                return response.json()[0]
            except Exception as e:
                raise Exception(f"Error getting latest ddragon version: {e}")

    async def _data_dragon_cdn_request(self, locale: str, endpoint: str) -> Any:
        url = (
            f"{self.DATA_DRAGON_BASE}/cdn/{self._version}/data/{locale}/{endpoint}.json"
        )

        return await self._get(url)
