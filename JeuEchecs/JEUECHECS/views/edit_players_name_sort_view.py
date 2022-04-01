"""
List of all players in alphabetical order
"""

import json


class ListPlayersAlphaOrder:
    def __init__(self):
        pass

    def run(self):

        end_player_sorted = []

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            content_players = dict_players["players"]
        nb_players = len(content_players.keys())

        print()
        for i in range(nb_players):
            player_sorted = content_players[str(i + 1)]["last_name"]
            end_player_sorted.append(player_sorted)
        end_player_sorted.sort(key=lambda x: x[1])
        print("\n-> Joueurs triés sur le nom : \n")
        for i in range(nb_players):
            print("    ", "last_name : ", end_player_sorted[i])
