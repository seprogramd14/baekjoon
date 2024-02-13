import sys
input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(start, h):
    stack = [start]
    while stack:
        node = stack.pop()
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for d in range(4):
            x, y = node[0] + dx[d], node[1] + dy[d]
            if 0 <= x < n and 0 <= y < n:
                if not check[x][y] and area[x][y] > h:
                    check[x][y] = 1
                    stack.append([x, y])

for h in range(max(map(max, area))):
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not check[i][j]:
                check[i][j] = 1 # 이동 가능
                cnt += 1
                dfs([i, j], h)
    answer = max(answer, cnt)
print(answer)