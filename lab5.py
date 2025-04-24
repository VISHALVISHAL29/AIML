import heapq

# Define the goal state
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Define the initial state
INITIAL_STATE = ((1, 2, 3),
                 (0, 4, 6),
                 (7, 5, 8))

# Possible moves for the blank tile (0)
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def position(state, value):
    """Finds the (x, y) position of a value in the matrix."""
    for i, row in enumerate(state):
        if value in row:
            return i, row.index(value)
    return None

def distance(state):
    """Computes the Manhattan distance heuristic."""
    return sum(abs(i - gx) + abs(j - gy)
               for i, row in enumerate(state)
               for j, val in enumerate(row)
               if val and (gx := position(GOAL, val)[0], gy := position(GOAL, val)[1]))

def get_neighbors(state):
    """Generates all possible states by moving the blank tile."""
    neighbors = []
    blank_x, blank_y = position(state, 0)

    for dx, dy in MOVES:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Convert state to a mutable list for swapping
            new_state = [list(row) for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            neighbors.append(tuple(tuple(row) for row in new_state))  # Convert back to tuple

    return neighbors

def best_first_search(initial_state):
    """Implements Best-First Search using Manhattan distance as a heuristic."""
    pq = []
    heapq.heappush(pq, (distance(initial_state), initial_state, []))
    visited = set()

    while pq:
        _, state, path = heapq.heappop(pq)
        
        if state == GOAL:
            return path
        
        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (distance(neighbor), neighbor, path + [neighbor]))

    return None

# Run the search
solution = best_first_search(INITIAL_STATE)

# Output the solution path
if solution:
    print("Solution path:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
