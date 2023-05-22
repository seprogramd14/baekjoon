def solution(k, m, score):
    answer = 0
    score.sort()
    while True:
        fruit_box = []
        if len(score) < m: break
        for _ in range(m):
            fruit_box.append(score.pop())
        answer += min(fruit_box) * m
    return answer