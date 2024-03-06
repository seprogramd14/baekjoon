import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    mbti = list(map(str, input().rstrip().split()))
    if n > 32:
        print(0)
    else:
        count = []
        for c in combinations(mbti, 3):
            cnt = 0
            for _c in combinations(c, 2):
                for i in range(4):
                    if _c[0][i] != _c[1][i]:
                        cnt += 1
            count.append(cnt)
        print(min(count))