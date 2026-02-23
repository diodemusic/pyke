from __future__ import annotations

import json
from typing import Any

import httpx
from httpx import Response

from . import exceptions
from .enums.continent import Continent
from .enums.region import Region


class _BaseApiClient:  # pyright: ignore[reportUnusedClass]
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(
        self, api_key: str | None, timeout: int, print_url: bool, print_rate_limit: bool
    ) -> None:
        if api_key is None:
            raise ValueError("API key is required, please pass a valid Riot API key.")

        self.api_key = api_key
        self.timeout = timeout
        self.print_url = print_url
        self.print_rate_limit = print_rate_limit
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))
        self._status_code_registry = {
            400: exceptions.BadRequest("Bad request", 400),
            401: exceptions.Unauthorized("Unauthorized", 401),
            403: exceptions.Forbidden("Forbidden", 403),
            404: exceptions.DataNotFound("Data not found", 404),
            405: exceptions.MethodNotAllowed("Method not allowed", 405),
            415: exceptions.UnsupportedMediaType("Unsupported media type", 415),
            500: exceptions.InternalServerError("Internal server error", 500),
            502: exceptions.BadGateway("Bad gateway", 502),
            503: exceptions.ServiceUnavailable("Service unavailable", 503),
            504: exceptions.GatewayTimeout("Gateway timeout", 504),
        }

    def _get_count(self, response: Response) -> int:
        header_value = response.headers.get("X-App-Rate-Limit-Count")

        if not header_value:
            return 0

        parts = header_value.split(":")

        if len(parts) < 1 or not parts[0]:
            return 0

        try:
            return int(parts[0])
        except ValueError:
            return 0

    def _get_limit(self, response: Response) -> int:
        header_value = response.headers.get("X-App-Rate-Limit")

        if not header_value:
            return 100

        parts = header_value.split(":")

        if len(parts) < 1 or not parts[0]:
            return 100

        try:
            return int(parts[0])
        except ValueError:
            return 100

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    async def _get(self, url: str, params: dict[Any, Any] | None = None) -> Any:
        if self.print_url:
            print(f"URL:        {url}")

        headers = {"X-Riot-Token": self.api_key}

        try:
            response = await self.client.get(url, headers=headers, params=params)
        except httpx.TimeoutException:
            raise exceptions.RequestTimeout(
                f"Request timed out after {self.timeout} seconds", 408
            )

        if self.print_rate_limit:
            self.count = self._get_count(response)
            self.limit = self._get_limit(response)
            print(f"Rate limit: ({self.count}/{self.limit})")

        code = response.status_code

        if code == 200:
            return self._response_json(response)
        elif code == 429:
            raise exceptions.RateLimitExceeded("Rate limit exceeded", code)

        raise self._status_code_registry.get(
            code,
            exceptions.UnknownError(
                "Unexpected response, something has gone terribly wrong", code
            ),
        )

    async def _continent_request(
        self, continent: Continent, path: str, params: dict[Any, Any] | None = None
    ) -> Any:
        url = f"{self.CONTINENT_BASE.format(continent=continent.value)}{path}"

        return await self._get(url, params)

    async def _region_request(
        self, region: Region, path: str, params: dict[Any, Any] | None = None
    ) -> Any:
        url = f"{self.REGION_BASE.format(region=region.value)}{path}"

        return await self._get(url, params)

    async def aclose(self) -> None:
        await self.client.aclose()
