import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
village = [[i for i in input().rstrip()] for _ in range(n)]

def bfs(i, j):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([(i, j)])
    count = 1 # 본인의 위치 포함

    while queue:
        i, j = queue.popleft()
        village[i][j] = '0'

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        for d in range(4):
            x, y = i + dx[d], j + dy[d]
            if 0 <= x < n and 0 <= y < n:
                if village[x][y] == '1' and visited[x][y] != 1:
                    visited[x][y] = 1
                    queue.append((x, y))
                    count += 1
    
    return count


house, num = 0, []
for i in range(n):
    for j in range(n):
        if village[i][j] == '1':
            house += 1
            num.append(bfs(i, j))
print(house)
for i in sorted(num):
    print(i)