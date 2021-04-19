enabled = True

def run():
    from economic_engine import EconomicEngine
    from state import State

    from initial_state import initial_state as state1
    from final_state import final_state as state2
    from strategies import Strategy1, Strategy2

    state = State.from_standard(state1, [Strategy1, Strategy2])
    EconomicEngine.run_phase(state)
    state2 = State.from_standard(state2, [Strategy1, Strategy2])

    return State.compare_native_states(state, state2)

if __name__ == "__main__":
    import sys
    sys.path.append("src")
    run()
