import sys
input = sys.stdin.readline

n = int(input())
for t in range(n):
    n, m, k, D = map(int, input().split())
    a, b = m*(m-1)*k, (n-1)*m*m
    B = D // (a+b)
    if B == 0:
        print(-1)
    else:
        print((a+b)*B)