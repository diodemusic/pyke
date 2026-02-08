from pyke import Pyke, Queue, Region

from .base import api


def test_regions(api: Pyke):
    for region in Region:
        league = api.league.challenger_leagues_by_queue(region, Queue.SOLO_DUO)

        assert isinstance(league, dict)
