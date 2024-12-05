import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]
width = [0] * n
d = [(-1, -1), (1, -1), (-1, 1), (1, 1)] # 왼쪽 위, 왼쪽 아래, 오른쪽 위, 오른쪽 아래

cnt = 0
def queen_check(start): # 대각선 2개 따져보기 (자신의 자리는 제외)
    global board
    for dx, dy in d:
        x, y = start
        while 0 <= (x:=x+dx) < n and 0 <= (y:=y+dy) < n:
            if board[x][y]:
                return 1
    return 0

def setting(q): # 현재 퀸 개수, 보드 상태
    global cnt, board, width
    for j in range(n):
        if not width[j]:
            board[q][j], width[j] = 1, 1
            if not queen_check((q, j)): # 퀸의 존재가 없으면 새로운 퀸을 배치
                if q == n-1: # 퀸의 개수가 일정 수에 도달하면 경우의 수 증가
                    cnt += 1
                else:
                    setting(q+1)
            board[q][j], width[j] = 0, 0 # 원래 상태로 리셋

setting(0)
print(cnt)