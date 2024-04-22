import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [[int(i) for i in input().rstrip()] for _ in range(n)]
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(start):
    queue = deque()
    queue.append(start + [0, 1]) # 시작, 차원, 시간 (낮은 홀수일 때, 밤을 짝수일 때)
    visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]
    visited[0][0][0] = 1
    while queue:
        x, y, dim, t = queue.popleft()
        if x == n-1 and y == m-1:
            return t
        
        for dx, dy in dire:
            i, j = x + dx, y + dy
            if 0 <= i < n and 0 <= j < m and not visited[dim][i][j]:
                if not matrix[i][j]: # 벽 아니면
                    visited[dim][i][j] = 1
                    queue.append([i, j, dim, t+1])
                elif dim < k and not visited[dim+1][i][j]:
                    if not t % 2: # 밤일 때 추가
                        queue.append([x, y, dim, t+1])
                    else:
                        visited[dim+1][i][j] = 1
                        queue.append([i, j, dim+1, t+1])
    return -1


print(bfs([0, 0]))