"""
List of all players in a tournament in alphabetical order
"""

import json

from global_vars import COUNTER_PLAYER

from .edit_tournament_view import ListTournament


class ListPlayersAlphaOrderTournament:
    def __init__(self):
        pass

    def run(self):

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            content_players = dict_players["players"]

        with open("db/tournament.json") as json_data:
            dict_tournaments = json.load(json_data)
            content_tournament = dict_tournaments["tournament"]
        nb_tournaments = len(content_tournament.keys())

        print("\n----------------------Table TOURNAMENT")
        print("-> ", nb_tournaments, "tournoi(s) enregistré(s) : ")

        AccesGet = input(
            "\nVisualiser la  table TOURNOI (taper O (=Oui) "
            "ou tout autre caratère pour sortir) : "
        )

        if AccesGet == "O":

            edit_tournament = ListTournament()
            edit_tournament.run()

            while True:
                try:
                    id_tournament = input("\n-> sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournoi "
                        "ou sortir [0]"
                    )

            id_tournament = int(id_tournament)
            id_players = dict_tournaments["tournament"][str(id_tournament)]["players"]

            end_player_sorted = []

            for i in range(COUNTER_PLAYER):
                player_sorted = content_players[id_players[i]]["last_name"]
                end_player_sorted.append(player_sorted)
            end_player_sorted.sort(key=lambda x: x[0])
            print("\n------- Joueurs triés sur le nom : ")
            for i in range(COUNTER_PLAYER):
                print("    ", end_player_sorted[i])
