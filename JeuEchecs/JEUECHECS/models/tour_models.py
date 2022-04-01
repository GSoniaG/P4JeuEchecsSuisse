"""
tour (round) model
"""

# from unicodedata import name


class Tour:
    def __init__(self, id_tournament, name, start_date, start_time, end_date, end_time):
        self.id_tournament = id_tournament
        self.name = name
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
