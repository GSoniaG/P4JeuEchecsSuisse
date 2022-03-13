"""
Liste de tous les tours d'un tournoi.
"""

import json
from .edit_tournament_view import ListTournament
from pprint import pprint
from tinydb import TinyDB, Query


class ListRounds:
    def __init__(self):
        pass

    def run(self):

        with open("db/tournament.json") as json_data:
            dict_tournaments = json.load(json_data)
            content_tournament = dict_tournaments["tournament"]
        nb_tournaments = len(content_tournament.keys())

        with open("db/tour.json", "r") as file:
            json_data = file.read()
            json_data = json.loads(json_data)

        print("\n________________________ Table TOURNOI")
        print(nb_tournaments, "tournoi(s) enregistré(s) dans la table TOURNAMENT")

        AccesGet = input(
            "\nVisualiser la  table TOURNOI (taper O (pour Oui) "
            "ou tout autre caratère pour sortir) ? "
        )

        if AccesGet == "O":

            display_tournament = ListTournament()
            tournament = display_tournament.run()

            while True:
                try:
                    id_tournament = input("\n------- sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournament ou sortir [0]"
                    )

            id_tournament = int(id_tournament)

            db = TinyDB("db/tour.json")
            tour = db.table("tour")
            Tour = Query()
            get_tour = tour.search(Tour.id_tournament == int(id_tournament))
            # [{'id_tournament': 1, 'name': '1', 'start_date': '2022-03-10',
            # 'start_time': '15:54:06.185695', 'end_date': '2022-03-10',
            # 'end_time': '15:55:29.556154'},

            print()
            pprint(get_tour, indent=2)
