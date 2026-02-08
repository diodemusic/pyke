import os

from dotenv import load_dotenv

from pyke import Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
api = Pyke(API_KEY)

# Does EUW have any issues or maintenance right now?
status = api.lol_status.platform_data(Region.EUW)

# If there are any incidents we will print the incident in english
for incident in status["incidents"]:
    if incident["incidentSeverity"]:
        print(
            f"{incident['incidentSeverity']['name']} incident: {incident['titles'][0]['content']}"
        )

        print("Platforms affected:")

        for platform in incident["platforms"]:
            print(platform["name"])

        print("-" * 20)
