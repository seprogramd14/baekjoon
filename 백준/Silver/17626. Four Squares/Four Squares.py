import sys
import math
input = sys.stdin.readline

n = int(input())

dp = [0]  * 50001

for i in range(1, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + 1
        for j in range(1, int(math.sqrt(i))+1): # 이거는 아직 잘 모르겠다.....
            dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])