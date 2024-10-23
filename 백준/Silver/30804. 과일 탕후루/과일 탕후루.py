import sys
input = sys.stdin.readline

n = int(input())
tanghuru = list(map(int, input().split()))
result = []

dis = [float('inf')] * 10
fruit = set()
left, right = 0, 0
while right < n:
    fruit.add(tanghuru[right])
    dis[tanghuru[right]] = right
    if len(fruit) > 2:
        fruit.clear()
        fruit.add(tanghuru[right])
        result.append(right - left)
        right -= 1
        left = min(dis) + 1
        dis = [float('inf')] * 10
    else:
        right += 1
result.append(right-left)
print(max(result))