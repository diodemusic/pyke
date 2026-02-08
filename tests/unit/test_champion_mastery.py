from pyke import Pyke, Region

from .base import TEST_PUUID, api


def test_masteries_by_puuid(api: Pyke):
    masteries_by_puuid = api.champion_mastery.masteries_by_puuid(
        region=Region.EUW,
        puuid=TEST_PUUID,
    )

    assert isinstance(masteries_by_puuid, list)

    for champion_mastery in masteries_by_puuid:
        assert isinstance(champion_mastery, dict)


def test_by_puuid_and_champion_id(api: Pyke):
    by_puuid_and_champion_id = api.champion_mastery.by_puuid_and_champion_id(
        region=Region.EUW, puuid=TEST_PUUID, champion_id=11
    )

    assert isinstance(by_puuid_and_champion_id, dict)


def test_masteries_by_puuid_top(api: Pyke):
    masteries_by_puuid_top = api.champion_mastery.masteries_by_puuid_top(
        region=Region.EUW, puuid=TEST_PUUID, count=10
    )

    assert isinstance(masteries_by_puuid_top, list)
    assert len(masteries_by_puuid_top) == 10

    for champion_mastery in masteries_by_puuid_top:
        assert isinstance(champion_mastery, dict)

    masteries_by_puuid_top = api.champion_mastery.masteries_by_puuid_top(
        region=Region.EUW, puuid=TEST_PUUID
    )

    assert isinstance(masteries_by_puuid_top, list)
    assert len(masteries_by_puuid_top) == 3

    for champion_mastery in masteries_by_puuid_top:
        assert isinstance(champion_mastery, dict)


def test_score_by_puuid(api: Pyke):
    score_by_puuid = api.champion_mastery.score_by_puuid(
        region=Region.EUW, puuid=TEST_PUUID
    )

    assert isinstance(score_by_puuid, int)
