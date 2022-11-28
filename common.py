def player_input(type_of_input, max_range, pokemons_in_hand=1):
    message_pokemons = "\nCHOOSE NUMBER OF POKEMONS WHICH PLAYER SHOULD HAVE (1-6)\n"
    message_generation = "\nCHOOSE NUMBER OF GENERATION (1-6)\n"
    message_action = "\nDo one of 5 actions: \n 1 - normal attack \n 2 - special attack \n 3 - defense \n " \
                     "4 - replace pokemon \n 5 - end game \n"
    message_replace = f"\nCHOOSE NUMBER OF POKEMON FROM YOUR HAND: "
    message_special_attack = f"\nCHOOSE NUMBER OF TYPE OF YOUR ACTIVE POKEMON: "

    if type_of_input == "pokemons":
        message_input = message_pokemons
    elif type_of_input == "generation":
        message_input = message_generation
    elif type_of_input == "action":
        message_input = message_action
    elif type_of_input == "replace":
        message_input = message_replace
    else:
        message_input = message_special_attack

    while True:
        try:
            num = int(input(message_input))
        except ValueError:
            print(f"Please input integer value from 1 to {max_range}...")
            continue
        if 0 < num < max_range + 1:
            if num != 4 or pokemons_in_hand > 0:
                return num
            else:
                print("You have no pokemons on hand!")
        else:
            print("Value is out of range")
