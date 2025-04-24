jug1 = 4
jug2 = 4
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

def heuristic(state):
    return abs(state[0] - target) + abs(state[1] - target)

def push(queue, item):
    queue.append(item)
    queue.sort()

def pop(queue):
    return queue.pop(0)

def solve():
    initial_state = (0, 0)
    pq = []
    push(pq, (heuristic(initial_state), 0, initial_state))
    visited_states = set()
    
    while pq:
        _, cost, current_state = pop(pq)
        
        if current_state in visited_states:
            continue
        
        print("Current State:", current_state)
        visited_states.add(current_state)
        
        if current_state[0] == target or current_state[1] == target:
            print("Goal Reached:", current_state)
            return
        
        for state in next_state(current_state):
            if state not in visited_states:
                push(pq, (cost + heuristic(state), cost + 1, state))
    
    print("No solution found")

solve()
