"""
enter 8 players and save them
"""


from global_vars import COUNTER_PLAYER
from tinydb import TinyDB
import json


class EntryPlayer:

    """enter 8 players and save"""

    def __init__(self):
        pass

    def run(self):

        """enter 8 players"""
        list_players = []
        current_player = []

        # ------------------------------input of 8 players-----------------------
        for nb_player in range(COUNTER_PLAYER):
            print("\n-------joueur ", nb_player + 1, " : ")
            first_name = input("prénom nom du joueur: ")
            last_name = input("nom du joueur: ")
            civility = input("genre du joueur Mr/Mme: ")
            birth = input("date de naissance du joueur (JJMMAAAA): ")
            classement = input("classement mondial du joueur (un nombre entier): ")
            classement = int(classement)

            # sérializer = convert 1 player instance to dictionary before registration
            current_player = {
                "first_name": first_name,
                "last_name": last_name,
                "civility": civility,
                "birth": birth,
                # "rank" : rank,
                "classement_mondial": classement,
                # "rank" : rank
            }
            list_players.append(current_player)
            # transform players into player objects, structure the data entered by the user
            # and save them in a data base
        # --------------------------save 8 players in file players.json------------------
        db = TinyDB("db/players.json")
        # data base jeuechec (tables : player+match+round+tournament)
        table_players = db.table("players")  # table joueur
        table_players.insert_multiple(list_players)

        # -----------reopen table players to get last of 8 Ids players added-------------
        # --------------to update playersfield in tournament table-----------------------
        db = TinyDB("db/players.json")
        table_players = db.table("players")
        with open("db/players.json") as json_data:
            players_dict = json.load(json_data)
            content_players = players_dict["players"].keys()
        nb_players = len(content_players)  # number Id created
        id_players_current_tournament = []
        for i in range(COUNTER_PLAYER):
            for item in players_dict:
                all_keys = list(players_dict[item].keys())
                current_key = all_keys[nb_players - i - 1]
                id_players_current_tournament.append(current_key)

        db = TinyDB("db/tournament.json")
        table_players = db.table("tournament")
        with open("db/tournament.json") as json_data:
            tournament_dict = json.load(json_data)
            content_tournament = tournament_dict["tournament"].keys()
        nb_tournaments = len(content_tournament)  # number Id created
        current_key = all_keys[nb_tournaments]

        tournament_dict["tournament"][str(nb_tournaments)][
            "players"
        ] = id_players_current_tournament

        with open("db/tournament.json", "w") as file:
            json.dump(tournament_dict, file)

        return id_players_current_tournament
        # returns the IDs of the 8 players in the current tournament
