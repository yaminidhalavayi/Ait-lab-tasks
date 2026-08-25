def is_safe(vertex, color, graph, colors):
    # Check if any adjacent vertex has same color
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

def graph_coloring(vertex, graph, colors, m):
    if vertex == len(graph):
        return True

    for color in range(1, m+1):
        if is_safe(vertex, color, graph, colors):
            colors[vertex] = color

            if graph_coloring(vertex+1, graph, colors, m):
                return True

            colors[vertex] = 0 # Backtrack
    return False

# Your graph from note
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

m = 3 # 3 zones / colors
colors = [0] * len(graph)

if graph_coloring(0, graph, colors, m):
    print("Valid seating arrangement")
    for i, color in enumerate(colors):
        print(f"Group {chr(65+i)} -> Zone {color}")
else:
    print("No valid arrangement exists")
