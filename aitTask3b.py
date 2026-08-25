import heapq

# Your graph from note
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'F': 5},
    'D': {'G': 2},
    'F': {'G': 4},
    'G': {}
}

# Heuristic value h(n) - from your note
h = {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'F': 4, 'G': 0}

def astar(start, goal):
    q = [(h[start], 0, start, [])] # (f = g+h, g=cost, node, path)
    visited = set()

    while q:
        f, cost, node, path = heapq.heappop(q)
        path = path + [node]

        if node == goal:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for n, d in graph[node].items():
            new_cost = cost + d
            f_value = new_cost + h[n]
            heapq.heappush(q, (f_value, new_cost, n, path))

    return None, 0

# --- Main ---
start = 'A'
goal = 'G'
path, cost = astar(start, goal)

print(f"Path: {' -> '.join(path)}")
print(f"Total Cost: {cost}")
