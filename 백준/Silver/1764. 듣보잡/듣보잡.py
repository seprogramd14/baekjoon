import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
S = set()
result = []

for i in range(n):
    name = input().rstrip()
    S.add(name)

for _ in range(m):
    check = input().rstrip()
    if check in S:
        result.append(check)

print(len(result))
for r in sorted(result): # 문제 잘 읽기
    print(r)