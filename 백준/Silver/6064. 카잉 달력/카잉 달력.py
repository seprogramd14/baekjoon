import sys
import math
input = sys.stdin.readline

result = []
for t in range(int(input())):
    m, n, x, y = map(int, input().split())
    
    for i in range(x, math.lcm(m, n)+1, m):
        if (i-1) % n + 1 == y:
            result.append(i)
    
    if len(result) < t+1:
        result.append(-1)
print(*result, sep="\n")
