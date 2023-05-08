def solution(board, moves):
    stack = []
    cut = 0
    for move in moves:
        idx = 0
        for board_part in board:
            if board_part[move-1] != 0:
                stack.append(board_part[move-1])
                board[idx][move-1] = 0
                break
            else: idx += 1
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            cut += 2
    return cut