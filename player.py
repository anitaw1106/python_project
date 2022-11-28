class Player:
    def __init__(self, name, list_of_pokemons, active_pokemon, pokemons_in_hand, dead_pokemons):
        self._name = name
        self._list_of_pokemons = list_of_pokemons
        self._active_pokemon = active_pokemon
        self._pokemons_in_hand = pokemons_in_hand
        self._dead_pokemons = dead_pokemons

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_active_pokemon(self):
        return self._active_pokemon

    def set_active_pokemon(self, pokemon):
        self._active_pokemon = pokemon

    def get_pokemons_in_hand(self):
        return self._pokemons_in_hand

    def set_pokemons_in_hand(self, pokemons):
        self._pokemons_in_hand = pokemons

    def get_dead_pokemons(self):
        return self._dead_pokemons

    def set_dead_pokemons(self, pokemons):
        self._dead_pokemons = pokemons

    def __str__(self):
        info = f"{self._name} has {len(self._list_of_pokemons)} pokemons:"
        for pokemon in self._list_of_pokemons:
            info += f" {pokemon.get_name()},"
        return info[:-1]
