import sys
sys.path.append("src")
print(sys.path)
from economic_engine import EconomicEngine
from combat_engine import CombatEngine
from movement_engine import MovementEngine
from state import State
sys.path.pop(-1)

import os
rootdir = 'unit_tests'

phases = {}

for subdir, dirs, files in os.walk(rootdir):
    for folder in dirs:
        if folder != '__pycache__':
            phase = list(folder.split('_'))
            if phase[0] not in list(phases.keys()):
                phases[phase[0]] = []
            phases[phase[0]].append(int(phase[2]))



for phase, test_indexs in phases.items():
    for test_index in test_indexs:
        file_path = 'unit_tests\\' + phase + str('_test_') + str(test_index)
        sys.path.append(file_path)
        from initial_state import game_state as initial_state
        from final_state import game_state as testing_final_state
        from strategies import Strategy
        strats = [Strategy, Strategy]

        state = State.from_standard(initial_state, strats)
        if phase == 'economic':
            EconomicEngine.run_phase(state)

        if phase == 'combat':
            CombatEngine.run_phase(state)

        if phase == 'movement':
            MovementEngine.run_phase(state)

        final_state = State.from_standard(testing_final_state, strats)

        assert State.compare_native_states(final_state, testing_final_state), "Tests failed" #his native states doesnt work so i cant see if my method works yet

        print(phase + str('_test_') + str(test_index) + ' Passed!!') 
        sys.path.pop(-1)

