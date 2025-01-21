import sys
from collections import Counter
input = sys.stdin.readline

land = int(input())
for _ in range(land):
    ls = list(map(int, input().split()))
    num, t = ls[0], Counter(ls[1:])
    check = [k for k in t if num//2 < t[k]]
    if check:
        print(check[0])
    else:
        print("SYJKGW")