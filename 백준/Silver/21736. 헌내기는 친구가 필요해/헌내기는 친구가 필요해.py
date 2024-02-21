import sys
input = sys.stdin.readline

h, w = list(map(int, input().split()))
uni = [[i for i in input().rstrip()] for _ in range(h)]
visited = [[0] * w for _ in range(h)]
def dfs(start):
    count = 0
    stack = [start]

    while stack:
        node = stack.pop()
        dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
        for d in range(4):
            x, y = node[0] + dx[d], node[1] + dy[d]
            if 0 <= x < h and 0 <= y < w:
                if uni[x][y] != 'X' and not visited[x][y]:
                    visited[x][y] = 1
                    stack.append([x, y])
                    if uni[x][y] == 'P':
                        count += 1
                        visited[x][y] = 2

    return count

start = []
for i in range(h):
    for j in range(w):
        if uni[i][j] == 'I':
            start = [i, j]

person = dfs(start)
print(person if person else "TT")