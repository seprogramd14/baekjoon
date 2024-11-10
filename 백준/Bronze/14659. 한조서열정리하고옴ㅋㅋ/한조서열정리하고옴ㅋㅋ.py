n = int(input())
archer = list(map(int, input().split()))
result = []

cp = 0
for i in range(1, n):
    if archer[cp] < archer[i]:
        result.append(i-cp-1)
        cp = i
result.append(n-cp-1)
print(max(result))