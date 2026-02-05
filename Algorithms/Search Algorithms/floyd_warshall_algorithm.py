# Floyd–Warshall Shortest Path Algorithm

# This is a All-Pairs Shortest Path Algorithm
# It supports negative edge weights.

INF = float("inf")

def floyd_warshall(graph):
    # 1) Initialize distance and next matrices
    n = len(graph)
    dist = [row[:] for row in graph]  # copy adjacency matrix

    # nxt[i][j] = next vertex to go to from i when heading toward j
    nxt = [
        [None if graph[i][j] == INF else j for j in range(n)]
        for i in range(n)
    ]

    # 2) Triple loop to update shortest distances and paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nxt[i][j] = nxt[i][k]

    # 3) Check for negative weight cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Graph contains negative weight cycle")
            return dist, nxt, True

    return dist, nxt, False

# Let n = nodes -> (number of vertices)
# O(n^3) - Time complexity
# O(n^2) - Space complexity

# Sample graph
graph = [
    [0,   4,   3,   INF],
    [INF, 0,   INF, 2],
    [-2,  INF, 0,   5],
    [3,   INF, INF, 0],
]

dist, nxt, has_neg_cycle = floyd_warshall(graph)
print("Has negative cycle?", has_neg_cycle)
print("All-pairs shortest distances:")
for row in dist:
    print(row)
