# Prim's Algorithm for Minimum Spanning Tree

import heapq
from collections import defaultdict

def prim(edges):
    # Build adjacency list
    graph = defaultdict(list)
    nodes = set()
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
        nodes.update([u, v])

    visited = set()
    mst = []
    total_weight = 0
    min_heap = []

    # Choose any starting point (here we choose edges[0][0])
    start = edges[0][0]
    visited.add(start)
    for weight, neighbor in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap and len(mst) < len(nodes) - 1:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for next_weight, neighbor in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, neighbor))

    return mst, total_weight

# Complexity Analysis
"""
Let:
- V = number of vertices (nodes)
- E = number of edges

# Time Complexity
- Building adjacency list: O(E)
- Heap operations (push + pop for edges): O(E log E)

Overall:
O(E log E) ≈ O(E log V)

# Space Complexity
- Adjacency list: O(V + E)
- Min-heap: O(E)
- Visited set + MST storage: O(V)

Overall:
O(V + E)
"""

# Example usage:
edges = [
    ("A", "B", 2),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 4),
    ("C", "D", 5),
    ("C", "E", 6),
    ("D", "E", 2),
    ("D", "F", 3),
    ("E", "F", 4),
]

mst, total = prim(edges)

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print(f"Total weight: {total}")