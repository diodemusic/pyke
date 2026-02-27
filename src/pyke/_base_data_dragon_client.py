import json
from typing import Any

import httpx
from httpx import Response

from . import exceptions

__all__ = ["_BaseDataDragonClient"]


class _BaseDataDragonClient:
    DATA_DRAGON_BASE = "https://ddragon.leagueoflegends.com"

    def __init__(self, timeout: int, print_url: bool) -> None:
        self.timeout = timeout
        self.print_url = print_url
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))
        self._version = self._get_latest_version()
        self._status_code_registry = {
            400: lambda: exceptions.BadRequest("Bad request", 400),
            401: lambda: exceptions.Unauthorized("Unauthorized", 401),
            403: lambda: exceptions.Forbidden("Forbidden", 403),
            404: lambda: exceptions.DataNotFound("Data not found", 404),
            405: lambda: exceptions.MethodNotAllowed("Method not allowed", 405),
            415: lambda: exceptions.UnsupportedMediaType("Unsupported media type", 415),
            429: lambda: exceptions.RateLimitExceeded("Rate limit exceeded", 429),
            500: lambda: exceptions.InternalServerError("Internal server error", 500),
            502: lambda: exceptions.BadGateway("Bad gateway", 502),
            503: lambda: exceptions.ServiceUnavailable("Service unavailable", 503),
            504: lambda: exceptions.GatewayTimeout("Gateway timeout", 504),
        }

    def _get_latest_version(self) -> str:
        with httpx.Client(timeout=self.timeout) as client:
            try:
                response = client.get(f"{self.DATA_DRAGON_BASE}/api/versions.json")
                return response.json()[0]
            except Exception as e:
                raise Exception(f"Error getting latest ddragon version: {e}")

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)

    async def _get(self, url: str) -> Any:
        if self.print_url:
            print(url)

        try:
            response = await self.client.get(url)
        except httpx.TimeoutException:
            raise exceptions.RequestTimeout(
                f"Request timed out after {self.timeout} seconds", 408
            )

        code = response.status_code

        if code == 200:
            return self._response_json(response)

        exc_factory = self._status_code_registry.get(code)

        if exc_factory:
            raise exc_factory()
        else:
            raise exceptions.UnknownError("Unexpected response", code)

    async def _data_dragon_request(self, path: str) -> Any:
        url = f"{self.DATA_DRAGON_BASE}{path}"

        return await self._get(url)

    async def _data_dragon_cdn_request(self, locale: str, endpoint: str) -> Any:
        url = (
            f"{self.DATA_DRAGON_BASE}/cdn/{self._version}/data/{locale}/{endpoint}.json"
        )

        return await self._get(url)

    async def aclose(self) -> None:
        await self.client.aclose()
