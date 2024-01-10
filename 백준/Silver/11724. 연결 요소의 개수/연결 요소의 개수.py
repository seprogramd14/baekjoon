import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = []

for _ in range(m):
    f, s = list(map(int, input().split()))
    graph[f].append(s)
    graph[s].append(f)

def bfs(graph, s):
    queue = deque([s])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

count = 0
for i in range(1, n+1):
    if i not in visited:
        count += 1
        bfs(graph, i)

print(count)