import os
import random

from dotenv import load_dotenv

from pyke import Continent, Level, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

api = Pyke(API_KEY)

# Let's grab a random challenge from the lol_challenges.config method
challenge = random.choice(api.lol_challenges.config(Region.EUW))

# Now we can get the top players from our random challenge
top_players = api.lol_challenges.leaderboards_by_level(
    Region.EUW, Level.CHALLENGER, challenge["id"]
)

# Let's make our own leaderboard for the top ten players
print("-" * 20)
challenge_english = challenge["localizedNames"]["en_GB"]
print(f"{challenge_english['name']}: {challenge_english['description']}")

for top_player in top_players[:10]:
    # Right now we only know the players puuid, let's get their Riot id with the account.by_puuid method
    account = api.account.by_puuid(Continent.EUROPE, top_player["puuid"])

    # Finally we can print the stats of our top players
    print(
        f"{account['gameName']}#{account['tagLine']} is rank {top_player['position']} with {top_player['value']} points."
    )
