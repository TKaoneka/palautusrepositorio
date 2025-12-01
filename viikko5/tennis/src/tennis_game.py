class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):

        if self.p1_score == self.p2_score and self.p1_score < 3:
            return self.equal_score()

        elif self.p1_score == self.p2_score and self.p1_score == 2:
            return self.advantage()
        else:
            return self.not_equal_score()

    def equal_score(self):
        score_names = ["Love-All", "Fifteen-all", "Thirty-All"]
        if self.p1_score < 3:
            score = score_names[self.p1_score]
        else:
            score = "Deuce"
        return score

    def not_equal_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Fourty"]
        if self.p1_score <= 3 and self.p2_score <= 3:
            return f"{score_names[self.p1_score]}-{score_names[self.p2_score]}"

        elif self.p1_score < 3 and self.p2_score == 4:
            return "Win for player2"

        elif self.p2_score < 3 and self.p1_score == 4:
            return "Win for player1"

    def advantage(self):
        score = ["Advantage player1", " Advantage player2"]
        temp_score = self.p1_score - self.p2_score
        if temp_score > 0:
            return score[0]
        else:
            return score[1]
