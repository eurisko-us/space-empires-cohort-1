import random
import math

class BasicStrategy:  # no movement or actual strategy, just funcitons like decide_removal or decide_which_unit_to_attack
    def __init__(self, player_index):
        self.player_number = player_index

    def decide_removal(self, hidden_game_state): #remove weakest 
        weakest_ship = sorted(hidden_game_state['players'][self.player_number]['units'], key=lambda ship: (ship['technology']['tactics'], -ship['player_number'], -ship['num']), reverse=True)[-1]
        return weakest_ship['type'], weakest_ship['num']

    def decide_which_unit_to_attack(self, hidden_game_state_for_combat, combat_state, coords, attacker_index):
        return next((ship['type'], ship['num']) for ship in combat_state[coords] if self.player_number != ship['player_number'] and ship['type'] != 'Home Base')

    def decide_which_units_to_screen(self, hidden_game_state_for_combat):
        return []
                    
    def decide_ship_movement(self, unit_index, game_state):
        return (0,0)
    
    def get_distance_to(self, friendly_unit_coords, enemy_unit_coords):
        return math.sqrt((friendly_unit_coords[0] - enemy_unit_coords[0]) ** 2 + (friendly_unit_coords[1] - enemy_unit_coords[1]) ** 2)

    def will_colonize_planet(self, coordinates, game_state):
        return False

    def upgrade_costs(self, stat_to_upgrade, game_state):
        return game_state['technology_data'][stat_to_upgrade][game_state['players'][self.player_number]['technology'][stat_to_upgrade]]

    def ship_cost(self, ship, game_state):
        return game_state['unit_data'][ship]['cp_cost']

    def get_movement_tech(self, ship_movement_level):
        if ship_movement_level == 1:
            return [1,1,1]
        elif ship_movement_level == 2:
            return [1,1,2]
        elif ship_movement_level == 3:
            return [1,2,2]
        elif ship_movement_level == 4:
            return [2,2,2]
        elif ship_movement_level == 5:
            return [2,2,3]
        elif ship_movement_level == 5:
            return [2,3,3]

    def get_translation(self, unit, translation):
        return (unit['coords'][0] + translation[0], unit['coords'][1] + translation[1])

          
