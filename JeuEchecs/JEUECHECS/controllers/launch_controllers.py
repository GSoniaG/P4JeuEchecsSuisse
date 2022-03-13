"""
main launches MenuManager which will run TournamentManager :
    initialization of players, tournaments
run method for each controller
"""

from global_vars import NB_ROUNDS
from views.entry_tournament_view import ViewTournament
from .menu_reports_controllers import HomeMenuReports
from views.update_player_rank_view import UpdatePlayerRank
from views.edit_players_name_sort_view import ListPlayersAlphaOrder
from views.edit_player_rank_view import ListPlayersRankOrder
from views.edit_tournament_view import ListTournament
from views.edit_rounds_view import ListRounds
from views.edit_matchs_view import ListMatchs
from tinydb import TinyDB
import json
from datetime import date
from datetime import datetime
import datetime


class LaunchChoice:
    def __init__(self):
        pass

    def run(self, user_choice):

        if user_choice == 1:
            # create a tournament
            # enter the 8 players and follow the course of the matches and rounds
            # enter the tournament data
            current_tournament = ViewTournament()  # Views.entrytournamentview.py
            current_tournament.run()

            self.update_tour_enddatetime()
            # at the end of tournament = update table tour : end_date end_time

        if user_choice == 2:
            """mettre à jour le classement mondial des joueurs hors tournoi"""
            # updateplayerrankview
            update_classement = UpdatePlayerRank()
            # launch update classement after each round
            update_classement.run()

        if user_choice == 3:
            """acces to the reports"""

            while True:
                report_menu = HomeMenuReports()  # report menu menureportscontrollers.py
                user_choice_report = report_menu.run()
                # run method for each controller

                # List of all players in a tournament in alphabetical order
                if user_choice_report == 1:
                    list_players = ListPlayersAlphaOrder()  # editplayersnamesortview
                    list_players.run()

                # List of all players in a tournament by world ranking
                if user_choice_report == 2:
                    list_players = ListPlayersRankOrder()  # editplayerrankview
                    list_players.run()

                # List of all tournaments
                if user_choice_report == 3:
                    list_tournament = ListTournament()  # edittournamentview
                    list_tournament.run()

                # List of all rounds in a tournament.
                if user_choice_report == 4:
                    list_rounds = ListRounds()  # editroundsview
                    list_rounds.run()

                # List of all matches in a tournament.
                if user_choice_report == 5:
                    list_matchs = ListMatchs()  # editmatchsview
                    list_matchs.run()

                if user_choice_report == 0:
                    break

        if user_choice == 0:
            """0 - quitter"""
            return

    def update_tour_enddatetime(self):
        # update table tour.json : fields "end_date" "end_time"

        no_tours = 0

        # get last Id tournament created to update table tour.json
        db = TinyDB("db/tournament.json")
        table_tournament = db.table("tournament")  # table Tournament
        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())  # last Id tournament created

        # prepare fields end_date end_time of table tour.json
        end_date = date.today()  # automatic current date
        end_date = end_date.isoformat()
        end_time = datetime.datetime.now()  # # automatic current hour
        time = end_time.time()  # Gives the time
        end_time = time
        end_time = time.isoformat()

        # get table tour.json to update
        with open("db/tour.json") as json_data:
            tour_dict = json.load(json_data)

        for i in range(nb_tournament):
            test_id_tournament = tour_dict["tour"][str(no_tours + 1)]["id_tournament"]
            if test_id_tournament == nb_tournament:
                for no_tour in range(NB_ROUNDS):
                    tour_dict["tour"][str(no_tour + 1)]["end_date"] = end_date
                    tour_dict["tour"][str(no_tour + 1)]["end_time"] = end_time
                    with open("db/tour.json", "w") as file:
                        file.write(json.dumps(tour_dict))
                    no_tour += 1
            i += 1
