"""
start of the tournament with creation of 8 players 
then creation of 4 rounds with creation of 4 matches per round
"""


from models.tournament_models import Tournament
from controllers.pairs_players_controller import PairsPlayers
from .entry_players_view import EntryPlayer
from global_vars import NB_ROUNDS
from datetime import date
from datetime import datetime
import datetime
from tinydb import TinyDB
import json


# db = TinyDB('db/tournament.json')
# table_tournament = db.table('tournament') # table Tournament


class ViewTournament:
    """creation of tournament"""

    def __init__(self):
        pass

    def run(self):

        list_tours = []
        current_tour = []
        id_players = []

        name = input("-> nom du tournoi : ")
        place = input("-> lieu du tournoi : ")
        # automatic génération date et hour at the biginning of tournament
        start_date = date.today()  # automatic current date
        start_date = start_date.isoformat()
        print("-> start_date : ", start_date)
        start_time = datetime.datetime.now()  # # automatic current hour
        time = start_time.time()  # Give the time
        start_time = time
        start_time = time.isoformat()
        end_date = ""  # data of tour.json
        end_time = ""  # data of tour.json
        time_control = ""
        players = []
        round_number = 4
        print("-> nombre de tours du tournoi = 4")
        time_control = input("-> time_control (bullet ou blitz ou coup rapide) : ")
        description = input("-> remarques générales (directeur du tournoi) :")

        # --------------------------------------------------------------------------
        current_tournament = {
            "name": name,
            "place": place,
            "start_date": start_date,
            "round_number": round_number,
            # "round" = "tour" : list instances rounds or tours
            "players": players,  # List indices of instances players
            "time_control": time_control,
            # time_control = contôle du temps (bullet,blitz ou coup rapide)
            "description": description,
        }
        # -----------------create tournament in file tournament.json -------------
        db = TinyDB("db/tournament.json")
        # data base jeuechec (tables : player+match+round+tournament)
        table_tournament = db.table("tournament")  # table joueur
        table_tournament.insert(current_tournament)

        # ----------------get ID of the created tournament------------------------
        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())  # last Id tournament created

        # ----------------create 4 tours (rounds) per tournament-------------------
        for i in range(NB_ROUNDS):
            current_tour = {
                "id_tournament": nb_tournament,
                "name": str(i + 1),
                "start_date": start_date,
                "start_time": start_time,
                "end_date": end_date,
                "end_time": end_time,
            }
            list_tours.append(current_tour)

        db = TinyDB("db/tour.json")
        table_tour = db.table("tour")  # table Tour
        table_tour.insert_multiple(list_tours)
        # list_tours = [{'id_tournament': 1, 'name': '1', 'start_date': '2022-03-10',
        # 'start_time': '14:57:52.536805', 'end_date': '', 'end_time': ''},
        # {'id_tournament': 1, 'name': '2', ....

        # ---------------enter 8 players arriving of tournament--------------------
        # transformer en modèle player - itérer pour créer un objet player
        # player = Player() # créer un objet

        list_players = EntryPlayer()  # call Views.entryplayersview
        id_players = list_players.run()
        # get the list of Id players of the current tournament

        # ----------------sort the players - creation of 4 pairs of 2 players--------
        pairsplayers = PairsPlayers(nb_tournament, start_date)
        # pairsplayerscontroller.py
        pairsplayers.run(id_players)
