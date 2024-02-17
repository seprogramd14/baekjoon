import sys
input = sys.stdin.readline

def square(n, start_x, end_x, start_y, end_y):
    if n == 1:
        return
    
    # 1. 가운데 구멍
    pos_x = (end_x - start_x) // 3 + start_x
    pos_y = (end_y - start_y) // 3 + start_y
    for i in range(pos_x, pos_x + n // 3):
        for j in range(pos_y, pos_y + n // 3):
            ls[i][j] = ' '
    
    # 2. 분해
    for i in range(3):
        for j in range(3):
            x = (end_x - start_x) // 3
            y = (end_y - start_y) // 3
            square(n//3, x * i + start_x, x * (i + 1) + start_x, y * j + start_y, y * (j + 1) + start_y)


n = int(input())
ls = [['*'] * n for _ in range(n)]
square(n, 0, n, 0, n)
for l in ls:
    print(''.join(l))