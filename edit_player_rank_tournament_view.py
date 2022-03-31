"""
List of all players in a tournament in rank order
"""

import json

from global_vars import COUNTER_PLAYER

from .edit_tournament_view import ListTournament


class ListPlayersRankOrderTournament:
    def __init__(self):
        pass

    def run(self):

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            # content_players = dict_players["players"]

        with open("db/tournament.json") as json_data:
            dict_tournaments = json.load(json_data)
            content_tournament = dict_tournaments["tournament"]
        nb_tournaments = len(content_tournament.keys())

        print("\n--------------------------------Table TOURNAMENT")
        print("-> ", nb_tournaments, "tournoi(s) enregistré(s) : ")

        AccesGet = input(
            "\nVisualiser la  table TOURNOI (taper O (=Oui) ou tout "
            "autre caratère pour sortir) ? "
        )

        if AccesGet == "O":

            edit_tournament = ListTournament()
            edit_tournament.run()

            while True:
                try:
                    Id_tournament = input("\n-> sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournoi "
                        "ou sortir [0]"
                    )

            Id_tournament = int(Id_tournament)
            content_tournament_players = dict_tournaments["tournament"][
                str(Id_tournament)
            ]["players"]

            endplayersorted = []

            for i in range(COUNTER_PLAYER):

                rank = [
                    dict_players["players"][content_tournament_players[i]][
                        "classement_mondial"
                    ]
                ]

                playersorted = [
                    "nom : ",
                    dict_players["players"][content_tournament_players[i]]["last_name"],
                    " - prénom : ",
                    dict_players["players"][content_tournament_players[i]][
                        "first_name"
                    ],
                    " - classement mondial : ",
                    rank,
                ]

                endplayersorted.append(playersorted)

            endplayersorted.sort(key=lambda x: x[5])
            print("\n-> Joueurs triés sur le classement mondial :")

            for i in range(COUNTER_PLAYER):
                print(
                    endplayersorted[i][0],
                    endplayersorted[i][1],
                    endplayersorted[i][2],
                    endplayersorted[i][3],
                    endplayersorted[i][4],
                    endplayersorted[i][5],
                )
