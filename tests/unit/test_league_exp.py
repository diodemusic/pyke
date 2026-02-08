from pyke import Division, Pyke, Queue, Region, Tier

from .base import api


def test_by_queue_tier_division(api: Pyke):
    by_queue_tier_division = api.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
    )

    assert isinstance(by_queue_tier_division, list)

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, dict)

    by_queue_tier_division = api.league_exp.by_queue_tier_division(
        Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
    )

    assert isinstance(by_queue_tier_division, list)

    for league_entry in by_queue_tier_division:
        assert isinstance(league_entry, dict)
