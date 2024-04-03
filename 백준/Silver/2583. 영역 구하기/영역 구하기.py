import sys
from collections import deque
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
paper = [[0] * m for _ in range(n)]

def bfs(start):
    queue = deque([start])
    paper[start[0]][start[1]] = 1
    count = 1
    while queue:
        i, j = queue.popleft()

        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in dire:
            x, y = d[0] + i, d[1] + j
            if 0 <= x < n and 0 <= y < m:
                if not paper[x][y]:
                    paper[x][y] = 1
                    count += 1
                    queue.append([x, y])
    return count

for i in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 4

result = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 0:
            result.append(bfs([i, j]))

print(len(result))
print(*sorted(result))