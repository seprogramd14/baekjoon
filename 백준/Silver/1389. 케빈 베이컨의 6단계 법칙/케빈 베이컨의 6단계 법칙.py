import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited = [0] * (n+1)
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if g != start and not visited[g]:
                visited[g] = visited[node] + 1
                queue.append(g)
    return sum(visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_num = float("INF")
result = 0
for i in range(1, n+1):
    num = bfs(i)
    if min_num > num:
        min_num, result = num, i
print(result)