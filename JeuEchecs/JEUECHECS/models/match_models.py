"""
model match
"""


class Match:
    def __init__(
        self, id_tour, id_tournament, date, joueur1_resultat, joueur2_resultat
    ):
        self.id_tour = id_tour
        self.id_tournament = id_tournament
        self.date = date
        self.joueur1_resultat = joueur1_resultat
        # list : reference to a player instance + score
        self.joueur2_resultat = joueur2_resultat

    def run(self):
        pass
