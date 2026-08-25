import random

dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 28],
    [20, 25, 30, 0, 12],
    [25, 17, 28, 12, 0]
]
n = 5
pheromone = [[1.0]*n for _ in range(n)]

alpha = 1.0 # pheromone importance
beta = 2.0 # distance importance
evaporation = 0.5

best_cost = float('inf')
best_path = None

for iteration in range(100):
    path = [0]
    visited = {0}
    cost = 0

    while len(path) < n:
        curr = path[-1]
        # calculate probabilities for unvisited
        probs = []
        cities = []
        total = 0
        for j in range(n):
            if j not in visited:
                tau = pheromone[curr][j] ** alpha
                eta = (1.0 / dist[curr][j]) ** beta
                total += tau * eta
                probs.append(tau * eta)
                cities.append(j)

        # roulette wheel selection
        r = random.random() * total
        cum = 0
        for idx, prob in enumerate(probs):
            cum += prob
            if cum >= r:
                next_city = cities[idx]
                break
        else:
            next_city = cities[-1]

        path.append(next_city)
        visited.add(next_city)
        cost += dist[curr][next_city]

    cost += dist[path[-1]][path[0]]

    # pheromone update
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)

    for i in range(n-1):
        pheromone[path[i]][path[i+1]] += 1.0 / cost
    pheromone[path[-1]][path[0]] += 1.0 / cost

    if cost < best_cost:
        best_cost = cost
        best_path = path

print(f"Best Path: {best_path} -> {best_path[0]}")
print(f"Best Cost: {best_cost}")
