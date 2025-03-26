import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [100000] * (n+1)
for i in range(1, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[n])