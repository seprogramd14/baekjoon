import sys
input = sys.stdin.readline

n = int(input())
grape = [int(input()) for _ in range(n)]
dp = [0, grape[0], sum(grape[:2])]

for i in range(3, n+1):
    dp.append(max([dp[i-1], dp[i-2]+grape[i-1], dp[i-3]+grape[i-2]+grape[i-1]]))
print(dp[n])