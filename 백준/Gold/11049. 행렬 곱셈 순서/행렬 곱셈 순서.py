import sys
input = sys.stdin.readline

matrix_num = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_num)]
matrix = matrix[0] + [m[1] for m in matrix[1:]]

dp = [[0]*matrix_num for _ in range(matrix_num)]

for iter in range(1, matrix_num):
    for row in range(matrix_num-iter):
        col = iter + row
        dp[row][col] = 2**32
        for k in range(row, col):
            dp[row][col] = min(dp[row][col], dp[row][k]+dp[k+1][col] + matrix[row]*matrix[k+1]*matrix[col+1])
print(dp[0][matrix_num-1])