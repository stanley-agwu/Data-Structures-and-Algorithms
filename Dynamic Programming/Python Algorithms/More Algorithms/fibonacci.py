# Fibonacci Sequence

# Brute Force (Recursion)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# O(2 ^ n) - Time complexity
# O(n) - Space complexity


# Memoization (Top-Down DP)
from functools import lru_cache

@lru_cache(None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Alternatively

def fib_memo(n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# O(n) - Time complexity
# O(n) - Space complexity

# Iterative (Bottom Up) Approach -> Best
def fib_i(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# O(n) - Time complexity
# O(1) - Space complexity