import sys
sys.path.append("src")
from economic_engine import EconomicEngine
from combat_engine import CombatEngine
from movement_engine import MovementEngine
from state import State

del sys.path[-1]


def run_test(phase,folder_name):
    sys.path.append('unit_tests/'+folder_name)
    from initial_state import game_state as state1
    from final_state import game_state as state2
    from strategies import Strategy
    Strategy1 = Strategy
    Strategy2 = Strategy
    print(folder_name)
    state = State.from_standard(state1, [Strategy1, Strategy2])
    if phase == 'Eco':
        EconomicEngine.run_phase(state)
    elif phase == 'Combat':
        CombatEngine.run_phase(state)
    elif phase == 'Move':
        MovementEngine.run_phase(state)
    state2 = State.from_standard(state2, [Strategy1, Strategy2])

    assert State.compare_native_states(state, state2),"Tests failed"

    print("This test passed: Economic Phase 1")


run_test('Move','movement_test_1')
run_test('Combat','combat_test_1')
run_test('Eco','economic_test_1')
run_test('Eco','economic_test_2')