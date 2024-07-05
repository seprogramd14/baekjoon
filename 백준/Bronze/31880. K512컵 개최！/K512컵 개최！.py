n, m = map(int, input().split())
plus = list(map(int, input().split()))
res = sum(plus)
for i in list(map(int, input().split())):
    if i:
        res *= i
print(res)