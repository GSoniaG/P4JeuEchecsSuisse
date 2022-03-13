"""
2nd page of main menu : rapport
choice of an option with return of the choice
"""

from global_vars import CHOICE_LIST_RAPPORTS  # options of reports menu
from views.entry_choice_menu_reports_view import ViewMenuChoiceReport


class HomeMenuReports:
    def __init__(self):
        self.user_choice_report = None

    def run(self):
        # user_choice_report = None # initialisation of var user_choice from main.py
        while self.user_choice_report not in CHOICE_LIST_RAPPORTS:
            print("")
            print("------------------------JEU D'ECHECS : RAPPORTS")
            print(
                """         
            1 - Liste de tous les joueurs d'un tournoi par ordre alphabétique
            2 - Liste de tous les joueurs d'un tournoi par classement mondial

            3 - Liste de tous les tournois.
            
            4 - Liste de tous les tours d'un tournoi.
            5 - Liste de tous les matchs d'un tournoi.

            
            0 - quitter

            """
            )

            app = ViewMenuChoiceReport()
            # call entrychoicemenuview.py and get choice with control
            self.user_choice_report = app.run()
            # get option menu vy user via view

        return self.user_choice_report
