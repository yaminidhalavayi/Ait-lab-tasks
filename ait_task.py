from collections import deque

def bfs_recommend(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)

    print("Recommended movies within 3 similarly levels:")
    
    while queue:
        movie, level = queue.popleft()
        
        if level > 3:
            continue
        
        print(f"{movie}, level {level}")

        if level < 3:
            for neighbour in graph.get(movie, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, level + 1))

# Your graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}

start_movie = input("enter starting movie: ").strip().upper()
if start_movie in graph:
    bfs_recommend(graph, start_movie)
else:
    print(f"Movie '{start_movie}' not found. Available: {list(graph.keys())}")
