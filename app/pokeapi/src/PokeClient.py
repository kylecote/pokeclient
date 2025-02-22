
import requests
import json
from src.Pokemon import Pokemon
from src.Generation import Generation

API_VERSION = 2
BASE_URI = f"https://pokeapi.co/api/v{API_VERSION}"

def get_pokemon(self, name=..., id=...):
    if name == ... and id == ...:
        raise ValueError("You must provide either a 'name' or an 'id'")
    
    searchArg = name if name != ... else id
    response = requests.get(f"{self.BASE_URI}/pokemon/{searchArg}")
    return json.loads(response.text)
    
    
def get_generation(self, name=..., id=...):
    if name == ... and id == ...:
        raise ValueError("You must provide either a 'name' or an 'id'")
    
    searchArg = name if name != ... else id
    response = requests.get(f"{self.BASE_URI}/generation/{searchArg}")
    return json.loads(response.text)