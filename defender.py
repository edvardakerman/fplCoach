from player import Player

class Defender(Player):
    
    def __init__(self, exp_goals_conceded_per_90, clean_sheets, goals_conceded):
        super().__init__()
        self.exp_goals_conceded_per_90 = exp_goals_conceded_per_90
        self.clean_sheets = clean_sheets
        self.goals_conceded = goals_conceded