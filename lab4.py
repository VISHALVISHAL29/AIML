jug1 = 4
jug2 = 5
target = 3


def next_state(state):
    x, y = state
    a = []
    a.append((jug1, y))
    a.append((x, jug2))
    a.append((0, y))
    a.append((x, 0))

    b = min(x, jug2 - y)
    a.append((x - b, y + b))

    c = min(y, jug1 - x)
    a.append((x + c, y - c))

    return a


def absolute(state):
    return abs(state[0] - target) + abs(state[1] - target)


def solve():
    current_state = (0, 0)
    visited_states = set()

    while True:
        print("Current State:", current_state)

        if current_state[0] == target or current_state[1] == target:
            print("Goal Reached:", current_state)
            return

        visited_states.add(current_state)

        next_states = next_state(current_state)
        next_states = [state for state in next_states if state not in visited_states]

        if not next_states:
            print("No new states to explore. Stuck at:", current_state)
            return

        next_state_selected = min(next_states, key=absolute)
        current_state = next_state_selected


solve()
