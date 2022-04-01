"""
update classement players by the manager
"""

import json


class UpdatePlayerRank:
    def __init__(self):
        pass

    def run(self):

        with open("db/players.json") as json_data:
            dict_players = json.load(json_data)
            content_players = dict_players["players"]
        nb_players = len(content_players.keys())
        key = list(dict_players["players"].keys())

        print(
            "\n-> Table PLAYER (classement mondial) à mettre à jour : ",
            nb_players,
            "joueurs enregistrés dans la table PLAYER",
        )
        print("Visualiser les joueurs et mettre à jour le classement " "mondial")
        AccesUpdate = input("taper O (=Oui) ou tout autre caratère pour sortir : ")

        while AccesUpdate == "O":
            """
            with open("db/players.json") as json_data:
                dict_players = json.load(json_data)
                content_players = dict_players["players"]
            nb_players = len(content_players.keys())
            """
            print()
            for i in range(nb_players):
                print(
                    "Id joueur : ",
                    key[i],
                    " - Nom :",
                    content_players[str(i + 1)]["last_name"],
                    " - Prénom :",
                    content_players[str(i + 1)]["first_name"],
                    " - Classement mondial =",
                    content_players[str(i + 1)]["classement_mondial"],
                )

            while True:
                try:
                    Id_player = input(
                        "\n-> Id_joueur (classement) à " "mettre à jour : "
                    )
                    break
                except ValueError:
                    print(
                        "saisie non valide ! Veuillez choisir un ID "
                        "joueur ou sortir [0]"
                    )
            Id_player = int(Id_player)

            actualclassement = dict_players["players"][str(Id_player)][
                "classement_mondial"
            ]

            print("-> classement actuel du joueur N°", Id_player, "=", actualclassement)
            Classement = input("-> classement de ce joueur à mettre à jour ? ")
            dict_players["players"][str(Id_player)]["classement_mondial"] = int(
                Classement
            )

            with open("db/players.json", "w") as file:
                file.write(json.dumps(dict_players))

            AccesUpdate = input(
                "\nVisu table PLAYER et màj classement mondial taper "
                "O (Oui) ou tout autre caratère pour sortir) : "
            )
