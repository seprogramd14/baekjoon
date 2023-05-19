from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
yo = deque([i for i in range(1, n+1)])
stack = []
for i in range(n):
    if yo:
        for _ in range(k-1):
            yo.append(yo.popleft())
    stack.append(yo.popleft())
print('<', end="")
print(*stack, sep=', ', end="")
print('>')