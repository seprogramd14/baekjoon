import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
        for d in range(8):
            x, y = node[0] + dx[d], node[1] + dy[d]
            if 0 <= x < h and 0 <= y < w:
                if Map[x][y] and not check[x][y]:
                    check[x][y] = 1
                    queue.append([x, y])

result = []
while True:
    w, h = list(map(int, input().split()))
    if not w and not h:
        break
    
    Map = [list(map(int, input().split())) for _ in range(h)]
    check = [[0] * w for _ in range(h)]
    land = 0

    for i in range(h):
        for j in range(w):
            if Map[i][j] and not check[i][j]:
                land += 1
                bfs([i, j])
    
    result.append(land)

for r in result:
    print(r)