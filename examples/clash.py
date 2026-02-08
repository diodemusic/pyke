import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

api = Pyke(API_KEY)

# Let's check if there is currently a clash
tournaments = api.clash.tournaments(Region.EUW)

if not tournaments:
    print("There are currently no clashes planned/running")
    quit()

# If there is a clash, let's see what position we are playing
# We will need our puuid
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# We can get our clash team like this
players = api.clash.by_puuid(Region.EUW, account["puuid"])

if not players:
    print("You are not in an active clash team")
    quit()

# Let's print what roles everyone is playing
for player in players:
    if player["puuid"] == account["puuid"]:
        # We already know our own riot id from the account call we made, no need to get it again
        riot_id = f"{account['gameName']}#{account['tagLine']}"
    else:
        # For everyone else let's convert puuid to riot id
        team_mate_account = api.account.by_puuid(Continent.EUROPE, player["puuid"])
        riot_id = f"{account['gameName']}#{account['tagLine']}"

    # Finally we can print the players riot id and role
    print(f"{riot_id} is playing the {player['position']['value']} role.")
