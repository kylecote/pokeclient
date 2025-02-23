
from typing import List
from .Util import ObjectReference

class Stat:
    def __init__(self, base_stat: int, effort: int, stat: ObjectReference):
        self.base_stat = base_stat
        self.effort = effort
        self.stat = stat

class Ability:
    def __init__(self, ability: ObjectReference, is_hidden: bool, slot: int):
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot

class GameIndex:
    def __init__(self, game_index: int, version: ObjectReference):
        self.game_index = game_index
        self.version = version

class VersionGroupDetail:
    def __init__(self, level_learned_at: int, move_learn_method: ObjectReference, version_group: ObjectReference):
        self.level_learned_at = level_learned_at
        self.move_learn_method = move_learn_method
        self.version_group = version_group

class Move:
    def __init__(self, move: ObjectReference, version_group_details: List[dict]):
        self.move = move
        self.version_group_details = version_group_details

class Types:
    def __init__(self, slot: int, type: ObjectReference):
        self.slot = slot
        self.type = type

class Pokemon:
    def __init__(self, 
                 abilities: List[Ability],
                 base_experience: int,
                 cries: dict,
                 forms: List[ObjectReference],
                 game_indices: List[dict],
                 height: int,
                 held_items: List[dict],
                 id: int,
                 is_default: bool,
                 location_area_encounters: str,
                 moves: List[dict],
                 name: str,
                 order: int,
                 past_abilities: List[dict],
                 past_types: List[dict],
                 species: ObjectReference,
                 sprites: dict,
                 stats: List[Stat],
                 types: List[dict],
                 weight: int):
                self.abilities = abilities
                self.base_experience = base_experience
                self.cries = cries
                self.forms = forms
                self.game_indices = game_indices
                self.height = height
                self.held_items = held_items
                self.id = id
                self.is_default = is_default
                self.location_area_encounters = location_area_encounters
                self.moves = moves
                self.name = name
                self.order = order
                self.species = species
                self.sprites = sprites
                self.stats = stats
                self.types = types
                self.weight = weight
    
    def __repr__(self):
        print(f"Pokemon: {self.name} {self.id}")

class PokemonListResultResponse:
    def __init__(self, count=0, next=..., previous=..., results=List[ObjectReference]):
        self.count = count
        self.results = results
    
    def __repr__(self):
         print(f"PokemonListResultResponse: {self.count} {self.results}")

