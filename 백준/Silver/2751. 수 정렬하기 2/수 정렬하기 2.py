import sys
input = sys.stdin.readline
n = int(input())
ls = [int(input()) for _ in range(n)]
print(*sorted(ls), sep='\n')