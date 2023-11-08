import sys
from math import *
input = sys.stdin.readline

jewel = int(input())
result = []
for i in range(2, ceil(sqrt(jewel))+1):
    while jewel % i == 0:
        result.append(i)
        jewel //= i

if jewel != 1:
    result.append(jewel)

print(len(result))
print(*result)