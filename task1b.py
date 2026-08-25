def dfs(graph, movie, visited):
    visited.add(movie)
    print(movie)
    for neighbour in graph[movie]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# Your graph from the note
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"] # you missed this in this page, added it
}

start_movie = input("Enter starting movie: ").strip().upper()
visited = set()

print(f"movies connected to {start_movie}:")
if start_movie in graph:
    dfs(graph, start_movie, visited)
    print("\nResult: Thus the program depth first search and traversed all movies connected to the selected movie is implemented successfully")
else:
    print(f"Movie {start_movie} not in graph")
