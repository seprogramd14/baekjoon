import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []

def bfs(start):
    queue = deque(graph[start])
    visited = [0] * n

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = 1
            queue.extend(graph[node])
    return visited

for i in range(n):
    graph.append([idx for idx, val in enumerate(list(map(int, input().split()))) if val])

for i in range(n):
    print(*bfs(i))