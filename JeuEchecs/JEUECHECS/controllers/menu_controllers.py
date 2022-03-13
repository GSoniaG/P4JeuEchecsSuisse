"""
1st page of main menu
choice of an option with return of the choice
"""


from views.entry_choice_menu_view import ViewMenuChoice
from global_vars import CHOICE_LIST  # options of main menu


class HomeMenu:
    def __init__(self):
        self.user_choice = None

    def run(self):
        # user_choice = None - initialization of var user_choice from main.py
        while self.user_choice not in CHOICE_LIST:
            print("")
            print("----------------------JEU D'ECHECS - MENU PRINCIPAL")
            print(
                """
            1 - créer un tournoi
                8 joueurs/tournoi-1 paire joueurs/match-4 matchs/tour-4 tours/tournoi
                joueurs triés/classement mondial tour1 puis par score

            2 - mettre à jour le classement mondial des joueurs

            3 - accéder aux rapports

            
            0 - quitter
            """
            )
            print("\n")

            app = ViewMenuChoice()
            # call entrychoicemenuview.py and get menu choice with control
            self.user_choice = app.run()
            # get option menu by user via view

        return self.user_choice
