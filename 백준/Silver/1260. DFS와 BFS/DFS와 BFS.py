from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, root, visited = []):
    visited.append(root)
    for node in graph[root]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

N, M, V = list(map(int, input().split()))
graph = dict()

for i in range(M):
    edge = list(map(int, input().split()))
    key = graph.keys()
    if edge[0] not in key:
        graph[edge[0]] = [edge[1]]
    else:
        graph[edge[0]] += [edge[1]]

    if edge[1] not in key:
        graph[edge[1]] = [edge[0]]
    else:
        graph[edge[1]] += [edge[0]]

graph_key = graph.keys()

for i in graph_key:
    graph[i].sort()

if V in graph_key:
    print(*dfs(graph, V))
    print(*bfs(graph, V))
else:
    print(V)
    print(V)