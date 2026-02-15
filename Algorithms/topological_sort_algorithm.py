# Topological Sort with Kahn’s Algorithm

"""
1. Applicable to Directed Acyclic Graphs (DAG)
2. Node → Task, Edge → Dependency
3. Arrow points from predecessor task to successor task

Goal -> Sort tasks according to dependencies.
"""

# Topological Sort implemented using Kahn’s Algorithm (BFS + In-degree method)

from collections import defaultdict, deque

def topological_sort(edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and compute in-degrees
    nodes = set()
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
        nodes.add(u)
        nodes.add(v)

    # Initialize queue with nodes having zero in-degree
    zero_in_degree = deque([node for node in nodes if in_degree[node] == 0])

    topo_order = []

    while zero_in_degree:
        current = zero_in_degree.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # Check for cycles
    if len(topo_order) != len(nodes):
        raise ValueError("Graph has at least one cycle, topological sort not possible.")

    return topo_order

# Let V = Number of nodes, E = Number of Edges
# O(V + E) - Time complexity
# O(V) - Space complexity

edges = [("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]

print(topological_sort(edges))
# Output might be: ['A', 'B', 'C', 'D', 'E', 'F']
