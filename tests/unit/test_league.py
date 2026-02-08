from pyke import Division, Pyke, Queue, Region, Tier

from .base import TEST_LEAGUE_ID, TEST_PUUID, api


def test_challenger_leagues_by_queue(api: Pyke):
    challenger_leagues_by_queue = api.league.challenger_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )
    league_list = challenger_leagues_by_queue["entries"]

    assert isinstance(challenger_leagues_by_queue, dict)
    assert isinstance(league_list, list)

    for league_entry in challenger_leagues_by_queue["entries"]:
        assert isinstance(league_entry, dict)


def test_by_puuid(api: Pyke):
    if not TEST_PUUID:
        quit()

    by_puuid = api.league.by_puuid(region=Region.EUW, puuid=TEST_PUUID)

    assert isinstance(by_puuid, list)

    for league_entry in by_puuid:
        assert isinstance(league_entry, dict)


def test_by_queue_tier_division(api: Pyke):
    by_queue_tier_division = api.league.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    assert isinstance(by_queue_tier_division, list)

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, dict)

    by_queue_tier_division = api.league.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    assert isinstance(by_queue_tier_division, list)

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, dict)


def test_grandmaster_leagues_by_queue(api: Pyke):
    grandmaster_leagues_by_queue = api.league.grandmaster_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    league_list = grandmaster_leagues_by_queue["entries"]

    assert isinstance(grandmaster_leagues_by_queue, dict)
    assert isinstance(league_list, list)

    for league_entry in grandmaster_leagues_by_queue["entries"]:
        assert isinstance(league_entry, dict)


def test_by_league_id(api: Pyke):
    if not TEST_LEAGUE_ID:
        quit()

    by_league_id = api.league.by_league_id(region=Region.EUW, league_id=TEST_LEAGUE_ID)

    league_list = by_league_id["entries"]

    assert isinstance(by_league_id, dict)
    assert isinstance(league_list, list)

    for league_entry in by_league_id["entries"]:
        assert isinstance(league_entry, dict)


def test_master_leagues_by_queue(api: Pyke):
    master_leagues_by_queue = api.league.master_leagues_by_queue(
        region=Region.EUW, queue=Queue.SOLO_DUO
    )

    league_list = master_leagues_by_queue["entries"]

    assert isinstance(master_leagues_by_queue, dict)
    assert isinstance(league_list, list)

    for league_entry in master_leagues_by_queue["entries"]:
        assert isinstance(league_entry, dict)
