import random


# https://bulbapedia.bulbagarden.net/wiki/Weather

class Arena:
    def __init__(self, player1, player2, weather=None):
        self._weather = self.choose_weather() if weather is None else weather
        self._weather_ratio = self.return_weather_ratio()
        self._player1 = player1
        self._player2 = player2

    @staticmethod
    def choose_weather():
        list_of_weather = ["Clear", "Cloudy", "Rain", "Thunderstorm", "Snow", "Blizzard", "Harsh sunlight",
                           "Sandstorm", "Fog"]
        return random.choice(list_of_weather)

    @staticmethod
    def return_weather_ratio():
        return {
            "Clear": {"Grass": 2,
                      "Ground": 1.5,
                      "Fire": 2},
            "Cloudy": {"Fairy": 2,
                       "Fighting": 1.5,
                       "Poison": 2},
            "Rain": {"Water": 2,
                     "Electric": 3,
                     "Bug": 1.5},
            "Thunderstorm": {"Water": 2,
                             "Electric": 3},
            "Snow": {"Ice": 2},
            "Blizzard": {"Ice": 2,
                         "Steel": 1.5},
            "Harsh sunlight": {"Fire": 1.8,
                               "Ground": 1.5},
            "Sandstorm": {"Ground": 1.9,
                          "Rock": 1.6},
            "Fog": {"Psychic": 2,
                    "Ghost": 1.7}
        }

    def get_weather(self):
        return self._weather

    def set_weather(self, weather):
        self._weather = weather

    def get_weather_ratio(self):
        return self._weather_ratio

    def set_weather_ratio(self, weather_ratio):
        self._weather_ratio = weather_ratio

    def get_player1(self):
        return self._player1

    def set_player1(self, player):
        self._player1 = player

    def get_player2(self):
        return self._player2

    def set_player2(self, player):
        self._player2 = player
