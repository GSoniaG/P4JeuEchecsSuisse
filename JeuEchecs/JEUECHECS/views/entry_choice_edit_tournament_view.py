"""
input of the menu option with input control
"""


class ViewMenuChoiceEditTournament:
    def __init__(self):
        pass

    def run(self):

        while True:
            try:
                user_choice_edit_tournament = int(input("-> votre choix : "))
                break
            except ValueError:
                print(
                    "saisie non valide ! Veuillez choisir un chiffre ou "
                    "sortir du menu [0]"
                )
        user_choice_edit_tournament = int(user_choice_edit_tournament)
        return user_choice_edit_tournament
