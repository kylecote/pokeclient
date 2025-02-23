from pokeapi import PokeClient, PageCursor


pokeClient = PokeClient()

#Test some base validation for the get_pokemon_by_name_or_id method
try:
    getbyIdExcept = pokeClient.get_pokemon_by_name_or_id()
except ValueError as e:
    print(f"Expected excpetion => {e}")

getById1 = pokeClient.get_pokemon_by_name_or_id(id=1)
print(getById1)

getByName = pokeClient.get_pokemon_by_name_or_id(name="charmander")
print(getByName)

pageCursor = PageCursor()
while pageCursor.hasNext == True:
    result = pokeClient.get_pokemon(pageCursor)
    print(f"Caught {len(result.results)} more pokemon")

try:
    getbyIdExcept = pokeClient.get_pokemon_by_name_or_id()
except ValueError as e:
    print(f"Expected excpetion => {e}")

getByGenId1 = pokeClient.get_generation_by_name_or_id(id=1)
print(getByGenId1)

getByGenName = pokeClient.get_generation_by_name_or_id(name="generation-ii")
print(getByGenName)

pageCursor = PageCursor(limit=5)
while pageCursor.hasNext == True:
    result = pokeClient.get_generation(pageCursor)
    print(f"Generation {len(result.results)} observed")

print("Gotta catch em all!")