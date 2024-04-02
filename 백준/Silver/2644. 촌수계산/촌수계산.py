import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
find = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

def bfs(start):
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if visited[g] == 0:
                visited[g] = visited[node] + 1
                queue.append(g)
    return visited


for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
result = bfs(find[0])
print(result[find[1]] - 1 if result[find[1]] else -1)