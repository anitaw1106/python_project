from copy import copy

from arena import Arena
from pokemonIO import PokemonIO
from player import Player
from move import Move
from common import player_input


def is_loser(attacker, defender):
    is_loser_flag = False
    if defender.get_active_pokemon() is None:
        is_loser_flag = True
        print(f"\n######################### {attacker.get_name()} WON THE GAME!!! #########################")
    return is_loser_flag


def choose_pokemons(pokemons_list, number_of_pokemons, player_name):
    for i, pokemon in enumerate(pokemons_list):
        print(f"#{i} - {pokemon[1]}")

    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

    chosen_pokemons = []
    len_of_list = len(pokemons_list)
    print(f"\n{player_name}, CHOOSE {number_of_pokemons} NUMBERS OF POKEMONS FROM ABOVE LIST")
    while len(chosen_pokemons) < number_of_pokemons:
        try:
            num = int(input(f"Chose your {ordinal(len(chosen_pokemons) + 1)} pokemon number: "))
        except ValueError:
            print(f"Please input integer value from 1 to {len_of_list}")
            continue
        if 0 < num < len_of_list:
            if num not in chosen_pokemons:
                chosen_pokemons.append(copy(pokemons_list[num - 1][1]))
            else:
                print("You have already chosen this pokemon")
        else:
            print("Value is out of range")

    return chosen_pokemons


def set_a_game():
    all_pokemons = PokemonIO("data/pokemon.csv").get_pokemon_dict()

    number_of_pokemons = player_input("pokemons", 6)
    generation_of_pokemons = player_input("generation", 6)
    # filter pokemons base on given generation
    given_generation_pokemons = {k: v for k, v in all_pokemons.items() if
                                 int(v.get_generation()) == generation_of_pokemons}
    given_generation_pokemons_list = list(given_generation_pokemons.items())
    player1_name = input("Type name of first player: ")
    player2_name = input("Type name of second player: ")

    player1_pokemons = choose_pokemons(given_generation_pokemons_list, number_of_pokemons, player1_name)
    player2_pokemons = choose_pokemons(given_generation_pokemons_list, number_of_pokemons, player2_name)

    player1 = Player(player1_name, player1_pokemons, player1_pokemons[0], player1_pokemons[1:], [])
    player2 = Player(player2_name, player2_pokemons, player2_pokemons[0], player2_pokemons[1:], [])

    arena = Arena(player1, player2, weather="Clear")

    print(f"\nIT'S {arena.get_weather().upper()} ON ARENA\n")
    print(f"PLAYER 1: {player1}")
    print(f"PLAYER 2: {player2}")

    return player1, player2, arena


def gameplay(player1, player2, arena):
    turn = 0
    end_flag = False
    while not end_flag:
        attacker = player1 if turn % 2 == 0 else player2
        defender = player1 if turn % 2 == 1 else player2
        print("\n===== POKEMONS STATS =====")
        print(f"{attacker.get_name()}: {attacker.get_active_pokemon()}")
        print(f"{defender.get_name()}: {defender.get_active_pokemon()}")
        print(f"\n============= PLAYER{turn % 2 + 1} TURN!!! =============")
        action = player_input("action", 5, len(attacker.get_pokemons_in_hand()))
        if action == 1:
            move = Move(attacker, defender, "normal")
            if attacker.get_active_pokemon().get_type1() in arena.get_weather_ratio()[arena.get_weather()]:
                move.attack(attacker.get_active_pokemon().get_type1(),
                            arena.get_weather_ratio()[arena.get_weather()][attacker.get_active_pokemon().get_type1()])
            else:
                move.attack(attacker.get_active_pokemon().get_type1(), 1)
            end_flag = is_loser(attacker, defender)

        elif action == 2:
            move = Move(attacker, defender, "special")
            if attacker.get_active_pokemon().get_type2() != "":
                print(f"CHOOSE TYPE OF POKEMON: \n 1 - {attacker.get_active_pokemon().get_type1()} \n "
                      f"2 - {attacker.get_active_pokemon().get_type2()}")
                type_of_pokemon = player_input("special_attack", 2)
                if type_of_pokemon == 1:
                    if attacker.get_active_pokemon().get_type1() in arena.get_weather_ratio()[arena.get_weather()]:
                        move.attack(attacker.get_active_pokemon().get_type1(),
                                    arena.get_weather_ratio()[arena.get_weather()][
                                        attacker.get_active_pokemon().get_type1()])
                    else:
                        move.attack(attacker.get_active_pokemon().get_type1(), 1)
                elif type_of_pokemon == 2:
                    if attacker.get_active_pokemon().get_type2() in arena.get_weather_ratio()[arena.get_weather()]:
                        move.attack(attacker.get_active_pokemon().get_type2(),
                                    arena.get_weather_ratio()[arena.get_weather()][
                                        attacker.get_active_pokemon().get_type2()])
                    else:
                        move.attack(attacker.get_active_pokemon().get_type2(), 1)
            else:
                if attacker.get_active_pokemon().get_type1() in arena.get_weather_ratio()[arena.get_weather()]:
                    move.attack(attacker.get_active_pokemon().get_type1(),
                                arena.get_weather_ratio()[arena.get_weather()][
                                    attacker.get_active_pokemon().get_type1()])
                else:
                    move.attack(attacker.get_active_pokemon().get_type1(), 1)
            end_flag = is_loser(attacker, defender)
        elif action == 3:
            move = Move(attacker, defender, "defence")
            move.defense()
        elif action == 4:
            move = Move(attacker, defender, "replace")
            move.replace()
        elif action == 5:
            end_flag = True

        turn += 1


if __name__ == "__main__":
    print("---------------WELCOME TO THE POKEMON FIGHTS---------------------")
    player1, player2, arena = set_a_game()
    gameplay(player1, player2, arena)


