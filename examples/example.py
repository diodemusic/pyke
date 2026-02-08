import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# Initialize the API
api = Pyke(API_KEY)

# Every pyke method follows the same convention as the Riot API
# For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

print(f"Riot ID: {account['gameName']}#{account['tagLine']}")
print(f"PUUID:   {account['puuid']}")

# pyke throws typed exceptions matching Riot API error codes
try:
    region = api.account.region_by_puuid(Continent.EUROPE, account["puuid"])
except exceptions.DataNotFound as e:
    print(e)  # Output: Data not found (Error Code: 404)
    quit()
