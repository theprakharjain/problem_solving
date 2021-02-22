# Rotate Image - Leetcode-Medium

# Solution-1 -------------------------------------------

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(matrix)
# Transpose
for i in range(n):
    for j in range(0, i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Reverse
for ele in matrix:
    ele.reverse()

# Solution-2 --------------------------------------------

# reverse
l = 0
r = len(matrix) - 1
while l < r:
    matrix[l], matrix[r] = matrix[r], matrix[l]
    l += 1
    r -= 1

# transpose
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Explanation-----------------------------------------------------
    # ~~~~~~~~~~~
    # We want to rotate
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ->
    # [7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]]

    # We can do this in two steps.
    # Reversing the matrix does this:
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]
    # ->
    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]

    # Transposing means: rows become columns, columns become rows.

    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]
    # ->
    # [7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]
