from abc import ABC


class Player(ABC):
    def __init__(self, name, points, form, position, minutes, goals_scored, assists, own_goals, yellow_cards, red_cards, bonus, threat):
        self.name = name
        self.form = form
        self.points = points
        self.position = position
        self.minutes = minutes
        self.goals_scored = goals_scored
        self.assists = assists
        self.own_goals = own_goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.bonus = bonus
        self.threat = threat

    def print(self):
        print(self.name + ": " + self.form + " | " + self.points + " | " + self.goals_scored)
    