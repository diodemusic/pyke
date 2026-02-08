import os

from dotenv import load_dotenv

from pyke import Division, Pyke, Queue, Region, Tier

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Let's get some gold 2 players
entries = api.league_exp.by_queue_tier_division(
    Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
)

# Now we can print our gold 2 players
for entry in entries:
    print(f"PUUID:  {entry['puuid']}")
    print(f"Rank:   {entry['tier']} {entry['rank']}")
    print(f"LP:     {entry['leaguePoints']}")
    print(f"Wins:   {entry['wins']}")
    print(f"Losses: {entry['losses']}")
    print("-" * 50)
