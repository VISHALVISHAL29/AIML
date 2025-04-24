from collections import deque

a = [[0, 2, 33, 4],
     [93, 0, 34, 8],
     [42, 11, 0, 14],
     [13, 19, 15, 0]]

n = len(a)
start_node = 0
bfs = deque([(start_node, [start_node])])
paths = []

while bfs:
    city, path = bfs.popleft()
    
    if len(path) == n:
        cost = 0
        for i in range(len(path) - 1):
            cost += a[path[i]][path[i + 1]]
        cost += a[path[-1]][start_node]
        
        paths.append((path + [start_node], cost))
        print(f" {path + [start_node]} - {cost}")
    
    else:
        for neighbor in range(n):
            if neighbor not in path:
                bfs.append((neighbor, path + [neighbor]))

if paths:
    best_path, min_cost = min(paths, key=lambda x: x[1])
    print(f"\nBest Path: {best_path} - {min_cost}")
