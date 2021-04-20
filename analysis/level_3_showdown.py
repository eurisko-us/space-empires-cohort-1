import sys
import random

sys.path.append('src')
sys.path.append('tests')
sys.path.append('src/strategies/level_3')

from game import Game
from player import Player

# from colby_strategy import ColbySiegeStrategyLevel3 as ColbyStrategyLevel3
# from david_strategy import DavidStrategyLevel3
# from elijah_strategy import ElijahStrategyLevel3
from george_strategy_level_3 import GeorgeStrategyLevel3
from numbers_berserker import NumbersBerserkerLevel3
from riley_strategy_level_3 import RileyStrategyLevel3


print("Playing games...")

def matchup(type1, type2):
    print(f"\n {type1.__name__} vs {type2.__name__}")
    wins = [0, 0, 0]
    games = 50
    winlog = False
    strats = [type1, type2]
    for i in range(games):
        if i == games//2:
            strats.reverse()
        random.seed(i+1)
        log = i in []
        # log = True
        game = Game((7, 7), game_level=3, die_size=10)
        game.start(strats)

        if game.run_until_completion(max_turns=100):
            if winlog: print(type(game.winner.strat).__name__, i)
            wins[[type1, type2].index(type(game.winner.strat))] += 1
        else:
            if winlog: print("tie", i)
            wins[2] += 1

        if log:
            input()
    wins = [w/games for w in wins]
    return wins

# I had to change colby's strategy
# print(matchup(ColbyStrategyLevel3, GeorgeStrategyLevel3))
# print(matchup(ColbyStrategyLevel3, RileyStrategyLevel3))
# print(matchup(ColbyStrategyLevel3, ElijahStrategyLevel3))
# print(matchup(ColbyStrategyLevel3, DavidStrategyLevel3))

# print(matchup(GeorgeStrategyLevel3, RileyStrategyLevel3))
# print(matchup(GeorgeStrategyLevel3, ElijahStrategyLevel3))
# print(matchup(GeorgeStrategyLevel3, DavidStrategyLevel3))

# print(matchup(RileyStrategyLevel3, ElijahStrategyLevel3))
# print(matchup(RileyStrategyLevel3, DavidStrategyLevel3))

# print(matchup(DavidStrategyLevel3, ElijahStrategyLevel3))

# print(matchup(NumbersBerserkerLevel3, ColbyStrategyLevel3))
# print(matchup(NumbersBerserkerLevel3, GeorgeStrategyLevel3))
# print(matchup(NumbersBerserkerLevel3, RileyStrategyLevel3))

print(matchup(NumbersBerserkerLevel3, ElijahStrategyLevel3))
# print(matchup(NumbersBerserkerLevel3, DavidStrategyLevel3))
