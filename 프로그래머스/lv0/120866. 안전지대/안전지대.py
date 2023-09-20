def solution(board): # 위험지대 2, 폭탄 1, 그냥 0
    x, y = [-1,-1,-1,0,0,0,1,1,1], [-1,0,1,-1,0,1,-1,0,1]
    answer = 0
    for idx, line in enumerate(board):
        for place in range(len(line)):
            if line[place] == 1:
                for _dx, _dy in zip(x, y):
                    dx, dy = idx + _dx, place + _dy
                    if 0 <= dx <= len(line)-1 and 0 <= dy <= len(line)-1 and board[dx][dy] == 0:
                        board[dx][dy] = 2
    for idx, line in enumerate(board):
        answer += line.count(0)
    return answer