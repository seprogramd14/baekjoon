def solution(keyinput, board):
    board = [board[0]//2, board[1]//2]
    keyboard = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    pos = [0,0]
    for key in keyinput:
        val = keyboard[key]
        pos = [pos[0]+val[0], pos[1]+val[1]]
        if pos[0] < -board[0]: pos[0]+=1
        if pos[0] > board[0]: pos[0]-=1
        if pos[1] < -board[1]: pos[1]+=1
        if pos[1] > board[1]: pos[1]-=1
    return pos