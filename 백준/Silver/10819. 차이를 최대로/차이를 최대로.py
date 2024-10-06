import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
m = 0
for p in permutations(list(map(int, input().split())), n):
    value = sum([abs(p[i] - p[i+1]) for i in range(len(p)-1)])
    if m < value:
        m = value

print(m)