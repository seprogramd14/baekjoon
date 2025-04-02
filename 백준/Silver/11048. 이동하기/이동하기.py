import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(r)]
move = [[0, 1], [1, 0]]

visited = [[-1]*c for _ in range(r)]
visited[0][0] = maze[0][0]
queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()

    for d in move:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < r and 0 <= dy < c:
            if visited[x][y] + maze[dx][dy] > visited[dx][dy]:
                visited[dx][dy] = visited[x][y] + maze[dx][dy]
                queue.append([dx, dy])
print(visited[r-1][c-1])