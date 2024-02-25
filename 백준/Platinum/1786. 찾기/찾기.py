import sys
input = sys.stdin.readline

t = input()[:-1]
p = input()[:-1]
pi = [0] * len(p)
i = 0
for j in range(1, len(p)):
    while i > 0 and p[i] != p[j]:
        i = pi[i-1]

    if p[i] == p[j]:
        i += 1
        pi[j] = i

j, count = 0, 0
result = []
for i in range(len(t)):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]
    
    if t[i] == p[j]:
        if j == (len(p) - 1):
            result.append(i - len(p) + 2) # 몇 번째에서 시작하는 지를 나타냄 (인덱스로 X)
            count += 1
            j = pi[j]
        else:
            j += 1

print(count)
print(*result)