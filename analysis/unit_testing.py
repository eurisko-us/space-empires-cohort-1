import sys
sys.path.append("src")
from economic_engine import EconomicEngine
from combat_engine import CombatEngine
from movement_engine import MovementEngine
from state import State
del sys.path[-1]
sys.path.append('unit_tests')
from economic_test_1.initial_state import initial_state as eco_init_1
from economic_test_1.final_state import final_state as eco_fin_1
from economic_test_1.strategies import Strategy1 as eco_strat1_1
from economic_test_1.strategies import Strategy2 as eco_strat2_1

from economic_test_2.initial_state import game_state as eco_init_2
from economic_test_2.final_state import game_state as eco_fin_2
from economic_test_1.strategies import Strategy1 as eco_strat1_2
from economic_test_1.strategies import Strategy2 as eco_strat2_2

from movement_test_1.initial_state import game_state as mov_init_1
from movement_test_1.final_state import game_state as mov_fin_1
from movement_test_1.strategies import Strategy as mov_strat_1

# from combat_test_2.initial_state import initial_state as com_init_2
# from combat_test_2.final_state import final_state as com_fin_2
# from combat_test_2.strategies import Strategy1 as com_strat1_2
# from combat_test_2.strategies import Strategy2 as com_strat2_2

def run_test(init_state,fin_state,strat1,strat2):
    phase=init_state["phase"]
    strat_1 = strat1
    strat_2 = strat2
    state = State.from_standard(init_state, [strat_1, strat_2])
    if phase == 'Economic':
        EconomicEngine.run_phase(state)
    elif phase == 'Combat':
        CombatEngine.run_phase(state)
    elif phase == 'Movement':
        MovementEngine.run_phase(state)
    state2 = State.from_standard(fin_state, [strat_1, strat_2])

    assert State.compare_native_states(state, state2),"Tests failed"

    print("Passed")

print("Economic test 1")
run_test(eco_init_1,eco_fin_1,eco_strat1_1,eco_strat2_1)
# print("Economic test 2")
# run_test(eco_init_2,eco_fin_2,eco_strat1_2,eco_strat2_2)
print("Movement test 1")
run_test(mov_init_1,mov_fin_1,mov_strat_1,mov_strat_1)
