from pokeapi import PokeClient, PageCursor

pokeClient = PokeClient()
get_pokemon_by_name_or_id = pokeClient.get_pokemon_by_name_or_id()
get_pokemon = pokeClient.get_pokemon()

getByIdResult = get_pokemon_by_name_or_id(id=1)

getByNameResult = get_pokemon_by_name_or_id(name="bulbasaur")
pageCursor = PageCursor()
while pageCursor:
    print(pageCursor.hasNext)
    result = get_pokemon(pageCursor)
    for pokemon in result.results:
        print(f"Pokemon: {pokemon.name}")
    if not pageCursor.getNextPage():
        break