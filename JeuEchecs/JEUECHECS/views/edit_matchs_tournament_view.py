"""
edit of all matches of a tournament
"""

import json

from .edit_tournament_view import ListTournament


class ListMatchs:
    def __init__(self):
        pass

    def run(self):

        print("\n\n_____________Liste de tous les matchs d'un tournoi")

        with open(r"db/tournament.json", "r") as f:
            json_data = f.read()
            json_data = json.loads(json_data)
            content_tournament = json_data["tournament"].keys()
            nb_tournaments = len(content_tournament)

        print("-> ", nb_tournaments, "tournoi(s) enregistré(s)")

        AccesGet = input(
            "\nVisualiser la  table TOURNOIS (taper O (=Oui) ou tout "
            "autre caratère pour sortir) ? : "
        )

        if AccesGet == "O":

            displayTournament = ListTournament()
            Id_tournament = displayTournament.run()

            while True:
                try:
                    Id_tournament = input("\n-> sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournoi ou "
                        "sortir [0]"
                    )

        Id_tournament = int(Id_tournament)

        with open("db/matchs.json") as json_data:
            dict_match = json.load(json_data)
            content_match = dict_match["matchs"]
        nb_match = len(content_match.keys())
        print("\n nb_match : ", nb_match, "\n")
        print("Id_tournament : ", Id_tournament)

        for i in range(nb_match):
            if dict_match["matchs"][str(i + 1)]["id_tournament"] == Id_tournament:
                print(
                    " - date  : ",
                    dict_match["matchs"][str(i + 1)]["date"],
                    " - id_joueur1_resultat  : ",
                    dict_match["matchs"][str(i + 1)]["id_joueur1_resultat"],
                    " - id_joueur2_resultat  : ",
                    dict_match["matchs"][str(i + 1)]["id_joueur2_resultat"],
                )
