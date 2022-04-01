"""
start of the tournament with creation of 8 players
then creation of 4 rounds with creation of 4 matches per round
"""

import json
from datetime import date, datetime

from controllers.pairs_players_controller import PairsPlayers
from global_vars import NB_ROUNDS
from tinydb import TinyDB

from .entry_players_view import EntryPlayer


class ViewTournament:
    def __init__(self):
        pass

    def run(self):

        list_tours = []
        current_tour = []
        id_players = []

        name = input("\n-> nom du tournoi : ")
        place = input("-> lieu du tournoi : ")
        # automatic génération date et hour at the biginning of tournament
        start_date = date.today()
        # automatic current date
        start_date = start_date.isoformat()
        print("-> start_date : ", start_date)
        start_time = datetime.now()
        # automatic current hour
        time = start_time.time()
        # Give the time
        start_time = time
        start_time = time.isoformat()
        time_control = ""
        players = []
        round_number = 4
        print("-> nombre de tours du tournoi = 4")
        time_control = input("-> time_control (bullet-blitz-coup rapide) : ")
        description = input("-> remarques générales :")
        # 2 fields to be updated at the end of each interrupted tournament
        list_idplayers_score = []
        number_rounds_created = 0

        # -----------------------------------------------------
        current_tournament = {
            "name": name,
            "place": place,
            "start_date": start_date,
            "round_number": round_number,
            "players": players,
            # List indices of instances players
            "time_control": time_control,
            "description": description,
            "list_idplayers_score": list_idplayers_score,
            "number_rounds_created": number_rounds_created,
        }

        # --------create tournament in file tournament.json --
        db = TinyDB("db/tournament.json")
        # data base jeuechec (tables : player+match+round+tournament)
        table_tournament = db.table("tournament")  # table joueur
        table_tournament.insert(current_tournament)

        # -----get ID of the created tournament---------
        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())
        # last Id tournament created

        # ------create 4 tours (rounds) per tournament-----
        # with "date" and "time" empty which will be filled automatically
        # with each creation of the turn in the tournament
        for i in range(NB_ROUNDS):
            current_tour = {
                "id_tournament": nb_tournament,
                "name": str(i + 1),
                "start_date": "",
                "start_time": "",
                "end_date": "",
                "end_time": "",
            }
            list_tours.append(current_tour)

        db = TinyDB("db/tour.json")
        table_tour = db.table("tour")
        table_tour.insert_multiple(list_tours)

        list_players = EntryPlayer()
        id_players = list_players.run()
        # get the list of Id players of the current tournament

        # --- sort the players - creation of 4 pairs of 2 players---
        pairsplayers = PairsPlayers(nb_tournament, start_date)
        pairsplayers.run(id_players)
