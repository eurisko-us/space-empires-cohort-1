enabled = False

def run():
    from movement_engine import MovementEngine
    from state import State

    from initial_state import game_state as state1
    from final_state import game_state as state2
    from strategies import Strategy
    state = State.from_standard(state1, [Strategy, Strategy])
    MovementEngine.run_phase(state)
    state2 = State.from_standard(state2, [Strategy, Strategy])

    return State.compare_native_states(state, state2)

if __name__ == "__main__":
    import sys
    sys.path.append("src")
    print(run())
