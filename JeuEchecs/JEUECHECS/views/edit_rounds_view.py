"""
Liste of all tours of tournament.
"""

import json

from .edit_tournament_view import ListTournament

# from pprint import pprint


class ListRounds:
    def __init__(self):
        pass

    def run(self):

        with open("db/tournament.json") as json_data:
            dict_tournaments = json.load(json_data)
            content_tournament = dict_tournaments["tournament"]
        nb_tournaments = len(content_tournament.keys())

        print("\n________________________ Table TOURNOI")
        print("-> ", nb_tournaments, "tournoi(s) enregistré(s) :")

        AccesGet = input(
            "\nVisualiser la  table TOURNOI (taper O (pour Oui) "
            "ou tout autre caratère pour sortir) ? "
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
                        "saisie non valide ! Veuillez choisir un N° tournament"
                        " ou sortir [0]"
                    )

            id_tournament = int(id_tournament)

            with open("db/tour.json") as json_data:
                dict_tour = json.load(json_data)
                content_tour = dict_tour["tour"]
            nb_tour = len(content_tour.keys())

            for i in range(nb_tour):
                if content_tour[str(i + 1)]["id_tournament"] == id_tournament:
                    print(
                        "name : ",
                        content_tour[str(i + 1)]["name"],
                        "start_date",
                        content_tour[str(i + 1)]["start_date"],
                    )

            """
            db = TinyDB("db/tour.json")
            tour = db.table("tour")
            Tour = Query()
            get_tour = tour.search(Tour.id_tournament == int(id_tournament))
            print()
            print("------- Liste de tous les tours d'un tournoi")
            pprint(get_tour, indent=4)
            """
