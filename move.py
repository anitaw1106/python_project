from common import player_input


# https://bulbapedia.bulbagarden.net/wiki/Damage
# https://bulbapedia.bulbagarden.net/wiki/Type
class Move:
    def __init__(self, player1, player2, type_of_move):
        self._player1 = player1
        self._player2 = player2
        self._type_of_move = type_of_move

    def attack(self, type_of_pokemon, weather_ratio):
        self._player2.get_active_pokemon().set_hp(
            round(self._player2.get_active_pokemon().get_hp() - self._player1.get_active_pokemon().damage(
                self._type_of_move,
                self._player2.get_active_pokemon(),
                type_of_pokemon,
                weather_ratio), 2)
        )
        if self._player2.get_active_pokemon().get_hp() <= 0:
            print(f"===== {self._player2.get_active_pokemon().get_name()} is dead =====")
            self._player2.get_dead_pokemons().append(self._player2.get_active_pokemon())
            if len(self._player2.get_pokemons_in_hand()) > 0:
                self._player2.set_active_pokemon(self._player2.get_pokemons_in_hand().pop(0))
            else:
                self._player2.set_active_pokemon(None)

    def defense(self):
        self._player1.get_active_pokemon().increase_defense()

    def replace(self):
        print("====== YOUR HAND ======")
        for i, pokemon in enumerate(self._player1.get_pokemons_in_hand()):
            print(f"#{i + 1} - {pokemon}")
        max_range = len(self._player1.get_pokemons_in_hand())
        num = player_input("replace", max_range)
        self._player1.get_pokemons_in_hand().append(self._player1.get_active_pokemon())
        self._player1.set_active_pokemon(self._player1.get_pokemons_in_hand().pop(num - 1))

    def get_player1(self):
        return self._player1

    def set_player1(self, player1):
        self._player1 = player1

    def get_player2(self):
        return self._player2

    def set_player2(self, player2):
        self._player2 = player2

    def get_type_of_move(self):
        return self._type_of_move

    def set_type_of_move(self, type_of_move):
        self._type_of_move = type_of_move
