"""
input of the menu option with input control
"""


class ViewMenuChoiceReport:
    def __init__(self):
        pass

    def run(self):

        while True:
            try:
                user_choice_report = int(input("-> votre choix : "))
                break
            except ValueError:
                print(
                    "saisie non valide ! Veuillez choisir un chiffre"
                    " ou sortir du menu [0]"
                )
        user_choice_report = int(user_choice_report)
        return user_choice_report
