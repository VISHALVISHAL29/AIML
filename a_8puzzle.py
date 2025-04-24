goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

current_state = [[1, 2, 3],
                 [0, 4, 6],
                 [7, 5, 8]]

def position(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return i, j
    return None

def distance(state):
    d = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                goal_x, goal_y = position(goal, state[i][j])
                d += abs(i - goal_x) + abs(j - goal_y)
    return d

def get_neighbors(state):
    neighbors = []
    blank_x, blank_y = position(state, 0)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in moves:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            neighbors.append(new_state)
    
    return neighbors

def a_star_search(initial_state):
    open_list = [(distance(initial_state), 0, initial_state, [])]  # f(n), g(n), state, path
    visited = set()
    
    while open_list:
        open_list.sort() 
        f, g, state, path = open_list.pop(0)
        
        state_tuple = tuple(tuple(row) for row in state)
        
        if state == goal:
            return path
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        for neighbor in get_neighbors(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                h = distance(neighbor)
                open_list.append((g + 1 + h, g + 1, neighbor, path + [neighbor]))
    
    return None

solution = a_star_search(current_state)
if solution:
    print("Solution path:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
