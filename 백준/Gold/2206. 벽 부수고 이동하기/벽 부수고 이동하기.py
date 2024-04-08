import sys
from collections import deque
input = sys.stdin.readline

# 입력 값
n, m = list(map(int, input().split()))
matrix = [[int(i) for i in input().rstrip()] for _ in range(n)]
dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# bfs 함수
def bfs(start):
    queue = deque([[start, 0]]) # 시작점 / 0, 1 세계 구분
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]
    visited[0][start[0]][start[1]] = 1
    visited[1][start[0]][start[1]] = 1
    while queue:
        node, world = queue.popleft()

        if node[0] == n-1 and node[1] == m-1:
            return visited[world][node[0]][node[1]]
        
        for d in dire:
            x, y = node[0] + d[0], node[1] + d[1]
            if 0 <= x < n and 0 <= y < m and visited[world][x][y] == 0:
                if matrix[x][y] == 0: # 0이 있으면 길이 되는 거임
                    visited[world][x][y] = visited[world][node[0]][node[1]] + 1
                    queue.append([[x, y], world])
                
                elif matrix[x][y] == 1: # 벽이라면
                    if world == 0: # 0세계라면
                        queue.append([[x, y], 1])
                        visited[1][x][y] = visited[world][node[0]][node[1]] + 1


result = bfs([0, 0])
if not result:
    print(-1)
else:
    print(result)
