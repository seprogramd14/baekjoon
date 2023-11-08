import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n-1], dp[n])