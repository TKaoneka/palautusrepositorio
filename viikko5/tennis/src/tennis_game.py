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
        if self.p1_score == self.p2_score:
            return self.equal_score()

        if self.p1_score >= 4 or self.p2_score >= 4:
            return self.advantage()

        return self.not_equal_score()

    def equal_score(self):
        score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
        if self.p1_score < 3:
            score = score_names[self.p1_score]
        else:
            score = "Deuce"
        return score

    def not_equal_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.p1_score <= 3 and self.p2_score <= 3:
            return f"{score_names[self.p1_score]}-{score_names[self.p2_score]}"

    def advantage(self):
        temp_score = self.p1_score - self.p2_score
        if temp_score == 1:
            return "Advantage player1"
        elif temp_score == -1:
            return "Advantage player2"
        elif temp_score >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
