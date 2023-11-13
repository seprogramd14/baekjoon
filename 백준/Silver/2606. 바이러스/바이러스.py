import sys
input = sys.stdin.readline
n = int(input())
e = int(input())

def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    
    return visited

graph = dict()

for i in range(e):
    n1, n2 = list(map(int, input().rstrip().split()))
    key = graph.keys()
    if n1 not in key:
        graph[n1] = [n2]
    else:
        graph[n1] += [n2]
    
    if n2 not in key:
        graph[n2] = [n1]
    else:
        graph[n2] += [n1]


if 1 in graph.keys():
    print(len(dfs(graph, 1)) - 1)
else:
    print(0)