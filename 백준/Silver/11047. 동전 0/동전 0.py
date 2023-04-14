n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = 0
for coin in reversed(coins):
    result += k // coin
    k %= coin
print(result)