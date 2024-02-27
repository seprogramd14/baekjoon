n = int(input())
cup = [0] * 4
cup[1] = 1
for _ in range(n):
    x, y = list(map(int, input().split()))
    cup[x], cup[y] = cup[y], cup[x]

print(cup.index(1))