class ColbyStrategyLevel3(BasicStrategy):
    def __init__(self, player_index):  # wutever else we need):
        self.player_number = player_index
        self.__name__ = 'ColbyStrategyLevel3'
        self.WE_SIEGIN_BOI = False
        self.DIE_DIE_DIE = False

    def decide_purchases(self, hidden_game_state):
        self.myself = hidden_game_state['players'][self.player_number]
        self.enemy = self.enemy
        
        self.num_of_friendly_ships = len(self.myself['units'])
        self.num_of_friendly_scouts = len([ship for ship in self.myself['units'] if ship['type'] == 'Scout'])
        self.num_of_enemy_ships = len(self.enemy['units'])
        self.num_of_enemy_ships_at_enemy_home_base = len([ship for ship in self.enemy['units'] if ship['coords'] == self.enemy_home_base_coords])
        self.num_of_enemy_scouts = len([ship for ship in self.enemy['units'] if ship['type'] == 'Scout'])
        self.num_of_friendly_scouts_in_siege_position = len(['' for ship in self.myself['units'] if ship['coords'] in self.possible_siege_positions])

        if self.num_of_friendly_scouts_in_siege_position < self.num_of_enemy_ships_at_enemy_home_base:
            self.WE_SIEGIN_BOI = True
            self.DIE_DIE_DIE = False
        elif self.num_of_friendly_scouts_in_siege_position > self.num_of_enemy_ships_at_enemy_home_base:
            self.WE_SIEGIN_BOI = False
            self.DIE_DIE_DIE = True
        else:
            self.WE_SIEGIN_BOI = False
            self.DIE_DIE_DIE = False

        self.home_coords = self.myself['homeworld']['coords']

        if self.num_of_enemy_ships > 0:
            closest_ship = min([unit for unit in self.enemy['units']], key = lambda unit: self.get_distance_to(self.home_coords, unit['coords']))

        else:
            closest_ship = self.enemy['homeworld']

        if self.WE_SIEGIN_BOI:
            if hidden_game_state['players'][self.player_number]['cp'] > 100:
                self.WE_SIEGIN_BOI = False
                self.DIE_DIE_DIE = True
            return {'units': [], 'technology': []}

        if self.get_distance_to(self.home_coords, closest_ship['coords']) > 3 and hidden_game_state['turn'] < 16:
            self.technology = hidden_game_state['players'][self.player_number]['technology']
            purchases = [self.get_technological_purchases('defense', hidden_game_state), self.get_technological_purchases('attack', hidden_game_state)]
            return max(purchases, key=lambda purchase: len(purchase['technology']))

        else:
            purchases = {'units': [], 'technology': []}
            total_cost = 0
            ship = self.choose_ship(purchases, total_cost, hidden_game_state)
            ship_cost = self.ship_cost(ship, hidden_game_state)
            creds = hidden_game_state['players'][self.player_number]['cp']
            while hidden_game_state['players'][self.player_number]['cp'] >= total_cost + self.ship_cost(ship, hidden_game_state):
                purchases['units'].append({'type': ship, 'coords': hidden_game_state['players'][self.player_number]['homeworld']['coords']})
                total_cost += self.ship_cost(ship, hidden_game_state)
                ship = self.choose_ship(purchases, total_cost, hidden_game_state)
            return purchases

    def get_technological_purchases(self, stat_to_upgrade, hidden_game_state):
        purchases = {'units': [], 'technology': []}
        tech_cost = hidden_game_state['technology_data'][stat_to_upgrade][self.technology[stat_to_upgrade] + len(purchases['technology'])]
        while self.myself['technology'][stat_to_upgrade] + len(purchases['technology']) + 1 < 3 and tech_cost <= self.myself['cp']:
            purchases['technology'].append(stat_to_upgrade)
            #print("hidden_game_state['technology_data'][stat_to_upgrade]", hidden_game_state['technology_data'][stat_to_upgrade])
            #print("self.technology[stat_to_upgrade] + len(purchases['technology'])", self.technology[stat_to_upgrade] + len(purchases['technology']))
            tech_cost = hidden_game_state['technology_data'][stat_to_upgrade][self.technology[stat_to_upgrade] + len(purchases['technology'])]
            #print("purchase", purchases)
            #print("hidden_game_state['technology_data'][stat_to_upgrade]", hidden_game_state['technology_data'][stat_to_upgrade])
            #print("self.technology[stat_to_upgrade] + len(purchases['technology'])", self.technology[stat_to_upgrade] + len(purchases['technology']))
        return purchases

    def choose_ship(self, purchases, total_cost, hidden_game_state):
        return 'Scout'

    def decide_ship_movement(self, unit_index, hidden_game_state):
        self.myself = hidden_game_state['players'][self.player_number]
        self.enemy = hidden_game_state['players'][len(hidden_game_state['players']) + 1 - self.player_number]
        self.home_base_coords = self.myself['homeworld']['coords']
        self.enemy_home_base_coords = self.enemy['homeworld']['coords']
        if self.enemy_home_base_coords[1] > 0: self.possible_siege_positions = [(self.enemy_home_base_coords[1] + 1, self.enemy_home_base_coords[1]), (self.enemy_home_base_coords[1] - 1, self.enemy_home_base_coords[1]), (self.enemy_home_base_coords[1], self.enemy_home_base_coords[1] - 1)]
        elif self.enemy_home_base_coords == 0: self.possible_siege_positions = [(self.enemy_home_base_coords[1] + 1, 0), (self.enemy_home_base_coords[1] - 1, 0), (self.enemy_home_base_coords[1], 1)]

        friendly_unit = self.myself['units'][unit_index]
        self.num_of_friendly_ships = len(self.myself['units'])
        self.num_of_friendly_scouts = len([ship for ship in self.myself['units'] if ship['type'] == 'Scout'])
        self.num_of_enemy_ships = len(self.enemy['units'])
        self.num_of_enemy_ships_at_enemy_home_base = len([ship for ship in self.enemy['units'] if ship['coords'] == self.enemy_home_base_coords])
        self.num_of_enemy_scouts = len([ship for ship in self.enemy['units'] if ship['type'] == 'Scout'])

        if self.num_of_enemy_scouts > 0:
            closest_ship_to_home_world = min([unit for unit in self.enemy['units']], key = lambda unit: self.get_distance_to(self.home_base_coords, unit['coords']))
            closest_ship_to_current_unit = min([unit for unit in self.enemy['units']], key = lambda unit: self.get_distance_to(friendly_unit['coords'], unit['coords']))
        else:
            closest_ship_to_home_world = self.enemy['homeworld']
            closest_ship_to_current_unit = self.enemy['homeworld']

        self.num_of_friendly_scouts_in_siege_position = len(['' for ship in self.myself['units'] if ship['coords'] in self.possible_siege_positions])
        self.closest_enemy_ship_distance_to_home_world = self.get_distance_to(self.home_base_coords, closest_ship_to_home_world['coords'])    
        self.num_of_enemy_ships_not_on_midline = len(['' for unit in self.enemy['units'] if unit['coords'] != self.enemy_home_base_coords and unit['coords'][0] != 3])
        
        if self.DIE_DIE_DIE:
            return self.get_translation(hidden_game_state, friendly_unit, closest_ship_to_current_unit['coords'])
        
        if hidden_game_state['turn'] < 18 and self.closest_enemy_ship_distance_to_home_world > 3:
            return (0,0)
        
        elif self.num_of_enemy_ships_not_on_midline > 0: 
            return self.get_translation(hidden_game_state, friendly_unit, closest_ship_to_current_unit['coords']) # move to counter flank strat

        elif hidden_game_state['turn'] > 18 and self.num_of_enemy_ships < self.num_of_friendly_scouts and friendly_unit['coords'] not in self.possible_siege_positions: # if turn > 18 and the enemy has more ships than us and the current unit is not in possible siege positions
            self.WE_SIEGIN_BOI = True
            return self.get_translation(hidden_game_state, friendly_unit, self.possible_siege_positions[friendly_unit['num'] % 3]) # move into designated siege position
        
        elif self.num_of_enemy_ships_at_enemy_home_base < self.num_of_friendly_scouts_in_siege_position: # if we have more ships in siege position than the enemy has scouts + shipyards then attack home base
            self.DIE_DIE_DIE = True
            return self.get_translation(hidden_game_state, friendly_unit, self.enemy_home_base_coords) # move towards enemy home base

        else:
            if self.closest_enemy_ship_distance_to_home_world > 3 and friendly_unit['coords'] in self.possible_siege_positions:# if ship in siege position and we dont have enough ships in siege positions dont move current ship

                if 10 < self.num_of_friendly_scouts_in_siege_position < self.num_of_enemy_ships_at_enemy_home_base: # if 10 < total number of ships in siege position < number of enemy ships
                    self.WE_SIEGIN_BOI = True
                    return (0,0) # dont move

                elif self.num_of_friendly_scouts_in_siege_position < 10 < self.num_of_enemy_ships: #if we have basically no ships in siege positions
                    return self.get_translation(hidden_game_state, friendly_unit, self.home_base_coords) #retreat

            else:

                if not self.WE_SIEGIN_BOI and friendly_unit['coords'] != closest_ship_to_current_unit['coords']: # if i amn't sieging and current unit not in same coord as closest ship to current unit
                    return self.get_translation(hidden_game_state, friendly_unit, closest_ship_to_current_unit['coords']) # move towards closest unit

                elif friendly_unit['coords'] == closest_ship_to_current_unit['coords']: #if current unit in same coord as closest ship to current unit
                    return (0,0) # dont move

            return (0,0) #else

    def get_translation(self, hidden_game_state, unit, target_unit_coords):
        translations = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        return min([(translation, self.get_distance_to(self.get_translation(hidden_game_state, unit, translation), target_unit_coords)) for translation in translations], key = lambda distance: distance[1])[0] #heheh 1 liner gang also the two codes do the same thing