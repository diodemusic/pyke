from json import JSONDecodeError
from typing import Any

from httpx import HTTPError

from ._base_client import _BaseClient
from .exceptions import InternalServerError

__all__ = ["_BaseDataDragonClient"]


class _BaseDataDragonClient(_BaseClient):
    DATA_DRAGON_BASE = "https://ddragon.leagueoflegends.com"

    def __init__(self, timeout: int, print_url: bool) -> None:
        super().__init__(timeout, print_url)
        self._version: str | None = None

    async def _get_latest_version(self) -> str:
        try:
            response = await self.client.get(
                f"{self.DATA_DRAGON_BASE}/api/versions.json"
            )
            return response.json()[0]
        except HTTPError as e:
            raise HTTPError(f"Error getting latest ddragon version: {e}") from e
        except JSONDecodeError as e:
            raise InternalServerError(
                f"Error response body is not valid json: {e}", 500
            ) from e
        except IndexError as e:
            raise IndexError(f"Error: response returned an empty list: {e}") from e

    async def _data_dragon_cdn_request(self, locale: str, endpoint: str) -> Any:
        if self._version is None:
            self._version = await self._get_latest_version()

        url = (
            f"{self.DATA_DRAGON_BASE}/cdn/{self._version}/data/{locale}/{endpoint}.json"
        )

        return await self._get(url)
