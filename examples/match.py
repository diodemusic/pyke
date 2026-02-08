import os

from dotenv import load_dotenv

from pyke import Continent, Division, Pyke, Queue, Region, Tier

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Let's get some plat 2 players
league = api.league.by_queue_tier_division(
    Region.EUW, Queue.SOLO_DUO, Tier.PLATINUM, Division.II
)

for player in league[0:10]:
    # Now we get the players last match ID
    match_ids = api.match.match_ids_by_puuid(Continent.EUROPE, player["puuid"], count=1)

    # Fetch and analyze the match
    for match_id in match_ids:
        match = api.match.by_match_id(Continent.EUROPE, match_id)

        # Count wins for top and mid champions
        for participant in match["info"]["participants"]:
            if participant["puuid"] == player["puuid"]:
                print(f"PUUID: {player['puuid']}")
                print(
                    f"They played {participant['championName']} in their most recent Solo/Duo game"
                )
                print(
                    f"They had {participant['kills']} kills and {participant['deaths']} deaths"
                )

                if participant["win"]:
                    print("They won this game")
                else:
                    print("They lost this game")

                print("-" * 20)
