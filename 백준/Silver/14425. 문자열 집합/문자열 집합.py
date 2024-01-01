import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
S = set()

for _ in range(n):
    s = input().rstrip()
    S.add(s)

count = 0
for _ in range(m):
    s = input().rstrip()
    if s in S:
        count += 1

print(count)