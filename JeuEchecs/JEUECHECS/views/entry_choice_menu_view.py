"""
input of the menu option with input control
"""


class ViewMenuChoice:
    def __init__(self):
        pass

    def run(self):

        while True:
            try:
                user_choice = int(input(">> votre choix : "))
                break
            except ValueError:
                print(
                    "saisie non valide ! Veuillez choisir un chiffre ou sortir du menu [0]"
                )
        user_choice = int(user_choice)
        return user_choice
