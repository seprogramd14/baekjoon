import sys
from itertools import permutations
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ls = [i for i in range(1, n+1)]

def check(lis):
    for i in range(1, len(lis)):
        if lis[i-1] >= lis[i]:
            return False
    return True

for p in permutations(ls, m):
    if check(p):
        print(*list(p))