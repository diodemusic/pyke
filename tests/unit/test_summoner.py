from pyke import Pyke, Region

from .base import TEST_PUUID, api


def test_by_puuid(api: Pyke):
    by_puuid = api.summoner.by_puuid(
        region=Region.EUW,
        puuid=TEST_PUUID,
    )

    assert isinstance(by_puuid, dict)
