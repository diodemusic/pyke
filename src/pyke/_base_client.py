import json
from typing import Any

import httpx
from httpx import Response

from . import exceptions

__all__ = ["_BaseClient"]


class _BaseClient:
    _STATUS_MESSAGES = {
        400: (exceptions.BadRequest, "Bad request"),
        401: (exceptions.Unauthorized, "Unauthorized"),
        403: (exceptions.Forbidden, "Forbidden"),
        404: (exceptions.DataNotFound, "Data not found"),
        405: (exceptions.MethodNotAllowed, "Method not allowed"),
        415: (exceptions.UnsupportedMediaType, "Unsupported media type"),
        429: (exceptions.RateLimitExceeded, "Rate limit exceeded"),
        500: (exceptions.InternalServerError, "Internal server error"),
        502: (exceptions.BadGateway, "Bad gateway"),
        503: (exceptions.ServiceUnavailable, "Service unavailable"),
        504: (exceptions.GatewayTimeout, "Gateway timeout"),
    }

    def __init__(self, timeout: int, print_url: bool) -> None:
        self.timeout = timeout
        self.print_url = print_url
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500, response)

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

        exc, message = self._STATUS_MESSAGES.get(
            response.status_code, (exceptions.UnknownError, "Unknown error")
        )

        raise exc(message, response.status_code, response)

    async def aclose(self) -> None:
        await self.client.aclose()
