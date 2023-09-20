def solution(todo_list, finished):
    return [i for i, j in zip(todo_list, finished) if not j]