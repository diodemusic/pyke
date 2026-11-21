import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY, timeout=60, print_url=True) as api:
        # If we get rate limited, the exception's response has a Retry-After header saying how many
        # seconds to wait. It can be missing, so we fall back to 10 seconds.
        try:
            await api.account.by_riot_id(Continent.EUROPE, "saves", "000")
        except exceptions.RateLimitExceeded as e:
            if e.response:
                await asyncio.sleep(int(e.response.headers.get("retry-after", "10")))


if __name__ == "__main__":
    asyncio.run(main())
