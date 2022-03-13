"""
sorting of players by world ranking or by score won during the matches according 
to the Swiss chess rules
"""


from global_vars import COUNTER_PLAYER, NB_ROUNDS  # options of reports menu
from ast import Break
from tinydb import TinyDB
import json
from views.update_player_rank_view import UpdatePlayerRank


db = TinyDB("db/matchs.json")
# database (tables : player+match+round+tournament)
table_matchs = db.table("matchs")  # table match


class PairsPlayers:
    """PairesJoueurs"""

    def __init__(self, nb_tournament, start_date):
        self.nb_tournament = nb_tournament
        self.start_date = start_date
        self.COUNTER_ROUNDS = 0
        self.save_pairs = (
            []
        )  # pairs of players of the tournamnet saved in self.save_pairs
        self.save_player = 0
        self.save_pair_score = []

    # ================Sort players with world ranking (classement mondial)=================
    def RoundOne(self, Id_players):  # 1st tour(round) or if same score between players
        self.COUNTER_ROUNDS += 1
        if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
            self.run(Id_players)

        with open("db/players.json") as json_data:
            players_dict = json.load(json_data)
            content_players = players_dict["players"]

        first_part = []
        second_part = []
        list_matchs = []
        classement = []
        list_sorted = []
        list_idplayers_score = []

        for i0 in range(COUNTER_PLAYER):
            current_classement = content_players[Id_players[i0]]["classement_mondial"]
            # current_classement = classement mondial of player i0 in player table
            classement.append(current_classement)
            current_list = [Id_players[i0], current_classement]
            list_sorted.append(current_list)
        list_sorted.sort(key=lambda x: x[1])  # sort players per classement mondial

        # Divide the players into upper and lower halves.
        for i1 in range(int(COUNTER_PLAYER / 2)):
            # sélect 4 first players after sort
            first_part.append(list_sorted[i1])
        for i2 in range(int(COUNTER_PLAYER / 2), COUNTER_PLAYER):
            # sélect 4 last players after sort
            second_part.append(list_sorted[i2])

        # generation of players pairs according to the Swiss chess rules
        # The best player in the top half is paired with the best player in the bottom half,
        # and so on. Eight players sorted by rank, then player 1 is paired with player 5,
        # player 2 is paired with player 5, player 2 is paired with player 6, and so on.
        pairs = [
            (first_part[0], second_part[0]),
            (first_part[1], second_part[1]),
            (first_part[2], second_part[2]),
            (first_part[3], second_part[3]),
        ]

        # Swiss chess rules : if player 1 has already played against player 2,
        # pair him/her with player 3 instead.
        if ([first_part[0], second_part[0]] in self.save_pairs) or (
            [second_part[0], first_part[0]] in self.save_pairs
        ):
            pairs = [
                (first_part[0], first_part[1]),
                (second_part[0], second_part[1]),
                (first_part[2], second_part[2]),
                (first_part[3], second_part[3]),
            ]

        # display 4 matches to enter them
        print(f"\nTOUR (tri classement mondial) : 4 prochains matchs ")
        print(
            "        => (2 paires de 2 joueurs [Indices joueur, classement mondial]) :"
        )
        print(f"Match 1 : {pairs[0]}\nMatch 2 : {pairs[1]}")
        print(f"Match 3 : {pairs[2]}\nMatch 4 : {pairs[3]}")

        for i3 in range(int(NB_ROUNDS)):  # loop for 4 matchs for on round(tour)
            # number or rounds = number of matchs (same variable)

            # entry of the results of 4 matches
            match = list(
                input(
                    f"saisir le résultat du Match {i3+1} (10 ou 01 ou 11 (match nul) :"
                )
            )
            match = [int(match[0]), int(match[1])]

            # translation of results of tied matches (ex aequo or match  = 11)
            if match[0] == match[1]:
                match[0] = 0.5  # if a match ends 11 : each player receives 1/2 point.
                match[1] = 0.5  # if a match ends 11 : each player receives 1/2 point.

            # save matches in match table
            current_match = {
                "id_tour": str(i3 + 1),
                "id_tournament": self.nb_tournament,
                "date": self.start_date,
                "id_joueur1_resultat": (first_part[i3][0], match[0]),
                "id_joueur2_resultat": (second_part[i3][0], match[1]),
                # a single match must be stored as a tuple containing two lists,
                # each containing two elements: a reference to a player instance and a score
            }

            # pair of players to save
            # with test of existence of pairs of players in self.save_pair
            if (first_part[i3][0], second_part[i3][0]) or (
                second_part[i3][0],
                first_part[i3][0],
            ) not in self.save_pair:
                self.save_pairs.append([first_part[i3][0], second_part[i3][0]])

            # sum score players per match
            if self.COUNTER_ROUNDS == 1:  # 1st tour(round)
                self.save_pair_score.append([first_part[i3][0], match[0]])
                self.save_pair_score.append([second_part[i3][0], match[1]])
            else:  # next tour(round)
                # temporary_pair_players_score = self.save_pair_score
                for player in self.save_pair_score:
                    player_score = [player[0], player[1]]  # get [player,score]
                    # sum of the score in the tournament's scorebook
                    if player[0] == str(first_part[i3][0]):  # test existence of player1
                        player[1] = player[1] + match[0]  # cumulative score
                        # player1_test_exists = 1
                for player in self.save_pair_score:
                    player_score = [player[0], player[1]]  # get [player,score]
                    # sum of the score in the tournament's scorebook
                    if player[0] == str(second_part[i3][0]):
                        # test existence of player2
                        player[1] = player[1] + match[1]  # cumulative score
                        # player2_test_exists = 1

            list_matchs.append(current_match)

            # updated variable list_idplayers_score common to the functions
            list_idplayers_score.append([first_part[i3][0], match[0]])
            list_idplayers_score.append([second_part[i3][0], match[1]])

        # updated match table
        table_matchs.insert_multiple(list_matchs)

        return list_idplayers_score

    # ====================Sort on the score of the tournament games===========================
    def RoundNext(self, list_idplayers_score):  # ROUNDS 2 3 and 4 with score sorting
        if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
            return

        self.list_idplayers_score = list_idplayers_score
        list_matchs = []
        self.list_idplayers_score.sort(key=lambda x: x[1])  # tri sur score

        pairs = [
            (self.list_idplayers_score[0], self.list_idplayers_score[1]),
            (self.list_idplayers_score[2], self.list_idplayers_score[3]),
            (self.list_idplayers_score[4], self.list_idplayers_score[5]),
            (self.list_idplayers_score[6], self.list_idplayers_score[7]),
        ]

        # Swiss chess rules befor next tour(round) : if player 1 has already played
        # against player 2, pair him/her with player 3 instead.
        # change the player2 of a pair if already played with player1
        # check if a pair of players has already been saved
        if (
            self.list_idplayers_score[0],
            self.list_idplayers_score[1] in self.save_pairs,
        ) or (
            self.list_idplayers_score[1],
            self.list_idplayers_score[0] in self.save_pairs,
        ):
            pairs = [
                (self.list_idplayers_score[0], self.list_idplayers_score[2]),
                (self.list_idplayers_score[1], self.list_idplayers_score[3]),
                (self.list_idplayers_score[4], self.list_idplayers_score[5]),
                (self.list_idplayers_score[6], self.list_idplayers_score[7]),
            ]

        # -----------------------------------------------------------------------------------
        Id_players = [
            self.list_idplayers_score[0][0],
            self.list_idplayers_score[1][0],
            self.list_idplayers_score[2][0],
            self.list_idplayers_score[3][0],
            self.list_idplayers_score[4][0],
            self.list_idplayers_score[5][0],
            self.list_idplayers_score[6][0],
            self.list_idplayers_score[7][0],
        ]

        for j in range(2, NB_ROUNDS + 1):  # next tours(or rounds)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
                return

            # test same number of points between at least 2 players
            # In the next round, sort all players according to their total number of points
            # If more than one player has the same number of points, sort them according to
            # their rank > classement mondial
            if (
                (self.list_idplayers_score[0][1] == self.list_idplayers_score[1][1])
                or (self.list_idplayers_score[2][1] == self.list_idplayers_score[3][1])
                or (self.list_idplayers_score[4][1] == self.list_idplayers_score[5][1])
                or (self.list_idplayers_score[6][1] == self.list_idplayers_score[7][1])
                and self.COUNTER_ROUNDS < 2
            ):
                # same number of points between at least 2 players > classement mondial

                a = (
                    (self.list_idplayers_score[0][1] == self.list_idplayers_score[1][1])
                    or (
                        self.list_idplayers_score[2][1]
                        == self.list_idplayers_score[3][1]
                    )
                    or (
                        self.list_idplayers_score[4][1]
                        == self.list_idplayers_score[5][1]
                    )
                    or (
                        self.list_idplayers_score[6][1]
                        == self.list_idplayers_score[7][1]
                    )
                    and self.COUNTER_ROUNDS < 2
                )
                self.run(Id_players)

            if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
                return
            self.COUNTER_ROUNDS += 1

            print(f"\nTOUR (tri rang ) : 4 prochains matchs => (2 paires de 2 joueurs ")
            ("[Indices joueur, classement score]) :")
            print(f"Match 1 : {pairs[0]}\nMatch 2 : {pairs[1]}")
            print(f"Match 3 : {pairs[2]}\nMatch 4 : {pairs[3]}")

            list_idplayers_score = []
            for i5 in range(NB_ROUNDS):
                match = list(
                    input(f"saisir le résultat du Match {i5+1} ")(
                        "(10 ou 01 ou 11 (match nul) :"
                    )
                )
                match = [int(match[0]), int(match[1])]

                if match[0] == match[1]:
                    match[0] = 0.5
                    match[1] = 0.5

                current_match = {
                    "id_tour": str(i5 + 1),
                    "id_tournament": self.nb_tournament,
                    "date": self.start_date,
                    "Id_Joueur1_resultat": (pairs[i5][0][0], match[0]),
                    "Id_Joueur2_resultat": (pairs[i5][1][0], match[1])
                    # A single match must be stored as a tuple containing two lists,
                    # each containing two elements: a reference to a player instance and a
                    # score.
                }

                list_matchs.append(current_match)

                # pair of players to save
                if (pairs[i5][0][0], pairs[i5][1][0]) or (
                    pairs[i5][1][0],
                    pairs[i5][0][0],
                ) not in self.save_pair:
                    self.save_pairs.append([pairs[i5][0][0], pairs[i5][1][0]])
                    # test existence of pairs of players in self.save_pair

                # sum score players per match scores : update cumulative score
                for player in self.save_pair_score:
                    player_score = [player[0], player[1]]  # get [player,score]
                    # sum of the score in the tournament's scorebook
                    # if player[0] == str(first_part[i3][0]): # test existence of player1
                    if player[0] == pairs[i5][0][0]:
                        player[1] = player[1] + match[0]  # cumulative score
                        # player1_test_exists = 1
                for player in self.save_pair_score:
                    player_score = [player[0], player[1]]  # get [player,score]
                    # sum of the score in the tournament's scorebook
                    # if player[0] == str(second_part[i3][0]):
                    # # test existence of player2
                    if player[0] == pairs[i5][1][0]:
                        player[1] = player[1] + match[1]  # cumulative score
                        # player2_test_exists = 1

            table_matchs.insert_multiple(list_matchs)

            list_idplayers_score.append([pairs[i5][0], match[0]])
            list_idplayers_score.append([pairs[i5][1], match[1]])

            update_classement = (
                UpdatePlayerRank()
            )  # launch update classement after each round
            update_classement.run()

    # ----------------------------------------------------------------------------
    def run(self, Id_players):

        while True:

            if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
                break

            if self.COUNTER_ROUNDS < NB_ROUNDS:

                list_idplayers_score = self.RoundOne(Id_players)
                # sort players per classeement mondial

                update_classement = UpdatePlayerRank()
                # launch update classement after each round
                update_classement.run()

                if self.COUNTER_ROUNDS + 1 > NB_ROUNDS:
                    return

                self.RoundNext(list_idplayers_score)
                # sort players per score of matchs
