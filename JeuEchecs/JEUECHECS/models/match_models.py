"""
model match
"""


class Match:
    """definition of Matchs"""

    def __init__(self):
        self.id_match = id_match
        self.id_tour = id_tour
        self.id_tournament = id_tournament
        self.date = date
        self.joueur1_resultat = joueur1_resultat
        # list : reference to a player instance + score
        self.joueur2_resultat = joueur2_resultat
