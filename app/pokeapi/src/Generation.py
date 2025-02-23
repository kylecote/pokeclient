
from typing import List
from .Util import ObjectReference

class Name:
    def __init__(self, 
                 language: ObjectReference, 
                 name: str):
        self.language = language
        self.name = name

class Generation:
    def __init__(self,
                 abilities: List[ObjectReference], 
                 id: int, 
                 main_region: ObjectReference, 
                 moves: List[ObjectReference], 
                 name: str, 
                 names: List[Name], 
                 pokemon_species: List[ObjectReference], 
                 types: List[ObjectReference], 
                 version_groups: List[ObjectReference]):
        self.abilities = abilities
        self.id = id
        self.main_region = main_region
        self.moves = moves
        self.name = name
        self.names = names
        self.pokemon_species = pokemon_species
        self.types = types
        self.version_groups = version_groups

    def __repr__(self):
        return f"Generation: name({self.name}) id({self.id}) main_region({self.main_region}) pokemon_species({self.pokemon_species}) types({self.types}) version_groups({self.version_groups})"

class GenerationListResultResponse:
    def __init__(self, count=0, next=..., previous=..., results=List[ObjectReference]):
        self.count = count
        self.results = results

    def __repr__(self):
         return f"GenerationListResultResponse: {self.count} {self.results}"
