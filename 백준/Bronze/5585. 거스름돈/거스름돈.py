n = int(input())
n = 1000 - n
money = [500, 100, 50, 10, 5, 1]
cut = 0
for i in money:
    cut += n // i
    n %= i
print(cut)