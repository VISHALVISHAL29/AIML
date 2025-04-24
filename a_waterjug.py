jug1 = 4
jug2 = 5
goal = 3

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

def heuristic(state):
    return abs(state[0] - goal) + abs(state[1] - goal)

def solve():
    open_list = []
    open_list.append((0 + heuristic((0, 0)), (0, 0), 0))  
    visited_states = set()

    while open_list:
        open_list.sort() 
        f, current_state, g = open_list.pop(0)
        
        print(current_state)

        if current_state[0] == goal or current_state[1] == goal:
            print("Goal Reached!", current_state)
            return
        
        visited_states.add(current_state)
        next_states = next_state(current_state)

        for state in next_states:
            if state in visited_states:
                continue
            next_g = g + 1
            h = heuristic(state)
            next_f = next_g + h
            open_list.append((next_f, state, next_g))
    
    print("No solution found!")

solve()
