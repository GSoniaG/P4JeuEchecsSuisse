"""
main launches MenuManager which will run TournamentManager :
    initialization of players, tournaments
run method for each controller
"""

from views.edit_matchs_tournament_view import ListMatchs
from views.edit_player_rank_tournament_view import ListPlayersRankOrderTournament
from views.edit_player_rank_view import ListPlayersRankOrder
from views.edit_players_name_sort_tournament_view import ListPlayersAlphaOrderTournament
from views.edit_players_name_sort_view import ListPlayersAlphaOrder
from views.edit_rounds_view import ListRounds
from views.edit_tournament_view import ListTournament
from views.entry_tournament_view import ViewTournament
from views.finalize_tournament_view import UpdateTournament
from views.update_player_rank_view import UpdatePlayerRank

from .menu_reports_controllers import HomeMenuReports


class LaunchChoice:
    def __init__(self):
        pass

    def run(self, user_choice):

        if user_choice == 1:
            current_tournament = ViewTournament()
            # Views.entrytournamentview.py
            current_tournament.run()

        if user_choice == 2:
            # views.update_player_rank_view.py : updateplayerrankview
            update_classement = UpdatePlayerRank()
            # launch update classement after each round
            update_classement.run()

        if user_choice == 3:
            # finalize a tournament
            # views.finalize_tournament_view
            finalize_tournament = UpdateTournament()
            # launch finalize a tournament
            finalize_tournament.run()

        if user_choice == 4:
            # acces to the reports

            while True:
                report_menu = HomeMenuReports()
                # report menu menureportscontrollers.py
                user_choice_report = report_menu.run()
                # run method for each controller

                if user_choice_report == 1:
                    # views.edit_players_name_sort_view : ListPlayersAlphaOrder
                    list_players = ListPlayersAlphaOrder()
                    list_players.run()

                if user_choice_report == 2:
                    # from views.edit_player_rank_view : ListPlayersRankOrder
                    list_players = ListPlayersRankOrder()
                    list_players.run()

                # List of all players in a tournament in alphabetical order
                if user_choice_report == 3:
                    list_players = ListPlayersAlphaOrderTournament()
                    # editplayersnamesortview.py
                    list_players.run()

                # List of all players in a tournament by world ranking
                if user_choice_report == 4:
                    list_players = ListPlayersRankOrderTournament()
                    # editplayerrankview.py
                    list_players.run()

                # List of all tournaments
                if user_choice_report == 5:
                    list_tournament = ListTournament()
                    # edittournamentview.py
                    list_tournament.run()

                # List of all rounds in a tournament.
                if user_choice_report == 6:
                    list_rounds = ListRounds()
                    # editroundsview.py
                    list_rounds.run()

                # List of all matches in a tournament.
                if user_choice_report == 7:
                    list_matchs = ListMatchs()
                    # editmatchsview.py
                    list_matchs.run()

                if user_choice_report == 0:
                    break

        if user_choice == 0:
            # 0 - quitter
            return
