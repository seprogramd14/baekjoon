import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split())) # 세로, 가로
Map = [list(map(int, input().split())) for _ in range(n)]
start = [[i, j] for j in range(m) for i in range(n) if Map[i][j] == 2][0]

def bfs(root):
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[root[0]][root[1]] = 0
    queue = deque([root])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        node = queue.popleft()
        for i in range(4):
            x, y = node[0] + dx[i], node[1] + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if visited[x][y] == -1 and Map[x][y]:
                    if [x, y] != root:
                        queue.append([x, y])
                        visited[x][y] = visited[node[0]][node[1]] + 1
    
    return visited

result = bfs(start)
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0 and result[i][j] == -1:
            result[i][j] = 0

for r in result:
    print(*r)