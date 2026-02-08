import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# First we are going to need our puuid
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Now we can get our summoner data
summoner = api.summoner.by_puuid(Region.EUW, account["puuid"])

# Now that we have our summoner data we can get things like our profile icon id and summoner level
# Which we cannot get with the account endpoint alone
print(
    f"{account['gameName']}#{account['tagLine']} is level {summoner['summonerLevel']}."
)

if summoner["summonerLevel"] > 500:
    print("What a nerd.")
