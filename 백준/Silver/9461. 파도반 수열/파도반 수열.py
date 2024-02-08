import sys
input = sys.stdin.readline

t = int(input())
ls = [int(input()) for _ in range(t)]

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for i in range(6, max(ls) + 1):
    dp[i] = dp[i-1] + dp[i-5]

for l in ls:
    print(dp[l])