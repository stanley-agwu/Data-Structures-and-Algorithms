# Disjoint Set (Union Find)

# Efficient Data structure for Connected Components
"""
A powerful data structure for tracking elements partitioned
into non-overlapping subsets.

Optimized with:
1. Path Compression and
2. Union by rank or Union by size
"""

# Optimized with Path Compression and Union by size
class DisjointSet:
    def __init__(self, n: int):
        """Initialize n disjoint sets: {0}, {1}, ..., {n-1}."""
        if n <= 0:
            raise ValueError("n must be a positive integer")
        self.parent = list(range(n))
        self.size = [1] * n  # size[root] = number of nodes in that set

    def find(self, x: int) -> int:
        """Return the representative (root) of the set containing x."""
        if self.parent[x] != x:
            # Path compression: make x point directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merge the sets containing x and y.
        Returns True if a merge happened, False if they were already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by size: attach smaller tree under larger tree
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

    def component_size(self, x: int) -> int:
        """Return the size of the set containing x."""
        return self.size[self.find(x)]


# Example usage
if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    print(ds.connected(0, 2))  # True
    print(ds.connected(0, 4))  # False
    ds.union(2, 4)
    print(ds.connected(0, 4))  # True
    print(ds.component_size(0))  # 5


# O(α(n)) - Time complexity - for Find() and Union()
# O(n) - Space complexity


# Optimized with Path Compression and Union by Rank

class DisjointSet2:
    def __init__(self, n: int):
        # parent[i] = parent of i (root nodes have parent[i] == i)
        self.parent = list(range(n))
        # rank[i] = rough upper bound on tree height (used for union by rank)
        self.rank = [0 for _ in range(n)]

    def find(self, x: int) -> int:
        # Path compression: make every node on the path point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Union by rank: attach smaller-rank tree under larger-rank tree
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # already in the same set

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

# O(α(n)) - Time complexity - for Find() and Union()
# O(n) - Space complexity

# Example usage
if __name__ == "__main__":
    ds = DisjointSet(6)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    print(ds.connected(0, 2))  # True
    print(ds.connected(0, 3))  # False
    ds.union(2, 4)
    print(ds.connected(0, 3))  # True
