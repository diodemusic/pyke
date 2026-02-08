from pyke import Pyke, Region

from .base import api


def test_platform_data(api: Pyke):
    test_platform_data = api.lol_status.platform_data(region=Region.EUW)

    assert isinstance(test_platform_data, dict)
