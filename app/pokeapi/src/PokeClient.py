
import requests
from typing import Optional
from .Util import PageCursor
from .Pokemon import Pokemon, PokemonListResultResponse
from .Generation import Generation, GenerationListResultResponse

BASE_URI = f"https://pokeapi.co/api/v2"


class PokeClient:
    
    def __init__(self):
        pass

    #Added thoughts of re-use here in the README.md
    def get_pokemon_by_name_or_id(self, name: Optional[str] = None, id: Optional[int] = None) -> Pokemon:
        searchArg = name if name is not None else id if id is not None else ""
        if searchArg == "":
            raise ValueError("You must provide either a 'name' or an 'id'")
        response = requests.get(f"{BASE_URI}/pokemon/{searchArg}")
        if not response.ok:
            raise requests.exceptions.HTTPError(response.text)
        return Pokemon(**response.json())

    def get_pokemon(self, pageCursor: PageCursor) -> PokemonListResultResponse:
        response = requests.get(f"{BASE_URI}/pokemon/",params={"offset":pageCursor.offset, "limit":pageCursor.limit})
        if not response.ok:
            raise requests.exceptions.HTTPError(response.text)
        pageCursor.getNextPage(response.json()["next"] is not None)
        return PokemonListResultResponse(**response.json())
    
    def get_generation(self, pageCursor: PageCursor) -> GenerationListResultResponse:
        response = requests.get(f"{BASE_URI}/generation/",params={"offset":pageCursor.offset, "limit":pageCursor.limit})
        if not response.ok:
            raise requests.exceptions.HTTPError(response.text)
        pageCursor.getNextPage(response.json()["next"] is not None)
        return GenerationListResultResponse(**response.json())
    
    def get_generation_by_name_or_id(self, name: Optional[str] = None, id: Optional[int] = None) -> Generation:
        searchArg = name if name is not None else id if id is not None else ""
        if searchArg == "":
            raise ValueError("You must provide either a 'name' or an 'id'")
        response = requests.get(f"{BASE_URI}/generation/{searchArg}")
        if not response.ok:
            raise requests.exceptions.HTTPError(response.text)
        return Generation(**response.json())
