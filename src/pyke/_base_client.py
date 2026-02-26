import json
from typing import Any

import httpx
from httpx import Response

from . import exceptions
from .enums.continent import Continent
from .enums.region import Region

__all__ = ["_BaseApiClient"]


class _BaseApiClient:
    CONTINENT_BASE = "https://{continent}.api.riotgames.com"
    REGION_BASE = "https://{region}.api.riotgames.com"

    def __init__(self, api_key: str | None, timeout: int, print_url: bool) -> None:
        if api_key is None:
            raise ValueError("API key is required, please pass a valid Riot API key.")

        self._api_key = api_key
        self.timeout = timeout
        self.print_url = print_url
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))
        self._status_code_registry = {
            400: lambda: exceptions.BadRequest("Bad request", 400),
            401: lambda: exceptions.Unauthorized("Unauthorized", 401),
            403: lambda: exceptions.Forbidden("Forbidden", 403),
            404: lambda: exceptions.DataNotFound("Data not found", 404),
            405: lambda: exceptions.MethodNotAllowed("Method not allowed", 405),
            415: lambda: exceptions.UnsupportedMediaType("Unsupported media type", 415),
            500: lambda: exceptions.InternalServerError("Internal server error", 500),
            502: lambda: exceptions.BadGateway("Bad gateway", 502),
            503: lambda: exceptions.ServiceUnavailable("Service unavailable", 503),
            504: lambda: exceptions.GatewayTimeout("Gateway timeout", 504),
        }

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    async def _get(self, url: str, params: dict[Any, Any] | None = None) -> Any:
        if self.print_url:
            print(f"URL: {url}")

        headers = {"X-Riot-Token": self._api_key}

        try:
            response = await self.client.get(url, headers=headers, params=params)
        except httpx.TimeoutException:
            raise exceptions.RequestTimeout(
                f"Request timed out after {self.timeout} seconds", 408
            )

        if response.status_code == 200:
            return self._response_json(response)
        elif response.status_code == 429:
            raise exceptions.RateLimitExceeded(
                "Rate limit exceeded", response.status_code
            )

        exc_factory = self._status_code_registry.get(response.status_code)

        if exc_factory:
            raise exc_factory()
        else:
            raise exceptions.UnknownError("Unexpected response", response.status_code)

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
