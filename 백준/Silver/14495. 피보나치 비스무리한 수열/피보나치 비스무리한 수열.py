import sys
input = sys.stdin.readline

dp = [1]*3
n = int(input())

for i in range(3, n):
    dp.append(dp[i-1] + dp[i-3])
print(dp[n-1])