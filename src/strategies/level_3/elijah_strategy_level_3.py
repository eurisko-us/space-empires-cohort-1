class ElijahStrategyLevel3:
    # Sends a barrage of scouts towards enemy
    # While attempting to attack shipyards first

    def __init__(self, player_index):
        self.player_index = player_index
        self.priorities = ["Shipyard", "Scout", "Colony"]
        self.opponent_index = 1 if player_index == 2 else 2

    def decide_ship_movement(self, unit_index, hidden_game_state):
        enemy = hidden_game_state['players'][self.opponent_index]
        enemy_home = enemy["homeworld"]['coords']
        units = hidden_game_state['players'][self.player_index]["units"]
        unit = units[unit_index]

        # Go to enemy base
        if unit['coords'] != enemy_home:
            direction = 1 if enemy_home[1] > unit['coords'][1] else -1
            return (0, direction)

        # Otherwise stay still
        return (0, 0)

    # Attack shipyards first, then scouts
    def decide_which_unit_to_attack(self, combat_state, coords, attacker_type, attacker_num):
        to_attack = min(combat_state[coords], key=lambda x: self.priorities.index(x['type']))
        return to_attack["player"], to_attack["type"], to_attack["num"]

    # Buy all possible scouts
    def decide_purchases(self, game_state):
        scout_price = game_state['unit_data']['Scout']['cp_cost']
        player = game_state['players'][self.player_index]
        cp = player['cp']
        home_coords = game_state['players'][self.player_index]['homeworld']['coords']
        sy_capacity = len([i for i in player['units'] if i['type'] == 'ShipYard'])
        amt = min(sy_capacity, cp//scout_price)
        return {'technology': [], 'units': [{'type': 'Scout', 'coords': home_coords}] * amt}
