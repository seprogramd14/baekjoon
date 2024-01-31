import sys
from collections import deque
input = sys.stdin.readline

m, n = list(map(int, input().split()))
box = [list(map(int, input().split())) for _ in range(n)]
start = [[i, j] for j in range(m) for i in range(n) if box[i][j] == 1]

def bfs(tomato):
    count = 0
    while tomato:
        queue, tomato = deque(tomato), []
        while queue:
            node = queue.popleft()
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

            for d in range(4):
                i, j = node[0] + dx[d], node[1] + dy[d]

                if 0 <= i < n and 0 <= j < m:
                    if not box[i][j]:
                        tomato.append([i, j])
                        box[i][j] = 1
        count += 1
    return count

result = bfs(start) - 1

for i in range(n):
    for j in range(m):
        if not box[i][j]:
            print(-1)
            exit()

print(result)