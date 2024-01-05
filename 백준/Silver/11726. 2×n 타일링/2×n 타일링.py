import sys
input = sys.stdin.readline

dp = [1, 2]

n = int(input())

for i in range(n-2):
    dp.append(dp[-1] + dp[-2])
print(dp[n-1]% 10007)