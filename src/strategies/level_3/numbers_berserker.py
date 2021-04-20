class NumbersBerserkerLevel3:
    # Buys as many scouts as possible, then
    # Sends all of its units directly towards the enemy home colony

    def __init__(self, player_index):
        self.player_index = player_index
        self.opponent_index = 1 if player_index == 2 else 2

    def decide_ship_movement(self, unit_index, hidden_game_state):
        myself = hidden_game_state['players'][self.player_index]
        opponent_index = 1 if self.player_index == 2 else 2
        opponent = hidden_game_state['players'][opponent_index]

        unit = myself['units'][unit_index]
        x_unit, y_unit = unit['coords']
        x_opp, y_opp = opponent['homeworld']['coords']

        translations = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        best_translation = (0,0)
        smallest_distance_to_opponent = 999999999999
        for translation in translations:
            delta_x, delta_y = translation
            x = x_unit + delta_x
            y = x_unit + delta_y
            dist = abs(x - x_opp) + abs(y - y_opp)
            if dist < smallest_distance_to_opponent:
                best_translation = translation
                smallest_distance_to_opponent = dist

        return best_translation

    def decide_which_unit_to_attack(self, combat_state, coords, attacker_type, attacker_num):
        return next((u['player'], u['type'], u['num']) for u in combat_state[coords] if self.player_index != u['player'])

    # Buy all possible scouts
    def decide_purchases(self, game_state):
        scout_price = game_state['unit_data']['Scout']['cp_cost']
        player = game_state['players'][self.player_index]
        cp = player['cp']
        home_coords = game_state['players'][self.player_index]['homeworld']['coords']
        sy_capacity = len([i for i in player['units'] if i['type'] == 'ShipYard'])
        amt = min(sy_capacity, cp//scout_price)
        return {'technology': [], 'units': [{'type': 'Scout', 'coords': home_coords}] * amt}
