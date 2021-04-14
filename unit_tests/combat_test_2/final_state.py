final_state = {
    'turn': 1,
    'winner': None,
    'board_size': (1, 3),
    'phase': 'Combat',
    'round': None,
    'players': {
        1: {
            'homeworld': {'coords': (0, 0), 'type': 'Homeworld', 'hits_left': 4, 'turn_created': 0}, 
            'units': [], 
            'technology': {'attack': 0, 'defense': 1, 'movement': 1, 'shipsize': 1}
        }, 
        2: {
            'homeworld': {'coords': (0, 2), 'type': 'Homeworld', 'hits_left': 4, 'turn_created': 0},
            'units': [
                {'num': 3, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                },  
                {'num': 4, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 5, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 6, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 7, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 8, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 9, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0,  
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                }, 
                {'num': 10, 'coords': (0, 1), 'type': 'Scout', 'hits_left': 1, 'turn_created': 0, 
                    'technology': {
                        'attack': 0,
                        'defense': 1,
                        'movement': 1,
                        'shipsize': 1,
                    }
                },  
            ], 
            'technology': {'attack': 0, 'defense': 1, 'movement': 1, 'shipsize': 1}, 
        }
    'planets': [(0,0), (0,2)],
    'unit_data': {
        'Battleship': {'cp_cost': 20, 'hullsize': 3, 'shipsize_needed': 5, 'tactics': 5, 'attack': 5, 'defense': 2, 'maintenance': 3},
        'Battlecruiser': {'cp_cost': 15, 'hullsize': 2, 'shipsize_needed': 4, 'tactics': 4, 'attack': 5, 'defense': 1, 'maintenance': 2},
        'Cruiser': {'cp_cost': 12, 'hullsize': 2, 'shipsize_needed': 3, 'tactics': 3, 'attack': 4, 'defense': 1, 'maintenance': 2},
        'Destroyer': {'cp_cost': 9, 'hullsize': 1, 'shipsize_needed': 2, 'tactics': 2, 'attack': 4, 'defense': 0, 'maintenance': 1},
        'Dreadnaught': {'cp_cost': 24, 'hullsize': 3, 'shipsize_needed': 6, 'tactics': 5, 'attack': 6, 'defense': 3, 'maintenance': 3},
        'Scout': {'cp_cost': 6, 'hullsize': 1, 'shipsize_needed': 1, 'tactics': 1, 'attack': 3, 'defense': 0, 'maintenance': 1},
        'Shipyard': {'cp_cost': 3, 'hullsize': 1, 'shipsize_needed': 1, 'tactics': 3, 'attack': 3, 'defense': 0, 'maintenance': 0},
        'Decoy': {'cp_cost': 1, 'hullsize': 0, 'shipsize_needed': 1, 'tactics': 0, 'attack': 0, 'defense': 0, 'maintenance': 0},
        'Colonyship': {'cp_cost': 8, 'hullsize': 1, 'shipsize_needed': 1, 'tactics': 0, 'attack': 0, 'defense': 0, 'maintenance': 0},
        'Base': {'cp_cost': 12, 'hullsize': 3, 'shipsize_needed': 2, 'tactics': 5, 'attack': 7, 'defense': 2, 'maintenance': 0},
    },
    'technology_data': {
        'shipsize': [0, 10, 15, 20, 25, 30],
        'attack': [20, 30, 40],
        'defense': [20, 30, 40],
        'movement': [0, 20, 30, 40, 40, 40],
        'shipyard': [0, 20, 30],
        'terraform': [25], 
        'tactics': [15, 20, 30], 
        'exploration': [15]},
    }
    'combat': {}
} #TLDR the last 8 ships of player 2 survive in the 10v10 combat scenario
