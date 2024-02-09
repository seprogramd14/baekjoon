import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board1 = [[i for i in input().rstrip()] for _ in range(n)] # 색약 X
board2 = [[0 for _ in range(n)] for _ in range(n)] # 색약 O 
check1 = [[0 for _ in range(n)] for _ in range(n)]
check2 = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board1[i][j] == 'G':
            board2[i][j] = 'R'
        else:
            board2[i][j] = board1[i][j]

def bfs(start, who):
    queue = deque([start])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        node = queue.popleft()

        for d in range(4):
            i, j = node[0] + dx[d], node[1] + dy[d]
            if 0 <= i < n and 0 <= j < n:
                if who == 1:
                    if not check2[i][j] and board2[i][j] == board2[node[0]][node[1]]:
                        check2[i][j] = 1
                        queue.append([i, j])
                else:
                    if not check1[i][j] and board1[i][j] == board1[node[0]][node[1]]:
                        check1[i][j] = 1
                        queue.append([i, j])

result = [0, 0]

for i in range(n):
    for j in range(n):
        if not check1[i][j]:
            check1[i][j] = 1
            bfs([i, j], 0)
            result[0] += 1
        if not check2[i][j]:
            check2[i][j] = 1
            bfs([i, j], 1)
            result[1] += 1

print(*result)