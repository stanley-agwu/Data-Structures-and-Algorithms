# Fenwick Tree (Binary Indexed Tree) Data Structures

# It's a data structure that efficiently supports cummulative frequency 
# operations, including point updates and range sum queries.

from typing import List, Optional


class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) for prefix sums.

    - 1-indexed internal array: bit[1..n]
    - Supports:
        add(i, delta): add delta to a[i]
        sum(i): prefix sum a[1] + ... + a[i]
        range_sum(l, r): sum a[l] + ... + a[r]
    """

    def __init__(self, arr: Optional[List[int]] = None):
        if arr is None:
            arr = []
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)  # 1-indexed

        # Build (O(n log n))
        for i, num in enumerate(arr, start=1):
            self.add(i, num)

    def add(self, index: int, delta: int) -> None:
        """Add `delta` to position `index` (1-indexed)."""
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index  # add LSB

    def sum(self, index: int) -> int:
        """Return prefix sum from 1..index (1-indexed)."""
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index  # remove LSB
        return res

    def range_sum(self, left: int, right: int) -> int:
        """Return sum from left..right (1-indexed, inclusive)."""
        if left > right:
            return 0
        return self.sum(right) - self.sum(left - 1)

    # Optional convenience helpers
    def get(self, index: int) -> int:
        """Get a[index] (1-indexed)."""
        return self.range_sum(index, index)

    def set(self, index: int, value: int) -> None:
        """Set a[index] = value (1-indexed)."""
        current = self.get(index)
        self.add(index, value - current)


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 5]  # 0-indexed input list
    ft = FenwickTree(arr)

    print(ft.sum(3))            # sum of first 3 elements: 2+1+3 = 6
    print(ft.range_sum(2, 5))   # 1+3+4+5? (positions 2..5) = 13

    ft.add(4, 10)               # a[4] += 10
    print(ft.get(4))            # now a[4] = 14
    print(ft.range_sum(1, 5))   # total sum
