import sys
from itertools import permutations, combinations
input = sys.stdin.readline

n = int(input())
num = [i for i in str(n)]
answer = []

for p in permutations(num, len(num)):
    new = int(''.join(p))
    if n < new:
        answer.append(new)

if len(answer):
    print(sorted(answer)[0])
else:
    print(0)