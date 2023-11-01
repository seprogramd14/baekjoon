import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

avg = sorted([int(input()) for i in range(n)])
mode = Counter(avg).most_common()

print(round(sum(avg) / len(avg)))
print(avg[len(avg)//2])
print(mode[0][0] if len(mode) == 1 or mode[0][1] != mode[1][1] else mode[1][0])
print(avg[-1] - avg[0])