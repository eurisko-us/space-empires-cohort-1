class TenvTenStrategy:
    def __init__(self, player_index):
        self.__name__ = 'TenvTenStrategy'
        self.player_number = player_index

    def decide_which_unit_to_attack(self, hidden_game_state_for_combat, combat_state, coords, attacker_index):
        return next((ship['type'], ship['num']) for ship in combat_state[coords] if self.player_number != ship['player_number'] and ship['type'] != 'Home Base')

    def decide_ship_movement(self, unit_index, game_state):
        myself = game_state['players'][self.player_number]
        if len(myself['units']) < 14:
            return (0, 0)
        elif len(myself['units']) == 14:  # 4 ship yards + 10 scouts
            if myself['units'][unit_index]['coords'] != (0, 1):
                if myself['units'][unit_index]['coords'] == (0, 0):
                    return (0, 1)
                elif myself['units'][unit_index]['coords'] == (0, 2):
                    return (0, -1)
        else:
            return (0, 0)

    def decide_purchases(self, hidden_game_state):
        purchases = {'units': [], 'technology': []}
        total_cost = 0
        creds = hidden_game_state['players'][self.player_number]['cp']
        while hidden_game_state['players'][self.player_number]['cp'] >= total_cost + 6 and len(hidden_game_state['players'][self.player_number]['units']) + len(purchases['units']) < 14:
            total_cost += 6
            purchases['units'].append(
                {'type': 'Scout', 'coords': hidden_game_state['players'][self.player_number]['homeworld']['coords']})
        return purchases