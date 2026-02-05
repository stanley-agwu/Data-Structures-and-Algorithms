# Dijkstra's Shortest Path Algorithm

import heapq

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    # Initialize shortest path dictionary
    shortest_paths = {vertex: float("inf") for vertex in graph}
    shortest_paths[start] = 0  # Set the start vertex distance to 0

    # Record the predecessor nodes for backtracking the shortest path
    predecessors = {vertex: None for vertex in graph}

    # Priority queue, stores (current distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if greater than the recorded shortest path
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Iterate through neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update shortest path and predecessor if a shorter path is found
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, predecessors

# Let V = nodes -> (number of vertices)
# Let E = edges -> (number of edges)
# Binary Heap -> Time complexity
# Extract -> O(V.log V) - Insert -> O(E.log V) - Overall -> O((E  +V).log V) 
# O(V) - Space complexity

# NOTE -> Dijkstra Algorithm does not work for Graphs with negative edge weights.
# For Graphs with negative Edge Weights, the Bellman-Ford Algorithm, should be used.

# Example graph
graph = {
    "A": {"B": 4, "C": 5},
    "B": {"A": 4, "C": 11, "D": 9, "E": 7},
    "C": {"A": 5, "B": 11, "E": 3},
    "D": {"B": 9, "E": 13, "F": 2},
    "E": {"B": 7, "C": 3, "D": 13, "F": 6},
    "F": {"D": 2, "E": 6},
}

# Calculate the shortest path from A to all nodes
shortest_paths, predecessors = dijkstra(graph, "A")

# Print the shortest paths
print("Shortest paths from A:")
for vertex, distance in shortest_paths.items():
    print(f"A -> {vertex}: {distance}")

# Print the predecessors
print("Predecessors:")
for vertex, predecessor in predecessors.items():
    print(f"{vertex}: {predecessor}")

# Backtrack the shortest path from A to F
def reconstruct_path(predecessors, start, end):
    path = []
    while end:
        path.append(end)
        end = predecessors[end]
    return path[::-1] if path[-1] == start else []

# Print the shortest path from A to F
print("Shortest path from A to F:", reconstruct_path(predecessors, "A", "F"))
