# Max Area of Land II (Rectangle)

"""
A farmer wants to farm their land with the maximum area where good 
land is present. The “land” is represented as a matrix with 1s and 0s, 
where 1s mean good land and 0s mean bad land. The farmer only want to 
farm in a rectangle of good land with the maximum area. Please help the 
farmer to find the maximum area of the land they can farm in good land.

Example:

0 1 1 0 1
1 1 0 1 0
1 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

"""

# Using Dynamic Programming

def largest_rectangle_of_good_land(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    r, c = len(matrix), len(matrix[0])
    heights = [0] * c
    max_area = 0

    for i in range(r):
        # build histogram of heights for this row
        for j in range(c):
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        # largest rectangle in histogram (heights)
        max_area = max(max_area, _largest_histogram_area(heights))

    return max_area

def _largest_histogram_area(h: list[int]) -> int:
    # monotonic increasing stack of indices
    stack = []
    max_area = 0
    n = len(h)

    for i in range(n + 1):
        cur = 0 if i == n else h[i]  # sentinel 0 to flush stack at end

        while stack and cur < h[stack[-1]]:
            height = h[stack.pop()]
            left_smaller_idx = stack[-1] if stack else -1
            width = i - left_smaller_idx - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

matrix = [
    [0,1,1,0,1],
    [1,1,0,1,0],
    [1,1,1,1,0],
    [1,1,1,1,0],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
print(largest_rectangle_of_good_land(matrix))  # 12
