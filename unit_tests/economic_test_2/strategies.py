class Strategy1:

    def __init__(self, player_number):
        self.player_number = player_number

    def decide_purchases(self, game_state):
        return {'units':[],'technology':['defense','defense']}

class Strategy2:

    def __init__(self, player_number):
        self.player_number = player_number

    def decide_purchases(self, game_state):
        return {'units':[],'technology':['defense','defense']}