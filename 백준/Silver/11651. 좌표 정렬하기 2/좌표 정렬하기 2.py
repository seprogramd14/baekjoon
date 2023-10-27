import sys
input = sys.stdin.readline
T = int(input())
result = []
for t in range(T):
    x, y = list(map(int, input().split()))
    result.append([x, y])

for i in sorted(result, key=lambda x : (x[1], x[0])):
    print(i[0], i[1])