# Segment Tree Data structure

# Segment Tree (Range Sum Query + Point Update)

from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        if not arr:
            raise ValueError("Array must be non-empty.")
        self.n = len(arr)
        self.arr = arr[:]                 # keep a copy
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        self.build(left, start, mid)
        self.build(right, mid + 1, end)
        self.tree[node] = self.tree[left] + self.tree[right]

    def query(self, l: int, r: int) -> int:
        """Return sum(arr[l..r]) inclusive."""
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid query range.")
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # No overlap
        if r < start or end < l:
            return 0

        # Total overlap
        if l <= start and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        return (self._query(left, start, mid, l, r) +
                self._query(right, mid + 1, end, l, r))

    def update(self, idx: int, value: int) -> None:
        """Set arr[idx] = value."""
        if idx < 0 or idx >= self.n:
            raise ValueError("Index out of bounds.")
        self.arr[idx] = value
        self._update(0, 0, self.n - 1, idx, value)

    def _update(self, node: int, start: int, end: int, idx: int, value: int) -> None:
        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        if idx <= mid:
            self._update(left, start, mid, idx, value)
        else:
            self._update(right, mid + 1, end, idx, value)

        self.tree[node] = self.tree[left] + self.tree[right]


# --- Example usage ---
if __name__ == "__main__":
    arr = [2, 1, 5, 3, 4]
    st = SegmentTree(arr)

    print(st.query(1, 3))  # sum of [1,5,3] = 9
    st.update(2, 10)       # arr becomes [2,1,10,3,4]
    print(st.query(1, 3))  # sum of [1,10,3] = 14
