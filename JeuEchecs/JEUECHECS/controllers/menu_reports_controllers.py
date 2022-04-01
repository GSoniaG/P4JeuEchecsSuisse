"""
2nd page of main menu : rapport
choice of an option with return of the choice
"""

from global_vars import CHOICE_LIST_RAPPORTS
from views.entry_choice_menu_reports_view import ViewMenuChoiceReport


class HomeMenuReports:
    def __init__(self):
        self.user_choice_report = None

    def run(self):
        while self.user_choice_report not in CHOICE_LIST_RAPPORTS:
            print("")
            print("------------------------JEU D'ECHECS : RAPPORTS\n")
            print(
                "\t1 - Liste de tous les joueurs par ordre alphabétique\n"
                "\t2 - Liste de tous les joueurs par classement mondial\n\n"
                "\t3 - Liste de tous les joueurs d'un tournoi par ordre alphabétique\n"
                "\t4 - Liste de tous les joueurs d'un tournoi par classement mondial\n\n"
                "\t5 - Liste de tous les tournois\n\n"
                "\t6 - Liste de tous les tours d'un tournoi\n"
                "\t7 - Liste de tous les matchs d'un tournoi.\n\n"
                "\t0 - quitter\n"
            )

            app = ViewMenuChoiceReport()
            self.user_choice_report = app.run()

        return self.user_choice_report
