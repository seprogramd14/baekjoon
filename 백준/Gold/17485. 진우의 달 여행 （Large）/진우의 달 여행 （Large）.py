import sys
input = sys.stdin.readline
inf = float('inf')

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]
dp = [[[inf] + [0 for _ in range(m)] + [inf] for _ in range(n+1)] for _ in range(3)]

for i in range(n):
    for j in range(m):
        dp[0][i+1][j+1] = fuel[i][j] + min(dp[1][i][j+1], dp[2][i][j+2])
        dp[1][i+1][j+1] = fuel[i][j] + min(dp[0][i][j], dp[2][i][j+2])
        dp[2][i+1][j+1] = fuel[i][j] + min(dp[0][i][j], dp[1][i][j+1])

ls = []
for k in range(3):
    ls.append(min(dp[k][-1]))
print(min(ls))