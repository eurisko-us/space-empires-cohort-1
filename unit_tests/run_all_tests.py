import sys
sys.path.append("src")
from economic_engine import EconomicEngine
from combat_engine import CombatEngine
from movement_engine import MovementEngine
from state import State

del sys.path[-1]




def run_test(phase,folder_name):
    sys.path.append('unit_tests/'+folder_name)
    from initial_state import game_state as initial_test_state
    from final_state import game_state as final_state
    from strategies import Strategy1
    from strategies import Strategy2
    Strategy_1 = Strategy1
    Strategy_2 = Strategy2
    print(folder_name)
    current_state = State.from_standard(initial_test_state, [Strategy_1, Strategy_2])

    if phase == 'economic':
        EconomicEngine.run_phase(current_state)
    elif phase == 'combat':
        CombatEngine.run_phase(current_state)
    elif phase == 'movement':
        MovementEngine.run_phase(current_state)

    final_test_state = State.from_standard(final_state, [Strategy_1, Strategy_2])

    # current_state = State.from_standard(current_state, [Strategy_1, Strategy_2])

    assert State.compare_native_states(current_state, final_test_state),"bad test boi"
    print('passsed')


# run_test('movement','movement_test_1')
# run_test('combat','combat_test_1')
# run_test('economic','economic_test_1')
# run_test('economic','economic_test_2') 