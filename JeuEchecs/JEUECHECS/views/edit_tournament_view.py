"""
list of all tournaments
"""

import json
from pprint import pprint


class ListTournament:
    def __init__(self):
        pass

    def run(self):

        with open(r"db/tournament.json", "r") as f:
            json_data = f.read()
            json_data = json.loads(json_data)
        print()
        pprint(json_data, indent=0)
        print()
