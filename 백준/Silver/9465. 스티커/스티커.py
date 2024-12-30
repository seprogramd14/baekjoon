import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]

    for i in range(1, n):
        for r in range(2):
            dp[r][i] = max(dp[1-r][i-1] + stickers[r][i], dp[r][i-1])
    print(max(dp[0][-1], dp[1][-1]))