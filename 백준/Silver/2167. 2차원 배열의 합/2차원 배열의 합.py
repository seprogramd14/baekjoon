import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = [list(map(int, input().split())) for _ in range(n)]
pre_num = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        pre_num[i][j] = pre_num[i-1][j] + pre_num[i][j-1] + num[i-1][j-1] - pre_num[i-1][j-1]

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(pre_num[x2][y2] + pre_num[x1-1][y1-1] - pre_num[x1 - 1][y2] - pre_num[x2][y1 - 1])