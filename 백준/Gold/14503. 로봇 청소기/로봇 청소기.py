import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서 (r, c)

cnt = 0
while True:
    if not room[r][c]:
        room[r][c] = 2
        cnt += 1
    
    is_not_trash = [room[r+i][c+j] for i, j in dire]

    if all(is_not_trash): # 쓰레기가 없다면
        back = dire[(d+2)%4]
        if room[r+back[0]][c+back[1]] != 1:
            r += back[0]
            c += back[1]
        else:
            print(cnt)
            break
    else: # 쓰레기가 있다면
        d = (d+3)%4
        while room[r+dire[d][0]][c+dire[d][1]]:
            d = (d+3)%4
        r += dire[d][0]
        c += dire[d][1]
