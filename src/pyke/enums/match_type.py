from enum import Enum


class MatchType(Enum):
    """# Type of match"""

    RANKED = "ranked"
    NORMAL = "normal"
    TOURNEY = "tourney"
    TUTORIAL = "tutorial"
