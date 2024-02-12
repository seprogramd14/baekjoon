import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
check = [0] * n
check[0] = 1

for i in range(1, n):
    bu = list()
    for j in range(i):
        if ls[j] < ls[i]:
            bu.append(check[j])
    if bu:
        check[i] = max(bu) + 1
    else:
        check[i] = 1

print(max(check))