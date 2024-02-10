import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls_sort = sorted(ls)
result = [0] * n

for i in range(n):
    idx = ls.index(ls_sort[i])
    result[idx], ls[idx] = i, 0

print(*result)