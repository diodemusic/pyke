# pyke

from __future__ import annotations

from ._base_client import _BaseApiClient
from ._base_data_dragon_client import _BaseDataDragonClient

# Data dragon
from .ddragon.challenges import ChallengesData
from .ddragon.champion import ChampionData
from .ddragon.champion_full import ChampionFullData
from .ddragon.feats import FeatsData
from .ddragon.item import ItemData
from .ddragon.language import LanguageData
from .ddragon.map import MapData
from .ddragon.profileicon import ProfileiconData
from .ddragon.runes_reforged import RunesReforgedData
from .ddragon.spellbuffs import SpellbuffsData
from .ddragon.sticker import StickerData
from .ddragon.summoner import SummonerData

# Riot API
from .endpoints.account import AccountEndpoint
from .endpoints.champion import ChampionEndpoint
from .endpoints.champion_mastery import ChampionMasteryEndpoint
from .endpoints.clash import ClashEndpoint
from .endpoints.league import LeagueEndpoint
from .endpoints.league_exp import LeagueExpEndpoint
from .endpoints.lol_challenges import ChallengesEndpoint
from .endpoints.lol_status import StatusEndpoint
from .endpoints.match import MatchEndpoint
from .endpoints.spectator import SpectatorEndpoint
from .endpoints.summoner import SummonerEndpoint

# from .ddragon.versions import VersionsData


class Pyke:
    """# Main entrypoint for interacting with the Riot API

    **Example:**  
        `api = Pyke("API_KEY")`

    **Args:**  
        `api_key (str | None)` Your Riot API key.  
        `smart_rate_limiting (bool, optional)` Automatically throttle requests to stay under rate limits. Defaults to True.  
        `timeout (int, optional)` Request timeout in seconds. Defaults to 60.  
        `max_rate_limit_retries (int, optional)` Maximum retry attempts for 429 rate limit errors. Defaults to 5.  
        `max_server_error_retries (int, optional)` Maximum retry attempts for 502/503/504 server errors. Defaults to 3.
    """  # fmt: skip

    def __init__(
        self,
        api_key: str | None,
        timeout: int = 60,
    ) -> None:
        self._client = _BaseApiClient(
            api_key,
            timeout,
        )

        self.account = AccountEndpoint(self._client)
        self.champion_mastery = ChampionMasteryEndpoint(self._client)
        self.champion = ChampionEndpoint(self._client)
        self.clash = ClashEndpoint(self._client)
        self.league_exp = LeagueExpEndpoint(self._client)
        self.league = LeagueEndpoint(self._client)
        self.lol_challenges = ChallengesEndpoint(self._client)
        self.lol_status = StatusEndpoint(self._client)
        self.match = MatchEndpoint(self._client)
        self.spectator = SpectatorEndpoint(self._client)
        self.summoner = SummonerEndpoint(self._client)


class DataDragon:
    def __init__(self, version: str | None = None, timeout: int = 10) -> None:
        self._client = _BaseDataDragonClient(version, timeout)

        # self.versions = VersionsData(self._client)
        self.spellbuffs = SpellbuffsData(self._client)
        self.item = ItemData(self._client)
        self.runes_reforged = RunesReforgedData(self._client)
        self.language = LanguageData(self._client)
        self.feats = FeatsData(self._client)
        self.champion_full = ChampionFullData(self._client)
        self.summoner = SummonerData(self._client)
        self.champion = ChampionData(self._client)
        self.challenges = ChallengesData(self._client)
        self.sticker = StickerData(self._client)
        self.profileicon = ProfileiconData(self._client)
        self.map = MapData(self._client)
