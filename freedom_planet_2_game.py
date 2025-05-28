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
class FreedomPlanet2ArchipelagoOptions:
    freedom_planet_2_custom_characters: CustomCharactersOption
    freedom_planet_2_custom_stages: CustomStagesOption

class FreedomPlanet2Game(Game):
    # Set the game name.
    name = "Freedom Planet 2"

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
    options_cls = FreedomPlanet2ArchipelagoOptions

    # Create this game's objectives.
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate
            (
                label="Clear STAGE as CHARACTER",
                data={ 
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.characters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10
            ),
            GameObjectiveTemplate
            (
                label="Clear STAGE as CHARACTER with BRAVESTONE equipped",
                data={ 
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.characters, 1),
                    "BRAVESTONE": (self.bravestones, 2)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1
            ),
            GameObjectiveTemplate
            (
                label="Clear CHALLENGES Battlesphere Challenge(s) as CHARACTER",
                data={ 
                    "CHALLENGES": (self.battlesphere_count_low, 1),
                    "CHARACTER": (self.characters, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5
            ),
            GameObjectiveTemplate
            (
                label="Clear CHALLENGES Battlesphere Challenges as CHARACTER",
                data={ 
                    "CHALLENGES": (self.battlesphere_count_high, 1),
                    "CHARACTER": (self.characters, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate
            (
                label="Clear CHALLENGES Battlesphere Challenge(s) as CHARACTER with BRAVESTONE equipped",
                data={ 
                    "CHALLENGES": (self.battlesphere_count_low, 1),
                    "CHARACTER": (self.characters, 1),
                    "BRAVESTONE": (self.bravestones, 2)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=5
            ),
            GameObjectiveTemplate
            (
                label="Clear CHALLENGES Battlesphere Challenges as CHARACTER with BRAVESTONE equipped",
                data={ 
                    "CHALLENGES": (self.battlesphere_count_high, 1),
                    "CHARACTER": (self.characters, 1),
                    "BRAVESTONE": (self.bravestones, 2)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3
            )
        ]

        # Return our list of objectives.
        return objectives
    
    # Define the list of stages.
    def stages(self) -> List[str]:
        # Create a list of the base game stages.
        base_stages = [
            "Dragon Valley",
            "Shenlin Park",
            "Tiger Falls",
            "Robot Graveyard",
            "Shade Armory",
            "Snowfields",
            "Avian Museum",
            "Airship Sigwada",
            "Phoenix Highway",
            "Zao Land",
            "Globe Opera 1",
            "Globe Opera 2",
            "Auditorium",
            "Palace Courtyard",
            "Tidal Gate",
            "Sky Bridge",
            "Lightning Tower",
            "Zulon Jungle",
            "Nalao Lake",
            "Ancestral Forge",
            "Magma Starscape",
            "Diamond Point",
            "Gravity Bubble",
            "Bakunawa Rush",
            "Refinery Room",
            "Clockwork Arboretum",
            "Inversion Dynamo",
            "Lunar Cannon",
            "Merga",
            "Weapon's Core"
        ]
        
        # Return a list with both the base game stages and the custom stages combined.
        return base_stages + sorted(self.archipelago_options.freedom_planet_2_custom_stages.value)
    
    # Define the list of characters.
    def characters(self) -> List[str]:
        # Create a list of the base game characters.
        base_characters = [
            "Lilac",
            "Carol",
            "Milla",
            "Neera"
        ]
        
        # Return a list with both the base game characters and the custom characters combined.
        return base_characters + sorted(self.archipelago_options.freedom_planet_2_custom_characters.value)
    
    # Define the list of Brave Stones.
    @staticmethod
    def bravestones() -> List[str]:
        return [
            "No Stocks",
            "Expensive Stocks",
            "Double Damage",
            "No Revivals",
            "No Guarding",
            "No Petals",
            "Time Limit",
            "Items To Bombs",
            "Life Oscillation",
            "One Hit KO"
        ]
    
    # Selects a random number between 1 (inclusive) and 5 (exclusive).
    @staticmethod
    def battlesphere_count_low() -> range:
        return range(1, 5)
    
    # Selects a random number between 5 (inclusive) and 11 (exclusive).
    @staticmethod
    def battlesphere_count_high() -> range:
        return range(5, 11)
    
# Archipelago Options
class CustomCharactersOption(OptionSet):
    """
    Any custom characters to include in the list of selectable characters for Freedom Planet 2 challenges (if any).
    """

    display_name = "Freedom Planet 2 Custom Characters"
    default = []
    
class CustomStagesOption(OptionSet):
    """
    Any custom stages to include in the list of selectable stages for Freedom Planet 2 challenges (if any).
    """

    display_name = "Freedom Planet 2 Custom Stages"
    default = []

