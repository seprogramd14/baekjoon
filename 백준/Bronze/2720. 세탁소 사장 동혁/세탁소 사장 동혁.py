import sys
input = sys.stdin.readline

cent = [25, 10, 5, 1]
t = int(input())

for _ in range(t):
    result = []
    n = int(input())
    for c in cent:
        result.append(n // c)
        n %= c
    print(*result)