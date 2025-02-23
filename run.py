from pokeapi import PokeClient, PageCursor

pokeClient = PokeClient()
try:
    getbyIdExcept = pokeClient.get_pokemon_by_name_or_id()
except ValueError as e:
    print(e)

getById1 = pokeClient.get_pokemon_by_name_or_id(id=1)
print(getById1)

getByName = pokeClient.get_pokemon_by_name_or_id(name="charmander")
print(getByName)

pageCursor = PageCursor()
while pageCursor:
    print(pageCursor.hasNext)
    result = pokeClient.get_pokemon(pageCursor)
    print(result)