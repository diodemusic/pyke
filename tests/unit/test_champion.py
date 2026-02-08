from pyke import Pyke, Region

from .base import api


def test_rotations(api: Pyke):
    rotations = api.champion.rotations(region=Region.EUW)

    assert isinstance(rotations, dict)
