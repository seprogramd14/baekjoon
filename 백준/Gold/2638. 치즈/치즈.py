# 치즈
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
dire = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def dfs(root):
    queue = deque([root])
    visited = [[0]*m for _ in range(n)]
    visited[root[0]][root[1]] = 1
    melt = []

    while queue:
        x, y = queue.popleft()
        for d in dire:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < n and 0 <= dy < m:
                if cheese[dx][dy]: # 치즈가 있을 때
                    visited[dx][dy] -= 1 # 치즈 닿은 면 수 표시
                    if visited[dx][dy] <= -2:
                        melt.append([dx, dy])
                else: # 치즈가 없을 때
                    if not visited[dx][dy]:
                        visited[dx][dy] = 1
                        queue.append([dx, dy])
    return melt

time = 0
while True:
    melt_pos = dfs([0, 0])
    
    if not melt_pos:
        print(time)
        break
    
    for x, y in melt_pos:
        cheese[x][y] = 0
    time += 1