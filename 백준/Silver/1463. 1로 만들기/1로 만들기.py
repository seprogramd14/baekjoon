n = int(input())

check = dict()
check[1] = 0

for i in range(2, n+1):
    ls = [check[i-1]]
    if i % 3 == 0:
        ls.append(check[i//3])
    if i % 2 == 0:
        ls.append(check[i//2])
    
    check[i] = min(ls) + 1

    if i == 2 or i == 3:
        check[i] = 1

print(check[n])