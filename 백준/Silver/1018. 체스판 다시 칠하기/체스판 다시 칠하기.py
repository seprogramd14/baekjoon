n,m = map(int, input().split())
board = [input() for _ in range(n)]
B = 'BWBWBWBW'
W = 'WBWBWBWB'
max = 0
min = 8*8

for v in range(n-7): # 처음부터 시작
  for k in range(m-7): # 반복 횟수
    cut, line = 0, 1
    if board[v][k] == 'W': # 맨 처음이 W일때
      for i in board[v:v+8]:
        idx = 0
        if line % 2 == 1:
          for j in i[k:k+8]:
            if j != W[idx]: cut += 1
            idx += 1
        elif line % 2 == 0:
          for j in i[k:k+8]:
            if j != B[idx]: cut += 1
            idx += 1
        line += 1
    elif board[v][k] == 'B': # 맨 처음이 B일때
      for i in board[v:v+8]:
        idx = 0
        if line % 2 == 1:
          for j in i[k:k+8]:
            if j != B[idx]: cut += 1
            idx += 1
        elif line % 2 == 0:
          for j in i[k:k+8]:
            if j != W[idx]: cut += 1
            idx += 1
        line += 1

    if cut<min: min = cut # 출력 부분 수정
    if cut>max: max = cut

print(min if 64-max>min else 8*8-max)