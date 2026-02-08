import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

current_game = api.spectator.by_puuid(
    Region.EUW,
    api.account.by_riot_id(Continent.EUROPE, "saves", "000")["puuid"],
)

teams = {100: "Blue", 200: "Red"}

for banned_champion in current_game["bannedChampions"]:
    team = teams[banned_champion["teamId"]]
    print(
        f"Team: {team} Pick: {banned_champion['pickTurn']} Banned champion: {banned_champion['championId']}"
    )
