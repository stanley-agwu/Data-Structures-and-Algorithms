# Max Area of Land

"""
A farmer wants to farm their land with the maximum area where good 
land is present. The “land” is represented as a matrix with 1s and 0s, 
where 1s mean good land and 0s mean bad land. The farmer only want to 
farm in a square of good land with the maximum area. Please help the 
farmer to find the maximum area of the land they can farm in good land.

Example:

0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

"""

# Using Dynamic Programming
def max_good_land_square_area(matrix):
    if not matrix or not matrix[0]:
        return 0

    r, c = len(matrix), len(matrix[0])
    table = [[0] * (c + 1) for _ in range(r + 1)]
    max_side = 0

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if matrix[i - 1][j - 1] == 1:
                table[i][j] = 1 + min(
                    table[i - 1][j],     # top
                    table[i][j - 1],     # left
                    table[i - 1][j - 1]  # top-left
                )
                max_side = max(max_side, table[i][j])
    return max_side * max_side

matrix = [
    [0,1,1,0,1],
    [1,1,0,1,0],
    [1,1,1,1,0],
    [1,1,1,1,0],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
print(max_good_land_square_area(matrix))  # 9