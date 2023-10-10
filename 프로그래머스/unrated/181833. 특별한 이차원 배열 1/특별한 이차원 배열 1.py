def solution(n):
    answer = [[0 for i in range(n)] for i in range(n)]
    for i, j in enumerate(answer):
        j[i] = 1
    return answer