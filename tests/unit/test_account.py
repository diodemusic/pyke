from pyke import Continent, Pyke

from .base import TEST_PUUID, api


def test_by_puuid(api: Pyke):
    by_puuid = api.account.by_puuid(
        continent=Continent.EUROPE,
        puuid=TEST_PUUID,
    )

    assert isinstance(by_puuid, dict)


def test_by_riot_id(api: Pyke):
    by_riot_id = api.account.by_riot_id(
        continent=Continent.EUROPE, game_name="saves", tag_line="000"
    )

    assert isinstance(by_riot_id, dict)


def test_region_by_puuid(api: Pyke):
    region_by_puuid = api.account.region_by_puuid(
        continent=Continent.EUROPE, puuid=TEST_PUUID
    )

    assert isinstance(region_by_puuid, dict)
