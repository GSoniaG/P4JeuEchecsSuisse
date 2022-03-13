"""
List of all players in a tournament in alphabetical order
"""

import json
from global_vars import COUNTER_PLAYER
from .edit_tournament_view import ListTournament


class ListPlayersRankOrder:
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
        print(nb_tournaments, "-> tournoi(s) enregistré(s) dans la table TOURNOI")

        AccesGet = input(
            "\nVisualiser la  table TOURNOI (taper O (=Oui) ou tout "
            "autre caratère pour sortir) ? "
        )

        if AccesGet == "O":

            edit_tournament = ListTournament()
            edit_tournament.run()

            while True:
                try:
                    Id_tournament = input("\n------- sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournoi ou sortir "
                        "[0]"
                    )

            Id_tournament = int(Id_tournament)
            content_tournament_players = dict_tournaments["tournament"][
                str(Id_tournament)
            ]["players"]
            # {"tournament": {"1": {"name": "DNKJM", "place": "",
            # "start_date": "2022-03-10", "round_number": 4,
            # "players": ["8", "7", "6", "5", "4", "3", "2", "1"], "time_control": "",
            # "description": ""}}}

            print(
                "Id joueurs non triés sur leur classement mondial : ",
                content_tournament_players,
            )

            endplayersorted = []

            for i in range(COUNTER_PLAYER):
                print("i : ", i)
                print("\ndict_players : ", dict_players)
                print()
                print(content_tournament_players[i])
                print()
                print(dict_players["players"][content_tournament_players[i]])
                print()
                print(
                    dict_players["players"][content_tournament_players[i]][
                        "classement_mondial"
                    ]
                )
                # {"players": {"1": {"first_name": "HGKEQJ", "last_name": "NVDWKJ", "civility": "",
                # "birth": "", "classement_mondial": 1},
                rank = dict_players["players"][content_tournament_players[i]][
                    "classement_mondial"
                ]
                # table players : {"players": {"1": {"first_name": "HGKEQJ", "last_name":
                # "NVDWKJ", "civility": "", "birth": "", "classement_mondial": 1},
                # "2": .....

                playersorted = [
                    "nom : ",
                    dict_players["players"][content_tournament_players[i]]["last_name"],
                    " - prénom : ",
                    dict_players["players"][content_tournament_players[i]][
                        "first_name"
                    ],
                    "classement_mondial : ",
                    rank,
                ]

                endplayersorted.append(playersorted)
            endplayersorted.sort(key=lambda x: x[5])
            print("joueurs triés sur le classement mondial : ")
            for i in range(COUNTER_PLAYER):
                print(endplayersorted[i])
