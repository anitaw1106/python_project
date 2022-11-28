import csv
from pokemon import Pokemon


class PokemonIO:
    def __init__(self, file_path):
        self._pokemon_dict = self.load_pokemon_file(file_path)

    @staticmethod
    def load_pokemon_file(file_path):
        with open(file_path, mode='r') as infile:
            reader = csv.reader(infile)
            next(reader, None)
            pokemon_dict = {}
            for row in reader:
                pokemon = Pokemon(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                  row[11], row[12])
                pokemon_dict[row[1]] = pokemon

        return pokemon_dict

    def get_pokemon_dict(self):
        return self._pokemon_dict

    def set_pokemon_dict(self, pokemon_dict):
        self._pokemon_dict=pokemon_dict
