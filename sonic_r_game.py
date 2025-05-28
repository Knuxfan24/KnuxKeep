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
class SonicRArchipelagoOptions:
    pass

class SonicRGame(Game):
    # Set the game name.
    name = "Sonic R"

    # Set the platforms for this game.
    platform = KeymastersKeepGamePlatforms.SAT
    platforms_other = [
        KeymastersKeepGamePlatforms.PC,
        KeymastersKeepGamePlatforms.PS2,
        KeymastersKeepGamePlatforms.GC
    ]

    # Set whether or not this game falls under AP-AfterDark.
    is_adult_only_or_unrated = False

    # Set this game's options.
    options_cls = SonicRArchipelagoOptions

    # Create this game's objectives.
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate
            (
                label="Win on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks, 1),
                    "CHARACTER": (self.easy_characters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Win on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks, 1),
                    "CHARACTER": (self.hard_characters, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=9
            ),
            GameObjectiveTemplate
            (
                label="Collect the Chaos Emerald(s) on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks_noradiant, 1),
                    "CHARACTER": (self.easy_characters_nosuper, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=8
            ),
            GameObjectiveTemplate
            (
                label="Collect the Chaos Emerald(s) on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks_noradiant, 1),
                    "CHARACTER": (self.hard_characters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=7
            ),
            GameObjectiveTemplate
            (
                label="Collect the Sonic Tokens on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks_noradiant, 1),
                    "CHARACTER": (self.characters_norivals, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Collect the Sonic Tokens and Chaos Emerald(s) on TRACK as CHARACTER.",
                data={
                    "TRACK": (self.tracks_noradiant, 1),
                    "CHARACTER": (self.characters_norivals, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=7
            ),
            GameObjectiveTemplate
            (
                label="Place 1st in every race and see the credits as CHARACTER.",
                data={
                    "CHARACTER": (self.easy_characters, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=8
            ),
            GameObjectiveTemplate
            (
                label="Place 1st in every race and see the credits as CHARACTER.",
                data={
                    "CHARACTER": (self.hard_characters, 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=7
            ),
            GameObjectiveTemplate
            (
                label="Perform a 100% run from a fresh save file.",
                data={ },
                is_time_consuming=True,
                is_difficult=False,
                weight=5
            )
        ]

        # Return our list of objectives.
        return objectives
    
    # Define the list of stages.
    @staticmethod
    def tracks() -> List[str]:
        return [
            "Resort Island",
            "Radical City",
            "Regal Ruin",
            "Reactive Factory",
            "Radiant Emerald"
        ]

    # Define the list of characters.
    @staticmethod
    def easy_characters() -> List[str]:
        return [
            "Sonic",
            "Tails",
            "Knuckles",
            "Metal Sonic",
            "Metal Knuckles",
            "Super Sonic"
        ]

    # Define the list of characters.
    @staticmethod
    def hard_characters() -> List[str]:
        return [
            "Amy",
            "Dr. Eggman",
            "Tails Doll",
            "Egg Robo"
        ]

    # Define the list of characters.
    @staticmethod
    def easy_characters_nosuper() -> List[str]:
        return [
            "Sonic",
            "Tails",
            "Knuckles",
            "Metal Sonic",
            "Metal Knuckles"
        ]

    # Define the list of characters.
    @staticmethod
    def characters_norivals() -> List[str]:
        return [
            "Sonic",
            "Tails",
            "Knuckles",
            "Amy",
            "Dr. Eggman"
        ]
    
    # Define the list of stages.
    @staticmethod
    def tracks_noradiant() -> List[str]:
        return [
            "Resort Island",
            "Radical City",
            "Regal Ruin",
            "Reactive Factory"
        ]