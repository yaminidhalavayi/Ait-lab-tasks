

cities = ['A', 'B', 'C', 'D', 'E']
dist = [ [0, 10, 15, 20, 25],
         [10, 0, 35, 25, 17],
         [15, 35, 0, 30, 28],
         [20, 25, 30, 0, 12],
         [25, 17, 28, 12, 0], ]

def cost(route):
    return sum(dist[route[i]][route[(i+1) % 5]] for i in range(5))

route = [0, 1, 2, 3, 4]

for _ in range(50):
    improved = False
    for i in range(1, 5):
        for j in range(i+1, 5):
            new = route[:]
            new[i], new[j] = new[j], new[i] # swap 2 cities

            # if new route is better, take it
            if cost(new) < cost(route):
                route = new
                improved = True
                break
        if improved:
            break
    if not improved: # no better neighbour found
        break

# Final result
print("Best route:", [cities[i] for i in route], "->", cities[route[0]])
print("Total distance:", cost(route))
