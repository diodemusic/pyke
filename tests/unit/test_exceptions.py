import httpx
import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Region, exceptions

BASE = "https://euw1.api.riotgames.com/lol/status/v4/platform-data"


# --- Exception class attributes ---


def test_exception_message() -> None:
    exc = exceptions.DataNotFound("Not found", 404)
    assert exc.message == "Not found"
    assert exc.error_code == 404


def test_exception_str() -> None:
    exc = exceptions.DataNotFound("Not found", 404)
    assert str(exc) == "Not found (Error Code: 404)"


def test_exception_inherits_from_riot_api_exception() -> None:
    exc = exceptions.BadRequest("Bad request", 400)
    assert isinstance(exc, exceptions.RiotAPIException)
    assert isinstance(exc, Exception)


def test_all_exception_classes() -> None:
    classes = [
        (exceptions.BadRequest, 400),
        (exceptions.Unauthorized, 401),
        (exceptions.Forbidden, 403),
        (exceptions.DataNotFound, 404),
        (exceptions.MethodNotAllowed, 405),
        (exceptions.UnsupportedMediaType, 415),
        (exceptions.RateLimitExceeded, 429),
        (exceptions.InternalServerError, 500),
        (exceptions.BadGateway, 502),
        (exceptions.ServiceUnavailable, 503),
        (exceptions.GatewayTimeout, 504),
        (exceptions.UnknownError, 999),
        (exceptions.RequestTimeout, 408),
    ]
    for cls, code in classes:
        exc = cls("test message", code)
        assert exc.error_code == code
        assert exc.message == "test message"
        assert str(exc) == f"test message (Error Code: {code})"


# --- HTTP status code mapping ---


@pytest.mark.asyncio
async def test_400_raises_bad_request(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(400))
    with pytest.raises(exceptions.BadRequest) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 400


@pytest.mark.asyncio
async def test_401_raises_unauthorized(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(401))
    with pytest.raises(exceptions.Unauthorized) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 401


@pytest.mark.asyncio
async def test_403_raises_forbidden(pyke_client: Pyke, respx_mock: MockRouter) -> None:
    respx_mock.get(BASE).mock(return_value=Response(403))
    with pytest.raises(exceptions.Forbidden) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 403


@pytest.mark.asyncio
async def test_404_raises_data_not_found(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(404))
    with pytest.raises(exceptions.DataNotFound) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 404


@pytest.mark.asyncio
async def test_405_raises_method_not_allowed(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(405))
    with pytest.raises(exceptions.MethodNotAllowed):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_415_raises_unsupported_media_type(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(415))
    with pytest.raises(exceptions.UnsupportedMediaType):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_429_raises_rate_limit_exceeded(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(429))
    with pytest.raises(exceptions.RateLimitExceeded) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 429


@pytest.mark.asyncio
async def test_500_raises_internal_server_error(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(500))
    with pytest.raises(exceptions.InternalServerError):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_502_raises_bad_gateway(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(502))
    with pytest.raises(exceptions.BadGateway):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_503_raises_service_unavailable(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(503))
    with pytest.raises(exceptions.ServiceUnavailable):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_504_raises_gateway_timeout(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(504))
    with pytest.raises(exceptions.GatewayTimeout):
        await pyke_client.lol_status.platform_data(Region.EUW)


@pytest.mark.asyncio
async def test_unknown_status_code_raises_unknown_error(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(418))
    with pytest.raises(exceptions.UnknownError) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 418


@pytest.mark.asyncio
async def test_timeout_raises_request_timeout(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(side_effect=httpx.TimeoutException("timed out"))
    with pytest.raises(exceptions.RequestTimeout) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)
    assert exc_info.value.error_code == 408


# --- Fresh exception instances ---


@pytest.mark.asyncio
async def test_each_raise_produces_fresh_exception(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(404))

    with pytest.raises(exceptions.DataNotFound) as first:
        await pyke_client.lol_status.platform_data(Region.EUW)

    with pytest.raises(exceptions.DataNotFound) as second:
        await pyke_client.lol_status.platform_data(Region.EUW)

    assert first.value is not second.value


# --- Pyke init validation ---


def test_none_api_key_raises() -> None:
    with pytest.raises(ValueError):
        Pyke(None)


def test_valid_api_key_accepted() -> None:
    client = Pyke("RGAPI-000000000000000000000000000000000000")
    assert client is not None


@pytest.mark.asyncio
async def test_exception_exposes_response(
    pyke_client: Pyke, respx_mock: MockRouter
) -> None:
    respx_mock.get(BASE).mock(return_value=Response(429))

    with pytest.raises(exceptions.RateLimitExceeded) as exc_info:
        await pyke_client.lol_status.platform_data(Region.EUW)

    assert exc_info.value.response is not None
    assert exc_info.value.response.status_code == 429


def test_exception_repr() -> None:
    exc = exceptions.DataNotFound("Not found", 404)
    assert (
        repr(exc) == "DataNotFound(message='Not found', error_code=404, response=None)"
    )
