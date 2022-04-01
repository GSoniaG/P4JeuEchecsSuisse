"""
1st page of main menu
choice of an option with return of the choice
"""

from global_vars import CHOICE_LIST  # options of main menu
from views.entry_choice_menu_view import ViewMenuChoice


class HomeMenu:
    def __init__(self):
        self.user_choice = None

    def run(self):
        while self.user_choice not in CHOICE_LIST:
            print("")
            print("----------------------JEU D'ECHECS - MENU PRINCIPAL")
            print(
                "\n\t1 - créer un tournoi (8 joueurs/tournoi)\n\n"
                "\t2 - mettre à jour le classement mondial des joueurs\n\n"
                "\t3 - finaliser un tournoi\n\n"
                "\t4 - accéder aux rapports\n\n"
                "\t0 - quitter\n\n"
            )

            app = ViewMenuChoice()
            self.user_choice = app.run()

        return self.user_choice
