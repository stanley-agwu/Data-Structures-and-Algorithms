# Kruskal's Algorithm for Minimum Spanning Tree

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # for union by rank

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal(indexed_edges, num_nodes):
    """
    Kruskal's algorithm implementation for indexed nodes
    """
    uf = UnionFind(num_nodes)
    indexed_edges.sort()
    mst = []
    total_weight = 0

    for weight, u, v in indexed_edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == num_nodes - 1:
                break

    return mst, total_weight


def prepare_indexed_graph(edges):
    """
    Input a list of edges in the form (weight, str_node_u, str_node_v),
    output indexed edges, number of nodes, and string-to-index mapping.
    """
    nodes = set()
    for _, u, v in edges:
        nodes.add(u)
        nodes.add(v)

    node_to_index = {node: idx for idx, node in enumerate(sorted(nodes))}
    index_to_node = {idx: node for node, idx in node_to_index.items()}
    indexed_edges = [(w, node_to_index[u], node_to_index[v]) for w, u, v in edges]

    return indexed_edges, len(nodes), node_to_index, index_to_node


def restore_mst_labels(mst_indexed, index_to_node):
    """
    Convert MST from indexed form to labeled form.
    """
    return [(index_to_node[u], index_to_node[v], w) for u, v, w in mst_indexed]

### Time Complexity (Kruskal + Union-Find)
"""
Let:
- V = number of vertices
- E = number of edges

#### 1. Sorting edges
- indexed_edges.sort()
- Complexity: O(E log E)

#### 2. Union-Find operations
- Each edge → at most 1 union + 2 finds
- With path compression + union by rank:
  - Amortized per operation: O(α(V)) (inverse Ackermann, ~ constant)

- Total:
  O(E · α(V))

#### 3. Building mappings (preprocessing)
- Collect nodes: O(E)
- Sorting nodes: O(V log V)
- Creating indexed edges: O(E)

---

### Overall Time Complexity
O(E log E + E · α(V) + V log V)

Dominant term:
O(E log E) ≈ O(E log V)

---

### Space Complexity
- Union-Find arrays: O(V)
- Edge list: O(E)
- Mappings (node_to_index, index_to_node): O(V)
- MST storage: O(V)

Overall:
O(V + E)
"""

# Example graph
edges = [
    (7, "A", "B"),
    (1, "A", "C"),
    (5, "B", "C"),
    (6, "B", "D"),
    (3, "C", "D"),
    (4, "C", "E"),
    (2, "D", "E"),
]

# Preprocess → Execute Kruskal → Restore labels
indexed_edges, num_nodes, node_to_index, index_to_node = prepare_indexed_graph(edges)
mst_indexed, total = kruskal(indexed_edges, num_nodes)
mst_labeled = restore_mst_labels(mst_indexed, index_to_node)

# Output result
print("MST edges:")
for u, v, w in mst_labeled:
    print(f"{u} - {v} (weight: {w})")

print(f"Total weight: {total}")