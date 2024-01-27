import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        c = [str(i) for i in sorted(list(c), reverse=True)]
        answer.append(int(''.join(c)))

answer.sort()

if n < 1023:
    print(answer[n])
else:
    print(-1)