import random


class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defence, special_attack, special_defence, speed,
                 generation, legendary, burning=0):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._total = total
        self._hp = float(hp)
        self._attack = float(attack)
        self._defence = float(defence)
        self._special_attack = float(special_attack)
        self._special_defence = float(special_defence)
        self._speed = speed
        self._generation = generation
        self._legendary = legendary
        self._burning = burning
        self._type_effectivenss = [
                [1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
                [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
                [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
                [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
                [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
                [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
                [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
                [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
                [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
                [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
                [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
                [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
                [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
                [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
                [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
                [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]
            ]
        self._type_indices = {
                "Normal": 0,
                "Fighting": 1,
                "Flying": 2,
                "Poison": 3,
                "Ground": 4,
                "Rock": 5,
                "Bug": 6,
                "Ghost": 7,
                "Steel": 8,
                "Fire": 9,
                "Water": 10,
                "Grass": 11,
                "Electric": 12,
                "Psychic": 13,
                "Ice": 14,
                "Dragon": 15,
                "Dark": 16,
                "Fairy": 17
            }

    def damage(self, type_of_attack, enemy_pokemon, type_of_pokemon, weather):
        level = 10
        power = 50
        A = self._attack if type_of_attack == "normal" else self._special_attack
        D = enemy_pokemon.get_defence() if type_of_attack == "normal" else enemy_pokemon.get_special_defence()
        targets = 1
        badge = 1
        critical = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1.5, 2])
        random_val = random.randint(217, 255) / 255
        burn = 0.5 if self._burning else 1
        other = 1
        stab = 1
        type_val = self._type_effectivenss[self._type_indices[type_of_pokemon]][enemy_pokemon.get_type_indices()[enemy_pokemon.get_type1()]]
        damage = round((2+(((2*level)/5 + 2)*power*A/D)/50)*targets*weather*badge*critical*random_val*stab*type_val*burn*other, 2)
        print(f"===== {self._name} hit {damage} to {enemy_pokemon.get_name()} =====")
        return damage

    def increase_defense(self):
        self._defence = round(self._defence * 1.1, 2)
        print(f"===== {self._name} increased its defence to {self._defence} =====")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_type1(self):
        return self._type1

    def set_type1(self, type1):
        self._type1 = type1

    def get_type2(self):
        return self._type2

    def set_type2(self, type2):
        self._type2 = type2

    def get_total(self):
        return self._total

    def set_total(self, total):
        self._total = total

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def get_attack(self):
        return self._attack

    def set_attack(self, attack):
        self._attack = attack

    def get_defence(self):
        return self._attack

    def set_defence(self, defence):
        self._defence = defence

    def get_special_attack(self):
        return self._special_attack

    def set_special_attack(self,special_attack):
        self._special_attack = special_attack

    def get_special_defence(self):
        return self._special_defence

    def set_special_defence(self, special_defence):
        self._special_defence = special_defence

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_generation(self):
        return self._generation

    def set_generation(self, generation):
        self._generation = generation

    def get_legendary(self):
        return self._legendary

    def set_legendary(self, legendary):
        self._legendary = legendary

    def get_burning(self):
        return self._burning

    def set_burning(self, burning):
        self._burning = burning

    def get_type_effectivenss(self):
        return self._type_effectivenss

    def set_type_effectivenss(self, type_effectivenss):
        self._type_effectivenss = type_effectivenss

    def get_type_indices(self):
        return self._type_indices

    def set_type_indices(self, type_indices):
        self._type_indices = type_indices

    def __str__(self):
        type2_str = " " if self._type2 == "" else f" TYPE2: {self._type2}, "
        return f"pokemon {self._name} stats - TYPE1: {self._type1}," + type2_str + f"HP: {self._hp}, " \
               f"ATTACK: {self._attack}, DEFENCE: {self._defence}, SPECIAL ATTACK: {self._special_attack}, " \
               f"SPECIAL DEFENCE: {self._special_defence}"



