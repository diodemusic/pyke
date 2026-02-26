from pyke import Continent, Division, Level, MatchType, Queue, Region, Tier

# --- Continent ---


def test_continent_values():
    assert Continent.AMERICAS.value == "americas"
    assert Continent.ASIA.value == "asia"
    assert Continent.EUROPE.value == "europe"
    assert Continent.SEA.value == "sea"


def test_continent_count():
    assert len(Continent) == 4


# --- Region ---


def test_region_values():
    assert Region.BR.value == "br1"
    assert Region.EUNE.value == "eun1"
    assert Region.EUW.value == "euw1"
    assert Region.JP.value == "jp1"
    assert Region.KR.value == "kr"
    assert Region.LAN.value == "la1"
    assert Region.LAS.value == "la2"
    assert Region.ME.value == "me1"
    assert Region.NA.value == "na1"
    assert Region.OCE.value == "oc1"
    assert Region.RU.value == "ru"
    assert Region.TR.value == "tr1"
    assert Region.SG.value == "sg2"
    assert Region.TW.value == "tw2"
    assert Region.VN.value == "vn2"


def test_region_no_duplicate_values():
    values = [r.value for r in Region]
    assert len(values) == len(set(values)), "Region enum has duplicate values"


# --- Queue ---


def test_queue_values():
    assert Queue.SOLO_DUO.value == "RANKED_SOLO_5x5"
    assert Queue.FLEX.value == "RANKED_FLEX_SR"


def test_queue_count():
    assert len(Queue) == 2


# --- Tier ---


def test_tier_values():
    assert Tier.IRON.value == "IRON"
    assert Tier.BRONZE.value == "BRONZE"
    assert Tier.SILVER.value == "SILVER"
    assert Tier.GOLD.value == "GOLD"
    assert Tier.PLATINUM.value == "PLATINUM"
    assert Tier.EMERALD.value == "EMERALD"
    assert Tier.DIAMOND.value == "DIAMOND"
    assert Tier.MASTER.value == "MASTER"
    assert Tier.GRANDMASTER.value == "GRANDMASTER"
    assert Tier.CHALLENGER.value == "CHALLENGER"


def test_tier_count():
    assert len(Tier) == 10


# --- Division ---


def test_division_values():
    assert Division.I.value == "I"
    assert Division.II.value == "II"
    assert Division.III.value == "III"
    assert Division.IV.value == "IV"


def test_division_count():
    assert len(Division) == 4


# --- Level ---


def test_level_values():
    assert Level.NONE.value == "NONE"
    assert Level.IRON.value == "IRON"
    assert Level.MASTER.value == "MASTER"
    assert Level.GRANDMASTER.value == "GRANDMASTER"
    assert Level.CHALLENGER.value == "CHALLENGER"
    assert Level.HIGHEST.value == "HIGHEST"
    assert Level.LOWEST.value == "LOWEST"


# --- MatchType ---


def test_match_type_values():
    assert MatchType.RANKED.value == "ranked"
    assert MatchType.NORMAL.value == "normal"
    assert MatchType.TOURNEY.value == "tourney"
    assert MatchType.TUTORIAL.value == "tutorial"


def test_type_count():
    assert len(MatchType) == 4
