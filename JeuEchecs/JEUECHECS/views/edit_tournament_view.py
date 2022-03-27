"""
list of all tournaments
"""

import json

# from pprint import pprint


class ListTournament:
    def __init__(self):
        pass

    def run(self):

        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())
        key = list(dict_tournament["tournament"].keys())

        print("\n-> Liste des tournois : \n")
        for i in range(nb_tournament):
            print(
                "    ",
                "no tournoi : ",
                key[i],
                " - name : ",
                dict_tournament["tournament"][str(i + 1)]["name"],
                " - place : ",
                dict_tournament["tournament"][str(i + 1)]["place"],
            )

        """
        with open(r"db/tournament.json", "r") as f:
            json_data = f.read()
            json_data = json.loads(json_data)
        print()
        print("------- Liste de tous les tournois :")
        pprint(json_data, indent=4)
        print()
        """
