# Palindromic Substrings - Leetcode-647-Medium

# Solution-1 -------------------------------------------

s = "aaa"

def countSubstrings(s):
    count = 0
    matrix = []

    for i in range(len(s)):
        matrix.append([0]*len(s))

    for i in range(len(s)):
        matrix[i][i] = 1
        count += 1

    for col in range(1, len(matrix[0])):
        for row in range(len(matrix)-1):
            if row == col-1 and s[col] == s[row]:
                matrix[row][col] = 1
                count += 1
            elif matrix[row+1][col-1] == 1 and s[col] == s[row]:
                matrix[row][col] = 1
                count += 1

    print(matrix)
    print(count)

countSubstrings(s)

