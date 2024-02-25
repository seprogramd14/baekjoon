import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
t = input().rstrip()
p = 'I' + ('OI' * n)
pi = [0] * (2 * n + 1)
i = 0

for j in range(1, (2 * n + 1)):
    while i > 0 and p[i] != p[j]:
        i = pi[i-1]

    if p[i] == p[j]:
        i += 1
        pi[j] = i

j, count = 0, 0
for i in range(l):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]

    if t[i] == p[j]:
        if j == ((2 * n + 1) - 1):
            count += 1
            j = pi[j]
        else:
            j += 1

print(count)