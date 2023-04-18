from typing import List
from Exercise.ex_3_Football_Team_Generator.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str or Player:
        try:
            match = [p for p in self.__players if player_name == p.name][0]
            self.__players.remove(match)
            return match
        except IndexError:
            return f"Player {player_name} not found"
