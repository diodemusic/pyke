import asyncio

from pyke import DataDragon


async def main():
    # Let's create a DataDragon instance, the latest version will be used
    async with DataDragon() as ddragon:
        # Now we can use ddragon like this
        champions = await ddragon.champion.get_all("en_GB")
        print(champions["data"]["Zaahen"]["blurb"])


if __name__ == "__main__":
    asyncio.run(main())
