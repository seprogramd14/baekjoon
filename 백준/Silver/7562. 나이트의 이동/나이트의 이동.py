import sys
from collections import deque
input = sys.stdin.readline

dire = [[-2, -1], [-2, 1], [2, -1], [2, 1],
        [-1, -2], [1, -2], [-1, 2], [1, 2]]

def bfs(start, end, n):
    queue = deque([start])
    visited = [[-1] * n for _ in range(n)]
    visited[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            return visited[x][y]
        for d in dire:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] == -1:
                    visited[dx][dy] = visited[x][y] + 1
                    queue.append([dx, dy])
    return -1

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(start, end, n))