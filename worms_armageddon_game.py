from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Set up the options.
@dataclass
class WormsArmageddonArchipelagoOptions:
    pass

class WormsArmageddonGame(Game):
    # Set the game name.
    name = "Worms Armageddon"

    # Set the platforms for this game.
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX
    ]

    # Set whether or not this game falls under AP-AfterDark.
    is_adult_only_or_unrated = False

    # Set this game's options.
    options_cls = WormsArmageddonArchipelagoOptions

    # Create this game's objectives.
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s).",
                data={ 
                    "OPPONENT": (self.opponent_count, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s) on a cavern map.",
                data={ 
                    "OPPONENT": (self.opponent_count, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s) on an open air map.",
                data={ 
                    "OPPONENT": (self.opponent_count, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s) using the SCHEME scheme.",
                data={ 
                    "OPPONENT": (self.opponent_count, 1),
                    "SCHEME": (self.schemes, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s) on a cavern map using the SCHEME scheme.",
                data={ 
                    "OPPONENT": (self.opponent_count, 1),
                    "SCHEME": (self.schemes, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win a match against OPPONENT computer player(s) on an open air map using the SCHEME scheme.",
                data={ 
                    "OPPONENT": (self.opponent_count, 1),
                    "SCHEME": (self.schemes, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            )
        ]

        # Return our list of objectives.
        return objectives
    
    # Selects a random number between 1 (inclusive) and 6 (exclusive).
    @staticmethod
    def opponent_count() -> range:
        return range(1, 6)
    
    # Define the list of schemes.
    @staticmethod
    def schemes() -> List[str]:
        return [
            "Beginner",
            "Intermediate",
            "Pro",
            "Tournament",
            "Classic",
            "Retro",
            "Artillery",
            "Sudden Sinking",
            "Strategic",
            "Darkside",
            "Armageddon",
            "Blast Zone"
        ]