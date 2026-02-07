# String Edit Distance Algorithm

# Edit Distance
"""
The minimum number of operations required to transform 
one string into another.
"""

# Key Idea -> Dynamic programming

# 1. Brute Force (Recursion)
def edit_dist(s1: str, s2: str) -> int:
    # if one string is empty,
    # return the length of the other
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    # If the first characters are the same,
    # continue with the rest of the strings
    if s1[0] == s2[0]:
        return edit_dist(s1[1:], s2[1:])

    # If the first characters are different,
    # try inserting, deleting, or replacing
    insert = edit_dist(s1, s2[1:])
    delete = edit_dist(s1[1:], s2)
    replace = edit_dist(s1[1:], s2[1:])

    return 1 + min(insert, delete, replace)

# O(n ^ 2) - Time complexity
# O(n) - Space complexity

# 2. Top Down approach (Recursion + Memoization)
def edit_dist_memo(s1: str, s2: str, memo = {}) -> int:
    # Use (s1, s2) as the key to query the cache
    if (s1, s2) in memo:
        return memo[(s1, s2)]

    if not s1:
        memo[(s1, s2)] = len(s2)
        return len(s2)
    if not s2:
        memo[(s1, s2)] = len(s1)
        return len(s1)

    if s1[0] == s2[0]:
        memo[(s1, s2)] = edit_dist_memo(s1[1:], s2[1:], memo)
        return memo[(s1, s2)]

    insert = edit_dist_memo(s1, s2[1:], memo)
    delete = edit_dist_memo(s1[1:], s2, memo)
    replace = edit_dist_memo(s1[1:], s2[1:], memo)

    memo[(s1, s2)] = 1 + min(insert, delete, replace)
    return memo[(s1, s2)]

# Let m, n = len(s1), len(s2)
# O(m . n) - Time complexity
# O(m) - Space complexity

# 3. Bottom-Up Approach (Tabulation method)
def edit_distance_tab(s1, s2):
    m, n = len(s1), len(s2)

    # Initialize a table table
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        table[i][0] = i  # Deletion operation
    for j in range(n + 1):
        table[0][j] = j  # Insertion operation

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]  # Characters match, no operation needed
            else:
                table[i][j] = min(
                    table[i][j - 1] + 1,      # Insertion
                    table[i - 1][j] + 1,      # Deletion
                    table[i - 1][j - 1] + 1   # Replacement
                )

    # Backtrack to find the operations
    i, j = m, n
    operations = []

    while i > 0 or j > 0:
        # Case 1: Characters match, keep
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            operations.append(f"Keep '{s1[i - 1]}'")
            i -= 1
            j -= 1

        # Case 2: Characters differ, perform edit operation
        else:
            # Replacement operation
            if i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + 1:
                operations.append(
                    f"Replace '{s1[i - 1]}' with '{s2[j - 1]}'"
                )
                i -= 1
                j -= 1

            # Insertion operation
            elif j > 0 and table[i][j] == table[i][j - 1] + 1:
                operations.append(f"Insert '{s2[j - 1]}'")
                j -= 1

            # Deletion operation
            elif i > 0 and table[i][j] == table[i - 1][j] + 1:
                operations.append(f"Delete '{s1[i - 1]}'")
                i -= 1

    operations.reverse()

    return table[m][n], table, operations

# Let m, n = len(s1), len(s2)
# O(m . n) - Time complexity
# O(m) - Space complexity

distance, table, steps = edit_distance_with_tab("horse", "ros")

print("Minimum edit distance:", distance)
print("Operations:")
for step in steps:
    print("-", step)


# Example
print(edit_dist("cat", "dog"))  # Outputs 3
