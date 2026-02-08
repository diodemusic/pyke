import logging
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

# Configure logging BEFORE creating the Pyke instance
# This is the standard Python way to enable logging for all libraries
logging.basicConfig(
    level=logging.INFO,  # Show INFO, WARNING, and ERROR logs
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

# Logging levels from least to most severe:
# - DEBUG: Detailed diagnostic information (not used in this example)
# - INFO: Request URLs, rate limit tracking (e.g., "(45/100) - https://...")
# - WARNING: Retries, rate limiting, malformed API responses
# - ERROR: Breaking failures

# Change level to logging.WARNING for quieter output (production)
# Change level to logging.DEBUG for maximum verbosity (troubleshooting)

# Create Pyke instance and make requests
api = Pyke(API_KEY)

# Make a request - you'll see INFO logs showing the URL and rate limit status
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

print(f"Riot ID: {account['gameName']}#{account['tagLine']}")
print(f"PUUID: {account['puuid']}")

# Other useful logging configurations:

# Completely silent (no logs from pyke):
logging.getLogger("pyke").setLevel(logging.CRITICAL)
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")

# Log to file instead of console:
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename="api_requests.log",
)
account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")
