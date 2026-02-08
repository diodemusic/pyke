import re

from pyke import Continent, Pyke, Type

from .base import TEST_MATCH_ID, TEST_PUUID, api


def test_match_ids_by_puuid(api: Pyke):
    match_ids_by_puuid = api.match.match_ids_by_puuid(
        continent=Continent.EUROPE,
        puuid=TEST_PUUID,
        start_time=1744502400,
        end_time=1760313600,
        queue=420,
        type=Type.RANKED,
        start=17,
        count=38,
    )

    for match_id in match_ids_by_puuid:
        assert isinstance(match_id, str)
        assert re.search(r"[A-Z0-9]+_\d{10}", match_id)


def test_by_match_id(api: Pyke):
    by_match_id = api.match.by_match_id(
        continent=Continent.EUROPE, match_id=TEST_MATCH_ID
    )

    assert isinstance(by_match_id, dict)


def test_timeline_by_match_id(api: Pyke):
    timeline_by_match_id = api.match.timeline_by_match_id(
        continent=Continent.EUROPE, match_id=TEST_MATCH_ID
    )

    assert isinstance(timeline_by_match_id, dict)
