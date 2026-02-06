from pyke import Continent

from .._base_client import _BaseApiClient


class AccountEndpoint:
    """There are three routing values for account-v1; americas, asia, and europe. You can query for any account in any region. We recommend using the nearest cluster."""

    def __init__(self, client: _BaseApiClient):
        self._client = client

    def by_puuid(self, continent: Continent, puuid: str):
        """# Get account by puuid

        **Example:**  
            `account = api.account.by_puuid(Continent.EUROPE, "some puuid")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `AccountDto` [AccountDto](/pyke/pyke/models/account_v1.html#AccountDto).
        """  # fmt: skip

        path = f"/riot/account/v1/accounts/by-puuid/{puuid}"
        data = self._client._continent_request(continent=continent, path=path)

        return data

    def by_riot_id(self, continent: Continent, game_name: str, tag_line: str):
        """# Get account by riot id

        **Example:**  
            `account = api.account.by_riot_id(Continent.EUROPE, "saves", "000")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `game_name (str)` Riot id game name.  
            `tag_line (str)` Riot id tag line.  

        **Returns:**  
            `AccountDto` [AccountDto](/pyke/pyke/models/account_v1.html#AccountDto).
        """  # fmt: skip

        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        data = self._client._continent_request(continent=continent, path=path)

        return data

    def region_by_puuid(self, continent: Continent, puuid: str):
        """# Get active region (lol and tft)

        **Example:**  
            `region = api.account.region_by_puuid(Continent.EUROPE, "some puuid")`

        **Args:**  
            `continent (Continent)` [Continent](/pyke/pyke.html#Continent) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `AccountRegionDTO` [AccountRegionDTO](/pyke/pyke/models/account_v1.html#AccountRegionDTO).
        """  # fmt: skip

        path = f"/riot/account/v1/region/by-game/lol/by-puuid/{puuid}"
        data = self._client._continent_request(continent=continent, path=path)

        return data
