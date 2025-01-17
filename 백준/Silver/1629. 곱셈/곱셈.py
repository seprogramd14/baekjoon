import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

res = 1
while b > 0:
    if b % 2 == 1:
        res = a*res % c
    b //= 2
    a = a*a % c
print(res)
