class DavidStrategyLevel3:
 
   def __init__(self, player_index):
       self.player_index = player_index
 

   def decide_ship_movement(self, unit_index, hidden_game_state):
        myself = hidden_game_state['players'][self.player_index]
        opponent_index = 1 if self.player_index == 2 else 1
        opponent = hidden_game_state['players'][opponent_index]

        unit = myself['units'][unit_index]
        x_unit, y_unit = unit['coords']
        x_home, y_home = myself['homeworld']['coords']
        x_opp, y_opp = opponent['homeworld']['coords']

        if (len([unit for unit in myself['units'] if unit['type'] == 'Shipyard']) <2 or len([unit for unit in myself['units'] if unit['technology']['attack'] == 2 and unit['technology']['defense'] == 2]) > 5) and hidden_game_state['turn'] >= 20:
            if unit['technology']['attack'] >= 1 or unit['technology']['defense'] >= 1:
                best_translation = self.best_move(unit, opponent, myself)
            else:
                best_translation = (0,0)
        else:
            best_translation = (0,0)

        return best_translation

   def best_move(self,unit, opponent, myself):
        x_unit, y_unit = unit['coords']
        x_home, y_home = myself['homeworld']['coords']
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
 
   def decide_removal(self, player_state):
      return -1
   def decide_which_unit_to_attack(self, combat_state, coords, attacker_type, attacker_index):
      combat_order = combat_state[coords]
    
      opponent_index = ((self.player_index-2)**2)+1
      for combat_index, unit in enumerate(combat_order):
          if unit['player'] == opponent_index:
              return (unit['player'],unit['type'],unit['num'])
   def decide_purchases(self,game_state):
      return_dict={
         'units': [],
         'technology': []}
      current_cp = game_state['players'][self.player_index]['cp']
      my_home=game_state['players'][self.player_index]['homeworld']['coords']
      # print(game_state['players'][self.player_index]['technology'])
      # new_defense= game_state['players'][self.player_index]['technology']['defense']
      home_colony_ship_capacity=len([shipyard for shipyard in game_state['players'][self.player_index]["units"] if shipyard["type"]=="Shipyard" and shipyard['coords']==my_home])
      if game_state["turn"]<=2:
        if current_cp>=game_state['technology_data']['defense'][0]:
          return_dict['technology'].append("defense")
      else:
        while current_cp>=game_state['unit_data']['Scout']['cp_cost'] and home_colony_ship_capacity>=game_state['unit_data']['Scout']['hullsize'] and (len([unit for unit in game_state["players"][self.player_index]["units"] if unit["type"]=="Scout"]))<17:
          current_cp-=game_state['unit_data']['Scout']['cp_cost']
          home_colony_ship_capacity -= game_state['unit_data']['Scout']['hullsize']
          return_dict['units'].append({'type': 'Scout', 'coords': game_state['players'][self.player_index]['homeworld']['coords']})
      return return_dict
 
 
 
   def decide_removal(self, player_state):
      return -1
   def decide_which_unit_to_attack(self, combat_state, coords, attacker_type, attacker_index):
      combat_order = combat_state[coords]
    
      opponent_index = ((self.player_index-2)**2)+1
      for combat_index, unit in enumerate(combat_order):
          if unit['player'] == opponent_index:
              return (unit['player'],unit['type'],unit['num'])

 
 
