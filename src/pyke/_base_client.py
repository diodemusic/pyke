import json
from typing import Any

import httpx
from httpx import Response

from . import exceptions

__all__ = ["_BaseClient"]


class _BaseClient:
    def __init__(self, timeout: int, print_url: bool) -> None:
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
            429: lambda: exceptions.RateLimitExceeded("Rate limit exceeded", 429),
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

    async def _get(
        self,
        url: str,
        headers: dict[Any, Any] | None = None,
        params: dict[Any, Any] | None = None,
    ) -> Any:
        if self.print_url:
            print(url)

        try:
            response = await self.client.get(url, headers=headers, params=params)
        except httpx.TimeoutException:
            raise exceptions.RequestTimeout(
                f"Request timed out after {self.timeout} seconds", 408
            )

        if response.status_code == 200:
            return self._response_json(response)

        exc_factory = self._status_code_registry.get(response.status_code)

        if exc_factory:
            raise exc_factory()
        else:
            raise exceptions.UnknownError("Unexpected response", response.status_code)

    async def aclose(self) -> None:
        await self.client.aclose()
