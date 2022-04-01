"""
suggest to the manager to stop the tournament in progress and resume it later
"""


class StopTournament:
    def __init__(self):
        pass

    def run(self):

        print("\n-> Interrompre le tournoi et le poursuivre plus tard ? ")
        StopTournament = input(
            "taper O (=Oui) ou tout autre caratère pour continuer" " le tournoi : "
        )

        if StopTournament == "O":
            return StopTournament
