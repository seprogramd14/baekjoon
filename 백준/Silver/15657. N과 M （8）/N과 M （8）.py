import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = sorted(list(map(int, input().split())))
ls = []

def backtrack(start):
    if len(ls) == m:
        print(*ls)
        return
    for i in range(start, n):
        ls.append(num[i])
        backtrack(i)
        ls.pop()

backtrack(0)