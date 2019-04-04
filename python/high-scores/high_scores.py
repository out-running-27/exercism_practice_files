class HighScores(object):
    def __init__(self, scores):
        """
        param scores is an ordered list of integers each representing an individual score
        """
        self.scores = scores

    def latest(self):
        """
        Returns int that is the last score from the list scores, None if empty
        """
        return self.scores[-1]

    def personal_best(self):
        """
        returns the highest integer from list scores
        """
        return max(self.scores)

    def personal_top_three(self):
        """
        returns the highest three integers from list scores.
        if less than 3 scores are available, then returns an ordered list of all elements
        """
        return sorted(self.scores, reverse=True)[:3]
