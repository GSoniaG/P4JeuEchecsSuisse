"""
List of all players in rank order
"""

import json


class ListPlayersRankOrder:
    def __init__(self):
        pass

    def run(self):

        end_player_sorted = []

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            content_players = dict_players["players"]
        nb_players = len(content_players.keys())

        for i in range(nb_players):
            rank = [dict_players["players"][str(i + 1)]["classement_mondial"]]
            playersorted = [
                "nom : ",
                dict_players["players"][str(i + 1)]["last_name"],
                " - prénom : ",
                dict_players["players"][str(i + 1)]["first_name"],
                " - classement mondial : ",
                rank,
            ]
            end_player_sorted.append(playersorted)
            end_player_sorted.sort(key=lambda x: x[5])

        print("\n-> Joueurs triés sur le classement mondial :\n")

        for i in range(nb_players):
            print(
                end_player_sorted[i][0],
                end_player_sorted[i][1],
                end_player_sorted[i][2],
                end_player_sorted[i][3],
                end_player_sorted[i][4],
                end_player_sorted[i][5][0],
            )
