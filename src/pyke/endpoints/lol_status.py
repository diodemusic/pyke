from typing import Any

from pyke import Region

from .._base_client import _BaseApiClient


class StatusEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    def platform_data(self, region: Region) -> dict[Any, Any]:
        """# Get League of Legends status for the given platform

        **Example:**  
            `status = api.lol_status.platform_data(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = "/lol/status/v4/platform-data"
        data = self._client._region_request(region=region, path=path)

        return data
