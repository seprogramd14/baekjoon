import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [[int(i) for i in input().rstrip()] for _ in range(n)]
dire = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(start):
    queue = deque([[start, 0]])
    visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
    visited[0][start[0]][start[1]] = 1
    while queue:
        node, dim = queue.popleft()
        if node[0] == n-1 and node[1] == m-1:
            return visited[dim][n-1][m-1]
        for d in dire:
            x, y = node[0] + d[0], node[1] + d[1]
            if 0 <= x < n and 0 <= y < m and not visited[dim][x][y]:
                if not matrix[x][y]:
                    queue.append([[x, y], dim])
                    visited[dim][x][y] = visited[dim][node[0]][node[1]] + 1
                elif matrix[x][y] and dim < k and not visited[dim+1][x][y]:
                    queue.append([[x, y], dim+1])
                    visited[dim+1][x][y] = visited[dim][node[0]][node[1]] + 1
    return -1


print(bfs([0, 0]))