"""
model player
"""

from tinydb import TinyDB


class Player:
    def __init__(self, first_name, last_name, civility, birth, classement):
        self.first_name = first_name
        self.last_name = last_name
        self.civility = civility
        self.birth = birth
        self.classement = classement

    @classmethod
    def save_multiple_players(cls, list_players):
        db = TinyDB(cls.table_name)
        table_players = db.table("players")
        table_players.insert_multiple([player.serialize() for player in list_players])

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "civility": self.civility,
            "birth": self.birth,
            "classement": self.classement,
        }
