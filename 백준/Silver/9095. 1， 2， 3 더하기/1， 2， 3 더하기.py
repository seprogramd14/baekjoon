import sys
input = sys.stdin.readline

n = int(input())

check = dict()
check[1] = 1
check[2] = 2
check[3] = 4

for _ in range(n):
    num = int(input())
    for i in range(4, num+1):
        if num in check.keys():
            break
        check[i] = check[i-1] + check[i-2] + check[i-3]
    print(check[num])