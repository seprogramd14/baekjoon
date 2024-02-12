import sys
import heapq
input = sys.stdin.readline

n, k = list(map(int, input().split()))
gems = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
result, i = 0, 0
money = []

for bag in bags:
    while i < n and gems[i][0] <= bag:
        heapq.heappush(money, -gems[i][1])
        i += 1
    if money:
        result -= heapq.heappop(money)
print(result)