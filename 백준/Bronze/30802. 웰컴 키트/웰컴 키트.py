import math

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum([math.ceil(s / t) for s in size]))
print(n // p, n % p)