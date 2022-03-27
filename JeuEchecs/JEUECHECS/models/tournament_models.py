"""
a tournament = liste of 4 rounds (tours)
"""


class Tournament:
    def __init__(self, name, place, date, tour, players, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.tour = tour
        self.players = players
        self.time_control = time_control
        self.description = description
