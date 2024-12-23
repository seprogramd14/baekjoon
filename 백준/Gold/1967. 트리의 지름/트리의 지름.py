import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
tree = {i+1:[] for i in range(n)}
for _ in range(n-1):
    r, c, v = map(int, input().split())
    tree[r].append([c, v])
    tree[c].append([r, v])

def dfs(root, total):
    for node, cost in tree[root]:
        if visited[node] == -1:
            visited[node] = cost + total
            dfs(node, visited[node])

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

max_node = visited.index(max(visited))
visited = [-1] * (n+1)
visited[max_node] = 0
dfs(max_node, 0)
print(max(visited))