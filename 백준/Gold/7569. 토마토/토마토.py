import sys
from collections import deque
input = sys.stdin.readline

M, N, H = list(map(int, input().split()))
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
start = [[k, i, j] for j in range(M) for i in range(N) for k in range(H) if box[k][i][j] == 1]
# 인덱스 접근 : 높이, 세로, 가로
def bfs(tomato):
    count = 0
    while tomato:
        queue, tomato = deque(tomato), []
        while queue:
            node = queue.popleft()

            dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
            for d in range(6):
                k, i, j = dx[d] + node[0], dy[d] + node[1], dz[d] + node[2]

                if 0 <= k < H and 0 <= i < N and 0 <= j < M:
                    if not box[k][i][j]:
                        tomato.append([k, i, j])
                        box[k][i][j] = 1
        count += 1
    return count

result = bfs(start) - 1

for k in range(H):
    for i in range(N):
        for j in range(M):
            if not box[k][i][j]:
                print(-1)
                exit()

print(result)