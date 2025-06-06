import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 1]

for i in range(2, n+1):
    dp.append(sum([dp[j]*dp[i-j-1] for j in range(i)]))
print(dp[n])