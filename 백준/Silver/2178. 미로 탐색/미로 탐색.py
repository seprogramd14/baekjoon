from collections import deque

def bfs(maze):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < n and 0 <= _y < m:
                if visited[_x][_y] == 0 and maze[_x][_y] == '1':
                    visited[_x][_y] = visited[x][y] + 1
                    queue.append((_x, _y))

import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

maze = [list(input().rstrip()) for _ in range(n)]
print(bfs(maze))