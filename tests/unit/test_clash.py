# from pyke import Pyke, Region

# from .base import TEST_PUUID, TEST_TEAM_ID, TEST_TOURNAMENT_ID, api


# def test_by_puuid(api: Pyke):
#     by_puuid = api.clash.by_puuid(Region.EUW, TEST_PUUID)

#     assert isinstance(by_puuid, list)

#     for player in by_puuid:
#         assert isinstance(player, dict)


# def test_by_team_id(api: Pyke):
#     by_team_id = api.clash.by_team_id(Region.EUW, TEST_TEAM_ID)

#     assert isinstance(by_team_id, dict)


# def test_tournaments(api: Pyke):
#     tournaments = api.clash.tournaments(Region.EUW)

#     assert isinstance(tournaments, list)

#     for tournament in tournaments:
#         assert isinstance(tournament, dict)


# def test_tournament_by_team_id(api: Pyke):
#     tournament_by_team_id = api.clash.tournament_by_team_id(Region.EUW, TEST_TEAM_ID)

#     assert isinstance(tournament_by_team_id, dict)


# def test_tournament_by_tournament_id(api: Pyke):
#     tournament_by_tournament_id = api.clash.tournament_by_tournament_id(
#         Region.EUW, TEST_TOURNAMENT_ID
#     )

#     assert isinstance(tournament_by_tournament_id, dict)
