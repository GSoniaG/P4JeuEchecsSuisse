"""
edit of all matches of a tournament
"""


import json
from .edit_tournament_view import ListTournament
from tinydb import TinyDB, Query
from pprint import pprint


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

        print(nb_tournaments, "tournoi(s) enregistré(s) dans la table TOURNAMENT")

        AccesGet = input(
            "\nVisualiser la  table TOURNOIS (taper O (=Oui) ou tout "
            "autre caratère pour sortir) ? : "
        )

        if AccesGet == "O":

            displayTournament = ListTournament()
            Id_tournament = displayTournament.run()

            while True:
                try:
                    Id_tournament = input("\n------- sélectionnez un N° tournoi : ")
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un N° tournoi ou "
                        "sortir [0]"
                    )

        Id_tournament = int(Id_tournament)

        db = TinyDB("db/matchs.json")
        match = db.table("matchs")
        Match = Query()
        get_match = match.search(Match.id_tournament == int(Id_tournament))
        pprint(get_match, indent=2)

        # print(get_match) : other manner to edit matches

        """ other manner to edit matches
        print()
        for i in range(nb_tournaments):
            print(i+1)
            pprint(get_match[i])
        """
