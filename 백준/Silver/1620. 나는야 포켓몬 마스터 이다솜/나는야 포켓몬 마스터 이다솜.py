import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
encyc = dict()

for i in range(n):
    name = input().rstrip()
    encyc[str(i+1)] = name
    encyc[name] = str(i+1)

for _ in range(q):
    check = input().rstrip()
    print(encyc[check])