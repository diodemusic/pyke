import os

from dotenv import load_dotenv

from pyke import Continent, Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

print(f"PUUID: {account['puuid']}")
print(f"Game name: {account['gameName']}")
print(f"Tag line: {account['tagLine']}")

region = api.account.region_by_puuid(Continent.EUROPE, account["puuid"])

print(f"PUUID: {region['puuid']}")
print(f"Game: {region['game']}")
print(f"Region: {region['region']}")
