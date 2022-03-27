"""
sorting of players by world ranking or by score won
during the matches according to the Swiss chess rules
"""

import json
from datetime import date, datetime

from global_vars import COUNTER_PLAYER, NB_ROUNDS
from tinydb import TinyDB
from views.stop_tournament_view import StopTournament
from views.update_player_rank_view import UpdatePlayerRank

db = TinyDB("db/matchs.json")
table_matchs = db.table("matchs")


class PairsPlayers:
    def __init__(self, nb_tournament, start_date):
        self.nb_tournament = nb_tournament
        # self.num_round = 0 # round counter
        self.start_date = start_date
        self.counter_rounds = 0
        self.save_player = []
        # list of players of the current tournament
        self.save_pairs = []
        # pairs of players of the tournamnet saved in self.save_pairs
        self.save_player_rank = []
        # list of players with rank from table players of current tournament
        self.save_player_score = []
        # list of players with score per match of the current tournament
        self.exit = ""

    # =========Sort players with world ranking (classement mondial)=========
    def RoundOne(self, Id_players):
        # 1st tour(round) or if same score between players
        print("self.counter_rounds 37 : ", self.counter_rounds)
        self.counter_rounds += 1
        print("self.counter_rounds 39 : ", self.counter_rounds)
        if self.counter_rounds + 1 > NB_ROUNDS:
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
            # current_classement = classement mondial of player
            classement.append(current_classement)
            current_list = [Id_players[i0], current_classement]
            list_sorted.append(current_list)
        list_sorted.sort(key=lambda x: x[1])
        # sort players per classement mondial

        # Divide the players into upper and lower halves.
        for i1 in range(int(COUNTER_PLAYER / 2)):
            # sélect 4 first players after sort
            first_part.append(list_sorted[i1])
        for i2 in range(int(COUNTER_PLAYER / 2), COUNTER_PLAYER):
            # sélect 4 last players after sort
            second_part.append(list_sorted[i2])

        # variable with field classement mondial
        self.save_player_rank = [
            [first_part[0], second_part[0]],
            [first_part[1], second_part[1]],
            [first_part[2], second_part[2]],
            [first_part[3], second_part[3]],
        ]

        # Swiss chess rules : if player 1 has already played against player 2,
        # pair him/her with player 3 instead.
        if ([first_part[0], second_part[0]] in self.save_pairs) or (
            [second_part[0], first_part[0]] in self.save_pairs
        ):
            self.save_player_rank = [
                [first_part[0], first_part[1]],
                [second_part[0], second_part[1]],
                [first_part[2], second_part[2]],
                [first_part[3], second_part[3]],
            ]
            print(
                "\n ---> player 1 has already played against player 2 : "
                "pair him/her with player 3 instead \n"
            )

        # display 4 matches to enter them by manager
        print(
            f"\nTOUR n° {self.counter_rounds} => tri par classement mondial "
            "(players) pour les 4 prochains matchs "
        )
        print(" => (2 paires de joueurs ['Indice joueur', classement mondial]) :")
        print(f"Match 1 : {self.save_player_rank[0]}")
        print(f"Match 2 : {self.save_player_rank[1]}")
        print(f"Match 3 : {self.save_player_rank[2]}")
        print(f"Match 4 : {self.save_player_rank[3]}")

        print("\nrésultat match : 10 ou 01 ou 11(match nul)")
        for i3 in range(int(NB_ROUNDS)):
            # loop for 4 matchs for on round(or tour)

            # entry of the results of 4 matches
            match = list(input(f"saisir le résultat du Match {i3+1} : "))
            match = [int(match[0]), int(match[1])]

            # translation of results of tied matches (ex aequo or match  = 11)
            if match[0] == match[1]:
                match[0] = 0.5
                # if a match ends 11 : each player receives 1/2 point.
                match[1] = 0.5
                # if a match ends 11 : each player receives 1/2 point.

            current_match = {
                "id_tour": self.counter_rounds,
                "id_tournament": self.nb_tournament,
                "date": self.start_date,
                "id_joueur1_resultat": (first_part[i3][0], match[0]),
                "id_joueur2_resultat": (second_part[i3][0], match[1]),
            }

            # pair of players to save with test of existence of pairs of players
            if ([first_part[i3][0], second_part[i3][0]]) not in self.save_pairs and (
                [second_part[i3][0], first_part[i3][0]],
            ) not in self.save_pairs:
                self.save_pairs.append([first_part[i3][0], second_part[i3][0]])

            # sum score players per match
            if self.counter_rounds == 1:  # 1st tour(round)
                self.save_player_score.append([first_part[i3][0], match[0]])
                self.save_player_score.append([second_part[i3][0], match[1]])
            else:
                for player in self.save_player_score:
                    # sum of the score in the tournament's scorebook
                    if player[0] == str(
                        first_part[i3][0]
                    ):  # test existence of player1 : first_part
                        player[1] = player[1] + match[0]
                        # cumulative score
                for player in self.save_player_score:
                    # player2_test_exists = 1 : second_part sum of the score
                    if player[0] == str(second_part[i3][0]):
                        # test existence of player2 - cumulative score
                        player[1] = player[1] + match[1]

            list_matchs.append(current_match)

            # updated variable list_idplayers_score common to the functions
            list_idplayers_score.append([first_part[i3][0], match[0]])
            list_idplayers_score.append([second_part[i3][0], match[1]])

        print("-> score players per match : ", list_idplayers_score)

        # updated match table
        table_matchs.insert_multiple(list_matchs)
        # return list_idplayers_score
        return self.save_player_score

    # ===============Sort on the score of the tournament games=======
    def RoundNext(self, list_idplayers_score):
        # ROUNDS 2 3 and 4 with score sorting

        print("self.counter_rounds 170 : ", self.counter_rounds)

        if self.counter_rounds + 1 > NB_ROUNDS:
            return

        self.list_idplayers_score = list_idplayers_score
        list_matchs = []
        self.list_idplayers_score.sort(key=lambda x: x[1])
        # sort on score

        pairs = [
            [self.list_idplayers_score[0][0], self.list_idplayers_score[1][0]],
            [self.list_idplayers_score[2][0], self.list_idplayers_score[3][0]],
            [self.list_idplayers_score[4][0], self.list_idplayers_score[5][0]],
            [self.list_idplayers_score[6][0], self.list_idplayers_score[7][0]],
        ]

        # Swiss chess rules befor next tour(round) : if player 1 has already played
        # against player 2, pair him/her with player 3 instead. Change the player2 of
        # a pair if already played with player1 check if a pair of players has already
        # been saved
        if pairs[0] in self.save_pairs or (pairs[0][1], pairs[0][0]) in self.save_pairs:
            pairs = [
                (pairs[0][0], pairs[1][0]),
                (pairs[0][1], pairs[1][1]),
                pairs[2],
                pairs[3],
            ]
        # ------------------------------------------------------------
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
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if self.counter_rounds + 1 > NB_ROUNDS:
                return
            pairs = [
                [self.list_idplayers_score[0][0], self.list_idplayers_score[1][0]],
                [self.list_idplayers_score[2][0], self.list_idplayers_score[3][0]],
                [self.list_idplayers_score[4][0], self.list_idplayers_score[5][0]],
                [self.list_idplayers_score[6][0], self.list_idplayers_score[7][0]],
            ]

            # test same number of points between at least 2 players. In the next round,
            # sort all players according to their total number of points. If more than
            # one player has the same number of points, sort them according to their
            # rank > classement mondial
            if (
                (self.list_idplayers_score[0][1] == self.list_idplayers_score[1][1])
                or (self.list_idplayers_score[2][1] == self.list_idplayers_score[3][1])
                or (self.list_idplayers_score[4][1] == self.list_idplayers_score[5][1])
                or (self.list_idplayers_score[6][1] == self.list_idplayers_score[7][1])
                and self.counter_rounds < 2
            ):
                # same number of points between at least - 2 players
                # > classement mondial
                print("\n ---> number of points : ", self.list_idplayers_score)
                print(
                    "\n ---> same number of points between at least 2 players"
                    " : sort them according to their rank > classement mondial\n"
                )
                print("self.counter_rounds 238 : ", self.counter_rounds)
                self.run(Id_players)

            if self.counter_rounds + 1 > NB_ROUNDS:
                return
            print("self.counter_rounds 243 : ", self.counter_rounds)
            self.counter_rounds += 1
            print("self.counter_rounds 245 : ", self.counter_rounds)

            self.list_idplayers_score.sort(key=lambda x: x[1])
            # sort on score

            if self.exit == "O":
                return

            print(
                f"\nTOUR n° {self.counter_rounds} => tri par rang (match) pour les 4 prochains matchs"
            )
            print(" => (2 paires de joueurs ['Indice joueur', rang]) :")
            match1 = [self.list_idplayers_score[0], self.list_idplayers_score[1]]
            match2 = [self.list_idplayers_score[2], self.list_idplayers_score[3]]
            match3 = [self.list_idplayers_score[4], self.list_idplayers_score[5]]
            match4 = [self.list_idplayers_score[6], self.list_idplayers_score[7]]
            print("Match 1 : ", match1)
            print("Match 2 : ", match2)
            print("Match 3 : ", match3)
            print("Match 4 : ", match4)

            list_idplayers_score = []

            print("\nrésultat match : 10 ou 01 ou 11(match nul)")

            for i5 in range(NB_ROUNDS):
                # loop for 4 matches
                pairs = [
                    [self.list_idplayers_score[0][0], self.list_idplayers_score[1][0]],
                    [self.list_idplayers_score[2][0], self.list_idplayers_score[3][0]],
                    [self.list_idplayers_score[4][0], self.list_idplayers_score[5][0]],
                    [self.list_idplayers_score[6][0], self.list_idplayers_score[7][0]],
                ]

                match = list(input(f"saisir le résultat du Match {i5+1} : "))
                match = [int(match[0]), int(match[1])]
                if match[0] == match[1]:
                    match[0] = 0.5
                    match[1] = 0.5

                current_match = {
                    "id_tour": self.counter_rounds,
                    "id_tournament": self.nb_tournament,
                    "date": self.start_date,
                    "Id_Joueur1_resultat": (pairs[i5][0], match[0]),
                    "Id_Joueur2_resultat": (pairs[i5][1], match[1]),
                }
                list_matchs.append(current_match)

                # pair of players to save
                if ([pairs[i5][0], pairs[i5][1]]) and (
                    [pairs[i5][1], pairs[i5][0]],
                ) not in self.save_pairs:
                    self.save_pairs.append([pairs[i5][0], pairs[i5][1]])
                    # test existence of pairs of players

                # sum score players per match scores : update cumulative score
                for player in self.save_player_score:
                    if player[0] == pairs[i5][0]:
                        # test existence of player1
                        player[1] = player[1] + match[0]
                        # cumulative score
                for player in self.save_player_score:
                    if player[0] == pairs[i5][1]:
                        # test existence of player2
                        player[1] = player[1] + match[1]
                        # cumulative score

                print("-> score players per match : ", self.save_player_score)

            table_matchs.insert_multiple(list_matchs)

            list_idplayers_score.append([pairs[i5][0], match[0]])
            list_idplayers_score.append([pairs[i5][1], match[1]])

            self.Update_End_Round()

            # 2 intermediate actions in the tournament : 1 = interrupt a tournament
            if self.counter_rounds < NB_ROUNDS:
                stop_tournament = StopTournament()
                self.exit = stop_tournament.run()
                if self.exit == "O":
                    self.Interruption_Tournament()
                    return
            # 2 = update classement per player after each round
            update_classement = UpdatePlayerRank()
            update_classement.run()

    def Interruption_Tournament(self):
        # -----get ID of the last created tournament---------
        with open("db/tournament.json") as json_data:
            dict_tournament = json.load(json_data)
            content_tournament = dict_tournament["tournament"]
        nb_tournament = len(content_tournament.keys())
        dict_tournament["tournament"][str(nb_tournament)][
            "list_idplayers_score"
        ] = self.save_player_score
        print("self.counter_rounds 342 : ", self.counter_rounds)
        dict_tournament["tournament"][str(nb_tournament)][
            "number_rounds_created"
        ] = self.counter_rounds
        with open("db/tournament.json", "w") as file:
            file.write(json.dumps(dict_tournament))

    def Update_End_Round(self):
        start_date = date.today()
        start_date = start_date.isoformat()
        start_time = datetime.now()
        time = start_time.time()
        start_time = time
        start_time = time.isoformat()
        end_date = date.today()
        end_date = end_date.isoformat()
        end_time = datetime.now()
        time = end_time.time()
        end_time = time
        end_time = time.isoformat()

        with open("db/tour.json") as json_data:
            tour_dict = json.load(json_data)
        content_tour = tour_dict["tour"]
        nb_tours = len(content_tour)
        for i in range(nb_tours):
            if tour_dict["tour"][str(i + 1)]["id_tournament"] == self.nb_tournament:
                if tour_dict["tour"][str(i + 1)]["name"] == str(self.counter_rounds):
                    tour_dict["tour"][str(i + 1)]["start_date"] = start_date
                    tour_dict["tour"][str(i + 1)]["start_time"] = start_time
                    tour_dict["tour"][str(i + 1)]["end_date"] = end_date
                    tour_dict["tour"][str(i + 1)]["end_time"] = end_time
                    with open("db/tour.json", "w") as file:
                        file.write(json.dumps(tour_dict))

    def Resumption_Tournament_Interrupted(
        self, Id_tournament, list_idplayers_score, number_rounds_created, Id_players
    ):
        self.Id_tournament = Id_tournament
        self.list_idplayers_score = list_idplayers_score
        self.number_rounds_created = number_rounds_created

        self.counter_rounds = self.number_rounds_created
        self.save_player_score = self.list_idplayers_score
        self.nb_tournament = self.Id_tournament

        print("self.number_rounds_created 383 : ", self.number_rounds_created)

        self.RoundNext(self.list_idplayers_score)
        print("self.number_rounds_created 388 : ", self.number_rounds_created)
        return self.counter_rounds

    def run(self, Id_players):
        while True:
            if self.counter_rounds + 1 > NB_ROUNDS:
                break
            if self.counter_rounds < NB_ROUNDS:
                print("self.counter_rounds 399 : ", self.counter_rounds)
                list_idplayers_score = self.RoundOne(Id_players)
                # sort players per classeement mondial
                self.Update_End_Round()  # current tour
                # ---------intermediate actions in the tournament----
                if self.counter_rounds < NB_ROUNDS:
                    print("self.counter_rounds 405 : ", self.counter_rounds)
                    stop_tournament = StopTournament()
                    # interrupt a tournament
                    self.exit = stop_tournament.run()
                if self.exit == "O":
                    self.Interruption_Tournament()
                    print("self.counter_rounds 411 : ", self.counter_rounds)
                    return
                print("self.counter_rounds 413 : ", self.counter_rounds)
                update_classement = UpdatePlayerRank()
                # launch update classement after each round
                # views.update_player_rank_view
                update_classement.run()
                if self.counter_rounds + 1 > NB_ROUNDS:
                    print("self.counter_rounds 419 : ", self.counter_rounds)
                    return
                self.RoundNext(list_idplayers_score)
                # sort players per score of matchs
