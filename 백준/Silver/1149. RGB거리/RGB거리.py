import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
cost = [[0] * 3 for _ in range(n)]
cost[0] = rgb[0].copy()

for i in range(1, n):
    for j in range(3):
        num = 0
        if j == 0:
            num = min(cost[i-1][1] + rgb[i][j], cost[i-1][2] + rgb[i][j])
        elif j == 1:
            num = min(cost[i-1][0] + rgb[i][j], cost[i-1][2] + rgb[i][j])
        else:
            num = min(cost[i-1][0] + rgb[i][j], cost[i-1][1] + rgb[i][j])
        cost[i][j] = num
print(min(cost[-1]))