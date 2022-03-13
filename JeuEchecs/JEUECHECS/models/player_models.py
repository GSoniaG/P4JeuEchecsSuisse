"""
model player
"""


class Player:
    """definition of players"""

    def __init__(self):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self.civility = civility
        self.birth = birth
        self.mondial_classement = mondial_classement
        # entered by the manager
        # the winner receives 1 point, the loser 0 point, else each player receives 0,5 point
        # self.rank = rank # positive number = 0 at the beginning or each tournament
