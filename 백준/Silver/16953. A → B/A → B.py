import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append([s, 1])
    while q:
        node, t = q.popleft()
        if node == end:
            return t

        if node * 2 <= end:
            q.append([node*2, t+1])
        
        if int(str(node)+'1') <= end:
            q.append([int(str(node)+'1'), t+1])
    return -1

start, end = map(int, input().split())
print(bfs(start))