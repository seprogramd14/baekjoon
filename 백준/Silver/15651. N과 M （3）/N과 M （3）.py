import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def rec(n, ls):
    for i in range(n):
        if len(ls) == m-1:
            print(*(ls+[i+1]))
        else:
            rec(n, ls+[i+1])

rec(n, [])