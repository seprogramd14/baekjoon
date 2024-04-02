import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[]]

def bfs(start):
    queue = deque([[start, 0]])
    visited = [0] * (n+1)
    visited[start] = 2
    while queue:
        node = queue.popleft()
        for g in graph[node[0]]:
            if not visited[g] and node[1] < 2:
                visited[g] = 1
                queue.append([g, node[1] + 1])
    return sum([v for v in visited if v == 1])

for _ in range(n):
    graph.append([idx+1 for idx, val in enumerate(input().rstrip()) if val == 'Y'])
result = []
for i in range(n):
    result.append(bfs(i+1))

print(max(result))