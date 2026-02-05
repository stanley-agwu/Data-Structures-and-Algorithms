# Bellman Ford Shortest Path Algorithm

import math

def bellman_ford(edges, start, nodes):
    # Initialize distances and predecessors
    distances = {node: math.inf for node in nodes}
    distances[start] = 0

    predecessors = {node: None for node in nodes}
    result = []  # store distance table after each iteration

    # Relaxation for V - 1 iterations
    for _ in range(len(nodes) - 1):
        updated = False  # record if there is an update in this round

        for u, v, weight in edges:
            if distances[u] != math.inf and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u  # record predecessor
                updated = True

        # record each round result
        result.append(distances.copy())

        # if no update in this round, stop early
        if not updated:
            break

    # Detect negative weight cycle
    for u, v, weight in edges:
        if distances[u] != math.inf and distances[u] + weight < distances[v]:
            return "There is a negative weight cycle in the graph."
        
    # distances: shortest distance from start to each node
    # predecessors: previous node on the shortest path
    # result: distance table after each relaxation round
    return distances, predecessors, result


# Let V = nodes -> (number of vertices)
# Let E = edges -> (number of edges)
# O(V.E) - Time complexity
# O(V^2) - Space complexity