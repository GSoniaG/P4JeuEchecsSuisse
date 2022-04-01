"""
update of unfinished rounds by tournament
"""

import json

from controllers.pairs_players_controller import PairsPlayers
from global_vars import NB_ROUNDS


class UpdateTournament:
    def __init__(self):
        pass

    def run(self):

        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())

        if nb_tournament == 1 and (
            dict_tournament["tournament"][str(1)]["number_rounds_created"] == 0
        ):
            print("\n -> il n'y a aucun tournoi à finaliser")
        else:
            for i in range(nb_tournament):
                if (
                    dict_tournament["tournament"][str(i + 1)]["number_rounds_created"]
                    != 0
                ) and (
                    dict_tournament["tournament"][str(i + 1)]["number_rounds_created"]
                    < NB_ROUNDS
                ):
                    print("\nN° Tournoi à finaliser : ", i + 1)
                    print(
                        "nom du tournoi : ",
                        dict_tournament["tournament"][str(i + 1)]["name"],
                    )
                    print(
                        "place du tournoi : ",
                        dict_tournament["tournament"][str(i + 1)]["place"],
                    )
                    print(
                        "date du tournoi : ",
                        dict_tournament["tournament"][str(i + 1)]["start_date"],
                    )
                    print(
                        "number_rounds_created : ",
                        dict_tournament["tournament"][str(i + 1)][
                            "number_rounds_created"
                        ],
                    )
                    print(
                        "Ids joueurs : ",
                        dict_tournament["tournament"][str(i + 1)]["players"],
                    )
                    print(
                        "score joueurs ['id joueur', score] : ",
                        dict_tournament["tournament"][str(i + 1)][
                            "list_idplayers_score"
                        ],
                    )

                    while True:
                        try:
                            Id_tournament = input("\n-> sélectionnez un N° tournoi : ")
                            break
                        except ValueError:
                            print(
                                "saisie non valide ! Veuillez choisir un N° tournoi ou sortir [0]"
                            )

                    list_idplayers_score = dict_tournament["tournament"][Id_tournament][
                        "list_idplayers_score"
                    ]
                    number_rounds_created = dict_tournament["tournament"][
                        Id_tournament
                    ]["number_rounds_created"]

                    print("number_rounds_created 74 : ", number_rounds_created)

                    # back to the update of the tournament matches to be finalized
                    start_date = dict_tournament["tournament"][str(i + 1)]["start_date"]
                    Id_players = dict_tournament["tournament"][str(i + 1)]["players"]

                    app = PairsPlayers(Id_tournament, start_date)
                    return_rounds_created = app.Resumption_Tournament_Interrupted(
                        Id_tournament,
                        list_idplayers_score,
                        number_rounds_created,
                        Id_players,
                    )
                    print("number_rounds_created 85 : ", number_rounds_created)
                    print("return_rounds_created 86 : ", return_rounds_created)

                    if return_rounds_created == NB_ROUNDS:
                        dict_tournament["tournament"][Id_tournament][
                            "list_idplayers_score"
                        ] = []
                        dict_tournament["tournament"][Id_tournament][
                            "number_rounds_created"
                        ] = 0
                        with open("db/tournament.json", "w") as file:
                            file.write(json.dumps(dict_tournament))
                tournament = 0

            if tournament == 0:
                print("\n -> il n'y a aucun tournoi à finaliser")
