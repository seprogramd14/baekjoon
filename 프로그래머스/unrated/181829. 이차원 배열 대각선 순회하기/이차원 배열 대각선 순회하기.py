def solution(board, k):
    answer = 0
    for idx, val in enumerate(board):
        l = k - idx if k - idx < len(board[0]) else len(board[0])
        if l < 0: break
        answer += sum(val[:l+1])
    return answer