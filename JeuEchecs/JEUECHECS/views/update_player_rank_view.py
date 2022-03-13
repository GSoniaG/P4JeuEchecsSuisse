"""
update classement players by the manager
"""


import json
from pprint import pprint


class UpdatePlayerRank:
    def __init__(self):
        pass

    def run(self):

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            content_players = dict_players["players"]
        nb_players = len(content_players.keys())

        with open(r"db/players.json", "r") as f:
            json_data = f.read()
            json_data = json.loads(json_data)

        print(
            "\n-----------Table PLAYER (classement mondial) à mettre à jour---------------"
        )
        print(nb_players, "joueurs enregistrés dans la table PLAYER")
        print("\nVisualiser les joueurs et mettre à jour le classement mondial")
        AccesUpdate = input(f"taper O (=Oui) ou tout autre caratère pour sortir) : ")

        while AccesUpdate == "O":

            with open(r"db/players.json", "r") as f:
                json_data = f.read()
                json_data = json.loads(json_data)
            pprint(json_data, indent=0)

            while True:
                try:
                    Id_player = input(
                        "\n-------- Id_joueur (classement) à mettre à jour : "
                    )
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un ID joueur ou sortir [0]"
                    )
            Id_player = int(Id_player)

            actualclassement = dict_players["players"][str(Id_player)][
                "classement_mondial"
            ]
            print(f"-> classement actuel du joueur {Id_player} : {actualclassement}")
            Classement = input("-------- classement de ce joueur à mettre à jour ? ")
            dict_players["players"][str(Id_player)]["classement_mondial"] = int(
                Classement
            )

            with open("db/players.json", "w") as file:
                file.write(json.dumps(dict_players))

            AccesUpdate = input(
                f"\nVisu table PLAYER et màj classement mondial taper O (Oui) ou tout "
                "autre caratère pour sortir) : "
            )
