from collections import deque
def move(board, pos, node, d):
    h, w = pos
    dire = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    x, y = node
    while 0 <= x + dire[d][0] < h and 0 <= y + dire[d][1] < w:
        if board[x + dire[d][0]][y + dire[d][1]] == "D":
            return [x, y]
        x += dire[d][0]
        y += dire[d][1]
    return [x, y]

def solution(board):
    h, w = len(board), len(board[0])
    start, end = [], []
    for i in range(h):
        for j in range(w):
            if board[i][j] == "R":
                start = [i, j]
            if board[i][j] == "G":
                end = [i, j]
    queue = deque([start])
    count = [[0]*w for _ in range(h)]
    count[start[0]][start[1]] = 1
    while queue:
        node = queue.popleft()
        for d in range(4):
            x, y = move(board, (h, w), node, d)
            
            if not count[x][y]:
                queue.append([x, y])
                count[x][y] = count[node[0]][node[1]] + 1
    ans = count[end[0]][end[1]] - 1
    return ans if ans else -1