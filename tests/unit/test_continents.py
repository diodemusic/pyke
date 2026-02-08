from pyke import Continent, Pyke, Queue, Region

from .base import api


def test_americas(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.NA, Queue.SOLO_DUO)
    puuid = league["entries"][0]["puuid"]
    account = api.account.by_puuid(Continent.AMERICAS, puuid)

    assert isinstance(account, dict)


def test_asia(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.KR, Queue.SOLO_DUO)
    puuid = league["entries"][0]["puuid"]
    account = api.account.by_puuid(Continent.ASIA, puuid)

    assert isinstance(account, dict)


def test_europe(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.EUW, Queue.SOLO_DUO)
    puuid = league["entries"][0]["puuid"]
    account = api.account.by_puuid(Continent.EUROPE, puuid)

    assert isinstance(account, dict)


def test_sea(api: Pyke):
    league = api.league.challenger_leagues_by_queue(Region.OCE, Queue.SOLO_DUO)
    puuid = league["entries"][0]["puuid"]
    account = api.account.by_puuid(Continent.ASIA, puuid)
    match_ids = api.match.match_ids_by_puuid(Continent.SEA, puuid)

    assert isinstance(account, dict)
    assert isinstance(match_ids, list)
    assert isinstance(match_ids[0], str)
