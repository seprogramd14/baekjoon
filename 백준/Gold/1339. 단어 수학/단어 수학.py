import sys
input = sys.stdin.readline

n = int(input())
alpha = [input().rstrip() for _ in range(n)]
check = dict()

for al in alpha:
    l = len(al) - 1
    for a in al:
        if a not in check.keys():
            check[a] = 10**l
        else:
            check[a] += 10**l
        l -= 1

value = sorted(list(check.values()), reverse=True)
result, c = 0, 9

for v in value:
    result += v * c
    c -= 1
print(result)