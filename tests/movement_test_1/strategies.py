class Strategy:

    def __init__(self, player_number):
        self.player_number = player_number

    def decide_ship_movement(self, unit_id, hidden_game_state):
        return (-1,0)
