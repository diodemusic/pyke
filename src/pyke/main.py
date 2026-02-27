# pyke

from __future__ import annotations

import types

from ._base_client import _BaseApiClient
from ._base_data_dragon_client import _BaseDataDragonClient
from .ddragon.challenges import ChallengesData
from .ddragon.champion import ChampionData
from .ddragon.champion_full import ChampionFullData
from .ddragon.item import ItemData
from .ddragon.item_modifiers import ItemModifiersData
from .ddragon.language import LanguageData
from .ddragon.map import MapData
from .ddragon.mission_assets import MissionAssetsData
from .ddragon.profileicon import ProfileiconData
from .ddragon.runes_reforged import RunesReforgedData
from .ddragon.spellbuffs import SpellbuffsData
from .ddragon.sticker import StickerData
from .ddragon.summoner import SummonerData
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


class Pyke:
    """# Main entrypoint for interacting with the Riot API

    **Example:**  
        `api = Pyke("RGAPI-...")`

    **Args:**  
        `api_key (str | None)` Your Riot API key.  
        `timeout (int, optional)` Request timeout in seconds. Defaults to 60.  
        `print_url (bool, optional)` Print endpoint URL. Defaults to False.  
    """  # fmt: skip

    def __init__(
        self,
        api_key: str | None,
        timeout: int = 60,
        print_url: bool = False,
    ) -> None:
        self._client = _BaseApiClient(api_key, timeout, print_url)

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

    async def __aenter__(self) -> Pyke:
        return self

    async def __aexit__(
        self,
        exc_type: BaseException | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._client.aclose()


class DataDragon:
    def __init__(self, timeout: int = 60, print_url: bool = False) -> None:
        self._client = _BaseDataDragonClient(timeout, print_url)

        self.spellbuffs = SpellbuffsData(self._client)
        self.item = ItemData(self._client)
        self.runes_reforged = RunesReforgedData(self._client)
        self.language = LanguageData(self._client)
        self.item_modifiers = ItemModifiersData(self._client)
        self.champion_full = ChampionFullData(self._client)
        self.summoner = SummonerData(self._client)
        self.champion = ChampionData(self._client)
        self.challenges = ChallengesData(self._client)
        self.mission_assets = MissionAssetsData(self._client)
        self.sticker = StickerData(self._client)
        self.profileicon = ProfileiconData(self._client)
        self.map = MapData(self._client)

    async def __aenter__(self) -> DataDragon:
        return self

    async def __aexit__(
        self,
        exc_type: BaseException | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._client.aclose()
