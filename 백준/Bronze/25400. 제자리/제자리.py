n = int(input())
ls = list(map(int, input().split()))
fix, r = 0, 0
for i in range(1, n+1):
    if len(ls) <= fix:
        break
    while ls[fix] != i:
        del ls[fix]
        if len(ls) == fix:
            break
    fix += 1
print(n - len(ls))