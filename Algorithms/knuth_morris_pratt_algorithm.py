# Knuth–Morris–Pratt Algorithm

# Knuth–Morris–Pratt Algorithm For Pattern Matching
# Including the LPS (Longest Prefix Suffix) table construction and the search routine

from typing import List

def build_lps_table(pattern: str) -> List[int]:
    """
    Build LPS array where table[i] = length of the longest proper prefix of pattern[0..i]
    which is also a suffix of pattern[0..i].

    Time:  O(m)
    Space: O(m)
    """
    m = len(pattern)
    table = [0] * m

    # length of the previous longest prefix suffix
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            table[i] = length
            i += 1
        else:
            if length != 0:
                # fall back in the pattern using LPS table
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1

    return table


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Return all starting indices where pattern occurs in text using KMP.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        # By convention, empty pattern matches at every position
        return list(range(n + 1))

    table = build_lps_table(pattern)
    matches = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                # match found, record start index
                matches.append(i - j)
                # continue searching for next match
                j = table[j - 1]
        else:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1

    return matches

# O(n + m) - Time complexity
# O(m) - Space complexity - (for the LPS table)

if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    print(kmp_search(text, pattern))  # [10]
