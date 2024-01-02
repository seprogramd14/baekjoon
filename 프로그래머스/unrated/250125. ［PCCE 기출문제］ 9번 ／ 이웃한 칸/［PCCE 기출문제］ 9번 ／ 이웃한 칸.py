def solution(board, h, w):
    l = len(board[0])
    check = board[h][w]
    answer = 0
    if 0 <= h-1 < l and board[h-1][w] == check:
        answer += 1
    if 0 <= h+1 < l and board[h+1][w] == check:
        answer += 1
    if 0 <= w-1 < l and board[h][w-1] == check:
        answer += 1
    if 0 <= w+1 < l and board[h][w+1] == check:
        answer += 1
    return answer