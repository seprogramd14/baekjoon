from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = {i+1:[] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

for i in range(n):
    graph[i+1].sort()

def dfs(root):
    res = []
    stack = [root]
    visited = [0]*(n+1)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            stack.extend(list(reversed(graph[node])))
            res.append(node)
    return res

def bfs(root):
    res = [root]
    queue = deque([root])
    visited = [0]*(n+1)
    visited[root] = 1
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if not visited[g]:
                visited[g] = 1
                queue.append(g)
                res.append(g)
    return res

print(*dfs(v))
print(*bfs(v))