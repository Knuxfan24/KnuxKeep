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
class Sonic06ArchipelagoOptions:
    s06_dlc_owned: Sonic06DLCOwned

class Sonic06Game(Game):
    # Set the game name.
    name = "SONIC THE HEDGEHOG (2006)"

    # Set the platforms for this game.
    platform = KeymastersKeepGamePlatforms.X360
    platforms_other = [ KeymastersKeepGamePlatforms.PS3 ]

    # Set whether or not this game falls under AP-AfterDark.
    is_adult_only_or_unrated = False

    # Set this game's options.
    options_cls = Sonic06ArchipelagoOptions

    # Create this game's optional objectives.
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate
            (
                label="Obtain an S-Rank.",
                data=dict(),
            ),
            GameObjectiveTemplate
            (
                label="No Deaths.",
                data=dict(),
            )
        ]

    # Create this game's objectives that don't require any options to be set.
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = [
            GameObjectiveTemplate
            (
                label="Clear STAGE as CHARACTER.",
                data={
                    "STAGE": (self.stages, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate
            (
                label="Defeat BOSS.",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate
            (
                label="Clear End of the World.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate
            (
                label="Clear Sonic's Wave Ocean without trapping the whale.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate
            (
                label="Clear Sonic's Flame Core without using Knuckles.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate
            (
                label="Clear Sonic's Flame Core as Knuckles.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate
            (
                label="Hit the weak point on the underside of the Egg Genesis as Sonic.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate
            (
                label="Clear Sonic's Kingdom Valley without using Silver.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate
            (
                label="Reach the second section of Sonic's Aquatic Base as Tails.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=4,
            ),
            GameObjectiveTemplate
            (
                label="Clear Shadow's Flame Core without using Rouge.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate
            (
                label="Clear Shadow's Flame Core as Rouge.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate
            (
                label="Skip the Ball Puzzle in Silver's Dusty Desert.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate
            (
                label="Hit the weak point on the head of the Egg Genesis as Silver.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate
            (
                label="Clear Silver's Kingdom Valley as Sonic.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate
            (
                label="Trigger the \"Control in Results Screen\" glitch.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            )
        ]
    
        # If Sonic's Very Hard mode is enabled, then add an objective for it.
        if "Very Hard Mode (Sonic)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear STAGE as Sonic in Very Hard Mode.",
                data={
                    "STAGE": (self.stages, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            )
        ])
    
        # If Shadow's Very Hard mode is enabled, then add an objective for it.
        if "Very Hard Mode (Shadow)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear STAGE as Shadow in Very Hard Mode.",
                data={
                    "STAGE": (self.stages_shadowVH, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            )
        ])
    
        # If Silver's Very Hard mode is enabled, then add an objective for it.
        if "Very Hard Mode (Silver)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear STAGE as Silver in Very Hard Mode.",
                data={
                    "STAGE": (self.stages_silverVH, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            )
        ])
    
        # If Sonic's Boss Attack mode is enabled, then add an objective for it.
        if "Boss Attack Mode (Sonic)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear Boss Attack as Sonic.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            )
        ])
    
        # If Shadow's Boss Attack mode is enabled, then add an objective for it.
        if "Boss Attack Mode (Shadow)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear Boss Attack as Shadow.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            )
        ])
    
        # If Silver's Boss Attack mode is enabled, then add an objective for it.
        if "Boss Attack Mode (Silver)" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear Boss Attack as Silver.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            )
        ])
    
        # If Team Attack Amigo is enabled, then add an objective for it.
        if "Team Attack Amigo" in self.dlc_owned:
            objectives.extend([
                GameObjectiveTemplate(
                label="Clear Team Attack Amigo.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=5,
            )
        ])

        # Return our list of objectives.
        return objectives
    
    # Define the list of stages.
    # TODO: The Shadow and Silver Very Hard ones can probably be made cleaner? Assuming Python can remove a specific entry from a list.
    @staticmethod
    def stages() -> List[str]:
        return [
            "Wave Ocean",
            "Dusty Desert",
            "White Acropolis",
            "Crisis City",
            "Flame Core",
            "Radical Train",
            "Tropical Jungle",
            "Kingdom Valley",
            "Aquatic Base",
        ]
    @staticmethod
    def stages_shadowVH() -> List[str]:
        return [
            "Wave Ocean",
            "Dusty Desert",
            "White Acropolis",
            "Crisis City",
            "Flame Core",
            "Radical Train",
            "Kingdom Valley",
            "Aquatic Base",
        ]
    @staticmethod
    def stages_silverVH() -> List[str]:
        return [
            "Dusty Desert",
            "White Acropolis",
            "Crisis City",
            "Flame Core",
            "Radical Train",
            "Tropical Jungle",
            "Kingdom Valley",
            "Aquatic Base",
        ]

    # Define the list of characters.
    @staticmethod
    def characters() -> List[str]:
        return [
            "Sonic",
            "Shadow",
            "Silver"
        ]

    # Define the list of bosses.
    @staticmethod
    def bosses() -> List[str]:
        return [
            "the Egg Cerebus as Sonic",
            "Silver The Hedgehog as Sonic",
            "Iblis Phase 2 as Sonic",
            "the Egg Genesis as Sonic",
            "the Egg Wyvern",
            "the Egg Cerebus as Shadow",
            "Iblis Phase 2 as Shadow",
            "Mephiles Phase 1",
            "Silver The Hedgehog as Shadow",
            "Mephiles Phase 2",
            "Iblis Phase 1",
            "Sonic The Hedgehog",
            "the Egg Genesis as Silver",
            "Shadow The Hedgehog",
            "Iblis Phase 3",
            "Solaris"
        ]
    
    # Get the values from the DLC owned option.
    @property
    def dlc_owned(self) -> Set[str]:
        return self.archipelago_options.s06_dlc_owned.value
    
# Archipelago Options
class Sonic06DLCOwned(OptionSet):
    """
    Indicates which SONIC THE HEDGEHOG (2006) DLC the player owns, if any.
    """

    display_name = "SONIC THE HEDGEHOG (2006) DLC Owned"
    valid_keys = [
        "Very Hard Mode (Sonic)",
        "Very Hard Mode (Shadow)",
        "Very Hard Mode (Silver)",
        "Boss Attack Mode (Sonic)",
        "Boss Attack Mode (Shadow)",
        "Boss Attack Mode (Silver)",
        "Team Attack Amigo",
    ]

    default = valid_keys